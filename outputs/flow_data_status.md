# Flow / Positioning Proxy Status

Generated at: `2026-10-16T00:52:41.609481+00:00`
Latest date: `2026-10-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.72`
- overall_flow_conflict_score: `41.06`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.73 | 41.06 | 55.11 | 62.68 | 0.0971 | 1.3223 | 1.0199 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.32 | 41.06 | 56.62 | 62.68 | 1.5121 | 1.4004 | 1.4407 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.32 | 41.06 | 56.62 | 62.68 | 1.1012 | 1.1812 | 1.2693 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 53.52 | 41.06 | 57.34 | 62.68 | 0.5966 | 1.0931 | 1.105 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
