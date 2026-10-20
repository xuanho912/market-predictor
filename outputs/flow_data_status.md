# Flow / Positioning Proxy Status

Generated at: `2026-10-20T06:05:57.373298+00:00`
Latest date: `2026-10-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.39`
- overall_flow_conflict_score: `60.54`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.81 | 60.54 | 57.18 | 96.41 | -0.2354 | 0.9285 | 0.9198 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.24 | 60.54 | 57.65 | 96.41 | 0.1296 | 0.8286 | 1.0272 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.92 | 60.54 | 56.56 | 96.41 | -1.1245 | 0.6569 | 0.7478 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.58 | 60.54 | 58.09 | 96.41 | -1.1579 | 0.6528 | 0.7278 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
