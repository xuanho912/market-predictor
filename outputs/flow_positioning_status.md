# Flow / Positioning Proxy Status

Generated at: `2026-10-09T18:23:57.474412+00:00`
Latest date: `2026-10-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.92`
- overall_flow_conflict_score: `35.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.14 | 35.93 | 77.31 | 53.4 | -2.7618 | 0.3115 | 0.2693 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.14 | 35.93 | 77.31 | 53.4 | -2.3737 | 0.3959 | 0.3733 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.26 | 35.93 | 75.71 | 53.4 | -2.493 | 0.4519 | 0.4743 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.14 | 35.93 | 77.31 | 53.4 | -1.8871 | 0.438 | 0.472 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
