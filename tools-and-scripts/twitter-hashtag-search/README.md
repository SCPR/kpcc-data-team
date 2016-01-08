twitter-hashtag-search
========================

**WHAT**: A quick and easy Python script to grab tweets from a given hashtag

If you liked this, you might also like [a quick and easy Python script to grab instagram posts from a given hashtag]()

Quickstart
==========

* cd into the directory

        cd twitter-hashtag-search

    * If you have virtualenv installed...

            mkvirtualenv twitter-hashtag-search
            pip install -r requirements.txt

    * Or just

            pip install -r requirements.txt

* open ```_init_.py``` and fill out some of the constants at the top

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

* Run the script to generate a csv

        python _init_.py
