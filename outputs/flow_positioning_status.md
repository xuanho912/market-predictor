# Flow / Positioning Proxy Status

Generated at: `2026-10-22T17:13:56.681949+00:00`
Latest date: `2026-10-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.71`
- overall_flow_conflict_score: `70.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.3 | 70.94 | 64.33 | 100.0 | -1.3517 | 0.5359 | 0.5679 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.91 | 70.94 | 65.51 | 100.0 | -0.3325 | 0.7237 | 0.8961 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.48 | 70.94 | 66.03 | 100.0 | -1.4728 | 0.599 | 0.5951 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.17 | 70.94 | 65.93 | 100.0 | -1.9158 | 0.4619 | 0.493 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
