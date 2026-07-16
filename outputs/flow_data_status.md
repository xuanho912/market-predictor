# Flow / Positioning Proxy Status

Generated at: `2026-07-16T06:06:43.536008+00:00`
Latest date: `2026-07-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.84`
- overall_flow_conflict_score: `35.65`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.14 | 35.65 | 59.9 | 61.46 | -0.81 | 1.0601 | 0.7897 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.84 | 35.65 | 59.8 | 61.46 | -1.1466 | 1.0053 | 0.762 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.96 | 35.65 | 59.83 | 61.46 | -0.7823 | 0.9982 | 0.7727 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.41 | 35.65 | 59.66 | 61.46 | -0.894 | 0.982 | 0.7231 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
