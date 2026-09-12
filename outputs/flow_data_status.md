# Flow / Positioning Proxy Status

Generated at: `2026-09-12T05:51:45.303212+00:00`
Latest date: `2026-09-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `43.73`
- overall_flow_conflict_score: `34.35`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.09 | 34.35 | 54.83 | 49.97 | 1.4024 | 1.1491 | 1.2331 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 39.56 | 34.35 | 52.69 | 49.97 | -0.649 | 0.8935 | 0.8611 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 46.09 | 34.35 | 54.83 | 49.97 | 1.7978 | 1.4 | 1.5006 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 43.2 | 34.35 | 53.88 | 49.97 | 0.3625 | 0.89 | 1.1287 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
