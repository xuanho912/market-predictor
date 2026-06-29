# FRED Data Status

Generated at: `2026-06-29T23:38:20.963842Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, IG_OAS, DGS3MO, DGS2, BAA_SPREAD, DGS10, RECESSION, FINANCIAL_STRESS, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-06-26 | 1.56 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-06-26 | 2.18 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-06-26 | 4.38 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-06-26 | 4.07 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-06-26 | 3.83 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-19 | -0.9568 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-06-26 | 2.83 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-06-26 | 0.77 | fred-api | False |  |
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
| SPY | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0269 | 0.009 |
| QQQ | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0269 | 0.009 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0269 | 0.0091 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0269 | 0.009 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
