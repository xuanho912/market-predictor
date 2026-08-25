# Flow / Positioning Proxy Status

Generated at: `2026-08-25T20:54:31.646638+00:00`
Latest date: `2026-08-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `71.38`
- overall_flow_conflict_score: `20.57`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.88 | 20.57 | 100.0 | 35.46 | -1.3747 | 0.6604 | 0.5814 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.95 | 20.57 | 100.0 | 35.46 | -1.1937 | 0.6105 | 0.589 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.43 | 20.57 | 100.0 | 35.46 | -0.8441 | 0.7908 | 0.7539 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 74.27 | 20.57 | 100.0 | 35.46 | -0.9093 | 0.6782 | 0.6247 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
