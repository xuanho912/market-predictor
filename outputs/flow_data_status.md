# Flow / Positioning Proxy Status

Generated at: `2026-10-17T08:04:29.260396+00:00`
Latest date: `2026-10-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.25`
- overall_flow_conflict_score: `64.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.03 | 64.92 | 57.9 | 99.01 | 1.8569 | 1.9272 | 1.5238 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.03 | 64.92 | 57.9 | 99.01 | 2.6615 | 1.8812 | 1.9022 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.03 | 64.92 | 57.9 | 99.01 | 1.299 | 1.2657 | 1.3011 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.91 | 64.92 | 59.5 | 99.01 | 2.5523 | 1.6273 | 1.6272 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
