# Flow / Positioning Proxy Status

Generated at: `2026-09-03T05:52:31.413672+00:00`
Latest date: `2026-09-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `46.88`
- overall_flow_conflict_score: `25.43`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.55 | 25.43 | 54.89 | 43.65 | -1.4122 | 0.8186 | 0.79 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 44.06 | 25.43 | 54.73 | 43.65 | -1.2139 | 0.7759 | 0.7451 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.86 | 25.43 | 57.28 | 43.65 | 1.5575 | 1.3563 | 1.334 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.04 | 25.43 | 55.7 | 43.65 | 0.1623 | 1.3379 | 0.9879 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
