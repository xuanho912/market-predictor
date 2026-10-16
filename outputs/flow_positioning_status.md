# Flow / Positioning Proxy Status

Generated at: `2026-10-16T16:42:23.767662+00:00`
Latest date: `2026-10-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `46.61`
- overall_flow_conflict_score: `59.07`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.23 | 59.07 | 55.79 | 89.83 | -1.6993 | 0.599 | 0.4735 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 46.96 | 59.07 | 56.68 | 89.83 | -0.5957 | 0.8069 | 0.8151 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.23 | 59.07 | 55.79 | 89.83 | -1.9896 | 0.4651 | 0.4781 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 51.02 | 59.07 | 58.02 | 89.83 | -1.3101 | 0.741 | 0.7404 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
