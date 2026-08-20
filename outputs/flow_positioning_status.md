# Flow / Positioning Proxy Status

Generated at: `2026-08-20T23:36:37.381446+00:00`
Latest date: `2026-08-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.75`
- overall_flow_conflict_score: `20.59`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 76.12 | 20.59 | 94.57 | 35.49 | -0.0867 | 1.2239 | 0.9671 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 74.53 | 20.59 | 94.05 | 35.49 | -0.5484 | 0.9983 | 0.8224 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 78.58 | 20.59 | 95.38 | 35.49 | 0.4878 | 1.4236 | 1.1047 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.77 | 20.59 | 93.8 | 35.49 | -0.6213 | 1.0457 | 0.7531 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
