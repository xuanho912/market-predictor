# Flow / Positioning Proxy Status

Generated at: `2026-06-19T23:43:14.231891+00:00`
Latest date: `2026-06-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `77.65`
- overall_flow_conflict_score: `22.29`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 79.18 | 22.29 | 100.0 | 34.87 | 1.2166 | 1.1339 | 1.4248 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.58 | 22.29 | 100.0 | 34.87 | 0.073 | 0.9403 | 1.0426 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.66 | 22.29 | 100.0 | 34.87 | 0.4229 | 0.9928 | 1.1003 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 79.18 | 22.29 | 100.0 | 34.87 | 1.3538 | 1.1327 | 1.2996 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
