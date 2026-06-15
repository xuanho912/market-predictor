# Flow / Positioning Proxy Status

Generated at: `2026-06-15T13:43:00.736598+00:00`
Latest date: `2026-06-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.27`
- overall_flow_conflict_score: `23.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 75.27 | 23.92 | 100.0 | 36.39 | -2.4049 | 0.0648 | 0.0814 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.27 | 23.92 | 100.0 | 36.39 | -1.9129 | 0.0824 | 0.1117 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 75.27 | 23.92 | 100.0 | 36.39 | -2.9948 | 0.0658 | 0.0815 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.27 | 23.92 | 100.0 | 36.39 | -2.9467 | 0.1204 | 0.1366 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
