# Flow / Positioning Proxy Status

Generated at: `2026-06-26T23:46:09.575185+00:00`
Latest date: `2026-06-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.64`
- overall_flow_conflict_score: `46.36`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.93 | 46.36 | 81.26 | 64.4 | 0.3968 | 1.1317 | 1.1286 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.24 | 46.36 | 80.05 | 64.4 | -0.4463 | 0.8954 | 0.863 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.63 | 46.36 | 83.78 | 64.4 | 1.1554 | 1.3837 | 1.2932 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.74 | 46.36 | 80.87 | 64.4 | -1.7398 | 0.6341 | 0.6461 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
