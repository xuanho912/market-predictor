# Flow / Positioning Proxy Status

Generated at: `2026-09-03T01:07:26.936884+00:00`
Latest date: `2026-09-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `49.19`
- overall_flow_conflict_score: `25.43`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.03 | 25.43 | 56.36 | 43.65 | 0.7606 | 1.2366 | 1.0627 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.01 | 25.43 | 56.35 | 43.65 | 0.6476 | 1.2645 | 1.0805 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.86 | 25.43 | 57.28 | 43.65 | 1.7532 | 1.5707 | 1.3574 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 46.85 | 25.43 | 55.64 | 43.65 | 0.0306 | 1.2231 | 0.9936 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
