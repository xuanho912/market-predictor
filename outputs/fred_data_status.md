# FRED Data Status

Generated at: `2026-10-23T17:12:20.537451Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `BAA_SPREAD, HY_OAS, DGS3MO, DGS2, IG_OAS, DGS10, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-10-21 | 1.44 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-10-21 | 2.76 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-10-21 | 5.13 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-10-21 | 4.81 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-10-21 | 4.25 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-10-16 | -0.6328 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-10-22 | 3.4 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-10-22 | 0.89 | fred-api | False |  |
| RECESSION | USREC | True | 2026-09-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.128 | 0.0685 |
| QQQ | WEAK_EDGE | RISK_WARNING | bearish_path | bearish_path | 0.1279 | 0.063 |
| IWM | MODERATE_EDGE | RISK_WARNING | bounce_path | bearish_path | 0.1279 | 0.0685 |
| DIA | MODERATE_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.1279 | 0.0576 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
