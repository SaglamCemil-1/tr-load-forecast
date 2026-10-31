from tr_load_forecast.epias_client import *

if __name__ == "__main__":
    #os.makedirs("data",exist_ok=True)

    consumption = get_month("2026-01-01", "2026-10-01", concept="realtime-consumption")
    save_csv(consumption, consumption_path)

    plan = get_month("2026-01-01", "2026-10-01", concept="load-estimation-plan")
    save_csv(plan, load_plan_path)