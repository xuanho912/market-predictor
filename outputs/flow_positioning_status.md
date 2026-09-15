# Flow / Positioning Proxy Status

Generated at: `2026-09-15T06:12:57.704818+00:00`
Latest date: `2026-09-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `42.97`
- overall_flow_conflict_score: `41.2`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.32 | 41.2 | 52.06 | 63.87 | 1.0283 | 1.0994 | 1.1758 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 43.23 | 41.2 | 51.71 | 63.87 | 0.6399 | 1.2018 | 1.1456 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 45.39 | 41.2 | 52.41 | 63.87 | 1.5355 | 1.2541 | 1.4353 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 38.92 | 41.2 | 50.29 | 63.87 | -0.5183 | 0.7524 | 0.8664 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
