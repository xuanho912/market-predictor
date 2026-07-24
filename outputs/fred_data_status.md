# FRED Data Status

Generated at: `2026-07-24T06:15:10.587651Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS3MO, DGS10, IG_OAS, DGS2, HY_OAS, BAA_SPREAD, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-22 | 1.58 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-22 | 2.39 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-22 | 4.67 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-22 | 4.31 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-22 | 3.89 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-17 | -0.7011 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-22 | 2.68 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-22 | 0.78 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0315 | 0.0108 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0315 | 0.0108 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0315 | 0.0108 |
| DIA | MODERATE_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.0314 | 0.0152 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
