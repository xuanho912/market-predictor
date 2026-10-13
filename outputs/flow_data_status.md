# Flow / Positioning Proxy Status

Generated at: `2026-10-13T11:07:47.163615+00:00`
Latest date: `2026-10-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.52`
- overall_flow_conflict_score: `37.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.45 | 37.66 | 78.58 | 55.02 | -2.1165 | 0.5328 | 0.4161 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.4 | 37.66 | 77.58 | 55.02 | -1.0468 | 0.8399 | 0.7335 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.61 | 37.66 | 77.32 | 55.02 | -1.6714 | 0.6765 | 0.6617 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.61 | 37.66 | 79.61 | 55.02 | -0.6077 | 0.8418 | 0.8547 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
