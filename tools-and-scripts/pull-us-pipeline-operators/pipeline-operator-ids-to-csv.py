import requests
import pandas as pd
import logging
import time
import datetime
from bs4 import BeautifulSoup

logger = logging.getLogger("root")
logging.basicConfig(
    format = "\033[1;36m%(levelname)s: %(filename)s (def %(funcName)s %(lineno)s): \033[1;37m %(message)s",
    level=logging.DEBUG
)

config = {
    "url": "http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html",
    "csv_name": "california_pipeline_operators.csv",
    "csv_columns": [
        "id",
        "california",
        "name",
        "incidents",
        "inspections",
        "enforcement-actions",
        "hazardous-liquid",
        "states-of-operation-hl",
        "inspected-miles-hl",
        "gas-transmission",
        "states-of-operation-gt",
        "inspected-miles-gt",
        "gas-gathering",
        "states-of-operation-gg",
        "inspected-miles-gg"
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
    raw_html = open_page_and_get_soup(config["url"])
    operator_results = generate_operator_shopping_list(raw_html)
    list_of_cali_operators = []
    for operator in operator_results:
        operator_html = open_page_and_get_soup(operator["url"])
        updated_operator = operator_details(operator, operator_html)
        list_of_cali_operators.append(updated_operator)
        #logger.DEBUG(list_of_cali_operators)
    create_pandas_dataframe(list_of_cali_operators, config["csv_columns"])


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


def generate_operator_shopping_list(raw_html):
    """
    this function should grab the information from the page only if that operator is in california
    it is fed a single link and returns a list of dictionaries with the relevant information
    """
    logger.debug("Building operator shopping list")
    initial_page = open_page_and_get_soup(config["url"])
    tbody = initial_page.find("tbody")
    list_tr = tbody.find_all("tr")
    list_rows = []
    for item in list_tr:
        row = {}
        url_stub = item.find("a").get("href")
        row["url"] = "http://primis.phmsa.dot.gov/comm/reports/operator/%s" % (url_stub)
        row["name"] = item.find_all("td")[1].text.strip()
        row["id"] = int(item.find_all("td")[0].text)
        if item.find_all("td")[4].text == " ":
            row["incidents"] = None
        else:
            row["incidents"] = item.find_all("td")[4].text.strip()
        if item.find_all("td")[5].text == " ":
            row["inspections"] = None
        else:
            row["inspections"] = item.find_all("td")[5].text.strip()
        if item.find_all("td")[6].text == " ":
            row["enforcement-actions"] = None
        else:
            row["enforcement-actions"] = item.find_all("td")[6].text.strip()
        list_rows.append(row)
    return list_rows


def operator_details(operator, operator_html):
    logger.debug("Gathering details for %s" % (operator["name"]))
    my_table = operator_html.find("thead")
    information = my_table.find_all("tr")
    if operator_html.find(text = "CA"):
        operator["california"] = True
    if "Hazardous Liquid" in my_table.text:
        operator["hazardous-liquid"] = "true"
        operator["states-of-operation-hl"] = information[1].find_all("td")[0].text.strip()
        operator["inspected-miles-hl"] = information[2].find_all("td")[0].text.strip().replace(",", "")
    if "Gas Transmission" in my_table.text:
        operator["gas-transmission"] = "true"
        operator["states-of-operation-gt"] = information[4].find_all("td")[0].text.strip()
        operator["inspected-miles-gt"] = information[5].find_all("td")[0].text.strip().replace(",", "")
    if "Gas Gathering" in my_table.text:
        operator["gas-gathering"] = "true"
        operator["states-of-operation-gg"] = information[7].find_all("td")[0].text.strip()
        operator["inspected-miles-gg"] = information[8].find_all("td")[0].text.strip().replace(",", "")
    logger.debug(operator)
    return operator


def create_pandas_dataframe(list, column_names):
    data_frame_operators = pd.DataFrame(list, columns=column_names)
    data_frame_operators["inspected-miles-hl"] = data_frame_operators["inspected-miles-hl"].convert_objects(convert_numeric = True)
    data_frame_operators["inspected-miles-gt"] = data_frame_operators["inspected-miles-gt"].convert_objects(convert_numeric=True)
    data_frame_operators["inspected-miles-gg"] = data_frame_operators["inspected-miles-gg"].convert_objects(convert_numeric=True)
    data_frame_operators["enforcement-actions"] = data_frame_operators["enforcement-actions"].convert_objects(convert_numeric=True)
    data_frame_operators["inspections"] = data_frame_operators["inspections"].convert_objects(convert_numeric=True)
    data_frame_operators["incidents"] = data_frame_operators["incidents"].convert_objects(convert_numeric=True)
    data_frame_operators = data_frame_operators.fillna("")
    data_frame_operators.to_csv(config["csv_name"], encoding = "utf-8")


if __name__ == "__main__":
    _init_()
