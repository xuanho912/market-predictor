# FRED Data Status

Generated at: `2026-06-24T23:47:29.565343Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS10, IG_OAS, BAA_SPREAD, DGS3MO, HY_OAS, DGS2, RECESSION, FINANCIAL_STRESS, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-06-23 | 1.51 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-06-23 | 2.29 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-06-23 | 4.5 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-06-23 | 4.16 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-06-23 | 3.85 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-19 | -0.9568 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-06-23 | 2.71 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-06-23 | 0.74 | fred-api | False |  |
| RECESSION | USREC | True | 2026-05-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `85`
- with current FRED status: `90`
- delta: `5`
- target 85 met: `True`
- current report score: `92.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0081 | 0.0029 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.008 | 0.003 |
| IWM | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0081 | 0.003 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.008 | 0.0029 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
