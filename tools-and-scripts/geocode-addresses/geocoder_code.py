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

def create_list_addresses_from_file():
    """
    convert text file of addresses to a list
    """
    list_of_addresses = []
    address_file = open("addresses.txt", "r")
    list_of_addresses = address_file.readlines()
    address_file.close()
    geocode_addresses_from_file(list_of_addresses)

def geocode_addresses_from_file(list_of_addresses):
    """
    run a list of addresses through the geocoder
    """
    geocoder = GoogleGeocoder()
    f = open("results.txt", "a")
    for address in list_of_addresses:
        try:
            address = address.replace("\n", "")
            search = geocoder.get(address)
        except Exception, exception:
            print "Can't geocode this"
            logger.error("%s" % (exception))
        if len(search) > 0:
            first_result = search[0]
            address_for_output = '%s\t%s\t%s\t%s\t%s\n' % (
                first_result.formatted_address.encode("ascii", "ignore"),
                first_result.geometry.location.lat,
                first_result.geometry.location.lng,
                first_result.geometry.location_type,
                first_result.geometry.partial_match
            )
            print address_for_output
            f.write(address_for_output)
        else:
            print "Can't geocode this"
        time.sleep(3)
    f.close()

if __name__ == "__main__":
    create_list_addresses_from_file()
