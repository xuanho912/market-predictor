# Flow / Positioning Proxy Status

Generated at: `2026-10-15T17:04:42.749796+00:00`
Latest date: `2026-10-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `42.03`
- overall_flow_conflict_score: `49.98`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 39.3 | 49.98 | 51.78 | 75.21 | -1.4982 | 0.6686 | 0.5149 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 42.63 | 49.98 | 52.87 | 75.21 | -0.4589 | 0.8501 | 0.8697 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 41.69 | 49.98 | 52.57 | 75.21 | -0.9435 | 0.7303 | 0.7844 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 44.49 | 49.98 | 53.48 | 75.21 | -1.8034 | 0.5883 | 0.5947 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
