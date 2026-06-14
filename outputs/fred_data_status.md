# FRED Data Status

Generated at: `2026-06-14T08:30:49.494131Z`

## Provider

- FRED_API_KEY present: `False`
- provider available: `False`
- fallback used: `True`
- rate limited: `False`
- successful series: `none`
- failed series: `DGS10, IG_OAS, DGS2, BAA_SPREAD, HY_OAS, DGS3MO, RECESSION, FINANCIAL_STRESS, DFII10`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | False |  |  | fred | True | no_api_key_and_csv_failed |
| DFII10 | DFII10 | False |  |  | fred | True | no_api_key_and_csv_failed |
| DGS10 | DGS10 | False |  |  | fred | True | no_api_key_and_csv_failed |
| DGS2 | DGS2 | False |  |  | fred | True | no_api_key_and_csv_failed |
| DGS3MO | DGS3MO | False |  |  | fred | True | no_api_key_and_csv_failed |
| FINANCIAL_STRESS | STLFSI4 | False |  |  | fred | True | no_api_key_and_csv_failed |
| HY_OAS | BAMLH0A0HYM2 | False |  |  | fred | True | no_api_key_and_csv_failed |
| IG_OAS | BAMLC0A0CM | False |  |  | fred | True | no_api_key_and_csv_failed |
| RECESSION | USREC | False |  |  | fred | True | no_api_key_and_csv_failed |

## Data Completeness Effect

- without FRED: `80`
- with current FRED status: `80`
- delta: `0`
- target 85 met: `False`
- current report score: `80`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
