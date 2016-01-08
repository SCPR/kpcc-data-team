#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import re
import datetime
from datetime import tzinfo
import csvkit
import pytz
from pytz import timezone
from dateutil import parser
from twitter import *

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

# hashtag to search
TWEET_HASHTAG = "#elnino"

# number of tweets to return
TWEET_COUNT=1000,

# twitter api key
TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")

# twitter api key
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")

# twitter api key
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")

# twitter api key
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

# your local timezone - http://pytz.sourceforge.net/
LOCAL_TIMEZONE = pytz.timezone("America/Los_Angeles")

# you can really only search back 6 or 7 days
START_DATE_FOR_SEARCH = LOCAL_TIMEZONE.localize(datetime.datetime(2015, 6, 5, 8, 0))

# what we'll name our csv file
CSV_FILENAME = "_%s_tweets.csv" % (TWEET_HASHTAG)


class TwitterHashtagSearch(object):

    twitter_timezone = timezone("UTC")

    # column names for our csv
    # this will change if you pull in more data
    csv_headers = [
        "hashtag",
        "tweet_utc_date",
        "user_name",
        "user_screen_name",
        "bot_or_not",
        "tweet_text",
        "tweet_url",
        "tweet_id",
        "user_profile_image_url",
        "user_location",
        "source",
        "in_reply_to_screen_name",
        "in_reply_to_status_id",
        "image_link",
        "retweet_count",
        "favorite_count",
        "time_zone",
        "geo_enabled",
        "geography",
        "coordinates",
        "lang",
    ]


    def _init(self, *args, **kwargs):
        """
        start the whole twitter hashtag search a rollin
        """

        # default params for our loop
        max_id = None
        search_is_done = False

        # set our date defaults for comparisons
        start_date_utc = START_DATE_FOR_SEARCH.astimezone(self.twitter_timezone)

        # open a file
        with open(CSV_FILENAME, "wb") as csv_file:

            # that will become our csv
            csv_output = csvkit.py2.CSVKitWriter(csv_file, delimiter=",", encoding="utf-8")

            # write the header row to the csv file
            csv_output.writerow(self.csv_headers)

            # begin the loop
            while (search_is_done == False):

                # return our tweets
                tweet_results = self.construct_twitter_search(TWEET_HASHTAG, max_id)

                # for each status
                for tweet in tweet_results["statuses"]:

                    # get the UTC time for each
                    tweet_date = parser.parse(tweet["created_at"])

                    # set some timezone information
                    tweet_date = tweet_date.replace(tzinfo=self.twitter_timezone)

                    # if the tweet falls between our begin and end range
                    if tweet_date >= start_date_utc:

                        # build a new csv row
                        csv_row = self.build_csv_row_from(tweet, tweet_date)

                        # write the new csv row
                        csv_output.writerow(csv_row)

                # if we get through the loop get the new max id, which is in effect paging
                max_id = self.get_max_id(tweet_results)

                # if no max_id
                if max_id == None:

                    # end the loop
                    search_is_done = True

                # otherwise
                else:

                    # get more of them
                    print "Retrieving more tweets since %s" % (max_id)


    def construct_twitter_search(self, hashtag, max_id):
        """
        function to auth with twitter and return tweets
        """

        # build the authorization for the twitter api
        twitter_object = Twitter(
            auth=OAuth(
                TWITTER_ACCESS_TOKEN,
                TWITTER_ACCESS_TOKEN_SECRET,
                TWITTER_CONSUMER_KEY,
                TWITTER_CONSUMER_SECRET
            )
        )

        # retrieve the tweets
        tweet_results = twitter_object.search.tweets(
            q=hashtag,
            count=1000,
            result_type="recent",
            include_entities=True,
            max_id=max_id,
            lang="en"
        )

        # return them
        return tweet_results


    def build_csv_row_from(self, tweet, tweet_date):
        """
        create a csv row from tweet results
        """

        # construct url format
        tweet_url = "https://twitter.com/" + tweet["user"]["screen_name"].encode('ascii', 'ignore') + "/status/" + str(tweet["id"])

        # output some information
        print "%s - %s - %s" % (
            tweet_date,
            tweet["user"]["screen_name"],
            tweet_url,
        )

        # see if an image is present in the dictionary
        has_image = tweet.has_key("media")

        # if there are images
        if has_image == True:

            # grab it
            tweet_image = tweet["media"]["media_url_https"]

        # otherwise
        else:

            # call it none
            tweet_image = None

        # build a row of tweet data
        csv_row_data = [
            TWEET_HASHTAG,
            tweet_date,
            tweet["user"]["name"].encode('ascii', 'ignore'),
            tweet["user"]["screen_name"].encode('ascii', 'ignore'),
            tweet["text"].encode('ascii', 'ignore'),
            tweet["text"].encode('ascii', 'ignore'),
            tweet_url.encode('ascii', 'ignore'),
            tweet["id"],
            tweet["user"]["profile_image_url"].encode('ascii', 'ignore'),
            tweet["user"]["location"].encode('ascii', 'ignore'),
            tweet["source"].encode('ascii', 'ignore'),
            tweet["in_reply_to_screen_name"],
            tweet["in_reply_to_status_id_str"],
            tweet_image,
            tweet["retweet_count"],
            tweet["favorite_count"],
            tweet["user"]["time_zone"],
            tweet["user"]["geo_enabled"],
            tweet["geo"],
            tweet["coordinates"],
            tweet["lang"],
        ]

        # print the row
        print csv_row_data

        # return the row
        return csv_row_data


    def get_max_id(self, results):
        """
        get the max_id of the next twitter search if present
        """
        # see if the metadata has a next_results key
        # value is the idea to pull tweets from
        more_tweets = results["search_metadata"].has_key("next_results")

        # if there are more
        if more_tweets == True:

            # find the max id
            parsed_string = results["search_metadata"]["next_results"].split("&")
            parsed_string = parsed_string[0].split("?max_id=")
            max_id = parsed_string[1]

        # otherwise
        else:

            # max id is nothing
            max_id = None

        # return the max id
        return max_id


if __name__ == '__main__':
    task_run = TwitterHashtagSearch()
    task_run._init()
    print "\nTask finished at %s\n" % str(datetime.datetime.now())
