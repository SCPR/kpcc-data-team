U.S. Pipeline Operator Scraper
====================================

* [Overview](#overview)
* [The Scripts](#the-scripts)
* [Explanation of Data Fields](#explanation-of-data-fields)
* [The Data](/data/2015-ca-pipeline-data)

Overview
--------

After a June 2015 oil spill in [Santa Barbara](http://www.scpr.org/news/2015/06/01/52117/things-to-know-about-the-california-oil-spill) along a pipeline owned by [Plains All American Pipeline](https://www.plainsallamerican.com/) we wanted to know more about operators in California and their infrastructure:

* Who operates in the state
* What kinds of pipelines do they operate
* What previous incidents have occured?

All of that information - and more - is available via the [Pipeline and Hazardous Materials Safety Administration](http://www.phmsa.dot.gov/) (PHMSA) website. But the data isn't always available in a format that makes it easy to analyze.

For instance, when looking at the [list of operators](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html) it's difficult to determine which states they operate in and find details about incidents that have occured along a company's pipelines and infrastructure.

We decided to attempt to fix that - or at least address - with a couple of scrapers:

* [pipeline-operator-ids-to-csv.py](/tools-and-scripts/pull-california-pipeline-operators/pipeline-operator-ids-to-csv.py)
* [pipeline-incident-details.py](/tools-and-scripts/pull-california-pipeline-operators/pipeline-incident-details.py)

Both are written in [Python](https://www.python.org/) and use [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) to go through the PHMSA website and gather information on pipelines. To get up and running simply install the dependencies - ```pip install requirements.txt```

The [data](/data/2015-ca-pipeline-data) gathered by the scrapers from the [Pipeline and Hazardous Materials Safety Administration](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html) contains the number of miles and types of pipelines, and incidents for operators within California that have had pipes break.

The Scripts
-----------

Here is a brief description of how the scripts work and how to change what states they are getting information on. Each operator has a config dictionary, which sets the csv name and column names. A full description of the columns is in the next section.

**pipeline-operator-ids-to-csv**

[pipeline-operator-ids-to-csv.py](/tools-and-scripts/pull-california-pipeline-operators/pipeline-operator-ids-to-csv.py) grabs more general information on all pipelines operating in the US and also checks to see if they operate in California.

* The scraper goes through [PHMSA's operator list](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html) and grabs all the information present on the page.

* The script then jumps into each page and checks to see if the operator is present in California. This can be edited to work for any state by changing the column name in config and by changing the operator_details funciton.

* The scraper then goes through the html to make a list of dictionaries, converts it into a pandas dataframe and exports it to a csv.

    * The data, taken direcly from the website, isn't really suitable for analysis because all of the numbers and dollars aren't stored as integers. Using pandas, its very easy to clean up the data.

**pipeline-incident-details**

[pipeline-incident-details.py](/tools-and-scripts/pull-california-pipeline-operators/pipeline-incident-details.py) focuses on grabbing information on pipeline incidents from a list of pipeline operator ids, which you can can acquire from the ```pipeline-operator-ids-to-csv``` scraper.

* If an operator has pipeline in the given state the scraper checks to see if there have been any incidents connected to the operator since 2006. Each pipeline operator has [a page with more detailed information](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorIM_opid_2616.html?nocache=2666#_Incidents_tab_4) on pipeline incidents. If there haven't been any incidents, then the pipeline passes over that operator and doesn't gather any information.

* Not every pipeline's details page is structured the same way, so the scraper opens each page and figures out the div tag for the details table. It jumps into the table and combs through the information, sanitizing the text and numbers, removing bizarre unicode and unnecessary spaces, and adds each row to a list of lists. It then writes the list of lists to a csv using python's built-in csv writer functions.

Explanation of Data Fields
--------------------------

No government dataset would be complete without some jargon, so here is an attempt to explain the data in each column for the two csv files.

**pipeline-incident-details.csv**

* **operator_id**
    * Each pipeline operator has a unique ID number

* **operator**
    * The name of the company operating the pipeline

* **date**
    * The date that the incident occured

* **system**
    * Lists which of the three systems, hazardous liquid (HL), gas gathering (GG), or gas transmission (GT), the pipe that broke was

* **city**
    * The city the pipeline was in

* **state**
    * The state the pipeline was in

* **county**
    * The county the pipeline was in

* **cause**
    * The cause for the pipeline incident. There are 7 possible causes: material/weld/equipment failure, corrosion, excavation damage, incorrect operation, natural force damage, other outside force damage, and all other causes

* **sub_cause**
    * a brief explanation of what caused the failure.

* **fatalities**
    * The number of people that died due to the incident

* **injuries**
    * The number of people that were injured due to the incident

* **property_damage_a**
    * The estimated sum of damages caused by the incident, estimated and reported by the operator

* **gross_barrels_spilled_haz_liq_b**
    * The total amount of hazardous liquid spilled during the incident

* **net_barrels_lost_haz_liq_b_c**
    * The total amount of hl spilled minus the amount of hl recovered

* **value_of_product_lost_d**
    * The monetary value of the product lost due to the incident

----

**phmsa_pipeline_operators.csv**

* **id**
    * Each pipeline operator has a unique ID number

* **california**
    * "True" if the operator has ANY pipeline in California

* **name**
    * The name of the company

* **incidents**
    * This number if from the main list of operators, but is not always accurate (part of the reason for the other scraper). Check each operator page for a more accurate incident details.

* **inspections**
    * Inspections are meant to ensure compliance with government safety regulations. More information on inspections and enforcement action can be found [here](http://phmsa.dot.gov/inspect-enforce) and information on inspections, such as number of investigators, can be found [here](http://phmsa.dot.gov/pipeline/inspections)

* **enforcement-actions**
    * When a company is found to be noncompliant, PHMSA can take enforcement actions against them. This is the number of enforcement actions levied agains this operator

* **hazardous-liquid**
    * You can check the full list of possible fluids and gases transported [here](http://primis.phmsa.dot.gov/comm/FactSheets/FSProductList.htm?nocache=2022), but in general, PHMSA defines hazardous liquids as "hydrocarbon liquids", so crude oil and refined petroleum.

* **states-of-operation-hl**
    * Which states the operator has hazardous liquid pipelines in.

* **inspected-miles-hl**
    * Federal and state inspected miles: Pipeline operators have to submit to both federal and state inspections. Information of the various state regulators can be found [here](http://phmsa.dot.gov/pipeline/state-programs) and information on the federal laws that must be obeyed can be read [here](http://phmsa.dot.gov/pipeline/stateprograms/federalstateauthorities)

* **gas-transmission**
    * Gas pipelines transport non-liquid products such as butane and natural gas

* **states-of-operation-gt**
    * Which states the operator has gas transmission pipelines in.

* **inspected-miles-gt**

* **gas-gathering**
    * These are pipes used for gathering, as opposed to transporting, gas

* **states-of-operation-gg**
    * Which states the operator has gas transmission pipelines in.

* **inspected-miles-gg**
