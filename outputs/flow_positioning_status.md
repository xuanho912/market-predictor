# Flow / Positioning Proxy Status

Generated at: `2026-07-11T04:32:32.327270+00:00`
Latest date: `2026-07-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.91`
- overall_flow_conflict_score: `18.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 71.11 | 18.56 | 89.17 | 32.0 | -1.2182 | 0.8883 | 0.7069 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 69.57 | 18.56 | 88.66 | 32.0 | -2.0003 | 0.6836 | 0.5558 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.83 | 18.56 | 87.11 | 32.0 | -1.3691 | 0.8074 | 0.5797 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.11 | 18.56 | 87.53 | 32.0 | -0.9722 | 0.9699 | 0.6963 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
