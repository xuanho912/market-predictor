# Flow / Positioning Proxy Status

Generated at: `2026-08-15T13:02:44.305146+00:00`
Latest date: `2026-08-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `67.65`
- overall_flow_conflict_score: `19.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 69.3 | 19.56 | 84.61 | 33.72 | -1.2419 | 0.8316 | 0.6462 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.61 | 19.56 | 84.38 | 33.72 | -1.2593 | 0.8063 | 0.5825 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 69.15 | 19.56 | 84.56 | 33.72 | -1.3948 | 0.8241 | 0.6325 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.55 | 19.56 | 82.72 | 33.72 | -1.1941 | 0.7633 | 0.536 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
