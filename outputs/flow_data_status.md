# Flow / Positioning Proxy Status

Generated at: `2026-09-25T23:23:44.126900+00:00`
Latest date: `2026-09-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.72`
- overall_flow_conflict_score: `36.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.16 | 36.66 | 81.27 | 53.96 | -0.9518 | 0.7059 | 0.8074 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.26 | 36.66 | 81.63 | 53.96 | -0.4983 | 0.7598 | 0.9074 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.4 | 36.66 | 80.37 | 53.96 | -0.0981 | 0.8794 | 1.0009 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.07 | 36.66 | 81.25 | 53.96 | -0.749 | 0.8432 | 0.7992 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
