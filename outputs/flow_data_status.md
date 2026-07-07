# Flow / Positioning Proxy Status

Generated at: `2026-07-07T05:10:38.376296+00:00`
Latest date: `2026-07-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.39`
- overall_flow_conflict_score: `45.99`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.18 | 45.99 | 71.39 | 69.85 | -0.9789 | 0.8747 | 0.7828 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.81 | 45.99 | 70.61 | 69.85 | -1.4594 | 0.6637 | 0.5518 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.5 | 45.99 | 69.19 | 69.85 | -1.4846 | 0.715 | 0.6182 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.06 | 45.99 | 70.69 | 69.85 | -1.5265 | 0.8006 | 0.5894 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
