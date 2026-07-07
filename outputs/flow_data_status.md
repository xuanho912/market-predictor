# Flow / Positioning Proxy Status

Generated at: `2026-07-07T23:44:24.657453+00:00`
Latest date: `2026-07-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.46`
- overall_flow_conflict_score: `30.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 62.22 | 30.18 | 74.76 | 46.24 | -1.4499 | 0.7917 | 0.6583 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.66 | 30.18 | 73.59 | 46.24 | -0.7148 | 1.0021 | 0.7786 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.72 | 30.18 | 72.96 | 46.24 | -1.4001 | 0.8252 | 0.6023 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.25 | 30.18 | 75.43 | 46.24 | -0.5402 | 1.1458 | 0.8433 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
