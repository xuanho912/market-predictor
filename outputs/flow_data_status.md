# Flow / Positioning Proxy Status

Generated at: `2026-08-07T13:42:24.977453+00:00`
Latest date: `2026-08-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.67`
- overall_flow_conflict_score: `21.39`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.67 | 21.39 | 65.85 | 36.87 | -2.8846 | 0.0635 | 0.0703 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.67 | 21.39 | 65.85 | 36.87 | -2.6337 | 0.0844 | 0.0899 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.67 | 21.39 | 65.85 | 36.87 | -3.0619 | 0.1109 | 0.1091 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.67 | 21.39 | 65.85 | 36.87 | -2.394 | 0.0632 | 0.075 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
