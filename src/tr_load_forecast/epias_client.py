import requests
import os
from dotenv import load_dotenv

load_dotenv()
_tgt = None
def get_TGT(
    force=False,
    username = os.getenv("EPIAS_USERNAME"),
    password = os.getenv("EPIAS_PASSWORD"),
    url="https://giris.epias.com.tr/cas/v1/tickets",
    headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "text/plain",
    }
):
    payload = {
        "username": username,
        "password": password,
    }
    global _tgt
    if (_tgt is None) or force:
        _tgt = requests.post(url,data=payload,headers=headers).text

    return {"TGT":_tgt}
    """
    username & password:   os.getenv() \n
    url:        url to create the ticket    \n
    payload:    dict contains username & password \n
    headers:    i don't know either \n
    returns -> respond
    """

def get_data(
        concept:str = "realtime-consumption",
        url:str = "https://seffaflik.epias.com.tr/electricity-service/v1/consumption/data/",
        startDate = "2026-09-15",
        endDate = "2026-09-15",
):
    header = get_TGT()
    startDate = startDate.strip() + "T00:00:00+03:00"
    endDate = endDate.strip() + "T00:00:00+03:00"
    package = {
        "startDate": startDate,
        "endDate": endDate,
    }

    posturl = url + concept
    return requests.post(url=posturl,headers=header,json=package)
    """
    concept: where to what to use
    posturl: last part of the URL(you want to use) \n
    payload: username and password
    """
if __name__ == "__main__":
    consumption_data = get_data(concept="realtime-consumption")
    if consumption_data.status_code==200 :
        consumption_data = consumption_data.json()
        print(consumption_data.keys())