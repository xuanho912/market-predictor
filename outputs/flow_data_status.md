# Flow / Positioning Proxy Status

Generated at: `2026-10-28T18:23:35.097629+00:00`
Latest date: `2026-10-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.23`
- overall_flow_conflict_score: `64.21`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.01 | 64.21 | 64.98 | 99.83 | -1.994 | 0.3328 | 0.302 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.01 | 64.21 | 64.98 | 99.83 | -1.6035 | 0.3621 | 0.379 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.89 | 64.21 | 66.58 | 99.83 | -1.8463 | 0.5541 | 0.4285 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.01 | 64.21 | 64.98 | 99.83 | -2.2544 | 0.4767 | 0.3826 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
