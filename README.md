# Capstone 2019 Dollaride Repo
![dollaride](./imgs/dollaride.png)
## American Census Survey (ACS) Mapping
- Using folium and ACS API endpoint, we browsed current commuting methods of NYC by census tract.
- acs2017_download.py is the code to download ACS data.
```
$ python acs2017_download.py [ACS ID] # It saves ACS data as ShapeFile.
```
- To plot interactive map, you can use acs_mapper_choropleth.py.
- The method is same as ACS downloading code.
- The map includes driving(alone, carpooled), public transportation(subway, bus, ferry), bicycle, walking, taxi and working at home.
![acs](./imgs/0_acs.jpg)

## For Hire Vehicles (FHV)
- NYC OpenData offers yearly FHV data.
- Due to the size of the data, I used Postgresql to minimize memory usage.
- Following figures are representing the numbef of trips between zones(Left: Weekday, Middle: Weekend, Right: Internal Trip)
- The figure of trip in weekday and weekend is same.
![fhv_pic](./imgs/fhv_pic.jpg)
Figure: weekday trips; weekend trips; internal trips;
## Route suggestion
- Suggested routes map are in the routes_map directory.
- The methodology is as follows:
![mk_route](./imgs/mk_route.png)

## Synthetic Population
- 
-
