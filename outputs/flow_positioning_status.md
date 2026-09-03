# Flow / Positioning Proxy Status

Generated at: `2026-09-03T22:42:21.297450+00:00`
Latest date: `2026-09-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.54`
- overall_flow_conflict_score: `21.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.96 | 21.63 | 69.44 | 36.67 | 1.1417 | 1.1794 | 1.167 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.47 | 21.63 | 66.33 | 36.67 | -0.22 | 0.9541 | 0.9502 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.81 | 21.63 | 66.45 | 36.67 | -0.0914 | 0.8408 | 0.9816 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.9 | 21.63 | 69.75 | 36.67 | 2.3812 | 1.8206 | 1.691 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
