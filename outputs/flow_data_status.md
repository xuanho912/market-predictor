# Flow / Positioning Proxy Status

Generated at: `2026-09-22T01:20:10.075434+00:00`
Latest date: `2026-09-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.93`
- overall_flow_conflict_score: `37.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.15 | 37.92 | 73.5 | 54.68 | 2.5827 | 1.3352 | 1.6397 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.15 | 37.92 | 73.5 | 54.68 | 2.7688 | 1.495 | 1.5762 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.27 | 37.92 | 71.9 | 54.68 | 1.8801 | 1.2201 | 1.5437 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.15 | 37.92 | 69.56 | 54.68 | -0.6139 | 0.6963 | 0.8066 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
