# Flow / Positioning Proxy Status

Generated at: `2026-09-22T23:47:49.443294+00:00`
Latest date: `2026-09-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.91`
- overall_flow_conflict_score: `36.15`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.58 | 36.15 | 93.56 | 52.07 | -0.7277 | 0.6363 | 0.8332 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.97 | 36.15 | 95.65 | 52.07 | 1.0324 | 1.0126 | 1.231 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.7 | 36.15 | 95.57 | 52.07 | 0.815 | 1.0163 | 1.2453 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.4 | 36.15 | 92.52 | 52.07 | 0.0161 | 0.8648 | 0.9849 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
