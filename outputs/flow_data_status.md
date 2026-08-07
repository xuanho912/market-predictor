# Flow / Positioning Proxy Status

Generated at: `2026-08-07T05:24:56.236818+00:00`
Latest date: `2026-08-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.23`
- overall_flow_conflict_score: `28.55`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.85 | 28.55 | 63.6 | 49.23 | -0.9774 | 0.6317 | 0.7688 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.08 | 28.55 | 63.67 | 49.23 | -0.7502 | 0.6432 | 0.7892 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.68 | 28.55 | 63.54 | 49.23 | -1.1795 | 0.7258 | 0.7533 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.31 | 28.55 | 64.08 | 49.23 | -0.3373 | 0.7659 | 0.9013 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
