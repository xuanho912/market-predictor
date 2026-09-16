# Flow / Positioning Proxy Status

Generated at: `2026-09-16T23:05:47.864886+00:00`
Latest date: `2026-09-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `43.85`
- overall_flow_conflict_score: `39.74`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 44.23 | 39.74 | 53.64 | 56.68 | 2.6562 | 1.3955 | 1.5276 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 42.72 | 39.74 | 53.15 | 56.68 | 1.0403 | 1.2059 | 1.1331 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 44.23 | 39.74 | 53.64 | 56.68 | 1.5064 | 1.1107 | 1.4241 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 44.23 | 39.74 | 53.64 | 56.68 | 2.3631 | 1.573 | 1.7741 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
