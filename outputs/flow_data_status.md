# Flow / Positioning Proxy Status

Generated at: `2026-07-18T05:53:34.718810+00:00`
Latest date: `2026-07-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.41`
- overall_flow_conflict_score: `49.0`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.39 | 49.0 | 67.2 | 81.17 | 0.9096 | 1.4785 | 1.1672 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.78 | 49.0 | 67.66 | 81.17 | 1.4599 | 1.6414 | 1.2959 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.64 | 49.0 | 67.28 | 81.17 | 0.8969 | 1.4882 | 1.1927 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.81 | 49.0 | 66.68 | 81.17 | 0.454 | 1.4549 | 1.1041 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
