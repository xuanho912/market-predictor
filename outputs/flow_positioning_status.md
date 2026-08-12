# Flow / Positioning Proxy Status

Generated at: `2026-08-12T13:49:54.366749+00:00`
Latest date: `2026-08-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.28`
- overall_flow_conflict_score: `18.95`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.5 | 18.95 | 70.19 | 32.67 | -2.8508 | 0.0976 | 0.0798 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.5 | 18.95 | 70.19 | 32.67 | -2.4594 | 0.1688 | 0.125 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.5 | 18.95 | 70.19 | 32.67 | -2.8826 | 0.1607 | 0.1255 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.62 | 18.95 | 68.59 | 32.67 | -2.22 | 0.1378 | 0.1211 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
