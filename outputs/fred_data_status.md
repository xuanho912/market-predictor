# FRED Data Status

Generated at: `2026-06-14T12:22:18.459673Z`

## Provider

- FRED_API_KEY present: `False`
- provider available: `False`
- fallback used: `True`
- rate limited: `False`
- successful series: `none`
- failed series: `BAA_SPREAD, DGS2, IG_OAS, HY_OAS, DGS10, DGS3MO, DFII10, FINANCIAL_STRESS, RECESSION`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | False |  |  | fred | True | no_api_key; csv_fallback_network_error |
| DFII10 | DFII10 | False |  |  | fred | True | no_api_key; csv_fallback_timeout |
| DGS10 | DGS10 | False |  |  | fred | True | no_api_key; csv_fallback_timeout |
| DGS2 | DGS2 | False |  |  | fred | True | no_api_key; csv_fallback_timeout |
| DGS3MO | DGS3MO | False |  |  | fred | True | no_api_key; csv_fallback_timeout |
| FINANCIAL_STRESS | STLFSI4 | False |  |  | fred | True | no_api_key; csv_fallback_timeout |
| HY_OAS | BAMLH0A0HYM2 | False |  |  | fred | True | no_api_key; csv_fallback_timeout |
| IG_OAS | BAMLC0A0CM | False |  |  | fred | True | no_api_key; csv_fallback_timeout |
| RECESSION | USREC | False |  |  | fred | True | no_api_key; csv_fallback_timeout |

## Data Completeness Effect

- without FRED: `85`
- with current FRED status: `85`
- delta: `0`
- target 85 met: `True`
- current report score: `85`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
