# Flow / Positioning Proxy Status

Generated at: `2026-10-05T20:42:37.799826+00:00`
Latest date: `2026-10-05`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.23`
- overall_flow_conflict_score: `38.02`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.08 | 38.02 | 92.9 | 53.17 | -0.465 | 0.9021 | 0.9237 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.04 | 38.02 | 92.23 | 53.17 | -1.2879 | 0.7402 | 0.7379 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.92 | 38.02 | 92.84 | 53.17 | -0.6371 | 0.841 | 0.9088 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.89 | 38.02 | 91.19 | 53.17 | -0.4761 | 0.956 | 0.8956 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
