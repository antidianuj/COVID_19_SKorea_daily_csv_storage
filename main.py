import requests
import json
import csv
from csv import writer



def indicator():
    try:
        csvfile=open('record.csv','r', newline='')
        return 1;
    except :
        return 0;
    
    
def csver(eta):
    if(indicator()==1):
        with open('record.csv', 'a') as f_object:
            
            writer_object = writer(f_object)
            writer_object.writerow(eta)
            f_object.close()
    else:
        with open('record.csv', 'a') as f_object:
            
            writer_object = writer(f_object)
            writer_object.writerow(ref_listy)
            writer_object.writerow(eta)
            f_object.close()
        
        
        
    
ref_listy=["Date","Active","Deaths","Recovered"]

url = "https://covid-19-data.p.rapidapi.com/report/country/name"

querystring = {"name":"South Korea","date":"2020-04-01"}

headers = {
    'x-rapidapi-key': "API-Key>",
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data=response.text
print(data)


parser=json.loads(data)
provincer=parser[0]['provinces']
confirmed=provincer[0]['confirmed']
recovered=provincer[0]['recovered']
deaths=provincer[0]['deaths']
active=provincer[0]['active']
date=parser[0]['date']

listy=[date,active,deaths,recovered,confirmed]
csver(listy)






