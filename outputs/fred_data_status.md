# FRED Data Status

Generated at: `2026-07-08T14:43:54.053076Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `BAA_SPREAD, DGS3MO, HY_OAS, DGS10, IG_OAS, DGS2, FINANCIAL_STRESS, RECESSION, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-02 | 1.54 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-06 | 2.24 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-06 | 4.48 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-06 | 4.13 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-06 | 3.87 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-26 | -0.6445 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-07 | 2.67 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-07 | 0.76 | fred-api | False |  |
| RECESSION | USREC | True | 2026-06-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `85`
- with current FRED status: `90`
- delta: `5`
- target 85 met: `True`
- current report score: `92.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0121 | 0.0043 |
| QQQ | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.012 | 0.0043 |
| IWM | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.012 | 0.0043 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.012 | 0.0043 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
