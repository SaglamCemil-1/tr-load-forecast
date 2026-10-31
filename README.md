# tr-load-forecast

**Overview & Purpose** <br>
This project uses energy consumption data from EPİAŞ to forecast day-ahead hourly electricity consumption and compare the results against the official Load Forecast Plan.

- **Data:** 01 Jan 2026 - 31 Oct 2026 <br>
**Consumption unit:** MWh

- **Current Status & Methodology** <br>
The data from EPİAŞ is reshaped into an array of shape `(days, 24)` [294 days, 24 hours/day], with predictions evaluated from day 1 to 303. Baseline predictions are generated using naive approaches that copy the consumption values from the previous day or the previous week.

- **Values calculated:** `` | ``

| Baseline      | MAPE (%) |
|---------------|----------|
| Previous day  | 5.5176   |
| Previous week | 5.5223   |
| Epiaş         | 2.6904   |

*Note: There were some missing values on 12-MAY-2026 I had to convert those days to nan to continue (the was no data from 12 MAY so I added Nan values there).*