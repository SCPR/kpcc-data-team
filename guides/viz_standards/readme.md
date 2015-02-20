## Visualizing information

Charts can be an effective and engaging way of displaying quantitative information. They can also be [total garbage](http://viz.wtf/). How can we make sure our charts stay on the right side of [the thin line between clever and stupid](https://www.youtube.com/watch?v=wtXkD1BC564)?

Here are some general principles we will keep in mind in making charts.

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
The [statistical program R](http://www.r-project.org/) can visualize large, complex datasets. It's something the KPCC data team uses internally in analyzing data.

Those visualizations can be adapted for publication. Packages like [ggplot2](http://ggplot2.org/) and [ggthemes](https://github.com/jrnold/ggthemes) can be used to get those images ready for primetime. We recently [featured R visualizations in a story](http://www.scpr.org/news/2015/02/18/49905/water-main-break-submerges-vehicles-in-hollywood/) for the first time.

Standards for our R visualizations are a work in progress. Those can be found here[TK--R standards], as well R code for spitting out viz.

**Advantages** 
- Can adapt visualizations created during [EDA](http://en.wikipedia.org/wiki/Exploratory_data_analysis)
- Highly customizable

**Drawbacks** 
- Static images
- Legends are tricky
- Steep learning curve; only 2 people in news room have any familiarity with R

Use cases:
- Data team: Effective tool for complex, customized visualizations.


## Interactive charting
Some stories and data sets benefit from an interactive treatment, allowing users to dive deeper into the data and look up specific informaiton. 

There are myriad options out there for creative interactive charts. In creating an interactive—especially from scratch—we will be mindful of the amount of time required. Creating a one-off for every project isn't possible, but some of those one-offs can become models that we can plug new data into for new stories.

Advantages and disadvantages are highly case-specific to the chart and code behind it.

Chartist
--------
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







