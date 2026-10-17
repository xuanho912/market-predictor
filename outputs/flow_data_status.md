# Flow / Positioning Proxy Status

Generated at: `2026-10-17T01:18:36.952935+00:00`
Latest date: `2026-10-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.46`
- overall_flow_conflict_score: `64.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 47.47 | 64.92 | 56.41 | 99.01 | 0.103 | 1.3246 | 1.0217 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.03 | 64.92 | 57.9 | 99.01 | 1.531 | 1.4066 | 1.4471 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.03 | 64.92 | 57.9 | 99.01 | 1.1059 | 1.1823 | 1.2705 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.31 | 64.92 | 58.65 | 99.01 | 0.6171 | 1.0973 | 1.1092 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
