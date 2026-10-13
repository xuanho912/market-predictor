# Flow / Positioning Proxy Status

Generated at: `2026-10-13T19:21:10.403061+00:00`
Latest date: `2026-10-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.64`
- overall_flow_conflict_score: `30.87`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.51 | 30.87 | 78.76 | 49.56 | -1.9801 | 0.5349 | 0.3655 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.41 | 30.87 | 79.05 | 49.56 | -1.3638 | 0.7354 | 0.6491 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.29 | 30.87 | 80.0 | 49.56 | -0.4259 | 0.9609 | 0.9112 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.34 | 30.87 | 81.32 | 49.56 | -0.6472 | 0.8405 | 0.8354 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
