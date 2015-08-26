California Pipeline Operator Scraper 
====================================

1. ```pip install requirements.txt```

2. Data taken from [here](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html) and a brief analysis can be found in our [data folder](https://github.com/SCPR/kpcc-data-team/tree/wcraft-dev/data/2015-ca-pipeline-data)

3. There are two datasets, one with data on pipeline incidents from operators within CA, and one and one for data on the number of miles and types of pipelines present in CA. The first dataset only has info on operators that have had pipes break, and the second gathers info on **all** pipeline operators in the US.  

4. The scripts can be easily modified to gather information on operators in any given state

5. Table of Contents
	* [Overview](#overview)
	* [The Scripts](#scripts)
	* [Explanation of Categories](#explanation-of-categories)

Overview
--------
After the [Santa Barbara pipeline spill](http://www.scpr.org/news/2015/06/01/52117/things-to-know-about-the-california-oil-spill) in June, 2015, we wanted to know more about pipelines operated in California. Who operates in the state, what kinds of pipelines do they operate, and who causes the most damage? 

All of that info is available on the Pipeline and Hazardous Materials Safety Administration (PHMSA) website, but the data isn't in an easily analyzable formate. Looking at the list of operators, we don't know what states they operate in or what kinds of damage they do. We decided to fix that.

There are two web scrappers here: cali-pipeline-ops-to-csv.py and pipeline-incident-details.py. Both scrapers are built using BeautifulSoup and go through the PHMSA website and gather info on pipelines.

The Scripts
-----------

Here is a brief description of how the scripts work and how to change what states they are getting information on. Each operator has a config dictionary, which sets the csv name and column names. A full description of the columns is in the next section.

###### pipeline-incident-details
The first scraper, [pipeline-incident-details.py](https://github.com/SCPR/kpcc-data-team/blob/wcraft-dev/tools-and-scripts/pull-california-pipeline-operators/pipeline-incident-details.py), focuses only on grabbing info on pipeline incidents and acccidents in California. 

* [PHMSA's operator list](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html) doesn't list which states the operator has pipelines in, so the script's first job is to go through the entire list and find which are in California. The function populate_config can be in changed in \_init_ to take any 2-letter state abbreviation, or 'all'. 

* If the operator has pipeline in the given state, it checks to see if there have been any incidents connected to the operator since 2006. Each pipeline operator has a page with more detailed info on pipeline failures. [Example](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorIM_opid_2616.html?nocache=2666#_Incidents_tab_4) This is where the juicy info on each pipeline is. If there haven't been any incidents, then the pipeline passes over that operator and doesn't gather any information.

*  Not every pipeline's details page is structured the same way, so the scraper opens each page and figures out the div tag for the details table. It jumps into the table and combs through the information, sanitizing the text and numbers, removing bizarre unicode and unnecessary spaces, and adds each row to a list of lists. It then writes the list of lists to a csv using python's built-in csv writer functions.

###### pipeline-operator-ids-to-csv
The second scraper, [pipeline-operator-ids-to-csv.py](https://github.com/SCPR/kpcc-data-team/blob/wcraft-dev/tools-and-scripts/pull-california-pipeline-operators/pipeline-operator-ids-to-csv.py) grabs more general information on all pipelines operating in the US and also checks to see if they operate in California. 

* The scraper goes through [PHMSA's operator list](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html) and grabs all the info present on the page. 
* The script then jumps into each page and checks to see if the operator is present in California. This can be edited to work for any state by changing the column name in config and by changing the operator_details funciton.  
* The scraper then goes through the html to make a list of dictionaries, converts it into a pandas dataframe and exports it to a csv. 
	* The data, taken direcly from the website, isn't really suitable for analysis because all of the numbers and dollars aren't stored as integers. Using pandas, its very easy to clean up the data.


Explanation of some of the categories
------------------------------------
 
A note on what some of the different categories mean. No government dataset would be complete without some jargon, so here is an explanation for what each column means

###### Columns in pipeline-incident-details.py

* Operator
* Date
* System
* City
* State
* County
* Cause
* Sub Cause
* Fatalities
* Injuries
* Property Damage (A)
* Gross Barrels Spilled (Haz Liq) (B)
* Net Barrels Lost (Haz Liq) (B)(C)
* Value of Product Lost (D)

###### Columns in pipeline-operator-ids-to-csv.py

* id
	* Each pipeline operator has a unique ID number  
* california
	* "True" if the operator has ANY pipeline in California  
* name
	* The name of the company  
* incidents
	* This number if from the main list of operators, but is not always accurate (part of the reason for the other scraper). Check each operator page for a more accurate incident details.
* inspections
	* Inspections are meant to ensure compliance with government safety regulations. More information on inspections and enforcement action can be found [here](http://phmsa.dot.gov/inspect-enforce) and information on inspections, such as number of investigators, can be found [here](http://phmsa.dot.gov/pipeline/inspections)
* enforcement-actions
	* When a company is found to be noncompliant, PHMSA can take enforcement actions against them. This is the number of enforcement actions levied agains this operator 
* hazardous-liquid
	* You can check the full list of possible fluids and gases transported [here](http://primis.phmsa.dot.gov/comm/FactSheets/FSProductList.htm?nocache=2022), but in general, PHMSA defines hazardous liquids as "hydrocarbon liquids", so crude oil and refined petroleum. 
* states-of-operation-hl
	* Which states the operator has hazardous liquid pipelines in. 
* inspected-miles-hl
	* Federal and state inspected miles: Pipeline operators have to submit to both federal and state inspections. Information of the various state regulators can be found [here](http://phmsa.dot.gov/pipeline/state-programs) and information on the federal laws that must be obeyed can be read [here](http://phmsa.dot.gov/pipeline/stateprograms/federalstateauthorities) 
* gas-transmission
	* Gas pipelines transport non-liquid products such as butane and natural gas 
* states-of-operation-gt
	* Which states the operator has gas transmission pipelines in.  
* inspected-miles-gt
* gas-gathering
	* These are pipes used for gathering, as opposed to transporting, gas
* states-of-operation-gg
	* Which states the operator has gas transmission pipelines in.
* inspected-miles-gg
