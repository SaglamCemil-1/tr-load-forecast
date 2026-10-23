import sys, os
import numpy as np
from tr_load_forecast.epias_client import *

# sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

consumption = get_data(
    concept="realtime-consumption",
    startDate="2026-09-15",
    endDate="2026-09-15",
).json()
#print(consumption["items"])

load_plan = get_data(
    concept="load-estimation-plan",
    startDate="2026-09-15",
    endDate="2026-09-15",
).json()
#print(load_plan["page"])
visualize_month = get_month("2026-08-17", "2026-09-17", concept="realtime-consumption",bytime="22:00")
for hour in visualize_month:
    print(f"DATE: {hour["date"][:10]},Consumption: {hour["consumption"]} ")