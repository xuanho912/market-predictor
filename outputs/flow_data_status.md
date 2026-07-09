# Flow / Positioning Proxy Status

Generated at: `2026-07-09T15:37:07.862397+00:00`
Latest date: `2026-07-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.82`
- overall_flow_conflict_score: `23.37`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.26 | 23.37 | 70.74 | 36.58 | -2.7712 | 0.2839 | 0.2226 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 50.38 | 23.37 | 69.14 | 36.58 | -2.7324 | 0.3829 | 0.304 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.38 | 23.37 | 69.14 | 36.58 | -2.2916 | 0.3608 | 0.2577 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.26 | 23.37 | 70.74 | 36.58 | -2.4365 | 0.2369 | 0.1683 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
