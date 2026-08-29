# Flow / Positioning Proxy Status

Generated at: `2026-08-29T03:57:00.580253+00:00`
Latest date: `2026-08-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `71.38`
- overall_flow_conflict_score: `20.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.66 | 20.63 | 89.85 | 35.56 | -0.3485 | 1.1193 | 0.8855 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 73.0 | 20.63 | 90.29 | 35.56 | 0.0729 | 1.1782 | 0.9948 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.48 | 20.63 | 89.46 | 35.56 | 0.6664 | 1.2695 | 1.1038 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.36 | 20.63 | 89.42 | 35.56 | -0.5936 | 0.8891 | 0.767 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
