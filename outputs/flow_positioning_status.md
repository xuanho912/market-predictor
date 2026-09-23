# Flow / Positioning Proxy Status

Generated at: `2026-09-23T09:01:55.294119+00:00`
Latest date: `2026-09-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.14`
- overall_flow_conflict_score: `36.15`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 70.84 | 36.15 | 95.61 | 52.07 | 0.9366 | 0.9545 | 1.2367 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 71.42 | 36.15 | 95.8 | 52.07 | 2.1028 | 1.2748 | 1.489 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.53 | 36.15 | 93.87 | 52.07 | -0.2621 | 0.7173 | 0.9197 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.76 | 36.15 | 92.31 | 52.07 | -0.2294 | 0.8323 | 0.9293 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
