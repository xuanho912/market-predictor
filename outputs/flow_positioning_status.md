# Flow / Positioning Proxy Status

Generated at: `2026-08-01T13:57:49.001952+00:00`
Latest date: `2026-07-31`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.6`
- overall_flow_conflict_score: `36.49`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.65 | 36.49 | 60.68 | 59.94 | 1.3842 | 1.1499 | 1.305 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.28 | 36.49 | 60.56 | 59.94 | 0.9361 | 0.9666 | 1.2555 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.65 | 36.49 | 60.68 | 59.94 | 1.4779 | 1.2288 | 1.3344 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.83 | 36.49 | 59.43 | 59.94 | 0.2182 | 0.886 | 1.0685 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
