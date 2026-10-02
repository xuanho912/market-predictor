# Flow / Positioning Proxy Status

Generated at: `2026-10-02T23:54:40.910082+00:00`
Latest date: `2026-10-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.84`
- overall_flow_conflict_score: `37.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.95 | 37.01 | 97.35 | 51.44 | -0.0187 | 1.0141 | 0.9989 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.12 | 37.01 | 99.05 | 51.44 | 0.0499 | 1.0377 | 1.0164 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.92 | 37.01 | 98.98 | 51.44 | 1.1261 | 1.192 | 1.2516 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.36 | 37.01 | 97.82 | 51.44 | 0.3367 | 1.2453 | 1.0675 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
