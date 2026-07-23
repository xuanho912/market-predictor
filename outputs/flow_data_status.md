# Flow / Positioning Proxy Status

Generated at: `2026-07-23T22:35:37.064795+00:00`
Latest date: `2026-07-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.34`
- overall_flow_conflict_score: `38.32`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.93 | 38.32 | 62.34 | 66.08 | 0.7043 | 1.218 | 1.136 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.55 | 38.32 | 62.22 | 66.08 | 0.6085 | 1.2012 | 1.1188 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.67 | 38.32 | 62.91 | 66.08 | 0.9978 | 1.2523 | 1.2423 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.21 | 38.32 | 62.43 | 66.08 | 0.7207 | 1.2843 | 1.1586 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
