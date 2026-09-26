# Flow / Positioning Proxy Status

Generated at: `2026-09-26T01:33:01.781548+00:00`
Latest date: `2026-09-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.6`
- overall_flow_conflict_score: `36.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.63 | 36.66 | 82.08 | 53.96 | 0.0383 | 0.8615 | 1.0257 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.05 | 36.66 | 81.57 | 53.96 | -0.646 | 0.7046 | 0.8882 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.36 | 36.66 | 82.0 | 53.96 | 1.0447 | 1.1167 | 1.267 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.37 | 36.66 | 81.34 | 53.96 | -0.6755 | 0.7884 | 0.8266 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
