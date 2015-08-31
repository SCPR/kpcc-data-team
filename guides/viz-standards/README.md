Thoughts On Standards For Visualizing Information
=================================================

Charts can be an effective and engaging way of displaying quantitative information. They can also be [total garbage](http://viz.wtf/). How can we make sure our charts fall on the right side of [the thin line between clever and stupid](https://www.youtube.com/watch?v=wtXkD1BC564)?

Below are general guidelines, along with tools we use and use cases for those tools. Parts of this borrow generously from [an excellent styleguide](https://github.com/SCPR/scpr-styleguide) put together by the KPCC Product Team (it's a Middleman site; to set it up, you can follow [the instructions laid out here](https://github.com/SCPR/scpr-longreads)).

## General charting guidelines
#### Colors

KPCC Orange is our hero color. Its primary role is to signify the brand in all our visual representations. It's a strong color, and should be used sparingly. Good use cases include logo treatments and design elements responsible for communicating KPCC's brand (app icons, website mastheads, product titling).

![](http://placehold.it/118x118/F87E21/FFFFFF&text=F87E21)

KPCC Orange: #F87E21

##### Accent Colors

KPCC's accent colors support our brand color. They are vibrant, chosen to invoke the feel of Southern California. Like our brand color, these should also be used judiciously.

![](http://placehold.it/118x118/D15904/FFFFFF&text=D15904) ![](http://placehold.it/118x118/31ABD4/FFFFFF&text=31ABD4) ![](http://placehold.it/118x118/007397/FFFFFF&text=007397) ![](http://placehold.it/118x118/0F1620/FFFFFF&text=0F1620)


KPCC Deep Orange: #D15904
KPCC Blue: #31ABD4
KPCC Deep Blue: #007397
KPCC Dark Blue: #0F1620

#### Neutral Colors

KPCC has two sets of neutral colors - warm and cool. Cool neutrals should be used for contexts that call for more austerity and formality - especially useful in editorial contexts. The warm neutrals are best for situations where we need to convey greater intimacy, personality and emotional connection.

##### Warm Neutrals
![](http://placehold.it/118x118/EDF2F4/FFFFFF&text=EDF2F4) ![](http://placehold.it/118x118/DEE4E5/FFFFFF&text=DEE4E5) ![](http://placehold.it/118x118/B5BEC0/FFFFFF&text=B5BEC0) ![](http://placehold.it/118x118/6C7579/FFFFFF&text=6C7579) ![](http://placehold.it/118x118/222628/FFFFFF&text=222628)

Near White: #EDF2F4; Light Gray: #DEE4E5; Medium Gray: #B5BEC0; Deep Gray: #6C7579; Dark Gray: #222628

##### Cool Neutrals

![](http://placehold.it/118x118/F6F6F6/FFFFFF&text=F6F6F6) ![](http://placehold.it/118x118/E8E8E8/FFFFFF&text=E8E8E8) ![](http://placehold.it/118x118/898989/FFFFFF&text=898989) ![](http://placehold.it/118x118/363636/FFFFFF&text=363636) ![](http://placehold.it/118x118/212121/FFFFFF&text=212121)

Near White: #F6F6F6; Light Gray: #E8E8E8; Medium Gray: #898989; Deep Gray: #363636; Dark Gray: #212121


###Fonts

	- Used in stories for h2 tags: font-family: "merriweatherbold", "Baskerville", "Garamond", "Cambria", Georgia, serif;
	- Used in stories for main text: "font-family: "merriweatherregular", "Baskerville", "Garamond", "Cambria", Georgia, serif;"
	- Used in stories as title: font-family: "freight-sans-pro", "Avenir Next", "Avenir", "Lucida Grande", "Corbel", "Tahoma", Arial, sans-serif;
	- Projects titles: font-family: proxima-nova, 'Helvetica Neue', Helvetica, Arial, sans-serif;
	- Projects description: font-family: proxima-nova, 'Helvetica Neue', Helvetica, Arial, sans-serif;



- Font size
	- TK

## General principles
- Collaborate on reporting, stories or projects with reporters.
- Offer advice on how to request records and data, find and clean datasets and check findings.
- Brainstorm how to present findings and data whether in a narrative or visual form.
- Recommend data to use to make apples-to-apples comparisons, data sources to shy away from and how to understand limitations.
- Request records and data, find and clean datasets and check findings when required.
- Offer insight about the things that don't lead to stories and how we do work.
- Ask "Who is our audience?", "What do they need?" and "What can we make?"
- [Humanize data](https://source.opennews.org/en-US/learning/connecting-dots/)

## Chartbuilder
KPCC's [chartbuilder tool](http://projects.scpr.org/internal/tools/kpcc-chartbuilder/), adapted [from Quartz](http://quartz.github.io/Chartbuilder/), quickly makes four simple types of charts: line, column, bar grid and scatter.

**Advantages**
- Easy
- Fast
- HTML data tables

**Drawbacks**
- Static images
- Limited color palette
- No interactivity

Use cases:
- Reporter at large: Many reporters and editors are already using Chartbuilder.
- Data team: Effective tool for many visualizations.

## R
The [open source programming language R](http://www.r-project.org/) can visualize large, complex datasets. It's something the KPCC data team uses internally in analyzing data.

Those visualizations can be adapted for publication. Packages like [ggplot2](http://ggplot2.org/) and [ggthemes](https://github.com/jrnold/ggthemes) can be used to get those images ready for primetime. We recently [featured R visualizations in a story](http://www.scpr.org/news/2015/02/18/49905/water-main-break-submerges-vehicles-in-hollywood/) for the first time.

Standards for our R visualizations are a work in progress. Those can be found here[TK--R standards], along with sample of R code for spitting out viz.

**Advantages**
- Can adapt visualizations created during [EDA](http://en.wikipedia.org/wiki/Exploratory_data_analysis)
- Highly customizable

**Drawbacks**
- Static images
- Legends are tricky
- Steep learning curve

Use cases:
- Data team: tool for complex, customized visualizations.


## Interactive charting
Some charts benefit from an interactive treatment, allowing users to dive deeper into the data and look up specific informaiton. Creating a one-off for every project isn't possible, but some of those one-offs can become models that we can plug new data into for new stories.

There are myriad options out there for creative interactive charts.

Advantages and disadvantages are highly case-specific to the chart and code behind it. The Chartist javascript library is broken down below.

###Chartist

We have recently used [the Chartist javascript library](http://gionkunz.github.io/chartist-js/) to create a [line graph](http://projects.scpr.org/charts/metro-on-time-performance/rail-performance/) and a [bar chart](http://projects.scpr.org/applications/monthly-water-use/).

If/as the the Chartist library develops, it may make sense to create a tool that would allow the web team to plug in data and create responsive charts.

**Advantages**
- Responsive
- Mobile-friendly
- Clean design
- Highly customizable
- Interactivity

**Drawbacks**
- Still being developed
- No built-in legends
- Coding knowledge a must

Use cases:
- Data team: Highly customizable charts
- Web team: Can use in future

## Maps/gifs/Data table

### Interactive maps

### Static maps/gifs
A couple recent stories have featured a static map (to indicate the radius that a study covered) and a gif (to display 10 different bus lines)

For both, I exported images from QGIS, using the Stamen Terrain layer as the background. I like that particular Stamen map as it does a nice job of indentifying cities and neighborhoods, which hopefully helps the user orient him/herself.













