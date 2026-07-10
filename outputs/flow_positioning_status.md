# Flow / Positioning Proxy Status

Generated at: `2026-07-10T23:45:42.576301+00:00`
Latest date: `2026-07-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.75`
- overall_flow_conflict_score: `18.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 70.95 | 18.56 | 89.11 | 32.0 | -1.2728 | 0.8703 | 0.6926 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.57 | 18.56 | 88.66 | 32.0 | -2.084 | 0.6554 | 0.5329 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.82 | 18.56 | 87.1 | 32.0 | -1.3734 | 0.8055 | 0.5783 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.66 | 18.56 | 87.38 | 32.0 | -1.0987 | 0.9117 | 0.6545 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
