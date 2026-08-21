# Flow / Positioning Proxy Status

Generated at: `2026-08-21T23:11:57.047339+00:00`
Latest date: `2026-08-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `74.69`
- overall_flow_conflict_score: `19.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 73.82 | 19.44 | 100.0 | 33.52 | -0.6219 | 0.9869 | 0.8301 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 73.81 | 19.44 | 100.0 | 33.52 | -0.5211 | 0.9821 | 0.8287 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 77.72 | 19.44 | 100.0 | 33.52 | 0.5945 | 1.3449 | 1.1572 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.43 | 19.44 | 100.0 | 33.52 | -0.5542 | 1.0094 | 0.7862 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
