# Flow / Positioning Proxy Status

Generated at: `2026-10-27T06:21:19.581040+00:00`
Latest date: `2026-10-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.46`
- overall_flow_conflict_score: `65.62`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.42 | 65.62 | 64.72 | 100.0 | -0.6928 | 0.8191 | 0.7798 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.69 | 65.62 | 65.14 | 100.0 | -0.2635 | 0.8444 | 0.8956 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.34 | 65.62 | 65.68 | 100.0 | -1.4508 | 0.7096 | 0.6008 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.4 | 65.62 | 66.02 | 100.0 | -1.2938 | 0.8046 | 0.6973 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
