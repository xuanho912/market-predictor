# FRED Data Status

Generated at: `2026-11-10T19:47:16.645869Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `BAA_SPREAD, DGS3MO, DGS10, HY_OAS, IG_OAS, DGS2, DFII10, FINANCIAL_STRESS, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-11-06 | 1.56 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-11-06 | 2.63 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-11-06 | 4.86 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-11-06 | 4.51 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-11-06 | 4.19 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-10-30 | -0.5224 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-11-09 | 3.34 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-11-09 | 0.91 | fred-api | False |  |
| RECESSION | USREC | True | 2026-10-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | RISK_WARNING | bounce_path | bearish_path | 0.0925 | 0.041 |
| QQQ | WEAK_EDGE | RISK_WARNING | bearish_path | bearish_path | 0.0925 | 0.0508 |
| IWM | MODERATE_EDGE | RISK_WARNING | bounce_path | bounce_path | 0.0925 | 0.0277 |
| DIA | MODERATE_EDGE | RISK_WARNING | bearish_path | bearish_path | 0.0925 | 0.042 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
