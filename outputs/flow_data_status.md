# Flow / Positioning Proxy Status

Generated at: `2026-11-13T01:22:40.638162+00:00`
Latest date: `2026-11-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.27`
- overall_flow_conflict_score: `61.29`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.65 | 61.29 | 76.76 | 95.93 | -0.4247 | 0.5792 | 0.7935 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 64.48 | 61.29 | 77.03 | 95.93 | -0.264 | 0.6276 | 0.8697 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.46 | 61.29 | 76.37 | 95.93 | -0.8627 | 0.5458 | 0.6852 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.5 | 61.29 | 76.38 | 95.93 | -0.5751 | 0.4685 | 0.6895 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
