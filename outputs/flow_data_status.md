# Flow / Positioning Proxy Status

Generated at: `2026-07-30T21:40:14.394924+00:00`
Latest date: `2026-07-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.07`
- overall_flow_conflict_score: `45.22`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.17 | 45.22 | 66.37 | 77.96 | 1.8224 | 1.2689 | 1.4088 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.29 | 45.22 | 64.77 | 77.96 | 2.3039 | 1.3643 | 1.6718 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.96 | 45.22 | 65.0 | 77.96 | 0.183 | 0.9103 | 1.0404 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.86 | 45.22 | 63.98 | 77.96 | -0.7091 | 0.6266 | 0.7898 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
