# Flow / Positioning Proxy Status

Generated at: `2026-07-06T15:57:28.618051+00:00`
Latest date: `2026-07-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.41`
- overall_flow_conflict_score: `42.76`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.41 | 42.76 | 70.29 | 65.03 | -2.6468 | 0.2815 | 0.252 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.41 | 42.76 | 70.29 | 65.03 | -2.1873 | 0.3127 | 0.26 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.41 | 42.76 | 70.29 | 65.03 | -2.4404 | 0.323 | 0.2792 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.41 | 42.76 | 70.29 | 65.03 | -2.2847 | 0.4481 | 0.3299 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
