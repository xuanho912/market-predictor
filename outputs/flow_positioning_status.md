# Flow / Positioning Proxy Status

Generated at: `2026-06-22T17:42:32.568716+00:00`
Latest date: `2026-06-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.9`
- overall_flow_conflict_score: `20.8`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.82 | 20.8 | 100.0 | 34.27 | -1.8135 | 0.3052 | 0.3663 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.82 | 20.8 | 100.0 | 34.27 | -1.2895 | 0.4658 | 0.4681 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 69.82 | 20.8 | 100.0 | 34.27 | -1.8945 | 0.4604 | 0.4814 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.14 | 20.8 | 100.0 | 34.27 | -1.6155 | 0.5155 | 0.6028 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
