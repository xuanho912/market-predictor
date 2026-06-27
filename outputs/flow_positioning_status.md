# Flow / Positioning Proxy Status

Generated at: `2026-06-27T05:06:03.833297+00:00`
Latest date: `2026-06-26`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.97`
- overall_flow_conflict_score: `46.36`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.42 | 46.36 | 81.42 | 64.4 | 0.4937 | 1.1593 | 1.1561 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.71 | 46.36 | 80.2 | 64.4 | -0.3241 | 0.9401 | 0.9061 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 71.63 | 46.36 | 83.78 | 64.4 | 1.3427 | 1.4375 | 1.3435 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.14 | 46.36 | 81.0 | 64.4 | -1.5918 | 0.6701 | 0.6828 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
