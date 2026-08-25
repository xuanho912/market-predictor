# Flow / Positioning Proxy Status

Generated at: `2026-08-25T13:13:54.430854+00:00`
Latest date: `2026-08-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.44`
- overall_flow_conflict_score: `20.84`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.11 | 20.84 | 89.62 | 35.93 | -1.0684 | 0.7963 | 0.7008 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.81 | 20.84 | 90.51 | 35.93 | -0.1512 | 1.0487 | 0.9466 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.71 | 20.84 | 89.49 | 35.93 | -1.2118 | 0.6956 | 0.6639 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 74.11 | 20.84 | 91.92 | 35.93 | 0.5774 | 1.4837 | 1.2358 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
