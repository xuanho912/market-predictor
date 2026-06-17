# Flow / Positioning Proxy Status

Generated at: `2026-06-17T00:01:18.125533+00:00`
Latest date: `2026-06-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `77.25`
- overall_flow_conflict_score: `26.72`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 79.62 | 26.72 | 100.0 | 38.67 | 0.3928 | 0.8719 | 1.131 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 77.18 | 26.72 | 100.0 | 38.67 | -0.1635 | 0.6837 | 0.9297 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.01 | 26.72 | 100.0 | 38.67 | -0.8741 | 0.6456 | 0.7997 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 76.18 | 26.72 | 100.0 | 38.67 | -0.8201 | 0.71 | 0.8192 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
