# Flow / Positioning Proxy Status

Generated at: `2026-08-27T22:19:19.190362+00:00`
Latest date: `2026-08-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `76.14`
- overall_flow_conflict_score: `20.73`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 76.39 | 20.73 | 100.0 | 35.74 | -0.6421 | 0.9814 | 0.7975 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 76.33 | 20.73 | 100.0 | 35.74 | -0.5757 | 0.9577 | 0.7907 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 76.19 | 20.73 | 100.0 | 35.74 | -0.8382 | 0.8254 | 0.7751 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.64 | 20.73 | 100.0 | 35.74 | -0.7741 | 0.8163 | 0.7145 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
