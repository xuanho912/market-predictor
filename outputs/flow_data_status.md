# Flow / Positioning Proxy Status

Generated at: `2026-10-21T23:35:48.754681+00:00`
Latest date: `2026-10-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.83`
- overall_flow_conflict_score: `59.08`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.15 | 59.08 | 62.67 | 92.9 | -0.7467 | 0.6669 | 0.7639 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.77 | 59.08 | 61.56 | 92.9 | -0.3009 | 0.6657 | 0.9003 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.36 | 59.08 | 62.08 | 92.9 | -1.592 | 0.5236 | 0.6004 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.03 | 59.08 | 62.63 | 92.9 | -0.9762 | 0.6783 | 0.7526 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
