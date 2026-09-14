# Flow / Positioning Proxy Status

Generated at: `2026-09-14T18:07:12.317120+00:00`
Latest date: `2026-09-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `37.38`
- overall_flow_conflict_score: `39.51`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 35.7 | 39.51 | 49.05 | 60.75 | -2.1947 | 0.5674 | 0.6068 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 37.31 | 39.51 | 49.58 | 60.75 | -1.2012 | 0.7904 | 0.7532 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 40.84 | 39.51 | 50.74 | 60.75 | 0.1398 | 0.9177 | 1.0503 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 35.67 | 39.51 | 49.04 | 60.75 | -1.3578 | 0.5247 | 0.6042 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
