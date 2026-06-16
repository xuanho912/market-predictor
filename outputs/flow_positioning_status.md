# Flow / Positioning Proxy Status

Generated at: `2026-06-16T08:02:30.670281+00:00`
Latest date: `2026-06-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `78.81`
- overall_flow_conflict_score: `25.88`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 80.03 | 25.88 | 100.0 | 38.1 | 0.1743 | 0.7557 | 1.0642 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 78.83 | 25.88 | 100.0 | 38.1 | -0.0813 | 0.71 | 0.9624 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 77.38 | 25.88 | 100.0 | 38.1 | -0.8418 | 0.6472 | 0.8009 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 79.02 | 25.88 | 100.0 | 38.1 | -0.0857 | 0.8665 | 0.983 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
