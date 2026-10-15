# Flow / Positioning Proxy Status

Generated at: `2026-10-15T00:07:23.586065+00:00`
Latest date: `2026-10-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `48.0`
- overall_flow_conflict_score: `37.16`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 43.25 | 37.16 | 56.04 | 57.14 | -1.35 | 0.8686 | 0.5937 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 46.15 | 37.16 | 56.99 | 57.14 | -0.6017 | 0.971 | 0.858 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 50.11 | 37.16 | 58.29 | 57.14 | 0.5697 | 1.1776 | 1.1169 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.51 | 37.16 | 59.08 | 57.14 | -0.0384 | 0.9991 | 0.993 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
