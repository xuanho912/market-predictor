# Flow / Positioning Proxy Status

Generated at: `2026-10-10T07:13:20.993187+00:00`
Latest date: `2026-10-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.28`
- overall_flow_conflict_score: `39.61`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 54.3 | 39.61 | 76.42 | 56.13 | -2.1584 | 0.5688 | 0.4918 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.84 | 39.61 | 76.6 | 56.13 | -1.6225 | 0.6528 | 0.6163 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.19 | 39.61 | 75.4 | 56.13 | -1.4758 | 0.6935 | 0.7279 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.78 | 39.61 | 77.23 | 56.13 | -0.8066 | 0.7358 | 0.793 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
