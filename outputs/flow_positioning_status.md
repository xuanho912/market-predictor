# Flow / Positioning Proxy Status

Generated at: `2026-11-03T19:31:34.015686+00:00`
Latest date: `2026-11-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.72`
- overall_flow_conflict_score: `70.32`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.42 | 70.32 | 78.46 | 100.0 | -1.3341 | 0.411 | 0.4732 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.42 | 70.32 | 78.46 | 100.0 | -1.0764 | 0.4678 | 0.5512 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.3 | 70.32 | 80.06 | 100.0 | -1.8181 | 0.4936 | 0.4399 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.75 | 70.32 | 78.57 | 100.0 | -1.5406 | 0.5942 | 0.5967 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
