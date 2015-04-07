##Mapping LA's bikeways

We're sharing LADOT's GIS data on bikeways in the city of Los Angeles. [Get it here](https://github.com/SCPR/kpcc-data-team/tree/aaron-dev/data/2014-04-bike-gis/gis_data).

The LADOT maintains such data and [updates it online as a Google map](http://bicyclela.org/maps_main.htm). However, the agency does not share the data behind it. The shapefile we're sharing here is current as of April 1, 2015.

Here's what it looks like if you map it across the city:
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/aaron-dev/data/2014-04-bike-gis/ladot_bikeways.png)

We have also created [a gif that shows the growth of the network](https://github.com/SCPR/kpcc-data-team/blob/aaron-dev/data/2014-04-bike-gis/bike_infra.gif) over the last decade.

Previously, we [published a map using Metro's data](http://www.scpr.org/news/2015/04/03/50740/bicyclists-still-can-t-cross-la-on-marked-bike-lan/). The drawback is that the most recent Metro data is from 2012. [You can download that on their website](http://developer.metro.net/introduction/bikeways-data/download-bikeways-data/).

This is the breakdown of bike classes in those shapefiles, per Metro's Dave Sotero:

- Class 1—off-street paved bike path
- Class 2 – On-street striped bike lane
- Class 3 – On-street bike route (signge only)
- Cycle Track – On-street Separated Bike Lane

The LADOT breaks its bikeways down in a different but related way. Here's how LADOT's Jonathan Raspa explains it:

```
The "bikeway" field tells you the type and the install date tells you the day it was installed. So to sort by install date, set up a definition query for the shapefile (or select by attribute) and you can look at all installs post-2012.

As far as the different types, the City's equivalent to Class 1 lanes is "Path", Class II is "Lane" (buffered and unbuffered), and Class III is "Bicycle Friendly Street", "Sharrows" or "Route". These are the designations that are in our shapefile
```

Let us know if use this data. Have fun. 