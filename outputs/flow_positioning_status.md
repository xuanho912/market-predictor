# Flow / Positioning Proxy Status

Generated at: `2026-07-08T04:36:08.986023+00:00`
Latest date: `2026-07-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.54`
- overall_flow_conflict_score: `30.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 62.39 | 30.18 | 74.82 | 46.24 | -1.3851 | 0.8108 | 0.6741 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.71 | 30.18 | 73.61 | 46.24 | -0.6962 | 1.0082 | 0.7833 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.78 | 30.18 | 72.98 | 46.24 | -1.3845 | 0.8318 | 0.6071 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.27 | 30.18 | 75.44 | 46.24 | -0.5326 | 1.1486 | 0.8453 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
