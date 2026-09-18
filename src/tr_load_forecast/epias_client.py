import requests
import os
from dotenv import load_dotenv
from datetime import date,timedelta
import time

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
    """ returns -> respond """
    payload = {
        "username": username,
        "password": password,
    }
    global _tgt
    if (_tgt is None) or force:
        _tgt = requests.post(url,data=payload,headers=headers).text

    return {"TGT":_tgt}
    

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

def safely_get_data(maxtry=3,awaittime=5,**kwargs):
    for try_ in range(1,maxtry+1):
        try:
            data= get_data(**kwargs)
            if data.status_code == 200:
                return data.json()
            print(f"try: {try_}, statuscode: {data.status_code}")
        except requests.RequestException as e:
            print(f"try: {try_},exception: {e}")
        time.sleep(awaittime)
    raise RuntimeError(f"tried: {maxtry} failed")

def get_start_end(year:int,month:int):
    """
    return->  str(firstday),str(lastday)
    """
    first_Day = date(year,month,1)
    if month == 12:
        next_month_first_Day = date(year+1,1,1)
    else:
        next_month_first_Day = date(year,month+1,1)
    last_day = next_month_first_Day - timedelta(days=1)
    return str(first_Day),str(last_day)

def get_month(start:str,end:str,concept="realtime-consumption"):
    """
    start,end: 'YYYY-MM-DD'
    return: all rows
    """
    s_year,s_month = int(start[:4]),int(start[5:7])
    e_year,e_month = int(end[:4]),int(end[5:7])

    allrows = list()
    year,month = s_year,s_month
    while (year,month) <= (e_year,e_month):
        month_first,month_last = get_start_end(year,month)
        data = safely_get_data(concept=concept,startDate=month_first,endDate=month_last)
        allrows.extend(data["items"])

        month+=1
        if month>12:
            month,year =1,year+1

    return allrows


####      
if __name__ == "__main__":
    dat = get_month("2026-07-01", "2026-09-01")
    print(dat[0])
    print(len(dat))