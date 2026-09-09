# Flow / Positioning Proxy Status

Generated at: `2026-09-09T06:02:35.689253+00:00`
Latest date: `2026-09-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.86`
- overall_flow_conflict_score: `28.02`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.1 | 28.02 | 63.64 | 40.65 | 1.5315 | 1.1949 | 1.2309 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 50.06 | 28.02 | 63.31 | 40.65 | -0.4357 | 0.9209 | 0.9167 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.63 | 28.02 | 63.82 | 40.65 | 0.1446 | 0.8944 | 1.0344 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 50.64 | 28.02 | 63.5 | 40.65 | 0.9007 | 1.2003 | 1.2539 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
