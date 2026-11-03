# FRED Data Status

Generated at: `2026-11-03T03:46:49.811416Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS3MO, HY_OAS, BAA_SPREAD, DGS10, IG_OAS, DGS2, DFII10, RECESSION, FINANCIAL_STRESS`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-10-30 | 1.53 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-10-30 | 2.6 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-10-30 | 4.94 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-10-30 | 4.56 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-10-30 | 4.16 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-10-23 | -0.5837 | fred-api | True |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-10-30 | 3.44 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-10-30 | 0.94 | fred-api | False |  |
| RECESSION | USREC | True | 2026-10-01 | 0.0 | fred-api | True |  |

## Data Completeness Effect

- without FRED: `79`
- with current FRED status: `85`
- delta: `6`
- target 85 met: `True`
- current report score: `87.0`

## Risk Expansion / Failed Bounce Effect

| symbol | edge without | edge with | primary without | primary with | risk expansion delta | failed bounce delta |
|---|---|---|---|---|---:|---:|
| SPY | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.1089 | 0.0561 |
| QQQ | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1089 | 0.0561 |
| IWM | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1089 | 0.0671 |
| DIA | RISK_WARNING | RISK_WARNING | bounce_path | bounce_path | 0.1089 | 0.0463 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
