# Flow / Positioning Proxy Status

Generated at: `2026-06-30T23:47:54.428341+00:00`
Latest date: `2026-06-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.13`
- overall_flow_conflict_score: `37.22`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.22 | 37.22 | 76.25 | 52.7 | -0.8302 | 0.8127 | 0.7932 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.84 | 37.22 | 76.12 | 52.7 | -0.7875 | 0.8092 | 0.7579 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.71 | 37.22 | 75.75 | 52.7 | -1.4078 | 0.6723 | 0.6553 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.74 | 37.22 | 75.43 | 52.7 | -2.125 | 0.5969 | 0.5174 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
