# Flow / Positioning Proxy Status

Generated at: `2026-11-20T20:25:08.572187+00:00`
Latest date: `2026-11-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.19`
- overall_flow_conflict_score: `73.6`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.25 | 73.6 | 67.56 | 100.0 | 1.4331 | 1.4509 | 1.7055 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.25 | 73.6 | 67.56 | 100.0 | 1.7464 | 1.9173 | 1.9059 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.25 | 73.6 | 67.56 | 100.0 | 1.7745 | 1.599 | 1.6563 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 48.99 | 73.6 | 66.17 | 100.0 | 0.0769 | 1.0607 | 1.0539 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
