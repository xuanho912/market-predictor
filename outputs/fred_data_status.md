# FRED Data Status

Generated at: `2026-08-13T03:35:48.368428Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `BAA_SPREAD, HY_OAS, IG_OAS, DGS10, DGS2, DGS3MO, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-08-10 | 1.62 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-08-11 | 2.43 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-08-11 | 4.7 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-08-11 | 4.22 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-08-11 | 3.89 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-08-07 | -0.7709 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-08-11 | 2.72 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-08-11 | 0.79 | fred-api | False |  |
| RECESSION | USREC | True | 2026-07-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0199 | 0.0047 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0199 | 0.0048 |
| IWM | MODERATE_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.02 | 0.0048 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.02 | 0.0047 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
