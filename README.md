# Capstone 2019 Dollaride Repo
![dollaride](./imgs/dollaride.png)

 While New York City has developed public transportation networks provided by MTA, a huge number of people living in outer boroughs are left outside the networks. These people are living in “transit deserts” and have a strong demand for transportation means. Part of the demand is met by so-called “dollar vans” – a chain of thousands of privately owned commuter vans which run across the NYC. A startup called “Dollaride” connects drivers and passengers in these marginalized communities using an  innovative transportation technology.
The project identifies methodology for calculating transit deserts (transit-underserved areas in terms of specific transit supply-demand equilibrium) in a large city. The methodology is based on earlier developed attitude by Jiao and Dillivan (2013), but some different parameters characterising a first-tier American city were suggested.  The outcome of the project is a map of transit deserts in NYC, based on a solid quantitative analysis and data. Another practical implication of the project is a list of new routes for Dollaride, which would benefit its passengers, drivers and NYC transportation authorities. 


## Transit Desert
- NYC Open Data and GTFS (Google's General Transit Feed Specifications) datasets
- We will consider the closest subway station or MTA bus stop, and identify the distance from them to the centroid of the census tract. In terms of transportation demand estimation, population data was used (with a granularity of a census tract, as the most computationally small data available). After that, for the purpose of creating an index of each transportational zone, z-score of the distance variable (supply) and z-score of the population density variable (demand) was calculated.
- z-score(Index)  =  0.5 x Population_density + 0.4 x (-1) Distance from a Subway Stop + 0.1 x (-1) Distance from a Bus Stop
![transit_desert](./imgs/transit_desert.png)

## For Hire Vehicles (FHV)
- NYC OpenData offers yearly FHV data.
- Due to the size of the data, I used Postgresql to minimize memory usage.
- This map shows the for-hire-vehicle trips during the weekdays between different taxi zones within Queens, Brooklyn, Bronx, Staten Island, and Newark airport. 
- The purple lines shown on the map represent the trips between different zones that have more than 100 trip counts, which can be regarded as popular routes for for-hire-vehicles on a taxi zone basis.
- The wider the purple band is, the more trips there are on that route. For example, the trips between Jackson Heights and Astoria, Williamsburg and Bed-Stuy, as well as Bay Ridge and Bath Beach have large volume of trips represented by the wide stroke of purple bands. 
![fhv_pic](./imgs/fhv_pic.png)
Figure: weekday trips; weekend trips; internal trips;
## Route suggestion
- Suggested routes map are in the routes_map directory.
- The methodology is as follows:
1. Set the initial taxi zone
2. Checking adjacent zones
3. Select next zone based on the potential rider
![mk_route](./imgs/mk_route.png)

## Synthetic Population
- The analysis on the synthetic population data reveal the travel pattern of the population in New York City in terms of the zone-to-zone travel basis. 
- The picture on the upper left shows the ranking of taxi zones that has the highest number of trips originating from that particular zone, which include Crown Heights North, Flatbush/Ditmas Park, Borough Park, and Jackson Heights, etc, which are marked in darker blue color.
- The picture on the upper left shows the ranking of taxi zones that has the highest number of trips ending in that particular zone, which include Crown Heights North, Flatbush/Ditmas Park, Borough Park, Flushing and Jackson Heights, etc, which are marked in darker blue color.
- The next step of the analysis focused on zone-to-zone travel patterns.
			§ For trips originating from Flatlands, Mill Basin, Canarsie, and Crown Heights North are popular destinations.\
			§ For trips originating from East New York, people tend to go to Howard Beach, Canarsie, and Downtown Brooklyn.\
			§ For trips originating from Crown Heights North, people like to go to Bushwick North, Prospect Park, as well as Flatlands.
![syn1](./imgs/syn1.png)
![syn2](./imgs/syn2.png)
