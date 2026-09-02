# Flow / Positioning Proxy Status

Generated at: `2026-09-02T05:53:36.032070+00:00`
Latest date: `2026-09-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `45.27`
- overall_flow_conflict_score: `38.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.9 | 38.01 | 53.48 | 56.36 | 0.7475 | 1.2345 | 1.0608 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 44.86 | 38.01 | 53.46 | 56.36 | 0.6334 | 1.2612 | 1.0777 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 47.77 | 38.01 | 54.42 | 56.36 | 1.815 | 1.4461 | 1.373 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 43.53 | 38.01 | 53.03 | 56.36 | 0.2741 | 1.4359 | 1.0202 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
