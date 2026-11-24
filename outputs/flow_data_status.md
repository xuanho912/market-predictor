# Flow / Positioning Proxy Status

Generated at: `2026-11-24T06:55:53.701748+00:00`
Latest date: `2026-11-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.24`
- overall_flow_conflict_score: `69.3`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.14 | 69.3 | 66.04 | 100.0 | 0.8698 | 1.0475 | 1.5117 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.14 | 69.3 | 66.04 | 100.0 | 0.8684 | 1.2112 | 1.4867 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.31 | 69.3 | 65.11 | 100.0 | 0.2978 | 0.9039 | 1.1443 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.38 | 69.3 | 64.48 | 100.0 | -0.0012 | 0.9113 | 1.0215 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
