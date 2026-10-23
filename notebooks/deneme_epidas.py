import sys, os
import numpy as np
import csv

matris_365 = np.ones(7056)
aim_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "consumption.csv")
with open(aim_path,"r") as file:
    read = csv.reader(file)
    header = next(read)
    integer = 0
    for rows in read:
        matris_365[integer] = rows[2]
        integer += 1

    day_count = integer/24

new_matris_dh = matris_365.reshape((294,24))

hourly_avg = np.mean(new_matris_dh,axis=0,dtype=float)
day_avg = np.mean(new_matris_dh,axis=1, dtype=float)
day_avg_f = day_avg.reshape((42,7))
weekdays_avg = np.mean(day_avg_f,axis=0)
week_avg = np.mean(day_avg_f,axis=1)

"""
clear_hourly_avg = np.round(hourly_avg,decimals=1)
clear_day_avg = np.round(day_avg_f,decimals=1)
clear_weekdays_avg = np.round(weekdays_avg,decimals=1)
clear_week_avg = np.round(week_avg,decimals=1)
"""

#axis 1 ->
#axis 0 | (down)
print(f"day avg: \n{day_avg_f}")
print(f"hourly_avg: \n{hourly_avg}")
print(f"per days: \n\t\t{weekdays_avg}")
print(f"week_avg: \n{week_avg}")

