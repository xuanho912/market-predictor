# Flow / Positioning Proxy Status

Generated at: `2026-08-14T20:53:27.771352+00:00`
Latest date: `2026-08-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `73.48`
- overall_flow_conflict_score: `19.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 74.61 | 19.56 | 91.17 | 33.72 | -1.6363 | 0.6736 | 0.5234 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 74.61 | 19.56 | 91.17 | 33.72 | -1.3755 | 0.7498 | 0.5417 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 74.97 | 19.56 | 91.29 | 33.72 | -1.5116 | 0.7812 | 0.5997 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 69.73 | 19.56 | 89.57 | 33.72 | -1.2746 | 0.7159 | 0.5026 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
