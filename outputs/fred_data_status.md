# FRED Data Status

Generated at: `2026-11-20T20:25:34.978979Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `DGS3MO, DGS2, DGS10, BAA_SPREAD, IG_OAS, HY_OAS, FINANCIAL_STRESS, DFII10, RECESSION`
- failed series: `none`

## Series

| name | series_id | success | latest_date | latest_value | source | stale | error |
|---|---|---:|---|---:|---|---:|---|
| BAA_SPREAD | BAA10Y | True | 2026-11-18 | 1.52 | fred-api | False |  |
| DFII10 | DFII10 | True | 2026-11-18 | 2.88 | fred-api | False |  |
| DGS10 | DGS10 | True | 2026-11-18 | 5.07 | fred-api | False |  |
| DGS2 | DGS2 | True | 2026-11-18 | 4.8 | fred-api | False |  |
| DGS3MO | DGS3MO | True | 2026-11-18 | 4.34 | fred-api | False |  |
| FINANCIAL_STRESS | STLFSI4 | True | 2026-11-13 | -0.8655 | fred-api | False |  |
| HY_OAS | BAMLH0A0HYM2 | True | 2026-11-19 | 3.52 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-11-19 | 0.94 | fred-api | False |  |
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
| SPY | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0457 | 0.0151 |
| QQQ | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0458 | 0.0151 |
| IWM | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0458 | 0.0152 |
| DIA | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0457 | 0.0151 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
