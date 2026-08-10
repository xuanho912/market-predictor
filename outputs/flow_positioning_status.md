# Flow / Positioning Proxy Status

Generated at: `2026-08-10T23:24:15.417640+00:00`
Latest date: `2026-08-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.09`
- overall_flow_conflict_score: `19.97`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.62 | 19.97 | 77.98 | 34.43 | -1.4116 | 0.6248 | 0.6428 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.97 | 19.97 | 77.77 | 34.43 | -1.4071 | 0.6035 | 0.5835 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.65 | 19.97 | 78.32 | 34.43 | -1.2238 | 0.8313 | 0.7371 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 67.13 | 19.97 | 78.48 | 34.43 | -0.6877 | 0.6977 | 0.7808 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
