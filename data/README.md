### KPCC/SCPR Data

A repository containing datasets, information and other goodies from KPCC/SCPR

* **[OpenData LA](https://github.com/SCPR/opendata-la-watchdog)**

    * **WHAT**: Using code created by the [Los Angeles Times Data Desk](https://github.com/datadesk) and its [Checkbook LA Watchdog project](https://github.com/datadesk/checkbook-la-watchdog), this is a "periodically updated archive of data" published by the city of Los Angeles on its [open data portal](https://data.lacity.org/).

    * **HOW ACQUIRED**: [Python script](https://github.com/SCPR/opendata-la-watchdog/blob/master/watchdog.py) will download each dataset.

* **[2014-la-county-certified-primary-results](https://github.com/SCPR/kpcc-data-team/tree/master/data/2014-la-county-certified-primary-results)**

    * **WHAT**: Certified results from LA County for the June 3, 2014 primary.

    * **HOW ACQUIRED**: Purchased from the LA County Registrar/Recorder for $54.00

    * **NOTES**: Converted from original .xls files to .csv using csvkit and the following commands.

        * Change the file permissions

                chmod -R 777 .

        * Convert .xls to .csv using csvkit

                for file in *.xls ; do in2csv $file > _$file | mv _$file `echo _$file | sed 's/\(.*\.\)xls/\1csv/'` ; done

* **[2014-la-county-general-election-results](https://github.com/SCPR/kpcc-data-team/tree/master/2014-la-county-general-election-results)**

    * **WHAT**: General election results from LA County for the Nov. 4, 2014 primary.

        * Results for each race available by:

            * [pre-certified-results](https://github.com/SCPR/kpcc-data-team/tree/master/2014-la-county-general-election-results/pre-certified-results)

                * [results-by-precinct](https://github.com/SCPR/kpcc-data-team/tree/master/2014-la-county-general-election-results/pre-certified-results/results-by-precinct)

    * **HOW ACQUIRED**: Downloaded from the [LA County Registrar/Recorder](http://www.lavote.net/home/voting-elections/election-resources/past-elections/past-election-results#Nov42014)

    * **NOTES**: Converted from original .xls files to .csv using csvkit and the following commands.

        * Change the file permissions

                chmod -R 777 .

        * Convert .xls to .csv using csvkit

                for file in *.xls ; do in2csv $file > _$file | mv _$file `echo _$file | sed 's/\(.*\.\)xls/\1csv/'` ; done

* **[la-county-voter-turnout-historic](https://github.com/SCPR/kpcc-data-team/tree/master/la-county-voter-turnout-historic)**

    * **WHAT**: Dates, registration, ballots cast, turnout and source data for midterm primary and general elections in Los Angeles County between 1942 and 2014.

    * **HOW ACQUIRED**: Acquired via [available data](http://apps1.lavote.net/General/ARCHIVES/OFFICIAL_ELECTION_RETURNS/Default.cfm) on the LA County Registrar/Recorder website

    * **NOTES**:
        * Registered voters not available for elections between 1942 and 1958.
        * Turnout figures not available for elections between 1942 and 1950; the 1954 midterm primary ; the 1958 midterm primary.

* **[2014-ca-election-tweets](https://github.com/SCPR/kpcc-data-teama/tree/master/2014-ca-election-tweets)**

    * **WHAT**: Tweets that used the hashtag #CAElection and #CAElections between 8 a.m. on Nov. 4, 2014 and 12:10 a.m. on Nov. 5, 2014.

    * **HOW ACQUIRED**: Pulled using the Twitter API.