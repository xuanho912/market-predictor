# Flow / Positioning Proxy Status

Generated at: `2026-08-21T04:23:38.467357+00:00`
Latest date: `2026-08-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.77`
- overall_flow_conflict_score: `20.59`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 76.13 | 20.59 | 94.57 | 35.49 | -0.0826 | 1.2253 | 0.9682 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 74.54 | 20.59 | 94.05 | 35.49 | -0.5457 | 0.9993 | 0.8232 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 78.63 | 20.59 | 95.39 | 35.49 | 0.4967 | 1.4267 | 1.107 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.79 | 20.59 | 93.8 | 35.49 | -0.6177 | 1.0477 | 0.7545 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
