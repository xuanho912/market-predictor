# Flow / Positioning Proxy Status

Generated at: `2026-08-26T02:42:03.005648+00:00`
Latest date: `2026-08-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `71.45`
- overall_flow_conflict_score: `20.57`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.97 | 20.57 | 100.0 | 35.46 | -1.3465 | 0.6712 | 0.5909 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.03 | 20.57 | 100.0 | 35.46 | -1.1673 | 0.6203 | 0.5984 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.54 | 20.57 | 100.0 | 35.46 | -0.805 | 0.803 | 0.7655 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 74.27 | 20.57 | 100.0 | 35.46 | -0.9086 | 0.6786 | 0.625 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
