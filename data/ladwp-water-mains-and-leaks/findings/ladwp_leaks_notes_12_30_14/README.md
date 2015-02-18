Notes (12/30/14)
================

* Garcetti's [Earthquake report](http://projects.scpr.org/documents/?doc=1376566-dec-8-2014-garcetti-earthquake-report) paints a stark picture of how the city's water infrastructure would fare in an earthquake: "the water system is the utility most vulnerable to earthquake damage, and that damage could be the largest cause of economic disruption following an earthquake"

* Locally, the DWP's 7,000 miles of pipe are "vulnerable from seismic shaking" from even small earthquakes.

* The solution: earthquake resistant ductile iron pipes (ERDIP). The problem: we don't have any. LADWP spokesperson says "we don't have a statistically significant amount of earthquake resilient pipe at this time." Building with those would make pipe projects 10-20% more expensive.

* The pipes we have now are getting old and breaking. Of the breaks in our dataset, here is when the broken pipes were originally installed. A single pipe that broke twice would be counted twice here. Many of them are from the 1920s
![](https://github.com/SCPR/kpcc-data-team/blob/aaron-dev/data/ladwp-water-mains-and-leaks/findings/ladwp_leaks_notes_12_30_14/images/year_installed_for_mains_with_leaks.png)

* Below is when all the pipes in the system were installed. Notice that there were big booms of pipe-building the 1920s, and from the 50s through the 70s (the colors here reflect the "likelihood of failure" grade that the DWP gives its pipes. Darker is worse)
![](https://github.com/SCPR/kpcc-data-team/blob/aaron-dev/data/ladwp-water-mains-and-leaks/findings/ladwp_leaks_notes_12_30_14/images/year_installed_by_likelihood_of_failure.png)

* The majority of pipes are graded C or worse by the LADWP for their "likelihood of failure". C means "medium likelihood of failure"—and that doesn't even factor in the risks posed by an earthquake.

* Finally, our pipes ain't getting any younger. You can see from this graph that several are approaching the end of their "useful life" (as defined by the DWP). The line here is the end of "useful life". Some are past it, and there are many pipes approaching that line:
![](https://github.com/SCPR/kpcc-data-team/blob/aaron-dev/data/ladwp-water-mains-and-leaks/findings/ladwp_leaks_notes_12_30_14/images/remaining_years_of_useful_life.png)

* The bottom line is that our pipes would take a big hit in an earthquake, but that they're vulnerable to failures and leaks even without one. The solution posed by the report is to build new, resilient pipes. But we're not building much of anything right now.

Reproducing these graphs (2/18/15)
================
* Following [a significant water main break in February, 2015](http://www.scpr.org/news/2015/02/18/49905/water-main-break-submerges-vehicles-in-hollywood/), I revisited earlier work to reproduces these graphs for use on the KPCC website. 

* I used the statistical program R. You can reproduce these graphs yourself using the data in this repo.

```R
# used Main_Leaks_2010_to_Current_date file with TWENTIES column
```mains <- Main_Leaks_2010_to_Current_date```

# turned TWENTIES vector into factors...necessary for this chart
```mains$TWENTIES <- as.factor(mains$TWENTIES)```

# plotted chart using ggplot library, which I make use of again later
```library(ggplot2)```
```hist_color <- ggplot(mains, aes(x=YR_INST, fill=TWENTIES)) + geom_bar(binwidth = 1) + xlim(1880,2015)  + scale_fill_manual(values = c("0" = "#5ABBDC", "1" = "#2788A9")) + ggtitle("When L.A.'s broken pipes were installed") + ylab("Number of leaks") + xlab("Year pipe was installed (1920s are in dark blue)") + theme(legend.position = "none")```
```plot(hist_color)```


## second chart
```REDACTED.CPRAMainlines <- read.csv("~/Desktop/projects/_inactive/watermain/data/LADWP_pipes/all_mains_trunks/REDACTED CPRAMainlines.csv")```
```REDACTED.CPRATrunkLine <- read.csv("~/Desktop/projects/_inactive/watermain/data/LADWP_pipes/all_mains_trunks/REDACTED CPRATrunkLine.csv")```

# rename columns for user friendliness
```colnames(REDACTED.CPRAMainlines)[33] <- "Grade"```
```colnames(REDACTED.CPRATrunkLine)[17] <- "Grade"```

# reformat and then add mains and trunks together.
```trunks_lof <- list(REDACTED.CPRATrunkLine$PIPE_PLR_Y,REDACTED.CPRATrunkLine$Grade)```
```mains_lof <- list(REDACTED.CPRAMainlines$PIPE_PLR_YEAR,REDACTED.CPRAMainlines$Grade)```
```mains_df <- as.data.frame(mains_lof)```
```trunks_df <- as.data.frame(trunks_lof)```
```colnames(mains_df) <- c("Year", "Grade")```
```colnames(trunks_df) <- c("Year", "Grade")```
```lof_df <- rbind(mains_df, trunks_df)```

## plot it
```ggplot(lof_df, aes(x=Year, fill=Grade)) + geom_bar(binwidth = 1) + scale_fill_manual(values = c("A" = "#ADDDED", "B" = "#6FC4E0", "C" = "#31aad3", "D" = "#227794", "F" = "#144454")) + xlim(1880,2015) + ggtitle("Grading the likelihood of failure of LADWP's pipes") + ylab("Number of pipes") + xlab("Year pipes were installed")```


## Third chart can use same data frame as first chart, but here have as different name for clarity
# add years beyond useful life column and T/F
```REDACTED.CPRAMainlines$BEYONDUSEFUL <- REDACTED.CPRAMainlines$AGE - REDACTED.CPRAMainlines$UL```
```REDACTED.CPRAMainlines$lifeleft <- REDACTED.CPRAMainlines$BEYONDUSEFUL <= 0```

# plot
```beyond_hist <- ggplot(REDACTED.CPRAMainlines, aes(x=BEYONDUSEFUL, fill=lifeleft)) + geom_bar(binwidth = 1) + xlim(-125,100) + scale_fill_manual(values = c("TRUE" = "#6FC4E0", "FALSE" = "#227794")) + ggtitle("How close are LADWP's pipes to the end of their 'useful life'?") + ylab("Number of pipes") + xlab("Years beyond useful life. Below 0 (light blue) indicates more years of useful life remain") + theme(legend.position = "none")```
```plot(beyond_hist)```
```