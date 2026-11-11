# Flow / Positioning Proxy Status

Generated at: `2026-11-11T00:45:02.228794+00:00`
Latest date: `2026-11-10`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.79`
- overall_flow_conflict_score: `71.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.61 | 71.93 | 84.45 | 100.0 | -0.4366 | 0.6009 | 0.8166 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.93 | 71.93 | 84.23 | 100.0 | -0.5417 | 0.5416 | 0.7551 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.58 | 71.93 | 86.08 | 100.0 | -0.4966 | 0.6828 | 0.8253 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 68.04 | 71.93 | 85.9 | 100.0 | -0.4309 | 0.528 | 0.776 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
