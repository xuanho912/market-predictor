# Flow / Positioning Proxy Status

Generated at: `2026-08-19T02:35:06.664740+00:00`
Latest date: `2026-08-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.05`
- overall_flow_conflict_score: `20.47`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.95 | 20.47 | 85.3 | 35.29 | -0.2648 | 1.2624 | 0.9376 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 72.48 | 20.47 | 86.78 | 35.29 | 0.6664 | 1.7178 | 1.2322 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 67.64 | 20.47 | 85.19 | 35.29 | -0.3504 | 1.2302 | 0.9093 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.14 | 20.47 | 85.36 | 35.29 | -0.1363 | 1.4106 | 0.955 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
