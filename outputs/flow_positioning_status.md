# Flow / Positioning Proxy Status

Generated at: `2026-06-22T16:01:34.403640+00:00`
Latest date: `2026-06-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.82`
- overall_flow_conflict_score: `20.62`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.82 | 20.62 | 100.0 | 34.13 | -2.0388 | 0.2207 | 0.2649 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.82 | 20.62 | 100.0 | 34.13 | -1.496 | 0.3682 | 0.37 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 69.82 | 20.62 | 100.0 | 34.13 | -2.3 | 0.319 | 0.3335 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 69.82 | 20.62 | 100.0 | 34.13 | -2.3411 | 0.3183 | 0.3722 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
