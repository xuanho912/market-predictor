# Flow / Positioning Proxy Status

Generated at: `2026-10-07T01:01:55.597238+00:00`
Latest date: `2026-10-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.29`
- overall_flow_conflict_score: `37.34`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.8 | 37.34 | 90.1 | 54.86 | -1.161 | 0.7567 | 0.7729 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.98 | 37.34 | 90.16 | 54.86 | -1.0495 | 0.8661 | 0.7893 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.98 | 37.34 | 90.49 | 54.86 | -0.8354 | 0.8439 | 0.8807 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.39 | 37.34 | 90.3 | 54.86 | -0.6713 | 0.8529 | 0.8272 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
