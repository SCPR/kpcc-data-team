import pandas as pd 
import urllib2
from bs4 import BeautifulSoup



#This function should grab the information from the page only if that operator is in California. It is fed a single link and returns a list of dictionaries with the relevant information 
def operator_information(master_list): 
    
    open_url=urllib2.urlopen(master_list)
    
    read_page=BeautifulSoup(open_url)
    
    tbody =  read_page.find('tbody')
    
    list_tr = tbody.find_all('tr')
    
    list_rows = []
    
    for item in list_tr:
        
        row = {"name": "NA" , "id": "NA", "incidents": "NA", "inspections": 'NA', "enforcement-actions": "NA", "hazardous-liquid": "false" , "states-of-operation-hl": "-" , "inspected-miles-hl": "-" , "gas-transmission": "false" , "states-of-operation-gt": "-" , "inspected-miles-gt": "-" , "gas-gathering": "false" , "states-of-operation-gg": "-" , "inspected-miles-gg": "-" }
        
        operator_page = BeautifulSoup(urllib2.urlopen("http://primis.phmsa.dot.gov/comm/reports/operator/"+item.find('a').get('href')))
        
        if operator_page.find(text = "CA"):

            my_table = operator_page.find("thead")

            information =  my_table.find_all('tr')
            
            info_text = my_table.text
            
            row["name"] = item.find_all('td')[1].text
            
            row["id"] = int(item.find_all('td')[0].text)
            
            if item.find_all('td')[4].text == ' ':
                row["incidents"] = 'null'
            else:
                row["incidents"] = item.find_all('td')[4].text
            
            if item.find_all('td')[5].text == ' ':
                row["inspections"] = 'null'
            else:
                row["inspections"] = item.find_all('td')[5].text
            
            if item.find_all('td')[6].text == ' ':
                row["enforcement-actions"] = 'null'
            else:
                row["enforcement-actions"] = item.find_all('td')[6].text
                    
            
            if "Hazardous Liquid" in info_text:
                row['hazardous-liquid'] = "true"
                row['states-of-operation-hl'] = information[1].find_all('td')[0].text
                row['inspected-miles-hl'] =information[2].find_all('td')[0].text

            if "Gas Transmission" in info_text:
                row['gas-transmission'] = "true"
                row['states-of-operation-gt'] = information[4].find_all('td')[0].text
                row['inspected-miles-gt'] = information[5].find_all('td')[0].text

            if "Gas Gathering" in info_text:
                row['gas-gathering'] = "true"
                row['states-of-operation-gg'] = information[7].find_all('td')[0].text
                row['inspected-miles-gg'] = information[8].find_all('td')[0].text
            
            list_rows.append(row)
    
    return list_rows
            
#create dataframe
data_frame_operators = pd.DataFrame(operator_information("http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html"), columns = ["name", "id", "incidents", "inspections", "enforcement-actions", "hazardous-liquid", "states-of-operation-hl", "inspected-miles-hl", "gas-transmission", "states-of-operation-gt", "inspected-miles-gt", "gas-gathering", "states-of-operation-gg", "inspected-miles-gg"] )

#getting rid of commas in numbers for conversion to sortable ints
data_frame_operators['inspected-miles-hl'] = data_frame_operators['inspected-miles-hl'].str.replace(',','')
data_frame_operators['inspected-miles-gt'] = data_frame_operators['inspected-miles-gt'].str.replace(',','')
data_frame_operators['inspected-miles-gg'] = data_frame_operators['inspected-miles-gg'].str.replace(',','')

data_frame_operators['inspected-miles-hl'] = data_frame_operators['inspected-miles-hl'].convert_objects(convert_numeric=True)
data_frame_operators['inspected-miles-gt'] = data_frame_operators['inspected-miles-gt'].convert_objects(convert_numeric=True)
data_frame_operators['inspected-miles-gg'] = data_frame_operators['inspected-miles-gg'].convert_objects(convert_numeric=True)

data_frame_operators['enforcement-actions'] = data_frame_operators['enforcement-actions'].convert_objects(convert_numeric=True)
data_frame_operators['inspections'] = data_frame_operators['inspections'].convert_objects(convert_numeric=True)
data_frame_operators['incidents'] = data_frame_operators['incidents'].convert_objects(convert_numeric=True)

data_frame_operators = data_frame_operators.fillna('-')
#export to csv
data_frame_operators.to_csv('California_Pipeline_operators.csv', encoding = 'utf-8')