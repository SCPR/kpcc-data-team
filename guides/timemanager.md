##Using the QGIS Time Manager plugin in QGIS to make gifs
While loading a bunch of graffiti data into QGIS, I was transfixed by how the data began popping up as bubbles. It was cool.

![](./images/purp.png =300x)
![](./images/blu.png =300x)

I realized that this data could be used to tell a story about graffiti in Los Angeles, which resulted [in this interactive](http://projects.scpr.org/maps/graffiti-map/).

The [Time Manager plug-in](http://anitagraser.com/projects/time-manager/) for QGIS by Anita Graser made that possible.


###Using Time Manager
To work with it, you need to load data into QGIS that has some sort of temporal element, as well as a geographic one. Make sure you have the plugin installed (you can do that using the "Plugins" menu in QGIS). 

Keep in mind you'll do all the styling outside of Time Manager, most likely using the properties on your layer.

Call the Time Manager toolbar up, which will look like this:
![](./images/time_mgr.png =700x)

Hit the "Settings" button. Make sure that "Display frame start time on map" is selected, because you want the time displayed on the images to lend clarity and help the viewer understand. (One feature you will not have using this method is a legend.)

If you click on the "Time display options" you'll be able to customize how the time is displayed (for example, I removed time of day from my gif). The placement options are limited, but for Los Angeles, where there is the "empty" space of the Pacific Ocean to the southwest, you have a nice option. Using a black background to the time display helps it fit nicely there with the Stamen map, with only the white letters visible to the viewer.

Note the "Accumulate features" box in the settings. I accumulated features for this image, but you may or may not want to do that.

The "Time frame start" tells the plugin when to begin. Note that for my gif, I had it start the day before my data does. This way the viewer could see the map without any of the features displayed before it begins stepping through time.

The "time frame size" tells the plugin at what speed you want it to step through time (i.e. I wanted one image for each day, so I chose "1 days").

To get started, make sure the On button is selected, and hit "Export Video". You'll choose a place to export your stills to and select it. After that time manager will essentially freeze QGIS until it's done spitting out those stills.

###Gif time
Go to [gifmaker.me](http://gifmaker.me/). This is a great website that lets you customize your gifs without watermarks.

Click on "Upload" and select all your images. Salt to taste and then export your gif and share it with the world. Make sure you provide meaningful context for it when you do.