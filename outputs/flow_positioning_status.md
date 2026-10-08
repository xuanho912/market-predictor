# Flow / Positioning Proxy Status

Generated at: `2026-10-08T00:25:53.952300+00:00`
Latest date: `2026-10-07`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.25`
- overall_flow_conflict_score: `39.7`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.98 | 39.7 | 89.98 | 57.58 | -1.1562 | 0.7577 | 0.7739 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.17 | 39.7 | 90.04 | 57.58 | -1.0412 | 0.8681 | 0.7911 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.28 | 39.7 | 88.76 | 57.58 | -0.8325 | 0.8443 | 0.8811 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 65.57 | 39.7 | 90.17 | 57.58 | -0.6713 | 0.8529 | 0.8272 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
