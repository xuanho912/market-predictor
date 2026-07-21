# Flow / Positioning Proxy Status

Generated at: `2026-07-21T04:35:31.564159+00:00`
Latest date: `2026-07-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.02`
- overall_flow_conflict_score: `56.06`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.04 | 56.06 | 64.1 | 94.18 | -0.0619 | 1.085 | 0.9602 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.26 | 56.06 | 63.19 | 94.18 | -1.3126 | 0.7684 | 0.7068 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.07 | 56.06 | 63.79 | 94.18 | -0.4415 | 0.9382 | 0.8723 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.72 | 56.06 | 62.69 | 94.18 | -1.5586 | 0.6643 | 0.5553 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
