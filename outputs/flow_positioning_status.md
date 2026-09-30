# Flow / Positioning Proxy Status

Generated at: `2026-09-30T18:03:54.242083+00:00`
Latest date: `2026-09-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.25`
- overall_flow_conflict_score: `35.57`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.01 | 35.57 | 94.47 | 51.36 | -2.4477 | 0.3948 | 0.3865 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.89 | 35.57 | 96.07 | 51.36 | -2.2399 | 0.4593 | 0.4449 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.11 | 35.57 | 94.5 | 51.36 | -1.9945 | 0.5519 | 0.575 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.01 | 35.57 | 94.47 | 51.36 | -2.1591 | 0.3971 | 0.3404 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
