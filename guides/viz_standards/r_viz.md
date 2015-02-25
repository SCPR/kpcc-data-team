## Visualizing information with R
The [statistical program R](http://www.r-project.org/) can visualize large, complex datasets. It's something the KPCC data team uses internally in analyzing data, and that we've used on our website before.

## Guidelines
- Colors
- Font
- Font size
- Legends
- Chart types/gallery/code examples

## Improvements
Tools exist to make web-friendly, interactive versions of R plots. A few of these are featured on [htmlwidgets for R](http://www.htmlwidgets.org/showcase_leaflet.html), including time series and scatterplots. [Shiny](http://shiny.rstudio.com/) is another option. To my knowledge, neither features responsive charting.

## Histogram
This is the code we used to visualize the likelihood of failure in LADWP pipes, as assessed by the department itself. This is a complicated example; elements could be stripped away from the code to produce a simpler graph (i.e. one without colors). I recommend avoiding 'xlim' (and its cousin) 'ylim' as a rule, but in this case it was helpful to exclude outliers.

It draws on the ggplot2 library, [documentation for which can be found here](http://docs.ggplot2.org/current/).

```ggplot(lof_df, aes(x=Year, fill=Grade)) + geom_bar(binwidth = 1) + scale_fill_manual(values = c("A" = "#ADDDED", "B" = "#6FC4E0", "C" = "#31aad3", "D" = "#227794", "F" = "#144454")) + xlim(1880,2015) + ggtitle("Grading the likelihood of failure of LADWP's pipes") + ylab("Number of pipes") + xlab("Year pipes were installed")```

And here's what that looked like![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/findings/ladwp_leaks_notes_12_30_14/images/year_installed_by_likelihood_of_failure.png)

For good measure, here is a code for a further customized chart:

```ggplot(lof_df, aes(x=Year, fill=Grade)) + geom_bar(binwidth = 1) + scale_fill_manual(values = c("A" = "#ADDDED", "B" = "#6FC4E0", "C" = "#31aad3", "D" = "#227794", "F" = "#144454")) + xlim(1880,2015) + ggtitle("Grading the likelihood of failure of LADWP's pipes") + ylab("Number of pipes") + xlab("Year pipes were installed") + theme(text = element_text(size=20), axis.text.x = element_text(angle=90, vjust=1))```


