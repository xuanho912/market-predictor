# Flow / Positioning Proxy Status

Generated at: `2026-08-29T04:10:37.789262+00:00`
Latest date: `2026-08-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.31`
- overall_flow_conflict_score: `20.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 70.83 | 20.63 | 89.58 | 35.56 | -0.596 | 0.997 | 0.8102 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.71 | 20.63 | 89.54 | 35.56 | -0.5488 | 0.9671 | 0.7985 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.58 | 20.63 | 87.86 | 35.56 | -0.8342 | 0.8265 | 0.7761 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.11 | 20.63 | 89.34 | 35.56 | -0.6951 | 0.8507 | 0.7446 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
