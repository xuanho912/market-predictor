# Flow / Positioning Proxy Status

Generated at: `2026-07-15T00:04:16.965783+00:00`
Latest date: `2026-07-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `45.78`
- overall_flow_conflict_score: `29.24`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 47.35 | 29.24 | 55.92 | 47.44 | -1.5397 | 0.8166 | 0.6213 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 47.92 | 29.24 | 56.11 | 47.44 | -1.6519 | 0.8426 | 0.673 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 43.66 | 29.24 | 54.71 | 47.44 | -0.9042 | 0.9761 | 0.7293 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 44.18 | 29.24 | 54.88 | 47.44 | -0.6482 | 1.0579 | 0.777 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
