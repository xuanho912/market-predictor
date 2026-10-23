# Flow / Positioning Proxy Status

Generated at: `2026-10-23T06:05:11.901052+00:00`
Latest date: `2026-10-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.89`
- overall_flow_conflict_score: `71.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.48 | 71.44 | 68.3 | 100.0 | 1.1185 | 1.2665 | 1.3426 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.48 | 71.44 | 68.3 | 100.0 | 2.1292 | 1.4788 | 1.8338 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.32 | 71.44 | 68.25 | 100.0 | -0.0005 | 1.0027 | 0.9968 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.28 | 71.44 | 67.58 | 100.0 | -0.8048 | 0.7595 | 0.8112 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
