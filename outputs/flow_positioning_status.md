# Flow / Positioning Proxy Status

Generated at: `2026-08-16T13:03:30.166003+00:00`
Latest date: `2026-08-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `76.1`
- overall_flow_conflict_score: `19.56`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 77.45 | 19.56 | 100.0 | 33.72 | -1.2419 | 0.8316 | 0.6462 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 76.88 | 19.56 | 100.0 | 33.72 | -1.2593 | 0.8063 | 0.5825 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 77.33 | 19.56 | 100.0 | 33.72 | -1.3948 | 0.8241 | 0.6325 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 72.74 | 19.56 | 100.0 | 33.72 | -1.1941 | 0.7633 | 0.536 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
