# Flow / Positioning Proxy Status

Generated at: `2026-07-27T21:35:33.961632+00:00`
Latest date: `2026-07-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.89`
- overall_flow_conflict_score: `43.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.43 | 43.94 | 64.04 | 75.75 | -0.6803 | 0.9439 | 0.8556 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.3 | 43.94 | 65.31 | 75.75 | 0.5616 | 1.2116 | 1.1086 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.43 | 43.94 | 65.68 | 75.75 | -0.5408 | 0.8999 | 0.8672 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.4 | 43.94 | 65.67 | 75.75 | -0.6139 | 0.9467 | 0.8642 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
