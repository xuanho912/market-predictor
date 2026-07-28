# Flow / Positioning Proxy Status

Generated at: `2026-07-28T04:32:43.442390+00:00`
Latest date: `2026-07-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.2`
- overall_flow_conflict_score: `43.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.49 | 43.94 | 64.06 | 75.75 | -0.6463 | 0.9505 | 0.8617 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.5 | 43.94 | 65.38 | 75.75 | 0.6061 | 1.2218 | 1.1184 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.67 | 43.94 | 65.76 | 75.75 | -0.4148 | 0.9217 | 0.8883 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.12 | 43.94 | 65.91 | 75.75 | -0.3126 | 1.0183 | 0.9297 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
