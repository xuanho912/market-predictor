# Flow / Positioning Proxy Status

Generated at: `2026-08-29T16:46:26.527677+00:00`
Latest date: `2026-08-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `71.54`
- overall_flow_conflict_score: `20.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.76 | 20.63 | 89.88 | 35.56 | -0.3126 | 1.1307 | 0.8945 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 73.08 | 20.63 | 90.32 | 35.56 | 0.089 | 1.1835 | 0.9992 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.6 | 20.63 | 89.5 | 35.56 | 0.6936 | 1.2761 | 1.1096 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.72 | 20.63 | 89.54 | 35.56 | -0.5085 | 0.9267 | 0.7994 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
