# FRED Data Status

Generated at: `2026-07-02T05:12:24.861031Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, DGS3MO, DGS10, IG_OAS, BAA_SPREAD, DGS2, DFII10, RECESSION, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-06-30 | 1.53 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-06-30 | 2.2 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-06-30 | 4.44 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-06-30 | 4.14 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-06-30 | 3.87 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-26 | -0.6445 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-06-30 | 2.75 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-06-30 | 0.76 | fred-api | False |  |
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
| SPY | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0193 | 0.0066 |
| QQQ | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0193 | 0.0066 |
| IWM | MODERATE_EDGE | MODERATE_EDGE | bounce_path | bounce_path | 0.0193 | 0.0066 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0194 | 0.0066 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
