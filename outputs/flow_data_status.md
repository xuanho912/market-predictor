# Flow / Positioning Proxy Status

Generated at: `2026-08-20T23:14:57.259894+00:00`
Latest date: `2026-08-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.31`
- overall_flow_conflict_score: `20.59`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.68 | 20.59 | 84.71 | 35.49 | -0.0867 | 1.2239 | 0.9671 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.09 | 20.59 | 84.19 | 35.49 | -0.5484 | 0.9983 | 0.8224 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.14 | 20.59 | 85.52 | 35.49 | 0.4878 | 1.4236 | 1.1047 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.33 | 20.59 | 83.94 | 35.49 | -0.6213 | 1.0457 | 0.7531 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
