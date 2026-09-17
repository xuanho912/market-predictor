# Flow / Positioning Proxy Status

Generated at: `2026-09-17T08:56:54.661210+00:00`
Latest date: `2026-09-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `43.84`
- overall_flow_conflict_score: `39.74`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.23 | 39.74 | 53.64 | 56.68 | 2.6562 | 1.3955 | 1.5276 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 42.69 | 39.74 | 53.14 | 56.68 | 1.0336 | 1.2047 | 1.132 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.23 | 39.74 | 53.64 | 56.68 | 1.5064 | 1.1107 | 1.4241 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 44.23 | 39.74 | 53.64 | 56.68 | 2.3634 | 1.5732 | 1.7743 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
