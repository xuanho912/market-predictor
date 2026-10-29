# Flow / Positioning Proxy Status

Generated at: `2026-10-29T00:17:25.564231+00:00`
Latest date: `2026-10-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.73`
- overall_flow_conflict_score: `59.4`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.56 | 59.4 | 65.37 | 92.38 | -0.8911 | 0.7686 | 0.715 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.94 | 59.4 | 67.46 | 92.38 | -0.4371 | 0.8105 | 0.8517 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.82 | 59.4 | 67.09 | 92.38 | -0.9041 | 0.9037 | 0.7497 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.6 | 59.4 | 65.71 | 92.38 | -0.8338 | 0.9429 | 0.8092 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
