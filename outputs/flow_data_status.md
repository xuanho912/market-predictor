# Flow / Positioning Proxy Status

Generated at: `2026-09-16T06:07:02.941505+00:00`
Latest date: `2026-09-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `41.66`
- overall_flow_conflict_score: `45.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.34 | 45.83 | 51.65 | 71.62 | 1.2613 | 1.0994 | 1.2138 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 37.85 | 45.83 | 49.52 | 71.62 | -0.7813 | 0.8914 | 0.8475 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.53 | 45.83 | 51.71 | 71.62 | 1.2299 | 1.0891 | 1.3441 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 39.94 | 45.83 | 50.2 | 71.62 | 0.0626 | 0.8811 | 1.0259 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
