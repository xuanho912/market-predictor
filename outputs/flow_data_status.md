# Flow / Positioning Proxy Status

Generated at: `2026-09-10T01:03:12.760898+00:00`
Latest date: `2026-09-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.81`
- overall_flow_conflict_score: `32.81`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.69 | 32.81 | 59.93 | 46.11 | 1.5374 | 1.1958 | 1.2319 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.81 | 32.81 | 58.0 | 46.11 | -0.4182 | 0.9246 | 0.9204 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 47.39 | 32.81 | 58.52 | 46.11 | 0.1547 | 0.8964 | 1.0367 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 46.35 | 32.81 | 58.18 | 46.11 | 0.9007 | 1.2003 | 1.2539 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
