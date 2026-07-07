# Flow / Positioning Proxy Status

Generated at: `2026-07-07T00:18:54.246107+00:00`
Latest date: `2026-07-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.97`
- overall_flow_conflict_score: `45.99`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.82 | 45.99 | 70.94 | 69.85 | -1.4591 | 0.7361 | 0.6587 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.81 | 45.99 | 70.61 | 69.85 | -1.4888 | 0.6511 | 0.5413 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.43 | 45.99 | 69.17 | 69.85 | -1.506 | 0.7076 | 0.6118 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.81 | 45.99 | 70.61 | 69.85 | -1.6782 | 0.7375 | 0.5429 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
