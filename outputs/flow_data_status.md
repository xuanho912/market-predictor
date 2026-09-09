# Flow / Positioning Proxy Status

Generated at: `2026-09-09T22:41:29.585148+00:00`
Latest date: `2026-09-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `46.51`
- overall_flow_conflict_score: `32.81`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 45.38 | 32.81 | 57.86 | 46.11 | -0.7657 | 0.8354 | 0.8812 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.09 | 32.81 | 57.76 | 46.11 | -0.7035 | 0.8839 | 0.8546 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 49.28 | 32.81 | 59.14 | 46.11 | 0.5684 | 1.022 | 1.1348 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 46.3 | 32.81 | 58.16 | 46.11 | 0.8593 | 1.0733 | 1.2565 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
