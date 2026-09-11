# Flow / Positioning Proxy Status

Generated at: `2026-09-11T16:31:37.704489+00:00`
Latest date: `2026-09-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `37.25`
- overall_flow_conflict_score: `33.98`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 36.23 | 33.98 | 51.5 | 49.34 | -2.5209 | 0.4841 | 0.5194 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 36.23 | 33.98 | 51.5 | 49.34 | -2.1375 | 0.5029 | 0.4843 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 38.75 | 33.98 | 52.33 | 49.34 | -0.8342 | 0.7439 | 0.7969 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 37.79 | 33.98 | 52.02 | 49.34 | -0.9839 | 0.5589 | 0.7088 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
