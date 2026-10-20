# FRED Data Status

Generated at: `2026-10-20T01:31:01.313549Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `IG_OAS, DGS3MO, DGS10, HY_OAS, BAA_SPREAD, DGS2, DFII10, FINANCIAL_STRESS, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-10-16 | 1.46 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-10-16 | 2.74 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-10-16 | 5.09 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-10-16 | 4.74 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-10-16 | 4.26 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-10-09 | -0.7206 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-10-16 | 3.31 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-10-16 | 0.85 | fred-api | False |  |
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
| SPY | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.1258 | 0.0623 |
| QQQ | WEAK_EDGE | RISK_WARNING | bearish_path | bearish_path | 0.1258 | 0.0623 |
| IWM | WEAK_EDGE | RISK_WARNING | bearish_path | bearish_path | 0.1258 | 0.0623 |
| DIA | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.1258 | 0.0623 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
