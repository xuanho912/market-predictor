# Flow / Positioning Proxy Status

Generated at: `2026-11-03T03:05:20.822496+00:00`
Latest date: `2026-11-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.47`
- overall_flow_conflict_score: `72.48`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.4 | 72.48 | 77.66 | 100.0 | 0.7821 | 1.2151 | 1.2917 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.67 | 72.48 | 77.74 | 100.0 | 0.8341 | 1.2493 | 1.389 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.74 | 72.48 | 77.77 | 100.0 | 0.033 | 1.2343 | 1.0121 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.07 | 72.48 | 76.24 | 100.0 | 0.0805 | 1.0839 | 1.0221 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
