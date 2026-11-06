# FRED Data Status

Generated at: `2026-11-06T19:28:12.058563Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `HY_OAS, DGS10, IG_OAS, DGS2, RECESSION, DFII10, DGS3MO, FINANCIAL_STRESS, BAA_SPREAD`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-11-04 | 1.52 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-11-04 | 2.64 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-11-04 | 4.9 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-11-04 | 4.58 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-11-04 | 4.21 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-10-30 | -0.5224 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-11-05 | 3.48 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-11-05 | 0.93 | fred-api | False |  |
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
| SPY | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.1107 | 0.0567 |
| QQQ | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1106 | 0.0567 |
| IWM | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.1107 | 0.0611 |
| DIA | RISK_WARNING | RISK_WARNING | bounce_path | bearish_path | 0.1107 | 0.0567 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
