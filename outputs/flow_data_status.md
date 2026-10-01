# Flow / Positioning Proxy Status

Generated at: `2026-10-01T00:49:34.394462+00:00`
Latest date: `2026-09-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.7`
- overall_flow_conflict_score: `34.89`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 62.76 | 34.89 | 95.61 | 50.54 | -0.8067 | 0.8661 | 0.838 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.41 | 34.89 | 95.5 | 50.54 | -0.9309 | 0.7757 | 0.8065 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.76 | 34.89 | 95.94 | 50.54 | -0.3979 | 0.8608 | 0.9295 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.86 | 34.89 | 95.32 | 50.54 | -0.9942 | 0.827 | 0.7564 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
