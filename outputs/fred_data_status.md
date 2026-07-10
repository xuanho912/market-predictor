# FRED Data Status

Generated at: `2026-07-10T05:12:12.883563Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, DGS10, IG_OAS, BAA_SPREAD, DGS2, RECESSION, DGS3MO, FINANCIAL_STRESS, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-08 | 1.56 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-08 | 2.31 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-08 | 4.56 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-08 | 4.21 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-08 | 3.87 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-03 | -0.7246 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-08 | 2.7 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-08 | 0.76 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.014 | 0.0026 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0139 | 0.0026 |
| IWM | MODERATE_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.014 | 0.0027 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.014 | 0.0027 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
