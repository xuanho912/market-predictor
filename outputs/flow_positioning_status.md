# Flow / Positioning Proxy Status

Generated at: `2026-07-07T15:17:42.701297+00:00`
Latest date: `2026-07-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.59`
- overall_flow_conflict_score: `36.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.03 | 36.83 | 74.7 | 54.9 | -2.8183 | 0.255 | 0.212 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.15 | 36.83 | 73.1 | 54.9 | -2.2008 | 0.4283 | 0.3325 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.15 | 36.83 | 73.1 | 54.9 | -2.395 | 0.3272 | 0.2388 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.03 | 36.83 | 74.7 | 54.9 | -1.8706 | 0.5975 | 0.4395 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
