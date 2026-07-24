# Flow / Positioning Proxy Status

Generated at: `2026-07-24T06:14:50.359400+00:00`
Latest date: `2026-07-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.4`
- overall_flow_conflict_score: `38.32`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.99 | 38.32 | 62.36 | 66.08 | 0.7198 | 1.2215 | 1.1392 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.7 | 38.32 | 62.27 | 66.08 | 0.6426 | 1.2096 | 1.1266 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.7 | 38.32 | 62.92 | 66.08 | 1.0048 | 1.2542 | 1.2442 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.21 | 38.32 | 62.44 | 66.08 | 0.7219 | 1.2846 | 1.1589 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
