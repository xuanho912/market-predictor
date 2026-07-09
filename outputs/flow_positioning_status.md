# Flow / Positioning Proxy Status

Generated at: `2026-07-09T23:57:21.104191+00:00`
Latest date: `2026-07-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.04`
- overall_flow_conflict_score: `21.43`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.79 | 21.43 | 71.59 | 34.43 | -1.5268 | 0.8099 | 0.6352 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.17 | 21.43 | 70.08 | 34.43 | -1.5032 | 0.8296 | 0.6591 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.16 | 21.43 | 69.74 | 34.43 | -1.4517 | 0.7912 | 0.5659 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.04 | 21.43 | 71.34 | 34.43 | -1.4539 | 0.7856 | 0.5581 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
