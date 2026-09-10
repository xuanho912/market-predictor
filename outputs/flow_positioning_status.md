# Flow / Positioning Proxy Status

Generated at: `2026-09-10T16:27:16.008064+00:00`
Latest date: `2026-09-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `37.23`
- overall_flow_conflict_score: `35.15`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 33.98 | 35.15 | 47.9 | 51.36 | -2.2514 | 0.5919 | 0.6006 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 38.49 | 35.15 | 49.38 | 51.36 | -1.898 | 0.6103 | 0.5586 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 37.51 | 35.15 | 49.06 | 51.36 | -0.3701 | 0.8749 | 0.9217 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 38.94 | 35.15 | 49.53 | 51.36 | 0.1186 | 0.8653 | 1.0312 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
