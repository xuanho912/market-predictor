# FRED Data Status

Generated at: `2026-06-17T00:01:37.560216Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS3MO, HY_OAS, IG_OAS, DGS2, DGS10, BAA_SPREAD, FINANCIAL_STRESS, DFII10, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-06-15 | 1.53 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-06-15 | 2.15 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-06-15 | 4.47 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-06-15 | 4.07 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-06-15 | 3.79 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-05 | -0.8681 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-06-15 | 2.66 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-06-15 | 0.73 | fred-api | False |  |
| RECESSION | USREC | True | 2026-05-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `85`
- with current FRED status: `90`
- delta: `5`
- target 85 met: `True`
- current report score: `92.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.003 | 0.0012 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0031 | 0.0012 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0031 | 0.0012 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0031 | 0.0012 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
