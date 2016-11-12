# to run from terminal, cd into the directory where you have this script and run RScript ie_2016.r

# install these packages and load them
# installation can be skipped if you already have these
install.packages("sqldf",repos = 'http://cran.us.r-project.org')
install.packages("readr",repos = 'http://cran.us.r-project.org')
install.packages("reshape2",repos = 'http://cran.us.r-project.org')
install.packages("dplyr",repos = 'http://cran.us.r-project.org')
install.packages("data.table",repos = 'http://cran.us.r-project.org')
library(sqldf)
library(readr)
library(reshape2)
library(dplyr)
library(data.table)

# grab basic filer information
# we're getting this from the CA Civic Data Coalition, who publish updated versions of each table daily. this saves us time compared with downloading the entire database from Cal-Access each day
# here we grab only the most recent name of the filers, which should be fine, provided we want only to look at the most recent cycle. adjust accordingly if looking at historical data.

# filers
filername_cd <- read_csv("http://calaccess.download/latest/filername_cd.csv")
    # make date a date
    filername_cd$EFFECT_DT <- as.Date(filername_cd$EFFECT_DT, format = '%m/%d/%Y')
    # grab ONLY most recent record
    filername_cd_most_recent <- setDT(filername_cd)[,.SD[which.max(EFFECT_DT)],keyby=FILER_ID]

# filings
filer_filings_cd <- read_csv("http://calaccess.download/latest/filer_filings_cd.csv")
    # lets make a simple version of this, for readability
    filer_filings_simple <- sqldf("select FILER_ID, FILING_ID from filer_filings_cd group by FILER_ID, FILING_ID")

# let's merge these two dataframes
filers_and_filings <- merge(filer_filings_simple, filername_cd_most_recent, by="FILER_ID", all.x = TRUE)

# bring in cover page of disclosure forms
cvr_campaign_disclosure_cd <- read_csv("http://calaccess.download/latest/cvr_campaign_disclosure_cd.csv")

    # filter dates and add them back
    test <- colsplit(cvr_campaign_disclosure_cd$RPT_DATE, ' ', c("date", "time", "am_pm"))
    test$gooddate <- as.Date(test$date, format = '%m/%d/%Y')
    cvr_campaign_disclosure_cd <- cbind(cvr_campaign_disclosure_cd, test$gooddate)

    cvr_campaign_disclosure_cd <- subset(cvr_campaign_disclosure_cd, `test$gooddate` > as.Date("2015-12-31") & `test$gooddate` < as.Date("2017-01-01"))
    colnames(cvr_campaign_disclosure_cd)[87] <- "RPT_DATE_new"

# simplify by selecting only these cols of interest
cvr_campaign_disclosure_cd_simple <- select(cvr_campaign_disclosure_cd, FILING_ID, AMEND_ID, FILER_NAML, SUP_OPP_CD, CAND_NAML, CAND_NAMF, CAND_NAMS, CAND_NAMT, BAL_NAME, BAL_NUM, BAL_JURIS, ELECT_DATE, OFFICE_CD, OFF_S_H_CD, OFFIC_DSCR, JURIS_CD, JURIS_DSCR, DIST_NO, ENTITY_CD, CMTTE_TYPE, CONTROL_YN, SPONSOR_YN, PRIMFRM_YN, BRDBASE_YN, BAL_ID, CAND_ID, RPT_DATE_new)

# get ONLY most recent ammendment. very important step.
cvr_campaign_disclosure_cd_simple <- setDT(cvr_campaign_disclosure_cd_simple)[,.SD[which.max(AMEND_ID)],keyby=FILING_ID]

# now ready to bring in independent expenditures. don't be fooled by the term 'late' in the documentation, these are all we need
# import and convert into a date
s496_cd <- read_csv("http://calaccess.download/latest/s496_cd.csv")
    s496_test <- colsplit(s496_cd$EXP_DATE, ' ', c("date", "time", "am_pm"))
    s496_test$gooddate <- as.Date(s496_test$date, format = '%m/%d/%Y')
    s496_cd <- cbind(s496_cd, s496_test$gooddate)
    colnames(s496_cd)[13] <- "exp_as_date"

# subset for just 2016, the 'current cycle' as of the writing of this code
# you'll need to update in the future
s496_cd_currentcycle <- subset(s496_cd, s496_cd$exp_as_date > as.Date("2015-12-31") & s496_cd$exp_as_date < as.Date("2017-01-01"))

# with work from above, get names on these IEs. that's why we did all the wrangling above
s496_cd_currentcycle_withnames <- merge(s496_cd_currentcycle, filers_and_filings, by="FILING_ID", all.x=TRUE)

# using FILING_ID and AMEND_ID let's get rid of pesky multiples of certain expenses, which are throwing off our totals if we analyze whats there now
# first ... how many ammendments does a filing id have?
num_amends_per_filing_id <- setDT(s496_cd_currentcycle_withnames)[,.SD[which.max(AMEND_ID)],keyby=FILING_ID]
num_amends_per_filing_id <- select(num_amends_per_filing_id, FILING_ID, AMEND_ID)
colnames(num_amends_per_filing_id)[2] <- "max_amend"
s496_cd_currentcycle_withnames <- merge(s496_cd_currentcycle_withnames,num_amends_per_filing_id, by="FILING_ID", all.x=TRUE)

