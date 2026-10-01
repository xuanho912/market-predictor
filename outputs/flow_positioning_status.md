# Flow / Positioning Proxy Status

Generated at: `2026-10-01T07:14:30.421562+00:00`
Latest date: `2026-09-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.64`
- overall_flow_conflict_score: `34.89`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.54 | 34.89 | 97.84 | 50.54 | 1.7734 | 1.4379 | 1.408 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.34 | 34.89 | 95.8 | 50.54 | -0.4959 | 0.9197 | 0.8915 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.54 | 34.89 | 95.87 | 50.54 | -0.4771 | 0.8729 | 0.9097 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.13 | 34.89 | 95.41 | 50.54 | -0.8191 | 0.9114 | 0.7812 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
