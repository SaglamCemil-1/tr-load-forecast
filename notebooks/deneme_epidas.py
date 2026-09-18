import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))
from tr_load_forecast.epias_client import get_data

consumption = get_data(
    concept="realtime-consumption",
    startDate="2026-09-15",
    endDate="2026-09-15",
).json()
print(consumption["items"][0])

load_plan = get_data(
    concept="load-estimation-plan",
    startDate="2026-09-15",
    endDate="2026-09-15",
).json()
print(load_plan["items"][0])