# Flow / Positioning Proxy Status

Generated at: `2026-07-14T21:29:53.447144+00:00`
Latest date: `2026-07-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `45.49`
- overall_flow_conflict_score: `29.24`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 47.21 | 29.24 | 55.87 | 47.44 | -1.5871 | 0.799 | 0.6079 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 47.5 | 29.24 | 55.97 | 47.44 | -1.8167 | 0.7949 | 0.635 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 43.62 | 29.24 | 54.7 | 47.44 | -0.9167 | 0.9713 | 0.7257 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 43.62 | 29.24 | 54.7 | 47.44 | -0.8253 | 0.988 | 0.7257 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
