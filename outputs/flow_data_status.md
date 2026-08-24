# Flow / Positioning Proxy Status

Generated at: `2026-08-24T20:57:34.488977+00:00`
Latest date: `2026-08-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `68.92`
- overall_flow_conflict_score: `20.84`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.0 | 20.84 | 89.58 | 35.93 | -1.1008 | 0.7854 | 0.6908 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.2 | 20.84 | 90.31 | 35.93 | -0.3214 | 0.9877 | 0.8911 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.66 | 20.84 | 89.47 | 35.93 | -1.2271 | 0.6909 | 0.6594 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 72.82 | 20.84 | 91.49 | 35.93 | 0.3746 | 1.3855 | 1.154 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
