# Flow / Positioning Proxy Status

Generated at: `2026-09-15T17:02:43.398875+00:00`
Latest date: `2026-09-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `35.54`
- overall_flow_conflict_score: `45.03`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 34.77 | 45.03 | 48.51 | 70.46 | -2.727 | 0.4089 | 0.4514 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 34.77 | 45.03 | 48.51 | 70.46 | -2.423 | 0.4412 | 0.4193 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 37.08 | 45.03 | 49.27 | 70.46 | -0.8868 | 0.6299 | 0.7773 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 35.55 | 45.03 | 48.76 | 70.46 | -1.2424 | 0.5473 | 0.6373 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
