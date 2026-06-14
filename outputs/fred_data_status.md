# FRED Data Status

Generated at: `2026-06-14T18:36:30.084492Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `IG_OAS, HY_OAS, DGS10, DGS3MO, BAA_SPREAD, DGS2, DFII10, FINANCIAL_STRESS, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-06-11 | 1.55 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-06-11 | 2.16 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-06-11 | 4.45 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-06-11 | 4.05 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-06-11 | 3.78 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-05 | -0.8681 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-06-11 | 2.78 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-06-11 | 0.75 | fred-api | False |  |
| RECESSION | USREC | True | 2026-05-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `85`
- with current FRED status: `90`
- delta: `5`
- target 85 met: `True`
- current report score: `90`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0105 | 0.0039 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0106 | 0.0039 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0105 | 0.0038 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0105 | 0.0038 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
