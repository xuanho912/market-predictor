# Flow / Positioning Proxy Status

Generated at: `2026-07-13T15:14:37.890296+00:00`
Latest date: `2026-07-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.15`
- overall_flow_conflict_score: `25.91`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.81 | 25.91 | 61.21 | 43.69 | -2.7861 | 0.2571 | 0.1943 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.93 | 25.91 | 59.61 | 43.69 | -2.8218 | 0.4514 | 0.334 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 48.93 | 25.91 | 59.61 | 43.69 | -2.3416 | 0.3143 | 0.223 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 48.93 | 25.91 | 59.61 | 43.69 | -2.109 | 0.3338 | 0.2431 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
