import requests
import logging
import time
import csv
from bs4 import BeautifulSoup
from random import randint

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

config = {
    "operator_ids": [
        2731
    ],
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
        determine_incidents_tab = get_list_items(raw_html, "OuterPanel", 1)
        if determine_incidents_tab["length"] == 4:
            incident_url = build_url(url, determine_incidents_tab["url_stub"])
            incident_details_html = open_page_and_get_soup(incident_url)
            determine_details_tab = get_list_items(incident_details_html, "Incidents", -1)
            incident_details_url = build_url(url, determine_details_tab["url_stub"])
            details_html = open_page_and_get_soup(incident_details_url)
            write_to_csv(details_html)

def populate_config(state):
    #populated the config dict with operator ID's only from the given state

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
            time.sleep(.25)
            request = requests.get(url, headers = config["request_headers"])
            if request.status_code == 200:
                raw_html = BeautifulSoup(request.content)
                return raw_html
            else:
                return False
        except Exception, exception:
            logger.error("(%s) %s - %s" % (str(datetime.datetime.now()), request_url, exception))
            return False

def write_to_csv(html):
    list_tr = html.find("div", {"id": "Incidents_tab_4"}).find_all("tr")
    op_name  = html.find("h4").text.lower().replace(" ","_")
    list_th = list_tr[0].find_all("th")
    with open(op_name + ".csv", "wb") as file:
        csv_output = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        csv_column_names = clean_text_for_csv(list_th, "th")
        csv_output.writerow(csv_column_names)
        list_td = list_tr[1:]
        for row in list_td:
            table_cells = row.find_all("td")
            csv_rows = clean_text_for_csv(table_cells, "td")
            logger.debug(csv_rows)
            csv_output.writerow(csv_rows)

def clean_text_for_csv(list, tag):
    if tag == "th":
        list_of_headers = []
        for item in list:
            output = item.get_text().encode("utf8").strip().lower().replace(" ", "_").replace("\xc2\xa0","")
            list_of_headers.append(output)
        return list_of_headers
    if tag == "td":
        list_of_row_data = []
        for item in list:
            output = item.get_text().encode("utf8").strip().replace(" ", "_").replace("\xc2\xa0","")
            list_of_row_data.append(output)
        return list_of_row_data

if __name__ == "__main__":
    _init_()