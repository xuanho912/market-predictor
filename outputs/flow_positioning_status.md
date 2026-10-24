# Flow / Positioning Proxy Status

Generated at: `2026-10-24T01:21:33.271658+00:00`
Latest date: `2026-10-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.72`
- overall_flow_conflict_score: `68.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.3 | 68.18 | 67.99 | 100.0 | 1.1246 | 1.2685 | 1.3447 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.3 | 68.18 | 67.99 | 100.0 | 2.1509 | 1.4878 | 1.8449 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.17 | 68.18 | 67.94 | 100.0 | 0.0052 | 1.0042 | 0.9983 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.11 | 68.18 | 67.27 | 100.0 | -0.8048 | 0.7595 | 0.8112 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
