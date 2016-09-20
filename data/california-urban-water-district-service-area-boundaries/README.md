# Water district shapefiles in California

In 2015, its fourth year of drought, California began imposing mandatory cutbacks on hundreds of urban water suppliers across the state. In 2016, the state allowed suppliers to set their own reduction targets. Many set those targets at zero.

Nevertheless, the [State Water Resources Control Board](http://www.waterboards.ca.gov/) continues to report [urban water use each month](http://www.waterboards.ca.gov/water_issues/programs/conservation_portal/conservation_reporting.shtml).

Exactly *where* are those urban districts, and what are their service areas? What geographic patterns can we find in water use?

These are surprisingly difficult questions to answer. **There is no central repository of water district shapefiles** in the state, according to the [Department of Water Resources](http://www.water.ca.gov/).

Available data "comes from a wide range of sources of a wide range of qualities," DWR spokeswoman Lauren Bisnett said. "There isn’t a better water agency dataset in existence to our knowledge, but ours should be considered a rough."

It is indeed rough. Many service areas in the dataset overlap, something that should not occur, and adjoining districts fit together like jagged puzzle pieces. One example is Los Angeles and San Fernando.

One other consideration: water district service areas frequently change.

# What's here

The [urban_water_districts.geojson file](urban_water_districts.geojson) is based on [GIS data initially compiled by the DWR](https://gis.water.ca.gov/app/boundaries/).

KPCC then matched more than 380 of the districts with data compiled by the State Water Resources Control Board monthly urban water use reports.

The attribute table also includes all the fields provided by the Department of Water Resource.

We are also attaching a [swrcb_water_district_name_key.csv](swrcb_water_district_name_key.csv) which was the "key" used to join the SWRCB data to the DWR's GIS data.

By itself this will not produce the geojson in this repo; there are several agencies that have multiple joins which have been cleaned up in the geojson. However, it may come in handy as the DWR futher refines their data, as they indicated to KPCC that they would.

Please let us know if you use these files: amendelsonATscprDOTorg

![](wd_blank_map.png)
