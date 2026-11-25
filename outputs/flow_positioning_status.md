# Flow / Positioning Proxy Status

Generated at: `2026-11-25T21:45:24.975978+00:00`
Latest date: `2026-11-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.72`
- overall_flow_conflict_score: `73.47`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.35 | 73.47 | 77.04 | 100.0 | 0.215 | 0.8238 | 1.1326 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.07 | 73.47 | 77.93 | 100.0 | 0.5989 | 1.016 | 1.312 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.9 | 73.47 | 77.22 | 100.0 | 0.3651 | 0.9282 | 1.1553 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.55 | 73.47 | 76.45 | 100.0 | -0.022 | 0.9088 | 1.0064 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
