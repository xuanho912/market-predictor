# Flow / Positioning Proxy Status

Generated at: `2026-06-16T00:16:04.703166+00:00`
Latest date: `2026-06-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `78.16`
- overall_flow_conflict_score: `25.88`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 77.66 | 25.88 | 100.0 | 38.1 | -0.509 | 0.662 | 0.8318 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 78.73 | 25.88 | 100.0 | 38.1 | -0.1087 | 0.7016 | 0.9511 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 77.32 | 25.88 | 100.0 | 38.1 | -0.8704 | 0.6418 | 0.7942 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 78.95 | 25.88 | 100.0 | 38.1 | -0.1211 | 0.8598 | 0.9753 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
