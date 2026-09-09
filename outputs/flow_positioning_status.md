# Flow / Positioning Proxy Status

Generated at: `2026-09-09T16:42:05.394069+00:00`
Latest date: `2026-09-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `43.27`
- overall_flow_conflict_score: `31.96`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 43.73 | 31.96 | 59.69 | 45.16 | -3.0002 | 0.3505 | 0.3696 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 43.73 | 31.96 | 59.69 | 45.16 | -2.1312 | 0.512 | 0.4948 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.7 | 31.96 | 60.0 | 45.16 | -1.4687 | 0.5895 | 0.6545 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 40.94 | 31.96 | 58.77 | 45.16 | -0.8271 | 0.6464 | 0.7567 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
