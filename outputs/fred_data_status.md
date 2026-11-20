# FRED Data Status

Generated at: `2026-11-20T03:58:26.558869Z`

## Provider

- FRED_API_KEY present: `True`
- provider available: `True`
- fallback used: `False`
- rate limited: `False`
- successful series: `IG_OAS, HY_OAS, DGS3MO, DGS10, BAA_SPREAD, DGS2, RECESSION, FINANCIAL_STRESS, DFII10`
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
| HY_OAS | BAMLH0A0HYM2 | True | 2026-11-18 | 3.47 | fred-api | False |  |
| IG_OAS | BAMLC0A0CM | True | 2026-11-18 | 0.93 | fred-api | False |  |
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
| SPY | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0561 | 0.0184 |
| QQQ | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0561 | 0.0184 |
| IWM | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0561 | 0.024 |
| DIA | RISK_WARNING | RISK_WARNING | bearish_path | bearish_path | 0.0562 | 0.0185 |

## Warning

If FRED uses local-cache-fred, stale_data remains true. Stale data must not be treated as fresh real-time confirmation.
