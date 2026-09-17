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

print(response.status_code) 
tgt = response.text
print(tgt.startswith("TGT-")) 