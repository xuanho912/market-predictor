# Flow / Positioning Proxy Status

Generated at: `2026-08-18T23:33:39.935724+00:00`
Latest date: `2026-08-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.14`
- overall_flow_conflict_score: `20.47`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.04 | 20.47 | 80.0 | 35.29 | -0.2648 | 1.2624 | 0.9376 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.57 | 20.47 | 81.49 | 35.29 | 0.6664 | 1.7178 | 1.2322 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.73 | 20.47 | 79.9 | 35.29 | -0.3504 | 1.2302 | 0.9093 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.23 | 20.47 | 80.07 | 35.29 | -0.1363 | 1.4106 | 0.955 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
