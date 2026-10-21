# Flow / Positioning Proxy Status

Generated at: `2026-10-21T06:05:46.895009+00:00`
Latest date: `2026-10-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.49`
- overall_flow_conflict_score: `62.76`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.06 | 62.76 | 60.05 | 100.0 | -0.5505 | 0.7658 | 0.8435 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.16 | 62.76 | 60.08 | 100.0 | -0.4186 | 0.644 | 0.8527 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.93 | 62.76 | 60.66 | 100.0 | 0.03 | 0.8702 | 1.0081 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.81 | 62.76 | 62.59 | 100.0 | 0.2482 | 0.9639 | 1.0607 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
