# Flow / Positioning Proxy Status

Generated at: `2026-06-15T17:16:38.732479+00:00`
Latest date: `2026-06-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.43`
- overall_flow_conflict_score: `25.38`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 75.27 | 25.38 | 100.0 | 37.68 | -1.7001 | 0.326 | 0.4096 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.27 | 25.38 | 100.0 | 37.68 | -1.0396 | 0.4068 | 0.5515 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 75.27 | 25.38 | 100.0 | 37.68 | -1.9268 | 0.4174 | 0.5165 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.92 | 25.38 | 100.0 | 37.68 | -1.5678 | 0.5625 | 0.6381 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
