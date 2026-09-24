# Flow / Positioning Proxy Status

Generated at: `2026-09-24T01:26:41.529011+00:00`
Latest date: `2026-09-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.0`
- overall_flow_conflict_score: `33.75`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.96 | 33.75 | 92.91 | 52.08 | -0.697 | 0.6422 | 0.8409 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 72.65 | 33.75 | 95.1 | 52.08 | 1.1176 | 1.03 | 1.2521 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 67.32 | 33.75 | 93.36 | 52.08 | 0.8572 | 1.0263 | 1.2575 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.05 | 33.75 | 91.63 | 52.08 | -0.2294 | 0.8323 | 0.9293 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
