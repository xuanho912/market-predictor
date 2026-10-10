# Flow / Positioning Proxy Status

Generated at: `2026-10-10T00:17:43.219458+00:00`
Latest date: `2026-10-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.75`
- overall_flow_conflict_score: `39.61`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.71 | 39.61 | 77.54 | 56.13 | -0.617 | 0.9817 | 0.8778 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.06 | 39.61 | 79.62 | 56.13 | 2.0378 | 1.681 | 1.4898 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.18 | 39.61 | 78.02 | 56.13 | 2.3734 | 1.3403 | 1.4134 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.05 | 39.61 | 78.96 | 56.13 | 0.6837 | 1.0563 | 1.1513 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
