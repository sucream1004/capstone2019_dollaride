# Capstone 2019 Dollaride Repo
![dollaride](./imgs/dollaride.png)

## Transit Desert
- NYC Open Data and GTFS (Google's General Transit Feed Specifications) datasets
- Index  =  0.5 x Population_density + 0.4 x (-1) Distance from a Subway Stop + 0.1 x (-1) Distance from a Bus Stop
![transit_desert](./imgs/transit_desert.png)


## For Hire Vehicles (FHV)
- NYC OpenData offers yearly FHV data.
- Due to the size of the data, I used Postgresql to minimize memory usage.
- Following figures are representing the numbef of trips between zones(Left: Weekday, Middle: Weekend, Right: Internal Trip)
- The figure of trip in weekday and weekend is same.
![fhv_pic](./imgs/fhv_pic.png)
Figure: weekday trips; weekend trips; internal trips;
## Route suggestion
- Suggested routes map are in the routes_map directory.
- The methodology is as follows:
![mk_route](./imgs/mk_route.png)

## Synthetic Population
- 
- 
![syn1](./imgs/syn1.png)
![syn2](./imgs/syn2.png)
