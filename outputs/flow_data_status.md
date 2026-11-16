# Flow / Positioning Proxy Status

Generated at: `2026-11-16T22:06:01.041364+00:00`
Latest date: `2026-11-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.88`
- overall_flow_conflict_score: `69.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.84 | 69.01 | 80.54 | 100.0 | 0.873 | 1.6464 | 1.4456 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.17 | 69.01 | 78.35 | 100.0 | -0.3243 | 0.9605 | 0.8475 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.41 | 69.01 | 79.42 | 100.0 | 0.2543 | 1.1841 | 1.0976 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.09 | 69.01 | 78.66 | 100.0 | -0.1435 | 1.2523 | 0.9312 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
