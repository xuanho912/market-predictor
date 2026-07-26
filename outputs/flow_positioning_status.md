# Flow / Positioning Proxy Status

Generated at: `2026-07-26T13:59:30.987234+00:00`
Latest date: `2026-07-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.57`
- overall_flow_conflict_score: `51.97`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.91 | 51.97 | 63.31 | 89.61 | -0.3492 | 0.9489 | 0.9221 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.19 | 51.97 | 64.39 | 89.61 | 0.5959 | 1.1548 | 1.1153 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.53 | 51.97 | 63.19 | 89.61 | -0.3948 | 0.8639 | 0.8875 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.66 | 51.97 | 63.23 | 89.61 | -0.3705 | 0.9324 | 0.8992 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
