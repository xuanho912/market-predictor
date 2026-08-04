# FRED Data Status

Generated at: `2026-08-04T00:16:51.494475Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS10, HY_OAS, IG_OAS, DGS2, DGS3MO, BAA_SPREAD, DFII10, FINANCIAL_STRESS, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-07-31 | 1.63 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-07-31 | 2.47 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-07-31 | 4.75 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-07-31 | 4.28 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-07-31 | 3.83 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-07-24 | -0.8263 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-07-30 | 2.84 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-07-30 | 0.8 | fred-api | False |  |
| RECESSION | USREC | True | 2026-07-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | WEAK_EDGE | WEAK_EDGE | bounce_path | bearish_path | 0.0622 | 0.0213 |
| QQQ | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0621 | 0.0213 |
| IWM | WEAK_EDGE | WEAK_EDGE | bearish_path | bearish_path | 0.0622 | 0.0268 |
| DIA | WEAK_EDGE | WEAK_EDGE | bounce_path | bounce_path | 0.0622 | 0.0213 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
