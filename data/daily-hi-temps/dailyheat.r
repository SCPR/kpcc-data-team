setwd("~/Github/kpcc-data-team/data/daily-hi-temps/")

# date
todaysdate <- Sys.Date()

# historical temps
library(readr)
library('dplyr')
dtla_daily_hi <- read_csv("~/Github/kpcc-data-team/data/daily-hi-temps/dtla_daily_hi.csv")
dtla_daily_hi$date <- paste(dtla_daily_hi$MO, dtla_daily_hi$`N DY`, sep="-")
dtla_daily_hi$date <- as.Date(dtla_daily_hi$date, format = '%m-%d')

today <- subset(dtla_daily_hi, date == todaysdate)
statement <- paste("DTLA's average high temperature on ", substr(todaysdate,6,10), " is ", today$TMAX, " degrees", sep="")
