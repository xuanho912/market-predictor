# Flow / Positioning Proxy Status

Generated at: `2026-07-20T22:35:08.208931+00:00`
Latest date: `2026-07-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.95`
- overall_flow_conflict_score: `56.06`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 54.94 | 56.06 | 64.07 | 94.18 | -0.1141 | 1.0746 | 0.9508 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.12 | 56.06 | 63.15 | 94.18 | -1.367 | 0.755 | 0.6941 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.04 | 56.06 | 63.78 | 94.18 | -0.4529 | 0.9353 | 0.8695 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.72 | 56.06 | 62.69 | 94.18 | -1.6159 | 0.6438 | 0.538 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
