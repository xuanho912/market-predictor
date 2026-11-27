# Flow / Positioning Proxy Status

Generated at: `2026-11-27T03:00:34.205329+00:00`
Latest date: `2026-11-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.56`
- overall_flow_conflict_score: `73.47`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.79 | 73.47 | 77.18 | 100.0 | 0.2746 | 0.8451 | 1.1619 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.48 | 73.47 | 78.06 | 100.0 | 0.6612 | 1.0396 | 1.3425 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.74 | 73.47 | 77.49 | 100.0 | 0.5023 | 0.9705 | 1.208 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.25 | 73.47 | 77.01 | 100.0 | 0.2141 | 1.0146 | 1.1236 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
