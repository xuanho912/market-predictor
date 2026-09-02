# Flow / Positioning Proxy Status

Generated at: `2026-09-02T01:01:03.470961+00:00`
Latest date: `2026-09-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.06`
- overall_flow_conflict_score: `22.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.65 | 22.93 | 64.61 | 37.72 | 0.573 | 1.2061 | 1.0365 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.75 | 22.93 | 64.65 | 37.72 | 0.5176 | 1.2348 | 1.0551 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.13 | 22.93 | 65.76 | 37.72 | 1.7297 | 1.5637 | 1.3514 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.71 | 22.93 | 63.98 | 37.72 | -0.0501 | 1.1843 | 0.9621 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
