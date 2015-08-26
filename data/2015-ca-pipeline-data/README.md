California Pipeline Operator Data 
====================================

The data was scraped from [here](http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html) using two web scrapers. Details on those can be found in our [tools and scripts folder](https://github.com/SCPR/kpcc-data-team/tree/wcraft-dev/tools-and-scripts/pull-california-pipeline-operators)

Analyzing the data 
------------------
Guiding Questions 

* Who are the biggest offenders in California?
* Is there a relation between mileage operated and number of incidents? What are the incidences per mile? 
* What is the most common cause of pipeline failure?
* What areas have been hit the hardest? 

There are 98 companies operating pipeline in CA. There have been 273 incidents in California since 2006, caused by 34 different pipeline operators. However, the majority of the incidents have been caused by a small number of companies.

![](./ca_pipeline_data_results/Pipeline_Operators_with_more_than_10_incidents.png)

However, this doesn't give us a full picture for the worst offenders in the state, because some of the companies operate vastly different quantities of pipeline.

![](./ca_pipeline_data_results/Operators_with_more_than_1000_miles.png)


Calculating the number of incidents per mile gives us a better idea of which companies have pipelines that are consistently breaking. We can see that Bp West Coast has a very high number of incidents per mile, even though they only have 161 miles. 

![](./ca_pipeline_data_results/Incidents_per_1000.png)

There have been 9 fatalities and 62 injuries, all caused by the same pipeline operator, Pacific Gas and Electric, in two separate incidences. The largest incident, [the San Bruno pipeline explosion](http://www.scpr.org/news/2015/04/09/50901/california-regulator-suggests-utility-pg-e-is-too/), caused over $300 million in damages and killed 8 people.

![](./ca_pipeline_data_results/Top_10_-_Property_Damages_Damages__chartbuilder.png)

In total, 6,054,736 barrels of hazardous liquid have been spilled by 31 different operators since 2006. Only three operators spilled more than 10,000 barrels. The next highest spiller lost 7,218 barrels. A huge part of PG&E's lead is the San Bruno explosion.

![](./ca_pipeline_data_results/Top_5_-_Barrels_Spilled_by_Operator_Barrels_Spilled_chartbuilder.png)


The most common cause of pipeline failures are material/weld/equipment failure and corrosion. 

![](./ca_pipeline_data_results/Cause_of_Pipeline_Failures__Number_of_Failures_Since_'06_chartbuilder.png)

Long Beach is by far the city with the highest number of incidents, which may make sense given that Long Beach is right next to the Port of Long Beach, one of the busiest in the world. Though the port is actually in Los Angeles, it makes sense that there would be a lot of operators in the city.

![](./ca_pipeline_data_results/Top_5_Cities_with_the_highest_number_of_incidents_Incidents_chartbuilder.png)

However, looking only within Long Beach, we can see which pipelines have the highest incident rate. Using the collected data, we could replicate this for any city in California. 

![](./ca_pipeline_data_results/Operator_incidents_in_Long_Beach_Incidents_in_Long_Beach_chartbuilder.png)

