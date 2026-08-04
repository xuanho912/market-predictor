# Flow / Positioning Proxy Status

Generated at: `2026-08-04T22:40:41.329502+00:00`
Latest date: `2026-08-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `74.67`
- overall_flow_conflict_score: `20.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 75.35 | 20.44 | 84.27 | 35.24 | 0.8702 | 0.9546 | 1.2098 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 76.35 | 20.44 | 84.59 | 35.24 | 1.5019 | 1.0888 | 1.4425 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.62 | 20.44 | 82.71 | 35.24 | -0.3511 | 0.7983 | 0.9336 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 76.35 | 20.44 | 84.59 | 35.24 | 2.0592 | 1.3197 | 1.6719 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
