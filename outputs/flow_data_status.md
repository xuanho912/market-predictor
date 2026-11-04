# Flow / Positioning Proxy Status

Generated at: `2026-11-04T00:44:31.773968+00:00`
Latest date: `2026-11-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.58`
- overall_flow_conflict_score: `69.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.49 | 69.94 | 77.02 | 100.0 | -0.5005 | 0.7065 | 0.8136 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.18 | 69.94 | 77.25 | 100.0 | -0.3358 | 0.744 | 0.8767 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.37 | 69.94 | 76.65 | 100.0 | -1.0114 | 0.798 | 0.7112 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.28 | 69.94 | 77.28 | 100.0 | -0.4846 | 0.8819 | 0.8857 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
