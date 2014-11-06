# 2014-la-county-general-election-results

* **WHAT**: General election results from LA County for the Nov. 4, 2014 primary.
    * Results for each race available by:
        * [pre-certified-results]()
            * [results-by-precinct]()
* **HOW ACQUIRED**: Downloaded from the [LA County Registrar/Recorder](http://www.lavote.net/home/voting-elections/election-resources/past-elections/past-election-results#Nov42014)
* **NOTES**: Converted from original .xls files to .csv using csvkit and the following commands.
    * Change the file permissions

            chmod -R 777 .

    * Convert .xls to .csv using csvkit

            for file in *.xls ; do in2csv $file > _$file | mv _$file `echo _$file | sed 's/\(.*\.\)xls/\1csv/'` ; done