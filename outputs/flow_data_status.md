# Flow / Positioning Proxy Status

Generated at: `2026-07-06T14:50:32.640436+00:00`
Latest date: `2026-07-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.63`
- overall_flow_conflict_score: `44.91`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.85 | 44.91 | 68.13 | 67.9 | -2.8138 | 0.1915 | 0.1714 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.85 | 44.91 | 68.13 | 67.9 | -2.3278 | 0.2322 | 0.1931 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 47.97 | 44.91 | 66.53 | 67.9 | -2.6536 | 0.2083 | 0.1801 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.85 | 44.91 | 68.13 | 67.9 | -2.4325 | 0.3649 | 0.2686 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
