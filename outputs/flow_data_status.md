# Flow / Positioning Proxy Status

Generated at: `2026-09-22T17:00:04.286524+00:00`
Latest date: `2026-09-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.81`
- overall_flow_conflict_score: `35.9`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.94 | 35.9 | 89.47 | 51.97 | -2.2355 | 0.2932 | 0.3835 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.01 | 35.9 | 89.5 | 51.97 | -1.7065 | 0.4718 | 0.5733 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.25 | 35.9 | 89.58 | 51.97 | -1.4688 | 0.4854 | 0.5947 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.06 | 35.9 | 87.87 | 51.97 | -1.3698 | 0.4629 | 0.5271 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
