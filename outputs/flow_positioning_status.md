# Flow / Positioning Proxy Status

Generated at: `2026-07-16T21:32:07.467885+00:00`
Latest date: `2026-07-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.49`
- overall_flow_conflict_score: `43.58`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.47 | 43.58 | 66.43 | 73.08 | -0.9307 | 0.989 | 0.748 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.64 | 43.58 | 66.81 | 73.08 | -0.6803 | 1.1291 | 0.8542 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.19 | 43.58 | 67.32 | 73.08 | -0.0167 | 1.3479 | 0.9957 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.65 | 43.58 | 67.8 | 73.08 | -0.9942 | 0.9255 | 0.6842 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
