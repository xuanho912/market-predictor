# Flow / Positioning Proxy Status

Generated at: `2026-08-28T05:38:28.996451+00:00`
Latest date: `2026-08-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `76.25`
- overall_flow_conflict_score: `20.73`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 76.49 | 20.73 | 100.0 | 35.74 | -0.6007 | 0.9954 | 0.8089 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 76.38 | 20.73 | 100.0 | 35.74 | -0.558 | 0.9639 | 0.7958 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.2 | 20.73 | 100.0 | 35.74 | -0.8342 | 0.8265 | 0.7761 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.92 | 20.73 | 100.0 | 35.74 | -0.6951 | 0.8507 | 0.7446 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
