# FRED Data Status

Generated at: `2026-09-05T15:19:40.386575Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, BAA_SPREAD, DGS3MO, DGS10, IG_OAS, DGS2, FINANCIAL_STRESS, RECESSION, DFII10`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-09-03 | 1.57 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-09-03 | 2.42 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-09-03 | 4.77 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-09-03 | 4.34 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-09-03 | 3.89 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-08-28 | -0.8526 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-09-03 | 2.65 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-09-03 | 0.81 | fred-api | False |  |
| RECESSION | USREC | True | 2026-08-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0117 | 0.004 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0118 | 0.004 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0117 | 0.0039 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0117 | 0.004 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
