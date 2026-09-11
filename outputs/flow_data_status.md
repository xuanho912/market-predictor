# Flow / Positioning Proxy Status

Generated at: `2026-09-11T01:02:01.767556+00:00`
Latest date: `2026-09-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `40.05`
- overall_flow_conflict_score: `35.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 37.64 | 35.92 | 49.31 | 52.69 | -0.6692 | 0.85 | 0.8966 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 37.31 | 35.92 | 49.2 | 52.69 | -0.6497 | 0.8958 | 0.8662 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 41.49 | 35.92 | 50.57 | 52.69 | 0.5959 | 1.0277 | 1.1412 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 43.78 | 35.92 | 51.32 | 52.69 | 0.9876 | 1.1075 | 1.2964 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
