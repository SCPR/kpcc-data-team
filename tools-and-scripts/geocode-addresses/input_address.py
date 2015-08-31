# Uses wrapper found here: https://github.com/datadesk/python-googlegeocoder
# pip install python-googlegeocoder

import csv
import logging
import time
import datetime
from googlegeocoder import GoogleGeocoder

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

def geocode_a_single_address():
    ''' convert text file of addresses to a list '''
    address = raw_input("Enter an address to geocode ... > ")
    geocoder = GoogleGeocoder()
    try:
        search = geocoder.get(address)
        if len(search) > 0:
            first_result = search[0]
            address_for_output = '%s\t%s\t%s\t%s\t%s\n' % (
                first_result.formatted_address.encode('ascii', 'ignore'),
                first_result.geometry.location.lat,
                first_result.geometry.location.lng,
                first_result.geometry.location_type,
                first_result.geometry.partial_match
            )
            print address_for_output
        else:
            print "Can't geocode this"
    except Exception, exception:
        logger.error("%s" % (exception))

if __name__ == "__main__":
    geocode_a_single_address()
