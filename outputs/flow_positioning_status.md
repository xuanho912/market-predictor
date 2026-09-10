# Flow / Positioning Proxy Status

Generated at: `2026-09-10T23:23:12.719269+00:00`
Latest date: `2026-09-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `42.14`
- overall_flow_conflict_score: `35.92`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 42.22 | 35.92 | 50.81 | 52.69 | 0.9221 | 1.1328 | 1.1496 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 38.8 | 35.92 | 49.68 | 52.69 | -0.0071 | 1.0935 | 1.0014 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 43.78 | 35.92 | 51.32 | 52.69 | 2.2283 | 1.5034 | 1.584 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 43.78 | 35.92 | 51.32 | 52.69 | 1.8384 | 1.335 | 1.591 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
