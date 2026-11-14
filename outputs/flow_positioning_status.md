# Flow / Positioning Proxy Status

Generated at: `2026-11-14T00:58:10.949917+00:00`
Latest date: `2026-11-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.31`
- overall_flow_conflict_score: `55.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.81 | 55.63 | 79.46 | 85.09 | -0.4389 | 0.8217 | 0.7722 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.29 | 55.63 | 79.61 | 85.09 | -0.3351 | 0.8368 | 0.8155 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.31 | 55.63 | 79.3 | 85.09 | -0.7418 | 0.7564 | 0.7269 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.83 | 55.63 | 78.81 | 85.09 | -0.6677 | 0.7315 | 0.5916 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
