California Pipeline Operator Scraper 
====================================

1. ```pip install requirements.txt```

2. Data taken from [here](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html)

How it Works
------------
<p>After the [Santa Barbara pipeline spill](http://www.scpr.org/news/2015/06/01/52117/things-to-know-about-the-california-oil-spill/) in June, 2015, we wanted to know more about pipelines operated in California. Who operates in the state, what kinds of pipelines do they operate, and who causes the most damage? All of that info is available on the Pipeline and Hazardous Materials Safety Administration (PHMSA) website, but the data isn't in an easily analyzable formate. Looking at the list of operators, we don't know what states they operate in or what kinds of damage they do. We decided to fix that. </p>

<p>There are two web scrappers here: cali-pipeline-ops-to-csv.py and pipeline-incident-details.py. Both scrapers are built using BeautifulSoup and go through the PHMSA website and gather info on pipelines, allowing us to gain some good insights. </p>

<p> The first scraper's job is to gather information on operators only within the state of California. The main page doesn't give any indication of what states the operator has pipelines in, so the script opens up the page and checks. It then grabs basic information on each operator, such as the name, incidents, inspections, enforcement actions, and what kinds of pipelines the company operates and how many miles.</p>

<p> The scraper grabs the information and adds each category to a list of dictionaries, converts it into a pandas dataframe and exports it to a csv. The data, taken direcly from the website, isn't really suitable for analysis because all of the numbers and dollars aren't stored as integers. Using pandas, its very easy to clean up the data.</p>

<p> The second scraper does a bit more involved job. Each pipeline operator has its own page, which has much more detailed info on pipeline failures. [Example](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorIM_opid_2616.html?nocache=2666#_Incidents_tab_4) This is where the juicy info on each pipeline is.</p>

<p>Not every pipeline's details page is structured the same way, so the scraper opens each page and figures out the div tag for the details table. It jumps into the table and combs through the information, sanitizing the text and numbers, removing bizarre unicode and unnecessary spaces, and adds each row to a list of lists. It then writes the list of lists to a csv using python's built-in csv writer functions.</p>

<p> The details page for each operator gives some very detailed info on pipeline accidents. In addition to the cost of property damage, we also get the cause and sub-cause of the pipeline failure, as well as the city, state, and county of the failure.</p>

Analyzing the data 
------------------
Guiding Questions 
* Who are the biggest offenders in California?
* Is there a relation between mileage operated and number of incidents? 
* What is the most common cause of pipeline failure? Most common sub-cause?








