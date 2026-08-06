# Flow / Positioning Proxy Status

Generated at: `2026-08-06T14:37:26.210225+00:00`
Latest date: `2026-08-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.67`
- overall_flow_conflict_score: `23.45`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.67 | 23.45 | 65.38 | 40.43 | -2.8171 | 0.1028 | 0.1251 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.67 | 23.45 | 65.38 | 40.43 | -2.1967 | 0.2215 | 0.2715 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.67 | 23.45 | 65.38 | 40.43 | -2.9243 | 0.1715 | 0.178 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.67 | 23.45 | 65.38 | 40.43 | -2.0008 | 0.2322 | 0.2732 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
