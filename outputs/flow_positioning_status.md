# Flow / Positioning Proxy Status

Generated at: `2026-11-20T01:54:57.566767+00:00`
Latest date: `2026-11-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.33`
- overall_flow_conflict_score: `64.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 47.48 | 64.66 | 62.46 | 96.33 | 0.0234 | 1.0111 | 1.0301 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.85 | 64.66 | 61.93 | 96.33 | -0.2769 | 1.0101 | 0.8865 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 46.5 | 64.66 | 62.14 | 96.33 | -0.2133 | 0.9979 | 0.9455 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.49 | 64.66 | 63.12 | 96.33 | 0.2679 | 1.4905 | 1.1697 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
