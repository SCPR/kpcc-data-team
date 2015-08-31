How to make a quick heatmap with QGIS
======================================

By [Will Craft](https://twitter.com/craftworksxyz)

This is a brief guide on how to make basic heatmaps using QGIS and the OpenStreetMap and Heatmap plugins. Steps taken from this [QGIS tutorial on how to make heatmaps](http://www.qgistutorials.com/en/docs/creating_heatmaps.html), which includes instructions on how to download plugins. This assumes a basic knowledge of QGIS, but it is very easy to learn how to use QGIS from scratch using the linked tutorial.

### Steps

* Get the data ready to be imported to QGIS. KPCC uses a version of the LA Times datadesk's [geocode-addresses](https://github.com/SCPR/kpcc-data-team/tree/wcraft-dev/tools-and-scripts/geocode-addresses) to convert addresses into geographic coordinates.
* Import the data by adding a delimited text layer and specifying which columns should be used as the x and y coordinates . If QGIS takes the csv and imports all the rows as columns, which is a known error, copy the data into a different program and save it again. Some programs save files in ways that QGIS has trouble with.
* Use [OpenStreetMap](http://www.qgistutorials.com/en/docs/downloading_osm_data.html) to get a map base layer. The linked tutorial is slightly out of date, but still a good overview of OSM. In QGIS, go to the Web tab then down to the OpenLayers plugin menu and select which map layout you want to use. Google maps, at least, automatically lines up your data points to the map. Double check still, of course.
*  Go to the Raster tab and down to the heatmap menu and select heatmap. Name the layer and change the radius based on how large or small you want each datapoint to be. The larger the radius, the more overlap between the datapoints, the more dense the map will look.
*  Doubleclick on the new layer and change the render type to 'singleband pseudocolor'. Then choose what range of color you want the heatmap to be and change the transparency so you can see the map through the heatmap layer.
