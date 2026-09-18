# Flow / Positioning Proxy Status

Generated at: `2026-09-18T01:16:18.552215+00:00`
Latest date: `2026-09-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `49.87`
- overall_flow_conflict_score: `33.86`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.63 | 33.86 | 58.86 | 52.27 | 2.6769 | 1.4016 | 1.5343 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.34 | 33.86 | 58.44 | 52.27 | 1.1002 | 1.2165 | 1.1431 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 47.75 | 33.86 | 57.26 | 52.27 | 1.519 | 1.1138 | 1.4281 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.75 | 33.86 | 57.26 | 52.27 | 2.3965 | 1.5871 | 1.79 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
