# FRED Data Status

Generated at: `2026-07-30T04:26:17.321708Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, IG_OAS, DGS10, BAA_SPREAD, DGS3MO, DGS2, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-28 | 1.62 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-28 | 2.41 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-28 | 4.61 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-28 | 4.26 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-28 | 3.9 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-24 | -0.8263 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-28 | 2.84 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-28 | 0.81 | fred-api | False |  |
| RECESSION | USREC | True | 2026-06-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0606 | 0.0208 |
| QQQ | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0606 | 0.0208 |
| IWM | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0606 | 0.0252 |
| DIA | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0605 | 0.0208 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
