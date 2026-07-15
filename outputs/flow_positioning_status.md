# Flow / Positioning Proxy Status

Generated at: `2026-07-15T22:35:44.488265+00:00`
Latest date: `2026-07-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.27`
- overall_flow_conflict_score: `35.65`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.75 | 35.65 | 59.44 | 61.46 | -1.2754 | 0.8894 | 0.6625 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.32 | 35.65 | 59.63 | 61.46 | -1.3572 | 0.9432 | 0.7149 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.93 | 35.65 | 59.83 | 61.46 | -0.7895 | 0.9954 | 0.7706 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.08 | 35.65 | 59.55 | 61.46 | -0.9911 | 0.9407 | 0.6927 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
