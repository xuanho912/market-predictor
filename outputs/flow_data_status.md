# Flow / Positioning Proxy Status

Generated at: `2026-08-06T06:16:19.830164+00:00`
Latest date: `2026-08-05`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.25`
- overall_flow_conflict_score: `20.2`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 68.23 | 20.2 | 76.81 | 34.82 | -0.4507 | 0.678 | 0.8968 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 67.12 | 20.2 | 76.45 | 34.82 | -0.7222 | 0.5951 | 0.796 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 67.27 | 20.2 | 76.5 | 34.82 | -0.8563 | 0.6954 | 0.8097 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 74.36 | 20.2 | 78.82 | 34.82 | 0.992 | 1.0243 | 1.342 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
