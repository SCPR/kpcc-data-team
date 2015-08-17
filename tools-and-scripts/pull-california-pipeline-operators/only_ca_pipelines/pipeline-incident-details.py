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
    get_ca_op_incident_details()
    

def get_all_incident_details():
    main_page = open_page_and_get_soup("http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html")
    op_ids = main_page.find('tbody').find_all("tr")
    for id in op_ids:
         config["operator_ids"].append(id.find('td').text.strip())
    #constructs a list of pipeline incident details urls
    url_prefix = "http://primis.phmsa.dot.gov/comm/reports/operator/OperatorIM_opid_"
    url_suffix = ".html?nocache=%s" % (randint(1000, 1999))
    list_operator_incident_urls = []
    for operator in config["operator_ids"]:
        url = build_url(url_prefix, operator, url_suffix)
        raw_html = open_page_and_get_soup(url)
        find_list_items = get_list_items(raw_html, "OuterPanel", 1)
        if find_list_items["length"] == 4:
            find_incidents_list_items = get_list_items(raw_html, "Incidents", -1)
            incident_div_tag  = find_incidents_list_items["url_stub"].replace("#","")
            """ACCESS AND PROCESS THE TABLE IN FRONT OF ME """
            #this determines whether there is a table to scrape
            try:
                if raw_html.find('div', {'id': incident_div_tag}).find("p").text == "No incidents reported since 2006.":
                    pass
                else:
                    write_to_csv(raw_html, incident_div_tag)
            except:
                pass

def get_ca_op_incident_details(): 
    #start from main operator list, go into each to see if it's in CA. If in CA, jump to incident tab html and grab rows that are only present in CA 
    main_page = open_page_and_get_soup("http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html")
    op_ids = main_page.find('tbody').find_all("tr")
    for id in op_ids:
         config["operator_ids"].append(id.find('td').text.strip())
    #constructs a list of pipeline incident details urls
    url_prefix = "http://primis.phmsa.dot.gov/comm/reports/operator/OperatorIM_opid_"
    url_suffix = ".html?nocache=%s" % (randint(1000, 1999))
    list_operator_incident_urls = []
    for operator in config["operator_ids"]:
        url = build_url(url_prefix, operator, url_suffix)
        raw_html = open_page_and_get_soup(url)
        if raw_html.find(text = "CA"):
            find_incidents_list_items = get_list_items(raw_html, "Incidents", -1)
            incident_div_tag  = find_incidents_list_items["url_stub"].replace("#","")
            try:
                write_to_ca_csv(raw_html, incident_div_tag)
            except:
                pass
            
            


def write_to_csv(html,div_tag):
    list_of_rows = []
    list_tr = html.find("div", {"id": div_tag }).find_all("tr")
    op_name  = html.find("h4").text.lower().replace(" ","_")
    column_names = map(lambda x: x.text.encode("utf8").strip().lower().replace(" ", "_").replace("\xc2\xa0",""), list_tr[0].find_all("th"))
    list_of_rows.append(column_names)
    for item in list_tr[1:-1]:
        """this removes the first row, which is the column names, the last row which is just totals
        and a weird hole in the table"""
        list_of_rows.append(map(lambda x: x.text.encode("utf8").strip().replace(",",""), item.find_all("td")[0:-1]))
    csv_file = open(op_name+".csv", "wb")
    writer = csv.writer(csv_file)
    writer.writerows(list_of_rows)

# I know I shouldn't just copy the function with one small change but I will clean it up later
def write_to_ca_csv(html,div_tag):
    list_of_rows = []
    list_tr = html.find("div", {"id": div_tag }).find_all("tr")
    op_name  = html.find("h4").text.lower().replace(" ","_")
    column_names = map(lambda x: x.text.encode("utf8").strip().lower().replace(" ", "_").replace("\xc2\xa0",""), list_tr[0].find_all("th"))
    for item in list_tr[1:-1]:
        if item.find_all("td")[3].text.strip() == "CA":
            rows.append(column_names)
            rows.append(map(lambda x: x.text.encode("utf8").strip().replace(",",""), item.find_all('td')[0:-1]))
            
    csv_file = open(op_name+".csv", "wb")
    writer = csv.writer(csv_file)
    writer.writerows(list_of_rows)


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



if __name__ == "__main__":
    _init_()
