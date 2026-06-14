# Flow / Positioning Proxy Status

Generated at: `2026-06-14T16:02:49.989242+00:00`
Latest date: `2026-06-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `73.6`
- overall_flow_conflict_score: `23.71`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.94 | 23.71 | 90.32 | 36.26 | 0.1662 | 0.7538 | 1.0616 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 72.09 | 23.71 | 90.37 | 36.26 | 0.148 | 0.6803 | 1.0784 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 74.43 | 23.71 | 91.14 | 36.26 | 0.7255 | 0.9264 | 1.189 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.94 | 23.71 | 91.63 | 36.26 | 2.6053 | 1.436 | 1.5859 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
