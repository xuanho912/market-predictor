# Flow / Positioning Proxy Status

Generated at: `2026-08-26T04:24:48.560386+00:00`
Latest date: `2026-08-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `71.54`
- overall_flow_conflict_score: `20.57`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 70.04 | 20.57 | 100.0 | 35.46 | -1.3231 | 0.6801 | 0.5987 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.09 | 20.57 | 100.0 | 35.46 | -1.1484 | 0.6272 | 0.6051 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.56 | 20.57 | 100.0 | 35.46 | -0.7984 | 0.805 | 0.7675 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 74.48 | 20.57 | 100.0 | 35.46 | -0.8531 | 0.7031 | 0.6476 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
