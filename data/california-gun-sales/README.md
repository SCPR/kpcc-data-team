# California gun sales

The California Department of Justice tracks gun sales and transfers in the state. This is more detailed than the federal data on background checks ([which Buzzfeed has helpfully posted here](https://github.com/BuzzFeedNews/nics-firearm-background-checks)) because it shows actual sales. The background checks are often used as an imperfect barometer of sales.

However, just because the state stores the information doesn't mean that it's easy to come by. Good luck finding it on the DOJ's data site. We're sharing the data here in case it's of interest to others.

Read up on [firearms in California from the DOJ's Bureau Of Firearms](https://oag.ca.gov/firearms/pubfaqs) before digging in. 

Some historical context is also [available here](http://oag.ca.gov/sites/all/files/agweb/pdfs/firearms/forms/dros_chart.pdf?).

# What's here

Data from a handful of requests to the state DOJ. Be alert to differences between DROS and CRIS; handguns and long guns; and approved, pending and denied sales.

* [dros2016.csv](./data/dros2016.csv): Sale-by-sale DROS transactions for 2016, including city and county. Originally provided as 34,308 pages of PDFs in January 2017, converted by KPCC
* [ca_guns_daily_county_aug_2016](./data/ca_guns_daily_county_aug_2016.csv): Daily 2016 DROS and CRIS data, broken down by county.
* [nov_dec_daily_comparison_2014_2015](./data/nov_dec_daily_comparison_2014_2015.csv): A comparison of statewide gun sales on the same calendar dates in November and December of 2014 and 2015. The San Bernardino mass shooting happened on December 2, 2015.
* [ca_guns_county_yearly_jan_2016](./data/ca_guns_county_yearly_jan_2016.csv): Yearly totals broken down by county, 2010 to 2015.
* [cnty_codes](./data/cnty_codes.csv): County codes that can be joined to the sales to make them more human-readable.


# KPCC coverage of California gun sales

* [Politics, gun-control anxiety cited for California's record 2016 gun sales
](http://www.scpr.org/news/2017/03/15/69644/california-gun-sales-shattered-records-last-year-w/)
* [Calif. gun transactions at highest level since '91, still rising](http://projects.scpr.org/charts/calif-dros-transactions/), 2012
* [Californians on pace to buy 1 million guns in 2016](http://www.scpr.org/news/2016/08/15/63411/californians-on-pace-to-buy-1-million-guns-in-2016/), August 2016
* [California gun sales spiking in 2016](http://www.scpr.org/news/2016/04/27/59895/california-seeing-records-numbers-of-people-wantin/), April 2016
* [Gun sales spiked in California after San Bernardino shooting](http://www.scpr.org/news/2016/01/20/56927/gun-sales-spiked-in-california-after-san-bernardin/)

Let us know if you use the data: amendelsonATscprDOTorg, [@a_mendelson](http://twitter.com/a_mendelson)