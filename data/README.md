Selected data we've gathered and worked with
============================================

A repository containing datasets, information and other goodies from KPCC/SCPR

* **[OpenData LA](https://github.com/SCPR/opendata-la-watchdog)**
    * **WHAT**: Using code created by the [Los Angeles Times Data Desk](https://github.com/datadesk) and its [Checkbook LA Watchdog project](https://github.com/datadesk/checkbook-la-watchdog), this is a "periodically updated archive of data" published by the city of Los Angeles on its [open data portal](https://data.lacity.org/).
    * **HOW ACQUIRED**: [Python script](https://github.com/SCPR/opendata-la-watchdog/blob/master/watchdog.py) will download each dataset.

* **[2014-04-bike-gis](/data/2014-04-bike-gis)**
    * **WHAT**: GIS of bikeways in the city of Los Angeles
    * **HOW ACQUIRED**: LADOT sent over email. Their GIS is superior to the data [kept by Metro](http://developer.metro.net/introduction/bikeways-data/download-bikeways-data/)

* **[2014-07-mwd-turf-removal-by-zipcode](/data/2014-07-mwd-turf-removal-by-zipcode)**
    * **WHAT**:
    * **HOW ACQUIRED**:

* **[2014-ca-election-tweets](/data/2014-ca-election-tweets)**
    * **WHAT**: Tweets that used the hashtag #CAElection and #CAElections between 8 a.m. on Nov. 4, 2014 and 12:10 a.m. on Nov. 5, 2014.
    * **HOW ACQUIRED**: Pulled using the Twitter API.

* **[2014-la-county-certified-primary-results](/data/2014-la-county-certified-primary-results)**
    * **WHAT**: Certified results from LA County for the June 3, 2014 primary.
    * **HOW ACQUIRED**: Purchased from the LA County Registrar/Recorder for $54.00
    * **NOTES**: Converted from original .xls files to .csv using csvkit and the following commands.
        * Change the file permissions
                chmod -R 777 .
        * Convert .xls to .csv using csvkit
                for file in *.xls ; do in2csv $file > _$file | mv _$file `echo _$file | sed 's/\(.*\.\)xls/\1csv/'` ; done

* **[2014-la-county-general-election-results](/data/2014-la-county-general-election-results)**
    * **WHAT**: General election results from LA County for the Nov. 4, 2014 primary.
        * Results for each race available by:
            * pre-certified [results-by-precinct](data/2014-la-county-general-election-results/pre-certified-results/results-by-precinct)
    * **HOW ACQUIRED**: Downloaded from the [LA County Registrar/Recorder](http://www.lavote.net/home/voting-elections/election-resources/past-elections/past-election-results#Nov42014)
    * **NOTES**: Converted from original .xls files to .csv using csvkit and the following commands.
        * Change the file permissions
                chmod -R 777 .
        * Convert .xls to .csv using csvkit
                for file in *.xls ; do in2csv $file > _$file | mv _$file `echo _$file | sed 's/\(.*\.\)xls/\1csv/'` ; done

* **[2015-ca-pipeline-data](/data/2015-ca-pipeline-data)**
    * **WHAT**:
    * **HOW ACQUIRED**:

* **[2015-dwp-claims](/data/2015-dwp-claims)**
    * **WHAT**: Data on claims paid out by the LADWP
    * **HOW ACQUIRED**: CPRA requests

* **[2015-nfl-stadiums](/data/2015-nfl-stadiums)**
    * **WHAT**: Information on football stadiums, including when they were built or renovated, how much they cost, how much of the funding was private, the capacity, and the geocoded location. Most notably, I adjusted for inflation so that stadium costs over time could be compared.
    * **HOW ACQUIRED**: Various sources (detailed at link), including academic, a csv on Github, and the BLS

* **[2015-ocb-data](/data/2015-ocb-data)**
    * **WHAT**: Gifs featured in 2 KPCC stories on graffiti reports and abatement in Los Angeles
    * **HOW ACQUIRED**: A large dataset was analyzed in the graffiti reporting, but at 734 MB it's too big for github. Email amendelsonATscprDOTorg if you would like to get it for yourself.

* **[2015-open-data-contracts](/data/2015-open-data-contracts)**
    * **WHAT**: Contracts between Southern California cities and counties and data portal vendors. "data_site_contracts.csv" collects much of the contract information.
    * **HOW ACQUIRED**: Series of public records requests to SoCal governments.

* **[la-county-voter-turnout-historic](/data/la-county-voter-turnout-historic)**
    * **WHAT**: Dates, registration, ballots cast, turnout and source data for midterm primary and general elections in Los Angeles County between 1942 and 2014.
    * **HOW ACQUIRED**: Acquired via [available data](http://apps1.lavote.net/General/ARCHIVES/OFFICIAL_ELECTION_RETURNS/Default.cfm) on the LA County Registrar/Recorder website
    * **NOTES**:
        * Registered voters not available for elections between 1942 and 1958.
        * Turnout figures not available for elections between 1942 and 1950; the 1954 midterm primary ; the 1958 midterm primary.

* **[ladwp-water-mains-and-leaks](/data/ladwp-water-mains-and-leaks)**
    * **WHAT**: Data on water main leaks and breaks.
    * **HOW ACQUIRED**: Provided by the LADWP in response to CPRA and email requests

* **[metro-on-time-performance](/data/metro-on-time-performance)**
    * **WHAT**: Monthly summaries of the 'on-time performance' of each Metro line (bus and rail), spanning five years.
    * **HOW ACQUIRED**: CPRA to the Metro records division
