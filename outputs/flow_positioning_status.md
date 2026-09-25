# Flow / Positioning Proxy Status

Generated at: `2026-09-25T01:06:14.450873+00:00`
Latest date: `2026-09-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.13`
- overall_flow_conflict_score: `33.59`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.37 | 33.59 | 89.85 | 51.8 | 1.2724 | 1.0582 | 1.3235 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.87 | 33.59 | 88.37 | 51.8 | 0.0791 | 0.7967 | 1.0313 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.25 | 33.59 | 87.51 | 51.8 | 0.5361 | 0.97 | 1.156 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.02 | 33.59 | 88.09 | 51.8 | 0.8694 | 1.1048 | 1.2582 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
