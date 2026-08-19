# Flow / Positioning Proxy Status

Generated at: `2026-08-19T13:11:19.559499+00:00`
Latest date: `2026-08-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.48`
- overall_flow_conflict_score: `20.47`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.23 | 20.47 | 71.41 | 35.29 | -0.2198 | 1.2798 | 0.9505 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.87 | 20.47 | 72.93 | 35.29 | 0.7086 | 1.7382 | 1.2468 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.93 | 20.47 | 71.31 | 35.29 | -0.2994 | 1.2489 | 0.9232 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.91 | 20.47 | 71.64 | 35.29 | 0.0095 | 1.4935 | 1.0111 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
