# Flow / Positioning Proxy Status

Generated at: `2026-07-29T04:33:55.339247+00:00`
Latest date: `2026-07-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.6`
- overall_flow_conflict_score: `53.73`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.18 | 53.73 | 66.75 | 92.65 | 0.1223 | 1.1237 | 1.0079 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.86 | 53.73 | 68.28 | 92.65 | 1.5453 | 1.3558 | 1.3414 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.63 | 53.73 | 66.57 | 92.65 | -0.0666 | 0.9785 | 0.9788 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 67.74 | 53.73 | 69.88 | 92.65 | 2.4595 | 1.4755 | 1.4402 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
