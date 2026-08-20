# Flow / Positioning Proxy Status

Generated at: `2026-08-20T04:22:01.950706+00:00`
Latest date: `2026-08-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `72.17`
- overall_flow_conflict_score: `18.85`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 72.54 | 18.85 | 96.24 | 32.49 | -0.55 | 1.1275 | 0.8636 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 72.88 | 18.85 | 96.35 | 32.49 | -0.3978 | 1.1148 | 0.8947 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.39 | 18.85 | 95.86 | 32.49 | -0.88 | 0.9824 | 0.7592 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 71.86 | 18.85 | 96.01 | 32.49 | -0.5401 | 1.1065 | 0.8015 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
