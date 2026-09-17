import os
from dotenv import load_dotenv
import requests

load_dotenv()
username = os.getenv("EPIAS_USERNAME")
password = os.getenv("EPIAS_PASSWORD")
url = "https://giris.epias.com.tr/cas/v1/tickets"

payload = {
    "username": username ,
    "password": password,
}

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}

response = requests.post(url, data=payload, headers=headers)
#testing -> print(response.status_code) 
tgt = response.text
#testing -> print(tgt.startswith("TGT-")) 

data_headers = {"TGT":tgt}
data_url = "https://seffaflik.epias.com.tr/electricity-service/v1/consumption/data/realtime-consumption"
package = {
    "startDate":    "2026-09-15T00:00:00+03:00",
    "endDate":      "2026-09-15T00:00:00+03:00",
}
pdo_consumption_data = requests.post(data_url,json=package,headers=data_headers)

if pdo_consumption_data.status_code == 200:
    consumption = pdo_consumption_data.json()
    print(consumption.keys())

else:
    print(pdo_consumption_data.text)

print(len(consumption["items"]))
print(consumption["items"][0])

new_data_url = "https://seffaflik.epias.com.tr/electricity-service/v1/consumption/data/load-estimation-plan" 
pdo_loadest_data = requests.post(new_data_url,json=package,headers=data_headers)

if pdo_loadest_data.status_code == 200:
    load_plan = pdo_loadest_data.json()
    print(load_plan.keys())

else:
    print(pdo_loadest_data.text)

print(len(load_plan["items"]))
print(load_plan["items"][0])