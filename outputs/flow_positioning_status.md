# Flow / Positioning Proxy Status

Generated at: `2026-11-18T08:37:02.777429+00:00`
Latest date: `2026-11-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.13`
- overall_flow_conflict_score: `66.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.44 | 66.44 | 72.46 | 100.0 | 0.9329 | 1.5852 | 1.4735 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.98 | 66.44 | 71.32 | 100.0 | 0.1771 | 1.3323 | 1.1085 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.0 | 66.44 | 71.99 | 100.0 | 0.6272 | 1.3637 | 1.212 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.12 | 66.44 | 71.04 | 100.0 | 0.079 | 1.4036 | 1.0473 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
