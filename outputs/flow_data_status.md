# Flow / Positioning Proxy Status

Generated at: `2026-06-24T05:13:44.767622+00:00`
Latest date: `2026-06-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.34`
- overall_flow_conflict_score: `25.21`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.98 | 25.21 | 94.68 | 37.45 | 0.3751 | 0.978 | 1.1357 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.89 | 25.21 | 94.33 | 37.45 | 0.1512 | 1.1142 | 1.0768 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.73 | 25.21 | 95.25 | 37.45 | -0.3674 | 0.9343 | 0.9173 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.78 | 25.21 | 93.63 | 37.45 | -0.4048 | 0.826 | 0.9112 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
