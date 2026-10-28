# Flow / Positioning Proxy Status

Generated at: `2026-10-28T10:02:20.561124+00:00`
Latest date: `2026-10-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.51`
- overall_flow_conflict_score: `64.27`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.0 | 64.27 | 65.04 | 100.0 | -0.8985 | 0.7659 | 0.7125 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.47 | 64.27 | 65.53 | 100.0 | -0.4489 | 0.8063 | 0.8472 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.4 | 64.27 | 65.17 | 100.0 | -0.9067 | 0.9027 | 0.7489 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.18 | 64.27 | 63.79 | 100.0 | -0.8338 | 0.9429 | 0.8092 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
