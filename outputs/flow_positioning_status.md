# Flow / Positioning Proxy Status

Generated at: `2026-08-03T15:20:29.073146+00:00`
Latest date: `2026-08-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.9`
- overall_flow_conflict_score: `33.26`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 54.64 | 33.26 | 61.76 | 57.35 | -2.3037 | 0.3181 | 0.3825 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.64 | 33.26 | 61.76 | 57.35 | -1.955 | 0.2963 | 0.3963 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.64 | 33.26 | 61.76 | 57.35 | -2.1865 | 0.3936 | 0.4515 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.68 | 33.26 | 62.1 | 57.35 | -1.124 | 0.5362 | 0.6612 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
