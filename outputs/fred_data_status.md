# FRED Data Status

Generated at: `2026-07-07T05:10:56.790433Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS3MO, DGS10, HY_OAS, IG_OAS, BAA_SPREAD, DGS2, FINANCIAL_STRESS, DFII10, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-01 | 1.54 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-02 | 2.26 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-02 | 4.49 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-02 | 4.14 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-02 | 3.82 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-26 | -0.6445 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-03 | 2.74 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-03 | 0.75 | fred-api | False |  |
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
| SPY | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0128 | 0.0045 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.0128 | 0.0046 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0128 | 0.0046 |
| DIA | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0128 | 0.0046 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
