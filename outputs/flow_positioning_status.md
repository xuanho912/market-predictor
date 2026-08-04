# Flow / Positioning Proxy Status

Generated at: `2026-08-04T14:42:09.669410+00:00`
Latest date: `2026-08-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.91`
- overall_flow_conflict_score: `20.54`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.55 | 20.54 | 72.06 | 35.41 | -2.6088 | 0.2014 | 0.2552 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.55 | 20.54 | 72.06 | 35.41 | -2.0973 | 0.2516 | 0.3333 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.55 | 20.54 | 72.06 | 35.41 | -2.7834 | 0.2004 | 0.2344 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.01 | 20.54 | 72.54 | 35.41 | -0.972 | 0.5523 | 0.6996 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
