# Flow / Positioning Proxy Status

Generated at: `2026-09-19T01:09:25.808075+00:00`
Latest date: `2026-09-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.56`
- overall_flow_conflict_score: `31.49`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.11 | 31.49 | 67.32 | 48.14 | 1.2677 | 1.0446 | 1.2615 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.99 | 31.49 | 68.92 | 48.14 | 1.3959 | 1.1976 | 1.2198 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.2 | 31.49 | 66.36 | 48.14 | 0.3984 | 0.8371 | 1.1196 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.95 | 31.49 | 67.26 | 48.14 | 0.8601 | 1.0626 | 1.2878 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
