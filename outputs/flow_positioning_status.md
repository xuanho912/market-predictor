# Flow / Positioning Proxy Status

Generated at: `2026-11-13T11:34:37.322896+00:00`
Latest date: `2026-11-12`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.08`
- overall_flow_conflict_score: `61.29`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.36 | 61.29 | 76.66 | 95.93 | -0.4952 | 0.5912 | 0.7678 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.81 | 61.29 | 76.48 | 95.93 | -0.571 | 0.54 | 0.7169 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 64.99 | 61.29 | 77.2 | 95.93 | -0.1973 | 0.7825 | 0.9161 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.16 | 61.29 | 75.94 | 95.93 | -1.0001 | 0.3382 | 0.4367 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
