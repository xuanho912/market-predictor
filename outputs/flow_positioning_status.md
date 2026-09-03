# Flow / Positioning Proxy Status

Generated at: `2026-09-03T16:28:10.561144+00:00`
Latest date: `2026-09-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.41`
- overall_flow_conflict_score: `21.07`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.84 | 21.07 | 64.59 | 36.15 | -2.6356 | 0.5275 | 0.5218 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.96 | 21.07 | 62.99 | 36.15 | -1.9458 | 0.5427 | 0.5403 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 48.96 | 21.07 | 62.99 | 36.15 | -2.0044 | 0.4289 | 0.5006 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.87 | 21.07 | 67.22 | 36.15 | 0.7284 | 1.258 | 1.1685 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
