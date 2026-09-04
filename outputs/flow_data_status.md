# Flow / Positioning Proxy Status

Generated at: `2026-09-04T16:25:16.353792+00:00`
Latest date: `2026-09-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.8`
- overall_flow_conflict_score: `24.55`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.02 | 24.55 | 58.01 | 39.16 | -3.0804 | 0.3595 | 0.3707 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 46.02 | 24.55 | 58.01 | 39.16 | -1.9817 | 0.5267 | 0.5299 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 46.02 | 24.55 | 58.01 | 39.16 | -2.2134 | 0.356 | 0.4277 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 41.14 | 24.55 | 56.41 | 39.16 | -1.6862 | 0.459 | 0.4909 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
