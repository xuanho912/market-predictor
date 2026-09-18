# Flow / Positioning Proxy Status

Generated at: `2026-09-18T16:27:27.003235+00:00`
Latest date: `2026-09-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.06`
- overall_flow_conflict_score: `32.2`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 43.97 | 32.2 | 60.88 | 49.41 | -0.8071 | 0.6733 | 0.8267 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 47.25 | 32.2 | 61.96 | 49.41 | -1.7735 | 0.6467 | 0.6813 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 43.9 | 32.2 | 60.86 | 49.41 | -0.662 | 0.6483 | 0.8201 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 41.11 | 32.2 | 59.94 | 49.41 | -1.7059 | 0.3518 | 0.4075 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
