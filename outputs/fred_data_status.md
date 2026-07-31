# FRED Data Status

Generated at: `2026-07-31T06:34:46.395232Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, IG_OAS, BAA_SPREAD, DGS3MO, DGS2, DGS10, FINANCIAL_STRESS, RECESSION, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-29 | 1.6 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-29 | 2.41 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-29 | 4.67 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-29 | 4.22 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-29 | 3.83 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-24 | -0.8263 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-29 | 2.87 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-29 | 0.81 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0633 | 0.0194 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0634 | 0.0216 |
| IWM | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.0633 | 0.026 |
| DIA | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.0633 | 0.0326 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
