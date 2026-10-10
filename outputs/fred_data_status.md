# FRED Data Status

Generated at: `2026-10-10T01:23:03.192554Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS2, DGS10, BAA_SPREAD, HY_OAS, DGS3MO, IG_OAS, FINANCIAL_STRESS, DFII10, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-10-08 | 1.48 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-10-08 | 2.87 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-10-08 | 5.22 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-10-08 | 4.75 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-10-08 | 4.23 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-10-02 | -0.4681 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-10-08 | 3.15 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-10-08 | 0.82 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.132 | 0.0419 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bearish_path | bearish_path | 0.132 | 0.0453 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.1319 | 0.0441 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.132 | 0.042 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
