# Flow / Positioning Proxy Status

Generated at: `2026-10-29T02:00:27.720339+00:00`
Latest date: `2026-10-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.85`
- overall_flow_conflict_score: `59.4`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 54.02 | 59.4 | 65.52 | 92.38 | -0.7078 | 0.8334 | 0.7565 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.58 | 59.4 | 67.34 | 92.38 | -0.5182 | 0.7818 | 0.8189 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.85 | 59.4 | 67.1 | 92.38 | -0.881 | 0.9729 | 0.7524 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.94 | 59.4 | 65.82 | 92.38 | -0.7015 | 1.0478 | 0.8409 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
