# Flow / Positioning Proxy Status

Generated at: `2026-09-29T18:07:34.748272+00:00`
Latest date: `2026-09-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.95`
- overall_flow_conflict_score: `43.74`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.95 | 43.74 | 80.83 | 58.01 | -2.3696 | 0.442 | 0.427 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 50.95 | 43.74 | 80.83 | 58.01 | -2.3253 | 0.4216 | 0.4382 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.95 | 43.74 | 80.83 | 58.01 | -2.1786 | 0.49 | 0.5291 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.95 | 43.74 | 80.83 | 58.01 | -1.879 | 0.5212 | 0.4767 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
