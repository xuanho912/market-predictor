# FRED Data Status

Generated at: `2026-07-03T05:01:52.277487Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `IG_OAS, DGS2, HY_OAS, BAA_SPREAD, DGS3MO, DGS10, FINANCIAL_STRESS, DFII10, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-01 | 1.54 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-01 | 2.25 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-01 | 4.48 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-01 | 4.17 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-01 | 3.85 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-26 | -0.6445 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-01 | 2.74 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-01 | 0.76 | fred-api | False |  |
| RECESSION | USREC | True | 2026-06-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `85`
- with current FRED status: `90`
- delta: `5`
- target 85 met: `True`
- current report score: `92.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0182 | 0.0064 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0182 | 0.0065 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0182 | 0.0064 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0182 | 0.0064 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
