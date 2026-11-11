# Flow / Positioning Proxy Status

Generated at: `2026-11-11T01:28:57.767776+00:00`
Latest date: `2026-11-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `68.89`
- overall_flow_conflict_score: `71.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 66.53 | 71.93 | 85.41 | 100.0 | 0.0749 | 0.7602 | 1.0695 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 67.1 | 71.93 | 85.6 | 100.0 | 0.1566 | 0.7711 | 1.1069 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 72.7 | 71.93 | 87.43 | 100.0 | 0.345 | 0.9483 | 1.139 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 69.22 | 71.93 | 86.29 | 100.0 | -0.2421 | 0.5976 | 0.883 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
