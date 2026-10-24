# Flow / Positioning Proxy Status

Generated at: `2026-10-24T08:26:05.664734+00:00`
Latest date: `2026-10-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.96`
- overall_flow_conflict_score: `68.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.31 | 68.18 | 65.69 | 100.0 | -0.6028 | 0.7445 | 0.819 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.32 | 68.18 | 65.7 | 100.0 | -0.5126 | 0.6504 | 0.8197 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.07 | 68.18 | 67.25 | 100.0 | -0.7659 | 0.8542 | 0.8076 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.13 | 68.18 | 67.6 | 100.0 | -0.4282 | 0.8949 | 0.9042 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
