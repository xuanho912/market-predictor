# Flow / Positioning Proxy Status

Generated at: `2026-09-05T00:55:08.207440+00:00`
Latest date: `2026-09-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.43`
- overall_flow_conflict_score: `24.12`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.03 | 24.12 | 63.66 | 38.61 | 1.2908 | 1.2038 | 1.1912 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.91 | 24.12 | 61.98 | 38.61 | -0.2035 | 0.9575 | 0.9537 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.24 | 24.12 | 62.09 | 38.61 | -0.0813 | 0.8427 | 0.9838 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.54 | 24.12 | 62.19 | 38.61 | 2.3799 | 1.82 | 1.6905 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
