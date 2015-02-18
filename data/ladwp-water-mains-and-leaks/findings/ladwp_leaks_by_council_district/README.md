LADWP water main leaks by council district
===============================

* No surprise that two of the oldest parts of the city have had the most water main breaks. When grouped by city council district, Council District 4 - which is up in this spring's primary - had the most. Council district 5 came in right behind. Both in are older parts of the city, and are two larger council districts.

![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/findings/ladwp_leaks_by_council_district/ladwp_leaks_by_council_district_all.png)

![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/master/data/ladwp-water-mains-and-leaks/findings/ladwp_leaks_by_council_district/ladwp_leaks_by_council_district_4.png)

* The data contains 5,238 leaks recorded by DWP, and spans Jan. 2010 to Nov. 2014. About 345 records could not be plotted against the council districts.

### By council district

| district | count |
|----------|-------|
| 4        | 782   |
| 5        | 774   |
| 10       | 443   |
| 11       | 433   |
| 13       | 376   |
| 8        | 370   |
| 12       | 310   |
| 14       | 298   |
| 3        | 270   |
| 1        | 266   |
| 15       | 158   |
| 7        | 113   |
| 6        | 92    |
| 2        | 89    |
| 9        | 66    |


### By year installed - District 4

| Year       | Count |
|------------|-------|
| 1927       | 88    |
| 1926       | 66    |
| 1924       | 60    |
| 1923       | 46    |
| 1928       | 41    |
| 1929       | 38    |
| 1920       | 25    |
| 1922       | 24    |
| 1925       | 24    |
| 1915       | 18    |
| 1954       | 17    |
| 1930       | 15    |
| 1931       | 15    |
| 1946       | 14    |
| 1934       | 12    |
| 1937       | 12    |


### By type of pipe - District 4

| Type        | Count   |
|-------------|---------|
| A.C.        | 4       |
| C.I.        | 433     |
| CONCRETE    | 1       |
| COPPER      | 10      |
| D.I.        | 6       |
| GALV        | 2       |
| MONO        | 1       |
| PLASTIC     | 3       |
| RIBBOUT     | 1       |
| STEEL       | 311     |
| blank       | 10      |
| Grand Total | 772     |


### By size of pipe - District 4

| Size       | Count |
|------------|-------|
| 6          | 344   |
| 4          | 219   |
| 8          | 115   |
| 2          | 41    |
| 12         | 29    |
| 16         | 8     |
| 20         | 4     |


### By cause of leak - District 4

| Cause            | Count |
|------------------|-------|
| RUST HOLE        | 267   |
| SPLIT            | 131   |
| ROUND CRACK      | 100   |
| RUPTURE          | 36    |
| CLAMP            | 33    |
| JOINT            | 16    |
| RUST HOLE, SPLIT | 11    |
| COUPLING         | 6     |
| CLAMP, RUST HOLE | 4     |

How We Got Here
================

### Get the data

* Change to the project directory

        cd /Volumes/one_tb_hd/_programming/2kpcc/_kpcc-data-team/data/ladwp-water-mains-and-leaks

* Download [LA Times neighborhood boundaries](http://boundaries.latimes.com/sets/).

* Unzip the file and move the zip file to ```_raw_data``` directory

        mkdir _raw_gis_data
        mkdir _working_data
        unzip la-county-neighborhoods-v6.zip -d _working_data
        mv la-county-neighborhoods-v6.zip _raw_gis_data

### Create the database

* **[Loading Shapefile into Postgres](http://www.gistutor.com/postgresqlpostgis/4-beginner-postgresqlpostgis-tutorials/18-importing-shapefile-gis-data-into-postgresql.html)**

    * Database should have been created, but if not... Create a new database. Add the PostGIS extension to it. Check to make sure it worked

            createdb kpcc_shapes
            psql kpcc_shapes -c "CREATE EXTENSION postgis;"
            psql kpcc_shapes
            select postgis_lib_version();

### Load neighborhood boundaries

* Create sql statement for shapefile

    * Template is: shp2pgsql -s <SRID> <shapefile> <tablename> <db_name> > filename.sql

            shp2pgsql -s 4269 /Volumes/one_tb_hd/_programming/2kpcc/_kpcc-data-team/data/ladwp-water-mains-and-leaks/_working_data/la-county-neighborhoods-v6/la_county_neighborhood_v6.shp _v6_la-county-neighborhoods kpcc_shapes > /Volumes/one_tb_hd/_programming/2kpcc/_kpcc-data-team/data/ladwp-water-mains-and-leaks/la-county-neighborhoods-v6.sql

* Load sql file into Postgres

    * Template is: psql -d gisdatabase –U username –h hostname –p port -f parcels.sql

            psql -d kpcc_shapes -f /Volumes/one_tb_hd/_programming/2kpcc/_kpcc-data-team/data/ladwp-water-mains-and-leaks/la-county-neighborhoods-v6.sql

* Move the sql file into the ```_working_data``` directory

        mv la-county-neighborhoods-v6.sql _working_data

### Load city council district boundaries

* Create sql statement for shapefile

    * Template is: shp2pgsql -s <SRID> <shapefile> <tablename> <db_name> > filename.sql

            shp2pgsql -s 4269 /Volumes/one_tb_hd/_programming/2kpcc/_kpcc-data-team/data/ladwp-water-mains-and-leaks/_working_data/la-city-council-districts-2012/la_city_council_district_2012.shp la_city_council_district_2012 kpcc_shapes > /Volumes/one_tb_hd/_programming/2kpcc/_kpcc-data-team/data/ladwp-water-mains-and-leaks/_working_data/la-city-council-districts-2012-v6.sql

* Load sql file into Postgres

    * Template is: psql -d gisdatabase –U username –h hostname –p port -f parcels.sql

            psql -d kpcc_shapes -f /Volumes/one_tb_hd/_programming/2kpcc/_kpcc-data-team/data/ladwp-water-mains-and-leaks/_working_data/la-city-council-districts-2012-v6.sql

* Move the sql file into the ```_working_data``` directory

        mv la-county-neighborhoods-v6.sql _working_data

### Load the leak data



