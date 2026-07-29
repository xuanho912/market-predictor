# FRED Data Status

Generated at: `2026-07-29T14:34:06.550377Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `IG_OAS, BAA_SPREAD, DGS2, HY_OAS, DGS10, DGS3MO, FINANCIAL_STRESS, DFII10, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-27 | 1.61 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-27 | 2.44 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-27 | 4.65 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-27 | 4.31 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-27 | 3.96 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-17 | -0.7011 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-28 | 2.84 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-28 | 0.81 | fred-api | False |  |
| RECESSION | USREC | True | 2026-06-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0606 | 0.0209 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0606 | 0.0209 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0606 | 0.0264 |
| DIA | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0606 | 0.0209 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
