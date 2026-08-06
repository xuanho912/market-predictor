# Flow / Positioning Proxy Status

Generated at: `2026-08-06T00:09:42.180181+00:00`
Latest date: `2026-08-05`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.18`
- overall_flow_conflict_score: `20.2`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 68.15 | 20.2 | 76.78 | 34.82 | -0.4813 | 0.6724 | 0.8893 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.97 | 20.2 | 76.4 | 34.82 | -0.7679 | 0.5848 | 0.7822 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 67.23 | 20.2 | 76.48 | 34.82 | -0.8733 | 0.6922 | 0.8059 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 74.36 | 20.2 | 78.82 | 34.82 | 0.8764 | 0.9929 | 1.3009 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
