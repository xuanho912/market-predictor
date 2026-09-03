# Flow / Positioning Proxy Status

Generated at: `2026-09-03T08:19:21.913377+00:00`
Latest date: `2026-09-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.34`
- overall_flow_conflict_score: `24.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.72 | 24.94 | 55.12 | 41.54 | -1.4122 | 0.8186 | 0.79 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 44.22 | 24.94 | 54.96 | 41.54 | -1.2139 | 0.7759 | 0.7451 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.03 | 24.94 | 57.52 | 41.54 | 1.528 | 1.2871 | 1.3408 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 48.4 | 24.94 | 56.33 | 41.54 | 0.3898 | 1.314 | 1.0557 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