# now subset to make sure we only have line items from max # of ammendments
s496_cd_currentcycle_withnames_collapse <- subset(s496_cd_currentcycle_withnames, AMEND_ID == max_amend)

# now ask who does spending effect? do it by joining cvr_campaign_disclosure_cd_simple
ie <- merge(s496_cd_currentcycle_withnames_collapse, cvr_campaign_disclosure_cd_simple, by="FILING_ID")

# we will condense by making sure there aren't extra ammendments sneaking in here that get deleted from our cvr_campaign_disclosure_cd_simple. the ammendement to 2049641 showed up in that but not in s496_cd. this removes about 12 out of 4000 ies as of 9/19, but affects edvoice, one of the cmtes, we were reporting on.
# so we will check to make sure amend_ids from the two datasets match and filter to only keep if they do.
# i believe you could also accomplish by joining on FILING_ID and AMEND_ID
ie$new_amend <- ifelse(ie$`AMEND_ID.x` != ie$`AMEND_ID.y`, "y", "n")
ie <- subset(ie, ie$new_amend == "n")

# to do certain kinds of queires, you'll need to standardize candidate names. here are some first steps.
ie$CAND_NAMF <- ifelse(is.na(ie$CAND_NAMF) == TRUE, "", ie$CAND_NAMF)
ie$CAND_NAML <- ifelse(is.na(ie$CAND_NAML) == TRUE, "", ie$CAND_NAML)
ie$CAND <- tolower(ifelse(ie$CAND_NAMF != "", (paste(ie$CAND_NAMF, ie$CAND_NAML, sep=" ")), ie$CAND_NAML))

# let's also make all support / oppose codes uppercase
ie$SUP_OPP_CD <- toupper(ie$SUP_OPP_CD)

# manually you will have to fix some names
# will need to continually update as new typos appear
# THIS WILL NOT WORK IN FUTURE CYCLES, WITH NEW CANDIDATES AND ERRORS. but here for reference.
    ie$CAND <- ifelse(ie$CAND == "bill haldin", "bill halldin",
           ifelse(ie$CAND == "laura friedman (i)", "laura friedman",
                  ifelse(ie$CAND == "eloise gomez reyes", "eloise reyes",
                         ifelse(ie$CAND == "eloise gomez-reyes", "eloise reyes",
                                ifelse(ie$CAND == "frank a. yokoyama", "frank yokoyama",
                                       ifelse(ie$CAND == "karina cervantez alejo", "karina cervantez-alejo",
                                              ifelse(ie$CAND == "mark j. maccarley", "mark maccarley",
                                                     ifelse(ie$CAND == "matthew dababneh", "matt dababneh",
                                                            ifelse(ie$CAND == "scott weiner", "scott wiener",
                                                                   ifelse(ie$CAND == "cheryl r. brown", "cheryl brown",
    ie$CAND))))))))))

# get clear race ids, for simple analysis
ie$DIST_NO <- as.numeric(ie$DIST_NO)
ie$JURIS_CD <- trimws(ie$JURIS_CD)
ie$DIST <- ifelse(ie$JURIS_CD == "ASM" | ie$JURIS_CD == "SEN", paste(ie$JURIS_CD, ie$DIST_NO, sep='-'), "")

# rename date col and make since primary...
# this can be reworked if you want to draw a line in the sand, i.e. was spending before or after a certain date (such as a primary election)
ie$since_primary <- ifelse(ie$exp_as_date > as.Date("2016-06-07"), "y", "n")

# filter for ONLY CA legislative races
ie_leg <- subset(ie, ie$JURIS_CD == "ASM" | ie$JURIS_CD == "SEN")

# clean up workspace mess, if only a bit
rm(test, s496_cd_currentcycle_withnames_collapse, s496_cd_currentcycle_withnames, s496_cd_currentcycle, num_amends_per_filing_id, s496_test)

# spit out a csv of our IEs
write.csv(ie_leg, "~/Desktop/ies_2016.csv")



# INCLUDING A FEW WAYS YOU CAN ANLYZE THIS DATA HERE

    # candidates attracting the most pro/anti in 2016 legislative races
    # ie_by_candidate_2016 <- sqldf("select CAND, SUP_OPP_CD, DIST, sum(AMOUNT) as amt from ie_leg group by CAND, DIST, SUP_OPP_CD order by amt desc")

    # 2016 legislative races attracting the most
    # sqldf("select DIST, sum(AMOUNT) as amt from ie_leg group by DIST order by amt desc")

    # candidates/spender/race breakdown
    # sqldf("select NAML, DIST, FILER_ID, sum(AMOUNT) as amt from ie_leg group by FILER_ID, DIST order by amt desc")

    # how much are these groups dropping in 2016 legislative races?
    # sqldf("select NAML, FILER_ID, sum(AMOUNT) as amt from ie_leg group by FILER_ID order by amt desc")

    # how much is being spent to support/oppose individual candidates since the primary election?
    # sqldf("select NAML, DIST, FILER_ID, CAND, SUP_OPP_CD, sum(AMOUNT) as amt from ie_leg where since_primary = 'y' group by FILER_ID, DIST, CAND, SUP_OPP_CD order by amt desc")





