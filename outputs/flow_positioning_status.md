# Flow / Positioning Proxy Status

Generated at: `2026-08-11T04:54:36.520143+00:00`
Latest date: `2026-08-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.84`
- overall_flow_conflict_score: `19.97`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.22 | 19.97 | 78.51 | 34.43 | -0.8756 | 0.7663 | 0.7885 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.42 | 19.97 | 77.92 | 34.43 | -1.2833 | 0.6458 | 0.6245 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.74 | 19.97 | 78.35 | 34.43 | -1.1899 | 0.8403 | 0.7452 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.0 | 19.97 | 78.76 | 34.43 | -0.4613 | 0.7678 | 0.8596 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
