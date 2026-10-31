# tr-load-forecast

**Overview & Purpose** <br>
This project uses energy consumption data from EPİAŞ to forecast day-ahead hourly electricity consumption and compare the results against the official Load Forecast Plan.

- **Data:** 01 Jan 2026 - 21 Oct 2026 <br>
**Consumption unit:** MWh

- **Current Status & Methodology** <br>
The data from EPİAŞ is reshaped into an array of shape `(days, 24)` [294 days, 24 hours/day], with predictions evaluated from day 7 to 294. Baseline predictions are generated using naive approaches that copy the consumption values from the previous day or the previous week.

- **Values calculated:** `average_daily_consumption` | `average_hourly_consumption`

| Baseline      | MAPE (%) |
|---------------|----------|
| Previous day  | 5.50     |
| Previous week | 5.56     |
| Epiaş         | 2.6974   |

*Note: There was some missing values on 12-05-2026 I had to convert those days to nan to contineu. <br>
`script.py` is only used for testing scripts (usually empty).*