# Flow / Positioning Proxy Status

Generated at: `2026-11-05T00:58:32.261120+00:00`
Latest date: `2026-11-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `73.65`
- overall_flow_conflict_score: `71.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.21 | 71.18 | 85.33 | 100.0 | 1.3854 | 1.3292 | 1.5655 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 71.21 | 71.18 | 85.33 | 100.0 | 1.1461 | 1.2568 | 1.5013 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.09 | 71.18 | 86.93 | 100.0 | 1.4369 | 1.6256 | 1.4425 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 76.09 | 71.18 | 86.93 | 100.0 | 2.9535 | 1.8777 | 1.93 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
