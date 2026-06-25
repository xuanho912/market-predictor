# Flow / Positioning Proxy Status

Generated at: `2026-06-25T05:18:30.994752+00:00`
Latest date: `2026-06-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.93`
- overall_flow_conflict_score: `35.25`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.78 | 35.25 | 80.27 | 49.01 | -0.2185 | 0.8193 | 0.9497 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.9 | 35.25 | 80.64 | 49.01 | 0.0633 | 1.069 | 1.0407 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.95 | 35.25 | 81.96 | 49.01 | -0.1317 | 0.9791 | 0.976 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.09 | 35.25 | 79.71 | 49.01 | -0.9874 | 0.7287 | 0.7958 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
