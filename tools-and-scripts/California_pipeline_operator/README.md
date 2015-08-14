California Pipeline Operator Scraper 
====================================

1. ```pip install requirements.txt```

2. Data taken from [here](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html)

How it Works
------------

<p> The scraper uses BeautifulSoup to parse through the HTML and then uses pandas to clean up the data. First, the script goes through the series of pipeline operators on the main page. If the operator has any pipeline in California, the script grabs five pieces of information from main page - name, ID number, number of enforcement actions, number of inspections, and number of incidents.</p>

<p> After getting the data from the main page, the scraper goes into each report page. There are three possible categories of pipeline that each operator may have - hazardous liquid, gas transmission, and gas gathering. The dataset either says TRUE, meaning that the operator operates that type of pipeline, or FALSE, meaning they don't. There are two other sub-categories, states of operation and inspected miles, which are the states that the type of pipeline is present in and the miles of pipeline that the operator controls of that specific type. </p>

<p> After all the data is gathered, the script takes a list of dictionaries and turns it into a pandas dataframe, which allows us to quickly manipulate and fix up the data and export it to a csv. The govt. database stores some of the numbers as integers and some as strings. Pandas allows us to go through the data and convert all numbers to integers, which allows numeric sorting after-the-fact. </p>