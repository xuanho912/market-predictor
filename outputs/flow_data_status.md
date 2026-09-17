# Flow / Positioning Proxy Status

Generated at: `2026-09-17T17:02:53.611853+00:00`
Latest date: `2026-09-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `41.79`
- overall_flow_conflict_score: `32.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 43.71 | 32.66 | 56.66 | 50.2 | -2.2002 | 0.4107 | 0.4956 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 43.71 | 32.66 | 56.66 | 50.2 | -2.3933 | 0.539 | 0.548 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 38.83 | 32.66 | 55.06 | 50.2 | -1.6739 | 0.3958 | 0.5292 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 40.91 | 32.66 | 55.74 | 50.2 | -0.7535 | 0.6252 | 0.7564 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
