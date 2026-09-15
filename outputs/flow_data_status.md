# Flow / Positioning Proxy Status

Generated at: `2026-09-15T01:02:03.001083+00:00`
Latest date: `2026-09-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `43.04`
- overall_flow_conflict_score: `41.2`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 45.39 | 41.2 | 52.41 | 63.87 | 1.4024 | 1.1491 | 1.2331 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 38.86 | 41.2 | 50.27 | 63.87 | -0.649 | 0.8935 | 0.8611 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 45.39 | 41.2 | 52.41 | 63.87 | 1.7978 | 1.4 | 1.5006 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 42.51 | 41.2 | 51.47 | 63.87 | 0.3625 | 0.89 | 1.1287 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
