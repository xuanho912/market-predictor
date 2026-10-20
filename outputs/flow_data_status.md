# Flow / Positioning Proxy Status

Generated at: `2026-10-20T17:10:34.321352+00:00`
Latest date: `2026-10-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.56`
- overall_flow_conflict_score: `62.93`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 45.78 | 62.93 | 58.62 | 100.0 | -1.6377 | 0.4388 | 0.4832 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 45.78 | 62.93 | 58.62 | 100.0 | -1.3305 | 0.3979 | 0.5265 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 46.4 | 62.93 | 58.82 | 100.0 | -1.5007 | 0.5373 | 0.6224 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.29 | 62.93 | 60.75 | 100.0 | -1.1407 | 0.6496 | 0.7148 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
