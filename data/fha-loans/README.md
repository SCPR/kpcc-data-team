# Monthly FHA loans in California

KPCC reporters recently crunched the numbers on FHA loans, a government-backed mortgage insured by the Federal Housing Administration. We are releasing the data used for our analysis in this repo.

These loans are a common choice for first-time buyers who prefer their low down payment options and relaxed credit requirements. The program data [is available on HUD's website](https://www.hud.gov/program_offices/housing/rmra/oe/rpts/sfsnap/sfsnap), but unfortunately for anyone hoping to analyze the use of the program over time, is spread across dozens of files.

In reporting this story, KPCC brought that data together in a manner that is more friendly for data analysis (i.e. a single csv file). In doing that, we also cleaned the `down_payment_src` column and created a `date` column.

The file available in this repo contains 89 months of FHA loan data for California, from January 2011 - May 2018. That data represents over 600,000 mortgages. Lenders submit the information about down payment support to HUD. Note that we only analyzed home purchases, not refinancing, and that this data is only for the state of California. Unfortunately, the FHA data is sometimes spread across multiple sheets of an Excel file. We grabbed only the data in the sheet containing California, so are not posting data for the entire nation.

Questions? Comments? Get in touch --> amendelsonATscprDOTorg