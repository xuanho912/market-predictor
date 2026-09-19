# Flow / Positioning Proxy Status

Generated at: `2026-09-19T08:19:39.132315+00:00`
Latest date: `2026-09-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.55`
- overall_flow_conflict_score: `31.49`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.11 | 31.49 | 67.32 | 48.14 | 2.5827 | 1.3352 | 1.6397 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.99 | 31.49 | 68.92 | 48.14 | 2.7688 | 1.495 | 1.5762 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.11 | 31.49 | 67.32 | 48.14 | 1.8801 | 1.2201 | 1.5437 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 45.99 | 31.49 | 64.98 | 48.14 | -0.6139 | 0.6963 | 0.8066 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
