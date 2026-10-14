# Flow / Positioning Proxy Status

Generated at: `2026-10-14T17:14:37.240822+00:00`
Latest date: `2026-10-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `46.51`
- overall_flow_conflict_score: `35.61`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 43.92 | 35.61 | 57.71 | 55.29 | -1.5104 | 0.7845 | 0.5112 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.79 | 35.61 | 58.32 | 55.29 | -1.0025 | 0.824 | 0.7363 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 46.6 | 35.61 | 58.59 | 55.29 | -0.883 | 0.8175 | 0.8103 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.72 | 35.61 | 59.61 | 55.29 | -1.4885 | 0.6363 | 0.6497 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
