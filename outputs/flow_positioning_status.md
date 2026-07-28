# Flow / Positioning Proxy Status

Generated at: `2026-07-28T14:40:46.238659+00:00`
Latest date: `2026-07-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.04`
- overall_flow_conflict_score: `57.42`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.82 | 57.42 | 67.47 | 99.0 | -3.0975 | 0.2639 | 0.2367 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.82 | 57.42 | 67.47 | 99.0 | -2.1075 | 0.4839 | 0.4785 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.82 | 57.42 | 67.47 | 99.0 | -3.1818 | 0.2122 | 0.2123 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.7 | 57.42 | 69.07 | 99.0 | -2.4257 | 0.5181 | 0.5054 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
