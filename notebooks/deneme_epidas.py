import numpy as np
from src.tr_load_forecast.epias_client import *

aim_path = consumption_path #os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "consumption.csv")
aim_path_2 = load_plan_path #os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "load_plan.csv")

def read_csv(path,consumption_col,date_col)->list:
    """ path: file path .csv
    col: consumption column """
    with open(path,"r") as file:
        read = csv.reader(file)
        header = next(read)
        values = list()
        dates = list()
        for rows in read:
            values.append(float(rows[consumption_col]))
            dates.append(rows[date_col])
        return [values,dates]

def align_rows(array_1,array_2):
    minimum_Val = min(len(array_1),len(array_2))
    minimum_Val -= minimum_Val%24
    return [array_1[:minimum_Val],array_2[:minimum_Val]]

def calculate_mape(array_1, array_2)->list:
    """ array_1: real data
        array_2: forecast
        return list: [dayly Mape,hourly Mape, ape Mean] """
    if len(array_1) == len(array_2):
        day = len(array_1)//24
    else:
        raise ValueError ("array lenghts are not same")
    ape = abs(((array_1-array_2)/array_1) * 100)
    ape_mean = np.nanmean(ape)
    dayly_mean = np.nanmean(ape.reshape(day,24),axis=1)
    hourly_mean = np.nanmean(ape.reshape(day,24),axis=0)

    return [dayly_mean,hourly_mean,ape_mean]


consumption_list = read_csv(aim_path,2,0)
estimation_plan = read_csv(aim_path_2,2,0)
#
mismatched_indicies = None
for t in range(len(consumption_list[1])):
    if consumption_list[1][t] != estimation_plan[1][t]:
        mismatched_indicies = t
        break
#
consumption= np.array(consumption_list[0])
estimation = np.array(estimation_plan[0])
if mismatched_indicies is not None:
    estimation = np.insert(estimation,mismatched_indicies,np.full(24,np.nan))
consumption,estimation = align_rows(consumption,estimation)

day_count = len(consumption) // 24
week_count = day_count // 7
new_matris_dh = consumption.reshape((day_count,24))
hourly_avg = np.mean(new_matris_dh,axis=0)
day_avg = np.mean(new_matris_dh,axis=1)
day_avg_f = day_avg[:week_count*7].reshape((week_count,7))
weekdays_avg = np.mean(day_avg_f,axis=0)
week_avg = np.mean(day_avg_f,axis=1)

print(f"day avg: \n{day_avg_f}")
print(f"hourly_avg: \n{hourly_avg}")
print(f"per days: \n\t\t{weekdays_avg}")
print(f"week_avg: \n{week_avg}")

real_day,forecast = consumption[168:],consumption[144:-24]
print(f"yesterday-today err:{calculate_mape(real_day,forecast)[2]:.4f}")

real_day,forecast = consumption[168:],consumption[:-168]
print(f"previous-this week err:{calculate_mape(real_day,forecast)[2]:.4f}")

real_day,forecast = consumption[168:],estimation[168:]
print(f"epiaş err:{calculate_mape(real_day,forecast)[2]:.4f}")
