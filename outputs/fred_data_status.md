# FRED Data Status

Generated at: `2026-09-18T16:27:50.738944Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS3MO, DGS2, IG_OAS, DGS10, HY_OAS, BAA_SPREAD, RECESSION, FINANCIAL_STRESS, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-09-16 | 1.43 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-09-16 | 2.68 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-09-16 | 5.01 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-09-16 | 4.74 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-09-16 | 4.14 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-09-11 | -0.8477 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-09-17 | 2.7 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-09-17 | 0.78 | fred-api | False |  |
| RECESSION | USREC | True | 2026-08-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0316 | 0.0117 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0316 | 0.0116 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0315 | 0.0116 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0315 | 0.0116 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
