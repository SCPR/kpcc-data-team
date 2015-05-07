##NFL Stadium data
Or is it [stadia](http://english.stackexchange.com/questions/29060/what-is-the-correct-plural-of-stadium)?

Anyway, in an effort to provide context around two stadium proposals in the Los Angeles area, I began searching for data regarding NFL stadium costs. Unfortunately, there is no detailed, reliable data source.

Instead, I brought together information from a handful of sources:

- John Vrooman, an economist at Vanderbilt. His spreadsheet on stadium construction and renovations over the past 20 years was the basis for our .csv.
- Lat/lon data and capacity [from here](https://github.com/zief0002/EPsy-8252/blob/master/data/NFL-Meta-Data.csv)
- I also calcualted the stadium costs, using Consumer Price Index data from the BLS to control for inflation in 2014 dollars.

I added another column "titular_jurisdiction", which answers the question "Do the San Francisco 49ers actually play in San Francisco?" (they don't) for each team.

This is all in stadium_cpi.csv.

In general, we see that stadium costs over time have exploded, even controlling for inflation:

![](/images/cost_over_time.png)

And the private share of construction costs has been rising (it's nominally 100% in the Southern California proposals):

![](/images/private_share.png)
