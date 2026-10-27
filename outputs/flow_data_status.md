# Flow / Positioning Proxy Status

Generated at: `2026-10-27T23:54:07.014141+00:00`
Latest date: `2026-10-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.33`
- overall_flow_conflict_score: `64.27`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.87 | 64.27 | 65.0 | 100.0 | -0.9323 | 0.7535 | 0.701 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 57.27 | 64.27 | 65.46 | 100.0 | -0.499 | 0.7884 | 0.8284 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.36 | 64.27 | 65.16 | 100.0 | -0.9163 | 0.8993 | 0.746 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 51.83 | 64.27 | 63.68 | 100.0 | -0.9576 | 0.9062 | 0.7777 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
