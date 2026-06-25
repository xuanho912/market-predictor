# FRED Data Status

Generated at: `2026-06-25T23:56:32.069757Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `BAA_SPREAD, DGS3MO, HY_OAS, IG_OAS, DGS2, DGS10, RECESSION, DFII10, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-06-24 | 1.52 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-06-24 | 2.23 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-06-24 | 4.41 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-06-24 | 4.11 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-06-24 | 3.85 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-06-19 | -0.9568 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-06-24 | 2.76 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-06-24 | 0.75 | fred-api | False |  |
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
| SPY | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0184 | 0.0063 |
| QQQ | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0185 | 0.0064 |
| IWM | STRONG_EDGE | STRONG_EDGE | bounce_path | bounce_path | 0.0184 | 0.0063 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0184 | 0.0063 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
