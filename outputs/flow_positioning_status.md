# Flow / Positioning Proxy Status

Generated at: `2026-10-06T18:25:29.472906+00:00`
Latest date: `2026-10-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.8`
- overall_flow_conflict_score: `37.13`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.8 | 37.13 | 90.2 | 54.76 | -2.4769 | 0.4204 | 0.4293 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 61.8 | 37.13 | 90.2 | 54.76 | -2.015 | 0.6015 | 0.5479 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.8 | 37.13 | 90.2 | 54.76 | -2.372 | 0.5432 | 0.5668 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.8 | 37.13 | 90.2 | 54.76 | -1.9657 | 0.4592 | 0.4454 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
