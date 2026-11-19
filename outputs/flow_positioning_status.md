# Flow / Positioning Proxy Status

Generated at: `2026-11-19T01:59:21.458181+00:00`
Latest date: `2026-11-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.09`
- overall_flow_conflict_score: `68.36`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.28 | 68.36 | 74.72 | 100.0 | 0.942 | 1.5902 | 1.4782 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.0 | 68.36 | 73.64 | 100.0 | 0.2029 | 1.3478 | 1.1213 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.09 | 68.36 | 74.33 | 100.0 | 0.6725 | 1.3818 | 1.2282 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.0 | 68.36 | 73.31 | 100.0 | 0.0853 | 1.4086 | 1.051 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
