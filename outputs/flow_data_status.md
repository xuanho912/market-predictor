# Flow / Positioning Proxy Status

Generated at: `2026-08-04T04:35:36.122899+00:00`
Latest date: `2026-08-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.6`
- overall_flow_conflict_score: `31.24`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.65 | 31.24 | 65.08 | 53.86 | 1.3842 | 1.1499 | 1.305 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.28 | 31.24 | 64.96 | 53.86 | 0.9361 | 0.9666 | 1.2555 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.65 | 31.24 | 65.08 | 53.86 | 1.4779 | 1.2288 | 1.3344 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.83 | 31.24 | 63.83 | 53.86 | 0.2182 | 0.886 | 1.0685 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
