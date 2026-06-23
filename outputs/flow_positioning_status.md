# Flow / Positioning Proxy Status

Generated at: `2026-06-23T23:39:07.449425+00:00`
Latest date: `2026-06-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `68.95`
- overall_flow_conflict_score: `25.21`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.56 | 25.21 | 94.54 | 37.45 | 0.2996 | 0.957 | 1.1113 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.6 | 25.21 | 94.23 | 37.45 | 0.1049 | 1.0953 | 1.0585 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.6 | 25.21 | 95.21 | 37.45 | -0.4132 | 0.9225 | 0.9057 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.04 | 25.21 | 93.39 | 37.45 | -0.6958 | 0.7647 | 0.8436 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
