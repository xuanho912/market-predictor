# Flow / Positioning Proxy Status

Generated at: `2026-09-11T23:33:28.095565+00:00`
Latest date: `2026-09-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `43.47`
- overall_flow_conflict_score: `34.35`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.09 | 34.35 | 54.83 | 49.97 | 1.3465 | 1.1396 | 1.2229 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 39.41 | 34.35 | 52.64 | 49.97 | -0.7117 | 0.8794 | 0.8475 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 46.09 | 34.35 | 54.83 | 49.97 | 1.7872 | 1.3967 | 1.4971 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 42.3 | 34.35 | 53.58 | 49.97 | 0.192 | 0.8487 | 1.0762 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
