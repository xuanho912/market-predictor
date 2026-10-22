# Flow / Positioning Proxy Status

Generated at: `2026-10-22T00:20:10.970845+00:00`
Latest date: `2026-10-21`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.05`
- overall_flow_conflict_score: `59.08`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.06 | 59.08 | 62.97 | 92.9 | -0.5391 | 0.769 | 0.8469 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.32 | 59.08 | 61.41 | 92.9 | -0.3985 | 0.6491 | 0.8595 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.92 | 59.08 | 63.58 | 92.9 | 0.037 | 0.8716 | 1.0097 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.9 | 59.08 | 63.9 | 92.9 | 0.2482 | 0.9639 | 1.0607 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
