# Flow / Positioning Proxy Status

Generated at: `2026-10-07T18:59:24.439787+00:00`
Latest date: `2026-10-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.09`
- overall_flow_conflict_score: `40.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.58 | 40.44 | 87.42 | 58.07 | -2.57 | 0.4102 | 0.4213 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 61.58 | 40.44 | 87.42 | 58.07 | -2.0172 | 0.6014 | 0.5475 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.01 | 40.44 | 87.88 | 58.07 | -1.8941 | 0.6721 | 0.6968 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.17 | 40.44 | 88.92 | 58.07 | -0.0393 | 0.986 | 0.9848 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
