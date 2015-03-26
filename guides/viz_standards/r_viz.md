## Visualizing information with R
The [statistical program R](http://www.r-project.org/) can visualize large, complex datasets. It's something the KPCC data team uses internally in analyzing data, and that we've used to create charts on our website.

## Guidelines
- Colors
- Font
- Font size
- Legends

##Making Charts in R
This section will demonstrate how to make various charts using R.

### Histogram
This is the code we used to visualize the likelihood of failure in LADWP pipes, as assessed by the department itself. This is what that looked like![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/findings/ladwp_leaks_notes_12_30_14/images/year_installed_by_likelihood_of_failure.png) You may have seen a similar graph [elsewhere](http://graphics.latimes.com/la-aging-water-infrastructure/).


To reproduce the graph in R, let's start at the beginning by setting the working directory. Here, we will assume the working directory is the Desktop.

	setwd("~/Desktop/")

Next, let's bring in the amazing ggplot package, which we will draw on. You can find documentation for ggplot2 [here](http://docs.ggplot2.org/current/). You have to install it the first time you use it, but need to use the library command every time.

	install.packages("ggplot2")
	library(ggplot2)

Now we bring in the actual data. You can find that on Github [here](https://github.com/SCPR/kpcc-data-team/blob/master/data/ladwp-water-mains-and-leaks/all_mains_trunks/REDACTED_CPRA_Mainlines.csv). This might take a moment, since there are more than 260,000 rows in the data set. Note that we don't want our strings to be factors. [(Wait, what are strings and factors?)](http://www.stat.berkeley.edu/~nolan/stat133/Fall05/lectures/DataTypes4.pdf)

	mains <- read.csv("~/Desktop/REDACTED_CPRA_Mainlines.csv", stringsAsFactors=FALSE)

You'll always want to explore the data before you get too far down the road with charting.

	summary(mains)
	str(mains)

OK, now let's get started using ggplot. Our code is on the right of "<-" and by using the arrow we assign it to "hist". Our x axis will be "PIPE_PLR_YEAR", the year pipes were installed or incorporated into the LADWP system. Our x is simply how many pipes were installed in that year.

	hist <- ggplot(mains, aes(x=PIPE_PLR_YEAR)) + geom_bar(binwidth = 1)

Now plot that

	plot(hist)
	
Not quite what we want. Why are all the bars so far over?

If we go  back to summary(mains), you can see that the minimum value is 0. Huh? If we look even closer, there are pipes that this data tells us were installed in Los Angeles in 127 A.D. and 1066 A.D. (the year of the Battle of Hastings)	. Since the LADWP obviously wasn't installing pipes then, let's limit our histogram to any pipe installed between 1880 and 2014. That covers the vast majority of our data set.

	hist <- ggplot(mains, aes(x=PIPE_PLR_YEAR)) + geom_bar(binwidth = 1) + xlim(1880,2015)
	plot(hist)
	
Much better. But be careful with xlim (and its cousin ylim), which will exclude outliers from our chart. You need to understand your data (and clean it) *before* considering those.
	
Next, let's make sur  our bars correspond to one year per bar. The graph will look the same, but this is a good practice for our histogram.
	
	hist <- ggplot(mains, aes(x=PIPE_PLR_YEAR)) + geom_bar(binwidth = 1) + xlim(1880,2015)

Let's add a little color. Or "fill", as we'll see it called here. The LOF_GRADE vector represents the LADWP's assessed "likelihood of failure" for every pipe. By adding that color, we can see if pipes of a certain age are more likely to fail.

	hist <- ggplot(mains, aes(x=PIPE_PLR_YEAR, fill=LOF_GRADE)) + geom_bar(binwidth = 1) + xlim(1880,2015)
	plot(hist)

Woah, sure looks like that's the case. Don't really love this color scheme, though. When I think about pipes under the ground, rainbows aren't the first thing that comes to mind.

Let's do something a little more watery, using [a scale of blues](https://github.com/SCPR/kpcc-data-team/tree/aaron-dev/guides/viz_standards#general-charting-guidelines) based on the SCPR website colors.

	hist <- ggplot(mains, aes(x=PIPE_PLR_YEAR, fill=LOF_GRADE)) + geom_bar(binwidth = 1) + xlim(1880,2015) + scale_fill_manual(values = c("A" = "#ADDDED", "B" = "#6FC4E0", "C" = "#31aad3", "D" = "#227794", "F" = "#144454"))
	plot(hist)	

Let's also change the name of the LOF_GRADE vector. That way it'll appear differently in our legend.

	colnames(mains)[33] <- "Grade"

Alright, let's add a main title and labels for our x and y axes. That will help the reader--we can't assume she'll know what PIPE_PLR_YEAR means.

	hist <- ggplot(mains, aes(x=PIPE_PLR_YEAR, fill=Grade)) + geom_bar(binwidth = 1) + xlim(1880,2015) + scale_fill_manual(values = c("A" = "#ADDDED", "B" = "#6FC4E0", "C" = "#31aad3", "D" = "#227794", "F" = "#144454")) + xlim(1880,2015) + ggtitle("Grading the likelihood of failure of LADWP's pipes") + ylab("Number of pipes") + xlab("Year pipes were installed")
	plot(hist)

And that's what we published. With hindsight, however, we can improve on it.

The text is on the small side. The font doesn't look like the rest of the site. And it weirds me out that 0 isn't the bottom of this chart, it looks like the histogram is floating off the air.

	hist <- ggplot(mains, aes(x=PIPE_PLR_YEAR, fill=Grade)) + geom_bar(binwidth = 1) + xlim(1880,2015) + scale_fill_manual(values = c("A" = "#ADDDED", "B" = "#6FC4E0", "C" = "#31aad3", "D" = "#227794", "F" = "#144454")) + xlim(1880,2015) + ggtitle("Grading the likelihood of failure of LADWP's pipes") + ylab("Number of pipes") + xlab("Year pipes were installed") + theme_bw() +  theme(plot.background = element_blank() ,panel.grid.major = element_blank() ,panel.grid.minor = element_blank(),panel.border = element_blank()) + theme(text = element_text(size=18, family="Baskerville"))
	plot(hist)

Much nicer, no? I think this improves on the published version. ![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/aaron-dev/guides/viz_standards/images/watergrades.png)

### Facet wraps a.k.a small multiples
Lets make a facet wrap in R. These are also known as small multiples, and are great at showing how related things changed over time. Our example here is a dataset representing how often the Los Angeles Metro's trains showed up late. [In reality](http://projects.scpr.org/charts/metro-on-time-performance/rail-performance/), we visualized these on a single line chart. But a facet wrap could have been effective as well.

You can download that data [here](https://github.com/SCPR/kpcc-data-team/blob/master/data/metro-on-time-performance/ontime_performance_orig_documentation.xlsx). We'll get started with it by setting our working directory. That's the Desktop for this example. We'll also bring in the Excel file--R can even read those with the xlsx library.

	setwd("~/Desktop/")
	install.packages("xlsx")
	library(xlsx)
	transpo_late <- read.xlsx("~/Desktop/ontime_performance_orig_documentation.xlsx", sheetName = "Rail")

Let's plot out a line chart.

	ggplot(transpo_late, aes(Year, On.Time.pct, color = Line)) + geom_line()	

There we go! Wait...that actually looks terrible. That's because there are twelve entries per line each year. If you sub in geom_point() that will be much more clear.

We need to group the lines by year. That sounds like something you could do easily in SQL. Thankfully, there's a package that allows you to use SQL syntax in R, the awesome sqldf.

	install.packages("sqldf")
	library(sqldf)
	linebyyear <- sqldf("select Year, Line, sum(`Total.Trips`) as trips, sum(`Late.Trips`) as latetrips from transpo_late group by Line, Year")

That's better. Now we need to calculate the percentage of trips that arrived late.

	linebyyear$latepct <- (linebyyear$latetrips/linebyyear$trips)*100

If we redo the earlier line chart, it will now look better.
	
	ggplot(linebyyear, aes(Year, latepct, color = Line)) + geom_line()	
But we want these lines on separate charts, not all together. If Los Angeles' rail system was more established, we might not be able to make out the differences between 15 lines so easily.

So in that hopeful spirit, lets do our "facet wrap".

	ggplot(data=linebyyear, aes(x=Year, y=latepct)) + geom_line() + facet_wrap(~ Line)

There we go. That arguably gives a clearer picture of each rail line.
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/aaron-dev/guides/viz_standards/images/facet_trains_nocolor.png)

We can try to prettify this as well, though that should always be the last step. Do the real work first.

	ggplot(data=linebyyear, aes(x=Year, y=latepct, color=Line)) + ylab("Percent of trains that left stations late") + ggtitle("How late are LA's train lines?") + geom_line(lwd = 2, alpha=0.8) + facet_wrap(~ Line) + theme_bw() +  theme(plot.background = element_blank() ,panel.grid.major = element_blank() ,panel.grid.minor = element_blank(),panel.border = element_blank()) + theme(text = element_text(size=15, family="Baskerville")) + theme(axis.text.x = element_text(angle = 90, hjust = 1)) + scale_colour_manual(values = c("#0072bb", "#01a4e5", "#ffb715", "#6cc06b", "#ea1d24"))

Does that abstract our data too much?
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/aaron-dev/guides/viz_standards/images/facet_trains.png)

## Future Improvements
Tools exist to make web-friendly, interactive versions of R plots. A few of these are featured on [htmlwidgets for R](http://www.htmlwidgets.org/showcase_leaflet.html), including time series and scatterplots. [Shiny](http://shiny.rstudio.com/) and [plotly](https://plot.ly/r/) are other options. The [googleVis package](http://cran.r-project.org/web/packages/googleVis/vignettes/googleVis_examples.html) provides an interface to Google Charts. To my knowledge, none features responsive charting.

