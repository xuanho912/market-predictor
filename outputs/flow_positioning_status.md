# Flow / Positioning Proxy Status

Generated at: `2026-09-16T16:59:16.866995+00:00`
Latest date: `2026-09-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `35.17`
- overall_flow_conflict_score: `37.4`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 34.78 | 37.4 | 51.0 | 53.41 | -2.927 | 0.3312 | 0.3625 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 34.78 | 37.4 | 51.0 | 53.41 | -2.9624 | 0.3773 | 0.3542 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 34.78 | 37.4 | 51.0 | 53.41 | -2.022 | 0.3154 | 0.4043 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 36.36 | 37.4 | 51.52 | 53.41 | -0.9727 | 0.6301 | 0.7106 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
