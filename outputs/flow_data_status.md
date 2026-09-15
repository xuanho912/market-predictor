# Flow / Positioning Proxy Status

Generated at: `2026-09-15T23:41:18.331942+00:00`
Latest date: `2026-09-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `41.36`
- overall_flow_conflict_score: `45.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 43.53 | 45.83 | 51.38 | 71.62 | 1.0527 | 1.066 | 1.1769 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 37.75 | 45.83 | 49.49 | 71.62 | -0.8245 | 0.8817 | 0.8384 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.53 | 45.83 | 51.71 | 71.62 | 1.1553 | 1.0715 | 1.3223 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 39.62 | 45.83 | 50.1 | 71.62 | 0.0003 | 0.8658 | 1.0081 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
