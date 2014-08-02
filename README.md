# KPCC/SCPR Data

A repository containing datasets, information and other goodies from KPCC/SCPR

* **[2014-la-county-certified-primary-results](https://github.com/SCPR/data/tree/master/2014-la-county-certified-primary-results)**
    * **WHAT**: Certified results from LA County for the June 3, 2014 primary.
    * **HOW ACQUIRED**: Purchased from the LA County Registrar/Recorder for $54.00
    * **NOTES**: Converted from original .xls files to .csv using csvkit and the following commands.
        * Change the file permissions

                chmod -R 777 .

        * Convert .xls to .csv using csvkit

                for file in *.xls ; do in2csv $file > _$file | mv _$file `echo _$file | sed 's/\(.*\.\)xls/\1csv/'` ; done