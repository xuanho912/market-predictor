# Flow / Positioning Proxy Status

Generated at: `2026-07-09T07:06:00.260740+00:00`
Latest date: `2026-07-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.59`
- overall_flow_conflict_score: `39.87`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.08 | 39.87 | 65.98 | 60.01 | -1.3273 | 0.858 | 0.7027 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.0 | 39.87 | 65.96 | 60.01 | -1.1454 | 0.8571 | 0.695 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.48 | 39.87 | 66.44 | 60.01 | -0.6044 | 1.1759 | 0.8294 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.79 | 39.87 | 67.53 | 60.01 | -1.1306 | 0.9764 | 0.6866 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
