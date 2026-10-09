# Flow / Positioning Proxy Status

Generated at: `2026-10-09T02:57:05.306544+00:00`
Latest date: `2026-10-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.77`
- overall_flow_conflict_score: `30.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.72 | 30.83 | 83.85 | 50.06 | -0.6252 | 0.9798 | 0.8761 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.08 | 30.83 | 85.94 | 50.06 | 2.0157 | 1.6734 | 1.4831 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.2 | 30.83 | 84.34 | 50.06 | 2.3695 | 1.3394 | 1.4124 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.08 | 30.83 | 85.28 | 50.06 | 0.6837 | 1.0563 | 1.1513 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
