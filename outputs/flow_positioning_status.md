# Flow / Positioning Proxy Status

Generated at: `2026-09-09T01:14:00.531286+00:00`
Latest date: `2026-09-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.64`
- overall_flow_conflict_score: `28.02`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 45.26 | 28.02 | 61.73 | 40.65 | -0.4606 | 0.8962 | 0.9243 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.35 | 28.02 | 64.06 | 40.65 | 0.3237 | 1.061 | 1.0678 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 49.04 | 28.02 | 62.97 | 40.65 | -0.7661 | 0.6853 | 0.8235 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 43.9 | 28.02 | 61.29 | 40.65 | -0.7327 | 0.7484 | 0.8003 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
