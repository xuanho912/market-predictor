# Flow / Positioning Proxy Status

Generated at: `2026-07-17T06:06:23.478428+00:00`
Latest date: `2026-07-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.09`
- overall_flow_conflict_score: `43.58`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.56 | 43.58 | 66.79 | 73.08 | -0.5532 | 1.1205 | 0.8475 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.49 | 43.58 | 67.09 | 73.08 | -0.3117 | 1.2313 | 0.9315 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.22 | 43.58 | 67.33 | 73.08 | -0.0069 | 1.3518 | 0.9985 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.09 | 43.58 | 67.94 | 73.08 | -0.8727 | 0.9791 | 0.7238 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
