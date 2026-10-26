# Flow / Positioning Proxy Status

Generated at: `2026-10-26T18:44:00.270490+00:00`
Latest date: `2026-10-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `52.65`
- overall_flow_conflict_score: `65.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.01 | 65.01 | 63.82 | 100.0 | -1.6752 | 0.4568 | 0.4348 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 50.81 | 65.01 | 64.08 | 100.0 | -0.9356 | 0.6035 | 0.6398 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.89 | 65.01 | 65.42 | 100.0 | -1.95 | 0.5121 | 0.4336 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.89 | 65.01 | 65.42 | 100.0 | -1.9887 | 0.5668 | 0.4913 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
