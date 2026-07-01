# Flow / Positioning Proxy Status

Generated at: `2026-07-01T05:56:21.410622+00:00`
Latest date: `2026-06-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.97`
- overall_flow_conflict_score: `37.22`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.2 | 37.22 | 76.57 | 52.7 | -0.5051 | 0.9037 | 0.8821 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.22 | 37.22 | 76.25 | 52.7 | -0.6839 | 0.8469 | 0.7932 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.9 | 37.22 | 76.14 | 52.7 | -1.0062 | 0.7836 | 0.7638 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.56 | 37.22 | 75.7 | 52.7 | -1.6821 | 0.7398 | 0.6413 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
