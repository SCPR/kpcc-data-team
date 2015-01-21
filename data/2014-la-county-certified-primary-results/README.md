2014-la-county-certified-primary-results
========================================

* **WHAT**: Certified results from LA County for the June 3, 2014 primary.
    * Results for each race available by:
        * [Voter precinct](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results/results-by-precinct)
        * District, such as:
            * [Board of Equalization](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results/results-by-district/by-board-of-equalization)
            * [Community](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results/results-by-district/by-community)
            * [Congressional District](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results/results-by-district/by-congressional-district)
            * [County Supervisor District](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results/results-by-district/by-county-supervisor-district)
            * [State Assembly District](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results/results-by-district/by-state-assembly-district)
            * [State Senate District](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results/results-by-district/by-state-senate-district)
* **HOW ACQUIRED**: Purchased from the LA County Registrar/Recorder for $54.00
* **NOTES**: Converted from original .xls files to .csv using csvkit and the following commands.
    * Change the file permissions

            chmod -R 777 .

    * Convert .xls to .csv using csvkit

            for file in *.xls ; do in2csv $file > _$file | mv _$file `echo _$file | sed 's/\(.*\.\)xls/\1csv/'` ; done