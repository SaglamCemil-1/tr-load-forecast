import os
import numpy as np
import csv

from unicodedata import decimal

aim_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "consumption.csv")
with open(aim_path,"r") as file:
    read = csv.reader(file)
    header = next(read)
    for i,rows in enumerate(read):
        pass
    i += 1
    if i%(24*7) != 0:
        i -= i%(24*7)
    day_count = i // 24
    week_count = day_count // 7

matris_365 = np.ones(i)
with open(aim_path, "r") as file:
    read = csv.reader(file)
    header = next(read)
    integer = 0
    for rows in read:
        if integer == i:
            break
        matris_365[integer] = rows[2]
        integer += 1

days = i//24
"""
matris_365_forecast_realdays = matris_365[168:]
matris_365_forecast_daylater = matris_365[144:-24]

#print("\n",matris_365_forecast_realdays)
#print("\n",matris_365_forecast_daylater)
ape_day = abs(((matris_365_forecast_realdays - matris_365_forecast_daylater) / matris_365_forecast_realdays) * 100)
print(f"mape: {np.mean(ape_day):.4f}")
day_later_forecast = ape_day.reshape(days-7,24)
day_later_forecast_houravg = np.mean(day_later_forecast, axis=0) #avg of every hour (01-02,02-03 ..)
day_later_forecast_dayavg = np.mean(day_later_forecast, axis=1) #avg of 1day (first day - second day)

print("d:",day_later_forecast_dayavg,max(day_later_forecast_dayavg),min(day_later_forecast_dayavg),sep="\n")
print("c:",day_later_forecast_houravg,max(day_later_forecast_houravg),min(day_later_forecast_houravg),sep="\n")
"""