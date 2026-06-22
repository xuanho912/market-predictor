# Flow / Positioning Proxy Status

Generated at: `2026-06-22T17:05:04.114316+00:00`
Latest date: `2026-06-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.82`
- overall_flow_conflict_score: `20.68`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.82 | 20.68 | 100.0 | 34.17 | -1.8922 | 0.2765 | 0.3318 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.82 | 20.68 | 100.0 | 34.17 | -1.3396 | 0.4426 | 0.4447 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 69.82 | 20.68 | 100.0 | 34.17 | -2.0178 | 0.4199 | 0.4391 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 69.82 | 20.68 | 100.0 | 34.17 | -2.07 | 0.3989 | 0.4664 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
