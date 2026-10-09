# Flow / Positioning Proxy Status

Generated at: `2026-10-09T00:36:03.647276+00:00`
Latest date: `2026-10-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.54`
- overall_flow_conflict_score: `30.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.48 | 30.83 | 83.12 | 50.06 | -1.6972 | 0.6536 | 0.6715 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.47 | 30.83 | 83.44 | 50.06 | -1.1766 | 0.8369 | 0.762 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.14 | 30.83 | 82.68 | 50.06 | -0.1177 | 0.9594 | 0.9946 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.08 | 30.83 | 85.94 | 50.06 | 1.1231 | 1.2933 | 1.2917 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
