# FRED Data Status

Generated at: `2026-10-03T01:35:21.031750Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, DGS3MO, DGS2, DGS10, IG_OAS, BAA_SPREAD, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-10-01 | 1.49 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-10-01 | 2.88 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-10-01 | 5.24 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-10-01 | 4.78 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-10-01 | 4.17 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-09-25 | -0.8074 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-10-01 | 3.24 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-10-01 | 0.86 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1384 | 0.0469 |
| QQQ | MODERATE_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.1384 | 0.0524 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.1384 | 0.0469 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.1384 | 0.058 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
