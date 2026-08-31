# Flow / Positioning Proxy Status

Generated at: `2026-08-31T19:10:48.086527+00:00`
Latest date: `2026-08-31`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.67`
- overall_flow_conflict_score: `21.6`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 68.05 | 21.6 | 87.91 | 37.24 | -1.9792 | 0.5838 | 0.4696 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.03 | 21.6 | 88.23 | 37.24 | -1.1574 | 0.7545 | 0.6557 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.42 | 21.6 | 87.38 | 37.24 | -0.6028 | 1.0189 | 0.863 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.17 | 21.6 | 86.31 | 37.24 | -1.6134 | 0.3995 | 0.3446 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
