# Flow / Positioning Proxy Status

Generated at: `2026-07-31T06:34:26.021056+00:00`
Latest date: `2026-07-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.31`
- overall_flow_conflict_score: `45.22`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.17 | 45.22 | 66.37 | 77.96 | 1.8859 | 1.2847 | 1.4262 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.29 | 45.22 | 64.77 | 77.96 | 2.391 | 1.3939 | 1.708 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.14 | 45.22 | 65.05 | 77.96 | 0.2243 | 0.918 | 1.0492 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.64 | 45.22 | 64.24 | 77.96 | -0.475 | 0.6836 | 0.8616 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
