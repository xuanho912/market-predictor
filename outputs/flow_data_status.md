# Flow / Positioning Proxy Status

Generated at: `2026-11-05T01:49:10.041419+00:00`
Latest date: `2026-11-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.08`
- overall_flow_conflict_score: `71.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.36 | 71.18 | 83.09 | 100.0 | -0.4523 | 0.7227 | 0.8322 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.35 | 71.18 | 83.41 | 100.0 | -0.2278 | 0.7828 | 0.9224 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.06 | 71.18 | 84.3 | 100.0 | -0.9683 | 0.8129 | 0.7244 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.55 | 71.18 | 85.12 | 100.0 | -0.2244 | 0.9472 | 0.9513 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
