# Flow / Positioning Proxy Status

Generated at: `2026-11-10T19:46:52.605549+00:00`
Latest date: `2026-11-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.26`
- overall_flow_conflict_score: `71.82`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.61 | 71.82 | 81.93 | 100.0 | -1.0573 | 0.3738 | 0.5079 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.61 | 71.82 | 81.93 | 100.0 | -0.9556 | 0.389 | 0.5423 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.94 | 71.82 | 83.68 | 100.0 | -1.0967 | 0.5033 | 0.6084 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.87 | 71.82 | 83.65 | 100.0 | -0.7489 | 0.409 | 0.6012 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
