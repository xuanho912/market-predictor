# Flow / Positioning Proxy Status

Generated at: `2026-11-04T02:48:06.374467+00:00`
Latest date: `2026-11-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.82`
- overall_flow_conflict_score: `69.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.6 | 69.94 | 77.05 | 100.0 | -0.4762 | 0.7147 | 0.823 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.31 | 69.94 | 77.29 | 100.0 | -0.3087 | 0.7537 | 0.8882 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.47 | 69.94 | 76.68 | 100.0 | -0.9823 | 0.808 | 0.7201 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.89 | 69.94 | 77.48 | 100.0 | -0.2672 | 0.9365 | 0.9406 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
