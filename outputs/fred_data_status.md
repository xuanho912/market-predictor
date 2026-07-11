# FRED Data Status

Generated at: `2026-07-11T04:32:50.864609Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, IG_OAS, DGS10, DGS2, DGS3MO, BAA_SPREAD, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-09 | 1.56 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-09 | 2.31 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-09 | 4.54 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-09 | 4.16 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-09 | 3.83 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-03 | -0.7246 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-09 | 2.7 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-09 | 0.76 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0137 | 0.0025 |
| QQQ | WEAK_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0138 | 0.0049 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0139 | 0.0025 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0138 | 0.0026 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
