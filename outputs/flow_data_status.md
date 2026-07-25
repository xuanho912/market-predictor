# Flow / Positioning Proxy Status

Generated at: `2026-07-25T04:32:14.178633+00:00`
Latest date: `2026-07-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.19`
- overall_flow_conflict_score: `51.97`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.73 | 51.97 | 64.56 | 89.61 | 0.7262 | 1.223 | 1.1406 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.58 | 51.97 | 64.51 | 89.61 | 0.6797 | 1.2188 | 1.1352 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.44 | 51.97 | 65.12 | 89.61 | 1.0106 | 1.2558 | 1.2458 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.0 | 51.97 | 64.65 | 89.61 | 0.7392 | 1.2893 | 1.163 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
