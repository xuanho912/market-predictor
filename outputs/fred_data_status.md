# FRED Data Status

Generated at: `2026-07-22T14:25:10.341566Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `IG_OAS, BAA_SPREAD, DGS2, HY_OAS, DGS10, DGS3MO, DFII10, RECESSION, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-20 | 1.61 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-20 | 2.35 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-20 | 4.6 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-20 | 4.21 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-20 | 3.86 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-10 | -0.882 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-21 | 2.69 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-21 | 0.78 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0389 | 0.0112 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.039 | 0.0133 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.039 | 0.0133 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.039 | 0.0133 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
