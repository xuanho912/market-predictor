# Flow / Positioning Proxy Status

Generated at: `2026-10-28T00:52:15.162167+00:00`
Latest date: `2026-10-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.14`
- overall_flow_conflict_score: `64.27`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.76 | 64.27 | 65.29 | 100.0 | -0.6862 | 0.8213 | 0.7819 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.06 | 64.27 | 65.72 | 100.0 | -0.2499 | 0.8491 | 0.9006 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.78 | 64.27 | 64.64 | 100.0 | -1.4488 | 0.7103 | 0.6014 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.95 | 64.27 | 63.39 | 100.0 | -1.2938 | 0.8046 | 0.6973 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
