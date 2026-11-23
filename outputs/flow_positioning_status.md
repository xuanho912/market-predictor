# Flow / Positioning Proxy Status

Generated at: `2026-11-23T23:56:37.521920+00:00`
Latest date: `2026-11-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.99`
- overall_flow_conflict_score: `69.3`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.14 | 69.3 | 66.04 | 100.0 | 0.8396 | 1.0354 | 1.4933 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.14 | 69.3 | 66.04 | 100.0 | 0.8239 | 1.1915 | 1.4614 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.13 | 69.3 | 65.05 | 100.0 | 0.2704 | 0.8951 | 1.1329 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.56 | 69.3 | 64.21 | 100.0 | -0.1413 | 0.8458 | 0.9474 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
