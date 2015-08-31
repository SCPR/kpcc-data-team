Using the QGIS Time Manager plugin to make gifs
================================================

By [Aaron Mendelson](http://www.scpr.org/about/people/staff/aaron-mendelson)

While loading a bunch of graffiti data into QGIS, I was transfixed by how the data began popping up as bubbles. It was cool.

![](/blog/images/blu_purp.png)

I realized that this data could be used to tell a story about graffiti in Los Angeles, which resulted [in this story](http://www.scpr.org/news/2015/08/17/53452/watch-a-month-of-graffiti-cleanup-in-los-angeles/).

The [Time Manager plug-in](http://anitagraser.com/projects/time-manager/) for QGIS by Anita Graser made that possible. This guide assumes a basic knowledge of QGIS. If you don't yet have that, or want to brush up, you can always [review the documentation](http://docs.qgis.org/2.8/).

### Using Time Manager
To work with it, you need to load data into QGIS that has some sort of temporal element, as well as a geographic one. You could use something as simple as this:

![](/blog/images/data_layout.png)

(You could actually use something even simpler. Here the TOTAL_SQFT_CLEANED column controls how large the circles are.)

Make sure you have the plugin installed (you can do that using the "Plugins" menu in QGIS).

Keep in mind you'll do all the styling outside of Time Manager, most likely using the properties on your layer.

Once you've done that, call the Time Manager toolbar up, which will look like this:
![](/blog/images/time_mgr.png)

Hit the "Settings" button. Make sure that "Display frame start time on map" is selected, because you want the time displayed on the images to lend clarity and help the viewer understand. (One feature you will not have using this method is a legend.)

If you click on the "Time display options" you'll be able to customize how the time is displayed (for example, I removed time of day from my gif). The placement options are limited, but for Los Angeles, where there is the "empty" space of the Pacific Ocean to the southwest, you have a nice option. Using a black background to the time display helps it match the Stamen toner map, with only the white letters visible to the viewer.

Note the "Accumulate features" box in the settings. I accumulated features for this image, but you may or may not want to do that.

The "Time frame start" tells the plugin when to begin. Note that for my gif, I had it start the day before my data does. This way the viewer could see the map without any of the features displayed before it begins stepping through time.

The "time frame size" tells the plugin at what speed you want it to step through time (i.e. I wanted one image for each day, so I chose "1 days").

To get started, make sure the On button is selected, and hit "Export Video". You'll choose a place to export your stills to and select it. After that time manager will essentially freeze QGIS until it's done spitting out those stills.

### Gif time
Go to [gifmaker.me](http://gifmaker.me/). This is a great website that lets you customize your gifs without watermarks.

Click on "Upload" and select all your images. Salt to taste and then export your gif and share it with the world. Make sure you provide meaningful context for it when you do.
