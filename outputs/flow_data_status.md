# Flow / Positioning Proxy Status

Generated at: `2026-11-07T00:12:00.193095+00:00`
Latest date: `2026-11-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.77`
- overall_flow_conflict_score: `75.0`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.39 | 75.0 | 81.08 | 100.0 | 0.4798 | 0.8329 | 1.2877 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.3 | 75.0 | 81.37 | 100.0 | 0.8228 | 0.9461 | 1.4878 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.41 | 75.0 | 79.77 | 100.0 | -0.0079 | 0.8412 | 1.0104 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.97 | 75.0 | 79.95 | 100.0 | 0.063 | 0.6827 | 1.05 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
