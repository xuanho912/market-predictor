# Flow / Positioning Proxy Status

Generated at: `2026-06-19T00:14:21.245322+00:00`
Latest date: `2026-06-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `77.05`
- overall_flow_conflict_score: `22.29`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 77.74 | 22.29 | 100.0 | 34.87 | 0.5619 | 0.9515 | 1.1956 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.35 | 22.29 | 100.0 | 34.87 | 0.0296 | 0.9241 | 1.0247 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.49 | 22.29 | 100.0 | 34.87 | 0.3777 | 0.9826 | 1.089 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 78.61 | 22.29 | 100.0 | 34.87 | 1.0031 | 1.0582 | 1.2141 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
