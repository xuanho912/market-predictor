# Flow / Positioning Proxy Status

Generated at: `2026-07-16T14:26:25.739932+00:00`
Latest date: `2026-07-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.11`
- overall_flow_conflict_score: `37.28`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.55 | 37.28 | 64.7 | 63.53 | -2.6755 | 0.1773 | 0.1341 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 50.67 | 37.28 | 63.1 | 63.53 | -2.9096 | 0.2535 | 0.1917 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.67 | 37.28 | 63.1 | 63.53 | -2.3154 | 0.2641 | 0.195 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.55 | 37.28 | 64.7 | 63.53 | -2.1346 | 0.3383 | 0.25 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
