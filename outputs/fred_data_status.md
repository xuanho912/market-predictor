# FRED Data Status

Generated at: `2026-10-22T17:14:17.947115Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS3MO, DGS2, DGS10, HY_OAS, IG_OAS, BAA_SPREAD, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-10-20 | 1.44 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-10-20 | 2.77 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-10-20 | 5.12 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-10-20 | 4.79 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-10-20 | 4.26 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-10-16 | -0.6328 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-10-21 | 3.27 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-10-21 | 0.88 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | RISK_WARNING | bearish_path | bearish_path | 0.1235 | 0.066 |
| QQQ | WEAK_EDGE | NO_EDGE | bearish_path | bearish_path | 0.1235 | 0.0605 |
| IWM | MODERATE_EDGE | RISK_WARNING | bearish_path | bearish_path | 0.1235 | 0.066 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.1235 | 0.0495 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
