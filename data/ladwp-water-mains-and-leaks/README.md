ladwp-water-mains-and-leaks
===========================

What
====

* Data acquired from the LADWP in 2014. There are three seperate csv files.

	* [```main_leaks_2010_to_partial_2014.csv```](https://github.com/SCPR/kpcc-data-team/blob/master/data/ladwp-water-mains-and-leaks/documented-leaks/main_leaks_2010_to_partial_2014.csv) contains information about leaks

	* [```REDACTED_CPRA_Mainlines.csv contains```](https://github.com/SCPR/kpcc-data-team/blob/master/data/ladwp-water-mains-and-leaks/all_mains_trunks/REDACTED_CPRA_Mainlines.csv) information about mains in the system

	* And [```REDACTED_CPRA_TrunkLine.csv```](https://github.com/SCPR/kpcc-data-team/blob/master/data/ladwp-water-mains-and-leaks/all_mains_trunks/REDACTED_CPRA_TrunkLine.csv) contains informaiton about trunks in the system.

* The latter two files were provided with location information redacted. Documentation was provided for the latter two csv files, but not for the leaks csv. Per an LADWP spokeswoman, "pipes larger than 20” in diameter are considered trunklines. Pipes smaller than that are mainlines."

How Acquired
============

* Leaks csv was provided in response to a records request. The mains and trunks data were provided in response to questions to LADWP about the status of the system's pipes.

Working With The Data
=====================

* Assuming you're not working on a windows machine with a couple quick commands in the terminal you can download any of the csv files in this directory and begin working with them on your machine.

    * Open your terminal or command line application.
        * On MacOS open Spotlight and search for Terminal
    * Change to your Desktop or other directory where you keep files you are working on.
        * To reach the Desktop type ```cd ~/Desktop``` and press the enter key.

    * Make a new directory to hold the data files and change to it.

        * ```mkdir ladwp_water_mains```
        * ```cd ladwp_water_mains```

    * You will want to access the raw data files in the repository. The links are below:

        * [```main_leaks_2010_to_partial_2014.csv```](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/main_leaks_2010_to_partial_2014.csv)

        * [```REDACTED_CPRA_Mainlines.csv contains```](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_Mainlines.csv)

        * [```REDACTED_CPRA_TrunkLine.csv```](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_TrunkLine.csv)

    * Using the link, you will use the ```curl``` command to download the data and output it to a file.

        * The format is curl <url to csv file> > <name of csv file you're saving>

        * For example:

                curl https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/main_leaks_2010_to_partial_2014.csv > main_leaks_2010_to_partial_2014.csv

                curl https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_Mainlines.csv > REDACTED_CPRA_Mainlines.csv

                curl https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_TrunkLine.csv > REDACTED_CPRA_TrunkLine.csv

    * You're now ready to work with these file in Excel, R or your application of choice.

Notes (12/30/14)
================

* Garcetti's [Earthquake report](http://projects.scpr.org/documents/?doc=1376566-dec-8-2014-garcetti-earthquake-report) paints a stark picture of how the city's water infrastructure would fare in an earthquake: "the water system is the utility most vulnerable to earthquake damage, and that damage could be the largest cause of economic disruption following an earthquake"

* Locally, the DWP's 7,000 miles of pipe are "vulnerable from seismic shaking" from even small earthquakes.

* The solution: earthquake resistant ductile iron pipes (ERDIP). The problem: we don't have any. LADWP spokesperson says "we don't have a statistically significant amount of earthquake resilient pipe at this time." Building with those would make pipe projects 10-20% more expensive.

* The pipes we have now are getting old and breaking. Of the breaks in our dataset, here is when the broken pipes were originally installed. A single pipe that broke twice would be counted twice here. Many of them are from the 1920s
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/images/year_installed_for_mains_with_leaks.png)

* Below is when all the pipes in the system were installed. Notice that there were big booms of pipe-building the 1920s, and from the 50s through the 70s (the colors here reflect the "likelihood of failure" grade that the DWP gives its pipes. Darker is worse)
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/images/year_installed_by_likelihood_of_failure.png)

* The majority of pipes are graded C or worse by the LADWP for their "likelihood of failure". C means "medium likelihood of failure"—and that doesn't even factor in the risks posed by an earthquake.

* Finally, our pipes ain't getting any younger. You can see from this graph that several are approaching the end of their "useful life" (as defined by the DWP). The line here is the end of "useful life". Some are past it, and there are many pipes approaching that line:
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/images/remaining_years_of_useful_life.png)

* The bottom line is that our pipes would take a big hit in an earthquake, but that they're vulnerable to failures and leaks even without one. The solution posed by the report is to build new, resilient pipes. But we're not building much of anything right now.
