#Water district shapefiles in California
In 2015, its fourth year of drought, California began imposing mandatory cutbacks on hundreds of urban water suppliers across the state. In 2016, the state allowed suppliers to set their own reduction targets. Many set those targets at zero.

Nevertheless, the State Water Resources Control Board [continues to report urban water use each month](http://www.waterboards.ca.gov/water_issues/programs/conservation_portal/conservation_reporting.shtml).

Exactly *where* are those urban districts, and what are their service areas? What geographic patterns can we find in water use?

These are surprisingly difficult questions to answer. **There is no central repository of water district shapefiles** in the state, according to the Department of Water Resources.

The GIS data in this repo was initally compiled by the DWR, and then joined to SWRCB data by KPCC.

DWR spokeswoman Lauren Bisnett said that the data "comes from a wide range of sources of a wide range of qualities. There isn’t a better water agency dataset in existence to our knowledge, but ours should be considered a rough."

It is indeed rough, with many overlapping service areas (there should be none, since service areas don't overlap), and adjoining districts that fit together like jagged puzzle pieces (see Los Angeles and San Fernando).

One other grain of salt: water district service areas frequently change.

#What's here
KPCC was able to match more than 380 of the districts in the monthly urban water use reports to the DWR data.

The [urban_water_districts.geojson file](urban_water_districts.geojson) is those districts, along with their name as represented each month in the SWRCB. This allows a user to join the shapefiles to the water use data.

The attribute table also includes all the fields provided by the DWR.

We are also attaching a [csv of the 'key' to joining the SWRCB data to the DWR's GIS data](swrcb_water_district_name_key.csv). By itself this will not produce the geojson in this repo; there will be several agencies that have multiple joins (which have been cleaned up in the geojson). However, it may come in handy as the DWR futher refines their data, as they indicated to KPCC that they would.

You can see the full extent of the DWR water district boundaries [on their website](https://gis.water.ca.gov/app/boundaries/).

Please let us know if you use these files: amendelsonATscprDOTorg

![](wd_blank_map.png)