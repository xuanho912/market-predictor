# Flow / Positioning Proxy Status

Generated at: `2026-09-30T10:02:24.551266+00:00`
Latest date: `2026-09-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.33`
- overall_flow_conflict_score: `38.27`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.38 | 38.27 | 85.18 | 54.22 | -0.8149 | 0.8643 | 0.8362 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.02 | 38.27 | 85.06 | 54.22 | -0.948 | 0.7721 | 0.8028 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.39 | 38.27 | 85.51 | 54.22 | -0.4069 | 0.8592 | 0.9278 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.51 | 38.27 | 84.89 | 54.22 | -0.9942 | 0.827 | 0.7564 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
