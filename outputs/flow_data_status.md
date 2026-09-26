# Flow / Positioning Proxy Status

Generated at: `2026-09-26T16:27:07.511461+00:00`
Latest date: `2026-09-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.91`
- overall_flow_conflict_score: `36.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.51 | 36.66 | 81.39 | 53.96 | -0.8084 | 0.7338 | 0.8393 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.33 | 36.66 | 81.66 | 53.96 | -0.4636 | 0.7657 | 0.9144 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.5 | 36.66 | 80.4 | 53.96 | -0.0548 | 0.887 | 1.0096 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.32 | 36.66 | 81.33 | 53.96 | -0.6703 | 0.8676 | 0.8224 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
