# Flow / Positioning Proxy Status

Generated at: `2026-09-23T17:02:54.449225+00:00`
Latest date: `2026-09-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.6`
- overall_flow_conflict_score: `36.31`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.88 | 36.31 | 88.51 | 53.36 | -2.1223 | 0.3244 | 0.4247 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.88 | 36.31 | 88.51 | 53.36 | -1.7685 | 0.4561 | 0.5545 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.25 | 36.31 | 86.99 | 53.36 | -1.4843 | 0.4813 | 0.5897 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.38 | 36.31 | 87.03 | 53.36 | -1.1626 | 0.5281 | 0.6014 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
