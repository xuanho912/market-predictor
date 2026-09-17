# Flow / Positioning Proxy Status

Generated at: `2026-09-17T00:58:21.865916+00:00`
Latest date: `2026-09-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `41.39`
- overall_flow_conflict_score: `39.74`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.07 | 39.74 | 53.59 | 56.68 | 1.2706 | 1.1009 | 1.2155 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 37.62 | 39.74 | 51.47 | 56.68 | -0.7544 | 0.8974 | 0.8533 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.23 | 39.74 | 53.64 | 56.68 | 1.2386 | 1.0912 | 1.3466 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 39.63 | 39.74 | 52.13 | 56.68 | 0.0626 | 0.8811 | 1.0259 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
