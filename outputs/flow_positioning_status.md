# Flow / Positioning Proxy Status

Generated at: `2026-09-29T06:59:00.270463+00:00`
Latest date: `2026-09-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.87`
- overall_flow_conflict_score: `38.22`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.67 | 38.22 | 84.67 | 53.82 | -0.1996 | 0.9575 | 0.9668 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.04 | 38.22 | 86.43 | 53.82 | 1.2501 | 1.1631 | 1.2581 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.87 | 38.22 | 85.39 | 53.82 | 0.4271 | 1.0478 | 1.0912 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.91 | 38.22 | 83.76 | 53.82 | -1.0324 | 0.7526 | 0.7147 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
