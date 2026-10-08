# Flow / Positioning Proxy Status

Generated at: `2026-10-08T02:42:13.715244+00:00`
Latest date: `2026-10-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.91`
- overall_flow_conflict_score: `39.7`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.85 | 39.7 | 89.6 | 57.58 | -1.7 | 0.653 | 0.6708 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.81 | 39.7 | 89.92 | 57.58 | -1.19 | 0.8335 | 0.7589 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.5 | 39.7 | 89.16 | 57.58 | -0.1289 | 0.9578 | 0.993 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 72.46 | 39.7 | 92.42 | 57.58 | 1.1231 | 1.2933 | 1.2917 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
