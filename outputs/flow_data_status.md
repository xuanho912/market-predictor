# Flow / Positioning Proxy Status

Generated at: `2026-06-23T05:17:04.636191+00:00`
Latest date: `2026-06-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `73.23`
- overall_flow_conflict_score: `21.16`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.82 | 21.16 | 100.0 | 34.54 | -0.6818 | 0.6579 | 0.7896 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 72.69 | 21.16 | 100.0 | 34.54 | -0.315 | 0.8815 | 0.8858 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.66 | 21.16 | 100.0 | 34.54 | -0.9012 | 0.7371 | 0.7708 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 76.77 | 21.16 | 100.0 | 34.54 | 0.8636 | 1.0143 | 1.186 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
