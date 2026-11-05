# Flow / Positioning Proxy Status

Generated at: `2026-11-05T11:32:27.858501+00:00`
Latest date: `2026-11-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `73.65`
- overall_flow_conflict_score: `71.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.21 | 71.18 | 85.33 | 100.0 | 1.409 | 1.3381 | 1.576 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 71.21 | 71.18 | 85.33 | 100.0 | 1.1581 | 1.2614 | 1.5068 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.09 | 71.18 | 86.93 | 100.0 | 1.4408 | 1.6271 | 1.4438 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 76.09 | 71.18 | 86.93 | 100.0 | 3.0023 | 1.9065 | 1.9596 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
