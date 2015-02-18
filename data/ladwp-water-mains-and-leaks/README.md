ladwp-water-mains-and-leaks
===========================

What
====

* Data acquired from the LADWP in 2014. There are three seperate csv files.

	* [```main_leaks_2010_to_partial_2014.csv```](https://github.com/SCPR/kpcc-data-team/blob/master/data/ladwp-water-mains-and-leaks/documented-leaks/main_leaks_2010_to_partial_2014.csv) contains information about leaks.
        * 1 header row + 5,238 records
        * spans Jan. 2010 to Nov. 2014

	* [```REDACTED_CPRA_Mainlines.csv```](https://github.com/SCPR/kpcc-data-team/blob/master/data/ladwp-water-mains-and-leaks/all_mains_trunks/REDACTED_CPRA_Mainlines.csv) contains information about mains in the system
        * 1 header row + 261,501 records

	* And [```REDACTED_CPRA_TrunkLine.csv```](https://github.com/SCPR/kpcc-data-team/blob/master/data/ladwp-water-mains-and-leaks/all_mains_trunks/REDACTED_CPRA_TrunkLine.csv) contains informaiton about trunks in the system.
        * 1 header row + 13,561 records

* ```REDACTED_CPRA_Mainlines.csv``` and ```REDACTED_CPRA_TrunkLine.csv``` were provided with location information redacted. Documentation was provided for the latter two csv files, but not for the leaks csv. Per an LADWP spokeswoman, "pipes larger than 20” in diameter are considered trunklines. Pipes smaller than that are mainlines."

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

        * [```REDACTED_CPRA_Mainlines.csv contains```](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_Mainlines.csv) - 1 header row + 261,501 records

        * [```REDACTED_CPRA_TrunkLine.csv```](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_TrunkLine.csv) - 1 header row + 13,561 records

    * Using the link, you will use the ```curl``` command to download the data and output it to a file.

        * The format is curl <url to csv file> > <name of csv file you're saving>

        * For example:

                curl https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/main_leaks_2010_to_partial_2014.csv > main_leaks_2010_to_partial_2014.csv

                curl https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_Mainlines.csv > REDACTED_CPRA_Mainlines.csv

                curl https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/documented-leaks/REDACTED_CPRA_TrunkLine.csv > REDACTED_CPRA_TrunkLine.csv

    * You're now ready to work with these file in Excel, R or your application of choice.