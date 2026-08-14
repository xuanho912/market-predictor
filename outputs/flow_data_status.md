# Flow / Positioning Proxy Status

Generated at: `2026-08-14T21:54:52.473444+00:00`
Latest date: `2026-08-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.27`
- overall_flow_conflict_score: `19.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 68.74 | 19.56 | 84.64 | 33.72 | -1.3371 | 0.7949 | 0.6175 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.29 | 19.56 | 84.49 | 33.72 | -1.2773 | 0.7978 | 0.5762 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 68.75 | 19.56 | 84.64 | 33.72 | -1.4474 | 0.8049 | 0.6178 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.31 | 19.56 | 82.85 | 33.72 | -1.2576 | 0.726 | 0.5098 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
