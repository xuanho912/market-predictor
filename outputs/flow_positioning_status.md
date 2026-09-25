# Flow / Positioning Proxy Status

Generated at: `2026-09-25T01:34:15.844833+00:00`
Latest date: `2026-09-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.48`
- overall_flow_conflict_score: `33.59`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 66.68 | 33.59 | 88.31 | 51.8 | 0.0279 | 0.8596 | 1.0234 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.1 | 33.59 | 87.79 | 51.8 | -0.6657 | 0.7013 | 0.8841 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.44 | 33.59 | 88.23 | 51.8 | 1.0399 | 1.1157 | 1.2659 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.71 | 33.59 | 86.02 | 51.8 | -0.5506 | 0.6965 | 0.8382 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
