# Flow / Positioning Proxy Status

Generated at: `2026-10-19T23:51:03.472513+00:00`
Latest date: `2026-10-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.17`
- overall_flow_conflict_score: `60.54`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.76 | 60.54 | 57.16 | 96.41 | -0.252 | 0.9249 | 0.915 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.19 | 60.54 | 57.63 | 96.41 | 0.12 | 0.8266 | 1.0239 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.9 | 60.54 | 56.56 | 96.41 | -1.1319 | 0.6553 | 0.7459 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 48.82 | 60.54 | 57.84 | 96.41 | -1.419 | 0.5906 | 0.6585 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
