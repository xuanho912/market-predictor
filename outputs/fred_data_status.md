# FRED Data Status

Generated at: `2026-07-15T00:04:40.055537Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `IG_OAS, BAA_SPREAD, DGS3MO, HY_OAS, DGS10, DGS2, FINANCIAL_STRESS, DFII10, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-13 | 1.56 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-13 | 2.36 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-13 | 4.62 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-13 | 4.26 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-13 | 3.89 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-03 | -0.7246 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-13 | 2.69 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-13 | 0.78 | fred-api | False |  |
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
| SPY | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.039 | 0.0179 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.039 | 0.0135 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.039 | 0.0114 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.039 | 0.018 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
