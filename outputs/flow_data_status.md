# Flow / Positioning Proxy Status

Generated at: `2026-06-26T05:40:49.928679+00:00`
Latest date: `2026-06-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.88`
- overall_flow_conflict_score: `31.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 62.85 | 31.83 | 86.87 | 44.37 | -0.4371 | 0.7985 | 0.8878 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.78 | 31.83 | 87.18 | 44.37 | -0.1193 | 0.9887 | 0.9729 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.27 | 31.83 | 88.65 | 44.37 | -0.2975 | 0.9159 | 0.9368 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.61 | 31.83 | 88.76 | 44.37 | -0.2089 | 0.9024 | 0.9675 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
