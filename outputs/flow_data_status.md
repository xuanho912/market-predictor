# Flow / Positioning Proxy Status

Generated at: `2026-10-12T21:19:37.061512+00:00`
Latest date: `2026-10-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.33`
- overall_flow_conflict_score: `37.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.45 | 37.66 | 78.58 | 55.02 | -2.1312 | 0.5258 | 0.4105 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.35 | 37.66 | 77.56 | 55.02 | -1.0631 | 0.8349 | 0.729 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.56 | 37.66 | 77.3 | 55.02 | -1.6913 | 0.6716 | 0.6569 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.96 | 37.66 | 79.4 | 55.02 | -0.831 | 0.7834 | 0.7955 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
