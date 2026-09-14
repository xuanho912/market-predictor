# Flow / Positioning Proxy Status

Generated at: `2026-09-14T23:16:51.952491+00:00`
Latest date: `2026-09-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `42.8`
- overall_flow_conflict_score: `41.2`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.08 | 41.2 | 51.99 | 63.87 | 0.9663 | 1.0895 | 1.1651 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 42.92 | 41.2 | 51.6 | 63.87 | 0.5662 | 1.1856 | 1.1299 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 45.39 | 41.2 | 52.41 | 63.87 | 1.4868 | 1.2409 | 1.4202 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 38.79 | 41.2 | 50.25 | 63.87 | -0.5591 | 0.7419 | 0.8544 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
