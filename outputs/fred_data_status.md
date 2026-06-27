# FRED Data Status

Generated at: `2026-06-27T05:06:19.436336Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, IG_OAS, BAA_SPREAD, DGS10, DGS2, DGS3MO, DFII10, FINANCIAL_STRESS, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-06-25 | 1.54 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-06-25 | 2.19 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-06-25 | 4.4 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-06-25 | 4.09 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-06-25 | 3.84 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-19 | -0.9568 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-06-25 | 2.78 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-06-25 | 0.76 | fred-api | False |  |
| RECESSION | USREC | True | 2026-05-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `78`
- with current FRED status: `90`
- delta: `12`
- target 85 met: `True`
- current report score: `92.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0218 | 0.0073 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.0217 | 0.0072 |
| IWM | MODERATE_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0218 | 0.0051 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0217 | 0.0073 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
