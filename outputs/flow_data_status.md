# Flow / Positioning Proxy Status

Generated at: `2026-06-30T05:19:37.204333+00:00`
Latest date: `2026-06-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.07`
- overall_flow_conflict_score: `44.96`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.8 | 44.96 | 75.3 | 62.96 | -0.3056 | 0.9793 | 0.9226 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.99 | 44.96 | 75.04 | 62.96 | -0.4883 | 0.9054 | 0.849 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.5 | 44.96 | 76.51 | 62.96 | -0.7824 | 0.8509 | 0.8151 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.98 | 44.96 | 77.33 | 62.96 | 0.1 | 1.1382 | 1.0234 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
