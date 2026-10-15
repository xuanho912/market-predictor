# Flow / Positioning Proxy Status

Generated at: `2026-10-15T01:26:49.714564+00:00`
Latest date: `2026-10-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.32`
- overall_flow_conflict_score: `37.16`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.71 | 37.16 | 59.15 | 57.14 | 1.0772 | 1.998 | 1.3024 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.71 | 37.16 | 59.15 | 57.14 | 1.8706 | 1.6999 | 1.5199 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.71 | 37.16 | 59.15 | 57.14 | 2.2131 | 1.5325 | 1.5193 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.14 | 37.16 | 59.94 | 57.14 | 0.7037 | 1.0841 | 1.1073 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
