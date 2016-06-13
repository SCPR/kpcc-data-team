#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import datetime
from datetime import tzinfo
import csvkit
import pytz
from pytz import timezone
from instagram.client import InstagramAPI

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

# hashtag to search
IMAGE_HASHTAG = "gapol"

# number of images to return
IMAGE_COUNT = 100

# instagram api key - register here: https://www.instagram.com/developer/register/
# my credentials set in my bash_profile. you can set here as string
INSTAGRAM_CLIENT_ID = os.environ.get("INSTAGRAM_CLIENT_ID")

# instagram api key - register here: https://www.instagram.com/developer/register/
# my credentials set in my bash_profile. you can set here as string
INSTAGRAM_CLIENT_SECRET = os.environ.get("INSTAGRAM_CLIENT_SECRET")

# your local timezone - http://pytz.sourceforge.net/
LOCAL_TIMEZONE = pytz.timezone("America/Los_Angeles")

# what we'll name our csv file
CSV_FILENAME = "_#%s_instagram.csv" % (IMAGE_HASHTAG)


class InstagramHashtagClient(object):

    # timezone of data from instagram
    instagram_timezone = timezone("UTC")

    def _init(self, *args, **kwargs):
        """
        start the ball a rolling with a request to instagram API
        open a csv file and output the headers and rows based on results
        """
        api = InstagramAPI(
            client_id = INSTAGRAM_CLIENT_ID,
            client_secret = INSTAGRAM_CLIENT_SECRET
        )
        instagram_media = api.tag_recent_media(IMAGE_COUNT, 0, IMAGE_HASHTAG)

        # open the csv file
        with open(CSV_FILENAME, "wb") as csv_file:

            csv_output = csvkit.py2.CSVKitWriter(csv_file, delimiter=",", encoding="utf-8")

            # write the header row to the csv file
            csv_output.writerow(["hashtag", "local_date_time", "user_name", "image_link", "image_caption", "like_count", "comment_count", "post_link", "post_type", "post_tags", "post_likes", "utc_date_time"])

            # loop through the results
            for item in instagram_media[0]:

                # build a new csv row
                csv_row = self.build_csv_row_from(item)

                # write the new csv row
                csv_output.writerow(csv_row)


    def build_csv_row_from(self, item):
        """
        parse the api data and build a csv row
        """
        utc_post_date = item.created_time.replace(tzinfo = self.instagram_timezone)
        local_post_date = utc_post_date.astimezone(LOCAL_TIMEZONE)
        try:
            csv_row_data = [
                IMAGE_HASHTAG,
                local_post_date,
                self.unicode_or_bust(item.user.username),
                self.unicode_or_bust(item.images["standard_resolution"].url),
                self.unicode_or_bust(item.caption.text),
                item.like_count,
                item.comment_count,
                self.unicode_or_bust(item.link),
                self.unicode_or_bust(item.type),
                self.join_list_elements(item.tags),
                self.join_list_elements(item.likes),
                utc_post_date,
            ]
            logger.info(csv_row_data)
            return csv_row_data
        except (RuntimeError, ValueError, TypeError, NameError) as exception:
            logger.error("%s - %s" % (exception, item.link))


    def join_list_elements(self, list):
        """
        for tags and users who liked, convert a list of times to commma-separated strings
        """
        output = []
        for item in list:
            if hasattr(item, "name"):
                output.append(item.name)
            elif hasattr(item, "username"):
                output.append(item.username)
        output = ", ".join(output)
        return output


    def unicode_or_bust(self, obj, encoding="utf-8"):
        """
        convert all byte strings to unicode
        """
        if isinstance(obj, basestring):
            if not isinstance(obj, unicode):
                obj = unicode(obj, encoding)
        return obj


if __name__ == "__main__":
    task_run = InstagramHashtagClient()
    task_run._init()
    print "\nTask finished at %s\n" % str(datetime.datetime.now())
