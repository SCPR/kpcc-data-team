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
        
        row = {"Name": "NA" , "ID": "NA", "Incidents": "NA", "Inspections": 'NA', "Enforcement Actions": "NA", "Hazardous Liquid": "NA" , "States of Operation-HL": "NA" , "Fed and State Inspected Miles-HL": "NA" , "Gas Transmission": "NA" , "States of Operation-GT": "NA" , "Fed and State Inspected Miles-GT": "NA" , "Gas Gathering": "NA" , "States of Operation-GG": "NA" , "Fed and State Inspected Miles-GG": "NA" }
        
        operator_page = BeautifulSoup(urllib2.urlopen("http://primis.phmsa.dot.gov/comm/reports/operator/"+item.find('a').get('href')))
        
        if operator_page.find(text = "CA"):

            my_table = operator_page.find("thead")

            information =  my_table.find_all('tr')
            
            info_text = my_table.text
            
            row["Name"] = item.find_all('td')[1].text
            
            row["ID"] = int(item.find_all('td')[0].text)
            
            if item.find_all('td')[4].text == ' ':
                row["Incidents"] = 'NA'
            else:
                row["Incidents"] = item.find_all('td')[4].text
            
            if item.find_all('td')[5].text == ' ':
                row["Inspections"] = 'NA'
            else:
                row["Inspections"] = item.find_all('td')[5].text
            
            if item.find_all('td')[6].text == ' ':
                row["Enforcement Actions"] = 'NA'
            else:
                row["Enforcement Actions"] = item.find_all('td')[6].text
                    
            
            if "Hazardous Liquid" in info_text:
                row['Hazardous Liquid'] = "Present"
                row['States of Operation-HL'] = information[1].find_all('td')[0].text
                row['Fed and State Inspected Miles-HL'] = information[2].find_all('td')[0].text

            if "Gas Transmission" in info_text:
                row['Gas Transmission'] = "Present"
                row['States of Operation-GT'] = information[4].find_all('td')[0].text
                row['Fed and State Inspected Miles-GT'] = information[5].find_all('td')[0].text

            if "Gas Gathering" in info_text:
                row['Gas Gathering'] = "Present"
                row['States of Operation-GG'] = information[7].find_all('td')[0].text
                row['Fed and State Inspected Miles-GG'] = information[8].find_all('td')[0].text
            
            list_rows.append(row)
    
    return list_rows
            
#create dataframe
data_frame_operators = pd.DataFrame(operator_information("http://primis.phmsa.dot.gov/comm/reports/operator/OperatorListNoJS.html"), columns = ["Name", "ID", "Incidents", "Inspections", "Enforcement Actions", "Hazardous Liquid", "States of Operation-HL", "Fed and State Inspected Miles-HL", "Gas Transmission", "States of Operation-GT", "Fed and State Inspected Miles-GT", "Gas Gathering", "States of Operation-GG", "Fed and State Inspected Miles-GG"] )

#export to csv
data_frame_operators.to_csv('California_Pipeline_operators.csv', encoding = 'utf-8')