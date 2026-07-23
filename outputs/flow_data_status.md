# Flow / Positioning Proxy Status

Generated at: `2026-07-23T14:41:56.752619+00:00`
Latest date: `2026-07-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `49.58`
- overall_flow_conflict_score: `36.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 49.58 | 36.44 | 60.01 | 62.82 | -2.7775 | 0.2731 | 0.2545 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.58 | 36.44 | 60.01 | 62.82 | -2.4607 | 0.3364 | 0.313 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 49.58 | 36.44 | 60.01 | 62.82 | -2.0598 | 0.4014 | 0.3979 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.58 | 36.44 | 60.01 | 62.82 | -2.1556 | 0.4638 | 0.4182 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
