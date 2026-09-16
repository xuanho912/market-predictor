# Flow / Positioning Proxy Status

Generated at: `2026-09-16T01:24:03.283858+00:00`
Latest date: `2026-09-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `42.14`
- overall_flow_conflict_score: `45.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 43.5 | 45.83 | 51.37 | 71.62 | 1.0357 | 1.1005 | 1.1771 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 42.45 | 45.83 | 51.03 | 71.62 | 0.6579 | 1.2058 | 1.1494 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.53 | 45.83 | 51.71 | 71.62 | 1.5389 | 1.2551 | 1.4364 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 38.06 | 45.83 | 49.59 | 71.62 | -0.5183 | 0.7524 | 0.8664 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
