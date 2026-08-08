# Flow / Positioning Proxy Status

Generated at: `2026-08-08T04:41:19.563167+00:00`
Latest date: `2026-08-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.45`
- overall_flow_conflict_score: `22.0`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.74 | 22.0 | 67.69 | 37.93 | -0.5323 | 0.793 | 0.8773 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.29 | 22.0 | 67.22 | 37.93 | -0.9514 | 0.6992 | 0.7453 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.45 | 22.0 | 67.6 | 37.93 | -0.7638 | 0.8648 | 0.8508 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.33 | 22.0 | 66.57 | 37.93 | -1.3353 | 0.4637 | 0.5514 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
