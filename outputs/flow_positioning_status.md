# Flow / Positioning Proxy Status

Generated at: `2026-11-09T22:24:31.054268+00:00`
Latest date: `2026-11-09`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.17`
- overall_flow_conflict_score: `72.21`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 68.3 | 72.21 | 84.49 | 100.0 | 0.0164 | 0.7395 | 1.04 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.22 | 72.21 | 83.15 | 100.0 | 0.1287 | 0.7614 | 1.0925 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 69.74 | 72.21 | 84.96 | 100.0 | 0.2944 | 0.9335 | 1.1212 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 66.43 | 72.21 | 83.88 | 100.0 | -0.2618 | 0.5904 | 0.8724 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
