# Flow / Positioning Proxy Status

Generated at: `2026-08-12T05:20:41.849832+00:00`
Latest date: `2026-08-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.8`
- overall_flow_conflict_score: `18.98`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.12 | 18.98 | 68.71 | 32.73 | -1.1063 | 0.78 | 0.7412 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.74 | 18.98 | 68.59 | 32.73 | -1.0246 | 0.7946 | 0.706 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.58 | 18.98 | 68.54 | 32.73 | -1.3798 | 0.8344 | 0.6916 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.75 | 18.98 | 68.59 | 32.73 | -0.8664 | 0.6644 | 0.7068 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
