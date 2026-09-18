# Flow / Positioning Proxy Status

Generated at: `2026-09-18T08:31:14.069869+00:00`
Latest date: `2026-09-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `49.41`
- overall_flow_conflict_score: `33.86`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.63 | 33.86 | 58.86 | 52.27 | 1.263 | 1.0437 | 1.2604 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.63 | 33.86 | 58.86 | 52.27 | 1.3664 | 1.1923 | 1.2144 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.81 | 33.86 | 56.3 | 52.27 | 0.3939 | 0.8362 | 1.1184 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.58 | 33.86 | 57.21 | 52.27 | 0.8601 | 1.0626 | 1.2878 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
