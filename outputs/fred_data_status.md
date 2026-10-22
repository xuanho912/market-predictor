# FRED Data Status

Generated at: `2026-10-22T01:22:30.256274Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `False`
- fallback used: `False`
- rate limited: `False`
- successful series: `none`
- failed series: `IG_OAS, HY_OAS, DGS2, DGS10, DGS3MO, BAA_SPREAD, DFII10, RECESSION, FINANCIAL_STRESS`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | False |  |  | fred | True | timeout |
| DFII10 | DFII10 | False |  |  | fred | True | timeout |
| DGS10 | DGS10 | False |  |  | fred | True | timeout |
| DGS2 | DGS2 | False |  |  | fred | True | timeout |
| DGS3MO | DGS3MO | False |  |  | fred | True | timeout |
| FINANCIAL_STRESS | STLFSI4 | False |  |  | fred | True | timeout |
| HY_OAS | BAMLH0A0HYM2 | False |  |  | fred | True | timeout |
| IG_OAS | BAMLC0A0CM | False |  |  | fred | True | timeout |
| RECESSION | USREC | False |  |  | fred | True | timeout |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `79`
- delta: `0`
- target 85 met: `False`
- current report score: `81.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0 | 0.0 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0 | 0.0 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0 | 0.0 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
