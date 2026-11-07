# Flow / Positioning Proxy Status

Generated at: `2026-11-07T07:15:34.033330+00:00`
Latest date: `2026-11-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.09`
- overall_flow_conflict_score: `75.0`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.6 | 75.0 | 81.14 | 100.0 | 0.5057 | 0.8421 | 1.302 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.3 | 75.0 | 81.37 | 100.0 | 0.8358 | 0.9509 | 1.4953 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.52 | 75.0 | 79.8 | 100.0 | 0.0122 | 0.8473 | 1.0178 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.93 | 75.0 | 80.27 | 100.0 | 0.1826 | 0.7257 | 1.1162 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
