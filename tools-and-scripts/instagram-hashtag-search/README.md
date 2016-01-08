instagram-hashtag-search
========================

**WHAT**: A quick and easy Python script to grab instagram posts from a given hashtag, based on a suggestion by [Maggie Lee](https://twitter.com/maggie_a_lee)

If you liked this, you might also like [a quick and easy Python script to grab tweets from a given hashtag]()

Quickstart
==========

* cd into the directory

        cd instagram-hashtag-search

    * If you have virtualenv installed...

            mkvirtualenv instagram-hashtag-search
            pip install -r requirements.txt

    * Or just

            pip install -r requirements.txt

* open ```_init_.py``` and fill out some of the constants at the top

        # hashtag to search
        IMAGE_HASHTAG = "gapol"

        # number of images to return
        IMAGE_COUNT = 100

        # instagram api key - register here: https://www.instagram.com/developer/register/
        # my credentials set in my bash_profile. you can set here as string
        INSTAGRAM_CLIENT_ID = "1234ABCD"

        # instagram api key - register here: https://www.instagram.com/developer/register/
        # my credentials set in my bash_profile. you can set here as string
        INSTAGRAM_CLIENT_SECRET = "1234ABCD"

        # your local timezone - find more here: http://pytz.sourceforge.net/
        LOCAL_TIMEZONE = pytz.timezone("America/Los_Angeles")

* Run the script to generate a csv

        python _init_.py
