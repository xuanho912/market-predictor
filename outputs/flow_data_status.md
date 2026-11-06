# Flow / Positioning Proxy Status

Generated at: `2026-11-06T19:27:47.055153+00:00`
Latest date: `2026-11-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.23`
- overall_flow_conflict_score: `74.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.57 | 74.63 | 78.14 | 100.0 | -0.4271 | 0.5144 | 0.7946 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.27 | 74.63 | 79.35 | 100.0 | 0.1416 | 0.7052 | 1.1057 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.43 | 74.63 | 77.76 | 100.0 | -0.8707 | 0.5748 | 0.6901 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.63 | 74.63 | 78.16 | 100.0 | -0.3901 | 0.5202 | 0.7995 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
