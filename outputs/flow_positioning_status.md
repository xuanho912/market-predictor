# Flow / Positioning Proxy Status

Generated at: `2026-08-22T13:03:53.083842+00:00`
Latest date: `2026-08-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `74.93`
- overall_flow_conflict_score: `19.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 73.91 | 19.44 | 100.0 | 33.52 | -0.5877 | 0.9984 | 0.8398 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 73.86 | 19.44 | 100.0 | 33.52 | -0.5047 | 0.9884 | 0.834 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 78.27 | 19.44 | 100.0 | 33.52 | 0.7302 | 1.3881 | 1.1944 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.68 | 19.44 | 100.0 | 33.52 | -0.4845 | 1.0453 | 0.8142 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
