# Flow / Positioning Proxy Status

Generated at: `2026-09-08T22:49:44.513852+00:00`
Latest date: `2026-09-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.65`
- overall_flow_conflict_score: `28.02`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.87 | 28.02 | 63.57 | 40.65 | 1.3363 | 1.1627 | 1.1976 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.85 | 28.02 | 63.24 | 40.65 | -0.527 | 0.9018 | 0.8974 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.53 | 28.02 | 63.79 | 40.65 | 0.1214 | 0.8898 | 1.0292 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.36 | 28.02 | 63.4 | 40.65 | 0.8482 | 1.185 | 1.2379 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
