# Flow / Positioning Proxy Status

Generated at: `2026-09-11T06:04:26.928233+00:00`
Latest date: `2026-09-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `42.34`
- overall_flow_conflict_score: `35.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 42.74 | 35.92 | 50.98 | 52.69 | 1.0596 | 1.1553 | 1.1725 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 39.07 | 35.92 | 49.77 | 52.69 | 0.0601 | 1.1089 | 1.0156 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 43.78 | 35.92 | 51.32 | 52.69 | 2.2405 | 1.5075 | 1.5884 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 43.78 | 35.92 | 51.32 | 52.69 | 1.865 | 1.3438 | 1.6015 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
