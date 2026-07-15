# Flow / Positioning Proxy Status

Generated at: `2026-07-15T14:12:42.204851+00:00`
Latest date: `2026-07-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `49.86`
- overall_flow_conflict_score: `23.9`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.08 | 23.9 | 58.83 | 41.21 | -2.8959 | 0.1433 | 0.109 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.08 | 23.9 | 58.83 | 41.21 | -3.2428 | 0.1582 | 0.1264 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.08 | 23.9 | 58.83 | 41.21 | -2.5465 | 0.1711 | 0.1279 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 46.2 | 23.9 | 57.23 | 41.21 | -2.3692 | 0.2388 | 0.1754 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
