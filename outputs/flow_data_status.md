# Flow / Positioning Proxy Status

Generated at: `2026-06-29T23:38:04.103586+00:00`
Latest date: `2026-06-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.72`
- overall_flow_conflict_score: `44.96`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.6 | 44.96 | 75.23 | 62.96 | -0.3726 | 0.9599 | 0.9041 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.42 | 44.96 | 74.85 | 62.96 | -0.6377 | 0.8505 | 0.7972 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.44 | 44.96 | 76.49 | 62.96 | -0.806 | 0.8449 | 0.8092 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.42 | 44.96 | 77.14 | 62.96 | -0.0599 | 1.101 | 0.9898 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
