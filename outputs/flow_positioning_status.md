# Flow / Positioning Proxy Status

Generated at: `2026-10-06T02:35:50.994786+00:00`
Latest date: `2026-10-05`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.6`
- overall_flow_conflict_score: `38.02`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.62 | 38.02 | 93.07 | 53.17 | -0.2128 | 0.9499 | 0.9727 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.22 | 38.02 | 92.28 | 53.17 | -1.2164 | 0.7561 | 0.7538 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.19 | 38.02 | 92.93 | 53.17 | -0.5024 | 0.8636 | 0.9332 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.36 | 38.02 | 91.35 | 53.17 | -0.3124 | 1.0009 | 0.9376 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
