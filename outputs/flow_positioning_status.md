# Flow / Positioning Proxy Status

Generated at: `2026-09-05T05:48:40.254116+00:00`
Latest date: `2026-09-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.3`
- overall_flow_conflict_score: `24.12`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.58 | 24.12 | 61.88 | 38.61 | -0.4606 | 0.8962 | 0.9243 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.79 | 24.12 | 62.6 | 38.61 | 0.3237 | 1.061 | 1.0678 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.48 | 24.12 | 61.51 | 38.61 | -0.7661 | 0.6853 | 0.8235 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 45.34 | 24.12 | 59.83 | 38.61 | -0.7327 | 0.7484 | 0.8003 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
