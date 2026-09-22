# Flow / Positioning Proxy Status

Generated at: `2026-09-22T01:36:16.138166+00:00`
Latest date: `2026-09-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.6`
- overall_flow_conflict_score: `37.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.4 | 37.92 | 73.25 | 54.68 | 0.9004 | 0.9472 | 1.2272 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.15 | 37.92 | 73.5 | 54.68 | 2.0911 | 1.2718 | 1.4855 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 48.37 | 37.92 | 69.96 | 54.68 | -0.2675 | 0.7161 | 0.9182 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 48.49 | 37.92 | 70.0 | 54.68 | -0.2294 | 0.8323 | 0.9293 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
