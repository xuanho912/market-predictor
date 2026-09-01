# Flow / Positioning Proxy Status

Generated at: `2026-09-01T08:56:12.417071+00:00`
Latest date: `2026-08-31`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `70.28`
- overall_flow_conflict_score: `19.0`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 72.65 | 19.0 | 91.83 | 32.75 | 0.0091 | 1.2125 | 0.9754 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 72.54 | 19.0 | 91.79 | 32.75 | -0.0522 | 1.1126 | 0.9673 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 72.67 | 19.0 | 91.83 | 32.75 | 1.1731 | 1.3975 | 1.2151 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.26 | 19.0 | 88.75 | 32.75 | -1.2018 | 0.6089 | 0.5253 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
