# Flow / Positioning Proxy Status

Generated at: `2026-09-25T00:00:45.834574+00:00`
Latest date: `2026-09-24`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.21`
- overall_flow_conflict_score: `33.59`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 66.32 | 33.59 | 88.19 | 51.8 | -0.0993 | 0.8363 | 0.9956 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.01 | 33.59 | 87.76 | 51.8 | -0.7015 | 0.6954 | 0.8766 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 66.27 | 33.59 | 88.17 | 51.8 | 1.0029 | 1.1078 | 1.2569 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.25 | 33.59 | 85.87 | 51.8 | -0.6785 | 0.6619 | 0.7965 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
