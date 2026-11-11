# Flow / Positioning Proxy Status

Generated at: `2026-11-11T02:19:48.648282+00:00`
Latest date: `2026-11-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.88`
- overall_flow_conflict_score: `71.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.82 | 71.93 | 84.52 | 100.0 | -0.3965 | 0.6151 | 0.8359 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.92 | 71.93 | 84.22 | 100.0 | -0.5446 | 0.5405 | 0.7536 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.59 | 71.93 | 86.09 | 100.0 | -0.4943 | 0.6834 | 0.8261 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.17 | 71.93 | 85.95 | 100.0 | -0.4093 | 0.5359 | 0.7877 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
