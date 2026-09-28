# Flow / Positioning Proxy Status

Generated at: `2026-09-28T19:43:05.445483+00:00`
Latest date: `2026-09-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.19`
- overall_flow_conflict_score: `37.96`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.36 | 37.96 | 83.14 | 53.44 | -1.372 | 0.7006 | 0.7073 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.75 | 37.96 | 84.25 | 53.44 | 0.0473 | 0.9319 | 1.0079 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.65 | 37.96 | 83.56 | 53.44 | -0.9347 | 0.792 | 0.8248 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 53.98 | 37.96 | 82.69 | 53.44 | -1.4499 | 0.6129 | 0.582 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
