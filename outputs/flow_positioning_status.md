# Flow / Positioning Proxy Status

Generated at: `2026-07-01T23:55:16.920722+00:00`
Latest date: `2026-07-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.67`
- overall_flow_conflict_score: `46.96`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.24 | 46.96 | 74.89 | 70.29 | -1.6347 | 0.6606 | 0.6154 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.5 | 46.96 | 75.3 | 70.29 | -0.9234 | 0.8228 | 0.7299 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.87 | 46.96 | 75.1 | 70.29 | -1.4452 | 0.707 | 0.673 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.08 | 46.96 | 74.84 | 70.29 | -1.6903 | 0.7308 | 0.6006 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
