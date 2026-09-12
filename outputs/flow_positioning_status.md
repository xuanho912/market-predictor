# Flow / Positioning Proxy Status

Generated at: `2026-09-12T00:46:28.823208+00:00`
Latest date: `2026-09-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.69`
- overall_flow_conflict_score: `34.35`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 45.08 | 34.35 | 54.5 | 49.97 | 1.0695 | 1.157 | 1.1741 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 41.48 | 34.35 | 53.32 | 49.97 | 0.0855 | 1.1148 | 1.0209 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 46.09 | 34.35 | 54.83 | 49.97 | 2.2519 | 1.5114 | 1.5924 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 46.09 | 34.35 | 54.83 | 49.97 | 1.865 | 1.3438 | 1.6015 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
