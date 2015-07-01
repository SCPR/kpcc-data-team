# The data
We have one year's worth of data. It covers one full year of claims, from May 1, 2014 through April 30, 2015.

A few important details about what this data actually represents.

* The claims represent $14,317,195.30 that the DWP paid out
* There were 624 claims paid out during this time period
* It's difficult to separate out claims from water main breaks. Something like half of the claims relate to water mains (many of those from the UCLA break). But those claims don't account for much of the money DWP pays out.
* Just two of the types of claims (Personal injury and wrongful death) make up more than half ($8.25 million) of the total paid out.
* The wrongful death payouts all stem from a single incident in July 2013.
	* There were five different payouts. It's unclear if 5 people died in the accident or if 5 family members got claims on the same death
	* The payouts range from $1 million to $250,000
	* Official description: "Requesting monetary reimbursement for loss of family member which was  hit and killed by DWP vehicle"
* There is a single $4.5 million payout for "being run-over by DWP vehicle". It's the largest in the dataset
	* It took 595 days before this claim paid out
	* Wonder why being run over by a DWP vehicle resulted in a much larger payout than being killed by a DWP vehicle???

## It can take a while to get your money
* Many of the claims are from incidents that happened before the May 2014-April 2015 window
* 115 of the claims took a year or more to resolve
	* They represent $7,333,213.78 of what was paid out. 51.2% of total payouts
* Someone waited 453 days to get their "Food spoilage as a result of erroneous shut off" claim paid out. Only got $112.50 for their trouble

How long between the incident and the payout?

* Shortest--10 days. related to two damaged vehicles from UCLA break, and renting cars afterward. Less than $250 each
* Median--184 days between incident and payout
* Mean--251 days. That's a litte over 8 months
* Longest--2,207 days (6 years). For an unspecified "breach of contract"

## You can't always get [the dollar amount] you want
* Overall, people asked for $52,131,003.67 on claims where they actually received $14,317,195.30. That's 27.5 %
* Only 18 claims received more money than they originally asked for
* 273 received the exact same amount they asked for
* 317 received less than they asked for
* Of course, this doesn't include claims that were rejected

## UCLA
* We have 624 total claims in our data. 253 of them were from the UCLA incident; that's nearly half
	* 25 claims was second most from an incident (a power outage/failure)
* Many descriptions mention damage to vehicles and personal property. The single largest payout was $41,748.60
* These are listed as matter number *1033780* in our data

## Some odd claims    
Most of these verbatim from description field 

* P/I-O/S as a result of falling through manhole cover on sidewalk (29999)
* Personal Injury due to fall through cover of DWP water vault (16000)
* P/I-O/S as a result of trip and fall on uneven sidewalk paneling (60000)
* CARQ:  P/I-O/S as a result of trip and fall on uneven pavement (27000)
* damage to t.v. due to failed transformer
* Damage to O/S vehicle (tires) due to driving over pothole
* looooots of traffic accidents (often "t/a" in description)
* Billing issue ($78.82) / billing dispute (55)
	* someone actually got their DWP bill reduced!

Two interesting claim types:

* GLAS-Damage To Glasses
* FDSP-Food Spoilage

## Graphs
There are a number of types of claims, but a small handful account for most of the money paid out:
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/aaron-dev/data/2015-dwp-claims/imgs/paid_by_claim.png)

We don't see a seasonal pattern in payouts:
![](https://raw.githubusercontent.com/SCPR/kpcc-data-team/aaron-dev/data/2015-dwp-claims/imgs/claims_per_month.png)

# Details of the data
* Some of the dates in the date_of_loss column are probably wrong, i.e. the person who reported a loss from UCLA break on the day before the break happened. They represent the date the claimant *reported* the loss happened, which could represent the date it was discovered
* The matter_sub column was created by combining (you guessed it) the matter and sub columns
	* If that appears multiple times, it means the same person received claims from the same incident multiple times
	* Totally possible some unlucky/litigious soul would be in there receiving multiple claims from multiple incidents
		* One person received 4 separate payouts from a 2013 main break
* The description field is often opaque but gives a general idea about what happened
* If you, like me, need to brush up on subrogation claims, [here's a start](http://www.investopedia.com/terms/s/subrogation.asp#ixzz3c2pWhEZY)
	* A lot of these claims are pursued by insurance companies
* This data was entered by hand. There may be errors for that reason. I caught a couple irregularities and ran them by the DWP spokespeople, who provided the correct numbers for them. There are very possibly other errors

I asked for details on the claim types in the data. Many are straightforward, here's the rest:

* PDOR- is damage to real property
* PIOS – is personal injury, like a trip and fall
* AASB – is a subrogation claim from an insurance company related to an auto accident
* SUBR – is a subrogation claim for anything other than an auto accident
* FIRE – could mean any type of fire related claim
* AAPI – is personal injury as a result of an Auto Accident
* AAPD would be property damage or out of pocket expenses due to an auto accident
* DMVH is damage to vehicle from causes other than a traffic collision
