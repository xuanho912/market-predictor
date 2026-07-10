# Flow / Positioning Proxy Status

Generated at: `2026-07-10T15:04:21.884302+00:00`
Latest date: `2026-07-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.0`
- overall_flow_conflict_score: `18.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 68.44 | 18.56 | 86.94 | 32.0 | -2.7601 | 0.2225 | 0.177 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.44 | 18.56 | 86.94 | 32.0 | -2.9602 | 0.2699 | 0.2194 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.56 | 18.56 | 85.34 | 32.0 | -2.295 | 0.3246 | 0.233 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.56 | 18.56 | 85.34 | 32.0 | -2.0075 | 0.4366 | 0.3134 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
