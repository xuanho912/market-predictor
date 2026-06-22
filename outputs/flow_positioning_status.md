# Flow / Positioning Proxy Status

Generated at: `2026-06-22T23:54:13.191617+00:00`
Latest date: `2026-06-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `72.83`
- overall_flow_conflict_score: `21.16`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.66 | 21.16 | 100.0 | 34.54 | -0.7347 | 0.643 | 0.7717 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 72.33 | 21.16 | 100.0 | 34.54 | -0.4123 | 0.842 | 0.846 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.52 | 21.16 | 100.0 | 34.54 | -0.9587 | 0.7227 | 0.7557 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.8 | 21.16 | 100.0 | 34.54 | 0.6003 | 0.962 | 1.1248 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
