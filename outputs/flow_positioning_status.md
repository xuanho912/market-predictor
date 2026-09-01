# Flow / Positioning Proxy Status

Generated at: `2026-09-01T23:34:27.401861+00:00`
Latest date: `2026-09-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.85`
- overall_flow_conflict_score: `38.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.29 | 38.01 | 53.28 | 56.36 | 0.573 | 1.2061 | 1.0365 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 44.39 | 38.01 | 53.31 | 56.36 | 0.5176 | 1.2348 | 1.0551 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 47.77 | 38.01 | 54.42 | 56.36 | 1.7962 | 1.441 | 1.3682 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 42.96 | 38.01 | 52.84 | 56.36 | 0.1639 | 1.3903 | 0.9878 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
