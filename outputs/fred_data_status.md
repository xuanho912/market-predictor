# FRED Data Status

Generated at: `2026-08-18T13:12:10.671942Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, IG_OAS, BAA_SPREAD, DGS2, DGS3MO, DGS10, FINANCIAL_STRESS, RECESSION, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-08-14 | 1.69 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-08-14 | 2.41 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-08-14 | 4.68 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-08-14 | 4.17 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-08-14 | 3.86 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-08-07 | -0.7709 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-08-14 | 2.67 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-08-14 | 0.8 | fred-api | False |  |
| RECESSION | USREC | True | 2026-07-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0282 | 0.0075 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0282 | 0.0097 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0282 | 0.0074 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0282 | 0.0075 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
