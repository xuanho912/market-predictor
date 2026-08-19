# Flow / Positioning Proxy Status

Generated at: `2026-08-19T23:12:33.459678+00:00`
Latest date: `2026-08-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.88`
- overall_flow_conflict_score: `18.85`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.25 | 18.85 | 83.13 | 32.49 | -0.5834 | 1.1153 | 0.8542 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.46 | 18.85 | 83.2 | 32.49 | -0.4616 | 1.0892 | 0.8741 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.19 | 18.85 | 82.78 | 32.49 | -0.8846 | 0.9807 | 0.7578 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.62 | 18.85 | 82.92 | 32.49 | -0.551 | 1.1007 | 0.7972 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
