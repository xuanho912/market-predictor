# Flow / Positioning Proxy Status

Generated at: `2026-07-24T21:35:40.301220+00:00`
Latest date: `2026-07-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.93`
- overall_flow_conflict_score: `51.97`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.18 | 51.97 | 63.07 | 89.61 | -0.668 | 0.8801 | 0.8552 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.57 | 51.97 | 63.85 | 89.61 | 0.2239 | 1.0698 | 1.0332 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.49 | 51.97 | 63.17 | 89.61 | -0.4102 | 0.8601 | 0.8836 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.49 | 51.97 | 63.17 | 89.61 | -0.4416 | 0.9169 | 0.8842 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
