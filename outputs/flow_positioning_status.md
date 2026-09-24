# Flow / Positioning Proxy Status

Generated at: `2026-09-24T17:16:48.723335+00:00`
Latest date: `2026-09-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.31`
- overall_flow_conflict_score: `33.86`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.27 | 33.86 | 83.47 | 52.27 | -2.2521 | 0.3721 | 0.4429 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.27 | 33.86 | 83.47 | 52.27 | -2.1629 | 0.4111 | 0.518 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.33 | 33.86 | 82.51 | 52.27 | -1.2187 | 0.6556 | 0.7436 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.39 | 33.86 | 81.87 | 52.27 | -1.574 | 0.3993 | 0.4803 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
