# Flow / Positioning Proxy Status

Generated at: `2026-11-06T01:59:10.672955+00:00`
Latest date: `2026-11-05`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.01`
- overall_flow_conflict_score: `76.14`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 66.01 | 76.14 | 80.84 | 100.0 | 1.4137 | 1.3399 | 1.5781 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.01 | 76.14 | 80.84 | 100.0 | 1.1709 | 1.2662 | 1.5126 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.01 | 76.14 | 80.84 | 100.0 | 1.4482 | 1.63 | 1.4464 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.01 | 76.14 | 80.84 | 100.0 | 3.0138 | 1.9134 | 1.9667 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
