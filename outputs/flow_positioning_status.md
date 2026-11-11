# Flow / Positioning Proxy Status

Generated at: `2026-11-11T19:38:36.514384+00:00`
Latest date: `2026-11-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.72`
- overall_flow_conflict_score: `60.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.39 | 60.18 | 82.7 | 90.8 | -1.1632 | 0.3128 | 0.4285 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.69 | 60.18 | 84.43 | 90.8 | -0.7931 | 0.4361 | 0.6043 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.39 | 60.18 | 82.7 | 90.8 | -1.5328 | 0.3473 | 0.436 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.39 | 60.18 | 82.7 | 90.8 | -0.9631 | 0.3195 | 0.4702 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
