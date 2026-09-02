# Flow / Positioning Proxy Status

Generated at: `2026-09-02T08:09:38.652191+00:00`
Latest date: `2026-09-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.43`
- overall_flow_conflict_score: `22.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.26 | 22.93 | 64.81 | 37.72 | 0.7475 | 1.2345 | 1.0608 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.22 | 22.93 | 64.8 | 37.72 | 0.6334 | 1.2612 | 1.0777 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.13 | 22.93 | 65.76 | 37.72 | 1.7484 | 1.5693 | 1.3562 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 51.12 | 22.93 | 64.11 | 37.72 | 0.0306 | 1.2231 | 0.9936 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
