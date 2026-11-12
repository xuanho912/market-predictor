# Flow / Positioning Proxy Status

Generated at: `2026-11-12T03:28:27.749032+00:00`
Latest date: `2026-11-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.72`
- overall_flow_conflict_score: `62.88`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.08 | 62.88 | 83.97 | 95.07 | -0.4374 | 0.5748 | 0.7875 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.86 | 62.88 | 84.22 | 95.07 | -0.2868 | 0.6195 | 0.8585 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.93 | 62.88 | 83.59 | 95.07 | -0.8687 | 0.5441 | 0.6831 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.0 | 62.88 | 83.61 | 95.07 | -0.5751 | 0.4685 | 0.6895 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
