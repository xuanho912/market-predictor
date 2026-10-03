# Flow / Positioning Proxy Status

Generated at: `2026-10-03T09:27:28.952663+00:00`
Latest date: `2026-10-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.28`
- overall_flow_conflict_score: `37.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.11 | 37.01 | 97.41 | 51.44 | 0.0294 | 1.0241 | 1.0087 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.3 | 37.01 | 99.11 | 51.44 | 0.0939 | 1.0466 | 1.0251 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.96 | 37.01 | 99.0 | 51.44 | 1.1559 | 1.1984 | 1.2583 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.77 | 37.01 | 98.28 | 51.44 | 0.6272 | 1.3349 | 1.1443 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
