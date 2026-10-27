# Flow / Positioning Proxy Status

Generated at: `2026-10-27T00:51:24.742237+00:00`
Latest date: `2026-10-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.5`
- overall_flow_conflict_score: `65.62`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.85 | 65.62 | 64.86 | 100.0 | -0.6028 | 0.7445 | 0.819 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.86 | 65.62 | 64.86 | 100.0 | -0.5126 | 0.6504 | 0.8197 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.61 | 65.62 | 66.42 | 100.0 | -0.7659 | 0.8542 | 0.8076 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.67 | 65.62 | 66.77 | 100.0 | -0.4282 | 0.8949 | 0.9042 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
