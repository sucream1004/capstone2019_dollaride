import geopandas as gpd
import pandas as pd

# taxi zone shape
boro = gpd.read_file('boro.geojson')
tz = gpd.read_file('1_fhv_analysis/taxi_zones.shp').drop(['OBJECTID', 'Shape_Leng', 'Shape_Area'], axis=1).to_crs({'init': 'epsg:4326'})

# centroid to plot linestring
tz_ = tz.copy()
tz_['geometry'] = tz_['geometry'].centroid
tz_.LocationID = tz_.LocationID.astype(str)
# x is pick-up and y is drop-off
def txtx(dat):
    df = dat.dropna().query('pulocationid != "0" and dolocationid != "0"')
    df = df.rename(index=str, columns={'count': 'cnt'})
    df = df.merge(tz_, left_on='pulocationid', right_on='LocationID')\
        .merge(tz_, left_on='dolocationid', right_on='LocationID')\
        .drop(['LocationID_x', 'LocationID_y'], axis=1)
    from shapely.geometry import Point, LineString
    df['geometry'] = [LineString([o,d]) for o,d in zip(df.geometry_x, df.geometry_y)]
    df = gpd.GeoDataFrame(df)
    df.crs = {'init': 'epsg:4326'}
    return df
    
if __name__ == "__main__":
    main()
    