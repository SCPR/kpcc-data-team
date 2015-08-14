import requests
import pandas as pd
import logging
import time
from bs4 import BeautifulSoup
from random import randint

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

config = {

    "operator_ids": [
        2731,
        12582,
    ],

    # "url": "http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html",
    # "csv_name": "california_pipeline_operators.csv",
    # "csv_columns": [
    #     "id",
    #     "california",
    #     "name",
    #     "incidents",
    #     "inspections",
    #     "enforcement-actions",
    #     "hazardous-liquid",
    #     "states-of-operation-hl",
    #     "inspected-miles-hl",
    #     "gas-transmission",
    #     "states-of-operation-gt",
    #     "inspected-miles-gt",
    #     "gas-gathering",
    #     "states-of-operation-gg",
    #     "inspected-miles-gg"
    # ],
    "request_headers": {
        "From": "ckeller@scpr.org",
        "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19"
    },
}

def _init_():
    """
    kicks off the whole process
    """
    url_prefix = "http://primis.phmsa.dot.gov/comm/reports/operator/OperatorIM_opid_"
    url_suffix = ".html?nocache=%s" % (randint(1000, 1999))
    for operator in config["operator_ids"]:
        url = build_url(url_prefix, operator, url_suffix)
        raw_html = open_page_and_get_soup(url)
        find_list_items = get_list_items(raw_html, "OuterPanel", 1)
        if find_list_items["length"] == 4:
            incident_url = build_url(url, find_list_items["url_stub"])
            incident_details_html = open_page_and_get_soup(incident_url)
            find_incidents_list_items = get_list_items(incident_details_html, "Incidents", -1)
            incident_details_url = build_url(url, find_incidents_list_items["url_stub"])
            logger.debug(incident_details_url)


            """ACCESS AND PROCESS THE TABLE IN FRONT OF ME """
            """ IF NO TABLE MAKE SURE TO HANDLE THE EXCEPTION """

        else:
            break

def get_list_items(html, id, position):
    target_div = html.find("div", {"id": id })
    list_id = "%s_tabs" % (id)
    target_list = target_div.find("ul", {"id": list_id})
    find_list_items = target_list.find_all("li")
    list_dict = {}
    list_dict["length"] = len(find_list_items)
    list_dict["url_stub"] = find_list_items[position].find("a").get("href")
    return list_dict

def build_url(*args):
    if len(args) == 3:
        output_url = "%s%s%s" % (args[0], args[1], args[2])
        return output_url
    elif len(args) == 2:
        output_url = "%s%s" % (args[0], args[1])
        return output_url
    else:
        return false

def open_page_and_get_soup(url):
    """
    make request to url and return response content
    """
    while True:
        try:
            time.sleep(3)
            request = requests.get(url, headers = config["request_headers"])
            if request.status_code == 200:
                raw_html = BeautifulSoup(request.content)
                return raw_html
            else:
                return False
        except Exception, exception:
            logger.error("(%s) %s - %s" % (str(datetime.datetime.now()), request_url, exception))
            return False



if __name__ == "__main__":
    _init_()
