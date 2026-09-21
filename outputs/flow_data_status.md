# Flow / Positioning Proxy Status

Generated at: `2026-09-21T23:25:36.747126+00:00`
Latest date: `2026-09-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.36`
- overall_flow_conflict_score: `37.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.05 | 37.92 | 73.14 | 54.68 | 0.8277 | 0.9326 | 1.2081 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.15 | 37.92 | 73.5 | 54.68 | 2.0588 | 1.2626 | 1.4737 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 48.31 | 37.92 | 69.95 | 54.68 | -0.2857 | 0.712 | 0.913 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.92 | 37.92 | 69.82 | 54.68 | -0.3887 | 0.7856 | 0.8768 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
