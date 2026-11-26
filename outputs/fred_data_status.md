# FRED Data Status

Generated at: `2026-11-26T04:34:24.563178Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS2, HY_OAS, IG_OAS, BAA_SPREAD, DFII10, DGS10, FINANCIAL_STRESS, RECESSION, DGS3MO`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-11-24 | 1.61 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-11-24 | 2.79 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-11-24 | 4.91 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-11-24 | 4.63 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-11-24 | 4.36 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-11-20 | -0.0697 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-11-24 | 3.72 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-11-24 | 0.98 | fred-api | False |  |
| RECESSION | USREC | True | 2026-10-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.2093 | 0.089 |
| QQQ | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.2093 | 0.089 |
| IWM | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.2093 | 0.1 |
| DIA | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.2093 | 0.089 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
