# Flow / Positioning Proxy Status

Generated at: `2026-06-16T15:33:42.199304+00:00`
Latest date: `2026-06-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.27`
- overall_flow_conflict_score: `26.91`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 75.27 | 26.91 | 100.0 | 38.86 | -2.1012 | 0.187 | 0.235 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.27 | 26.91 | 100.0 | 38.86 | -1.5018 | 0.2426 | 0.3298 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 75.27 | 26.91 | 100.0 | 38.86 | -2.4632 | 0.2592 | 0.3211 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.27 | 26.91 | 100.0 | 38.86 | -2.3295 | 0.35 | 0.4038 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
