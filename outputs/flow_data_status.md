# Flow / Positioning Proxy Status

Generated at: `2026-07-14T05:57:55.840332+00:00`
Latest date: `2026-07-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.45`
- overall_flow_conflict_score: `34.16`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.85 | 34.16 | 56.23 | 54.61 | -1.0248 | 0.9893 | 0.748 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.41 | 34.16 | 56.41 | 54.61 | -0.9706 | 1.0795 | 0.7988 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.69 | 34.16 | 56.18 | 54.61 | -0.8606 | 1.0335 | 0.7334 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 42.86 | 34.16 | 55.58 | 54.61 | -1.3317 | 0.761 | 0.5542 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
