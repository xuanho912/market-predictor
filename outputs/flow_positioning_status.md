# Flow / Positioning Proxy Status

Generated at: `2026-08-07T01:06:41.719460+00:00`
Latest date: `2026-08-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.7`
- overall_flow_conflict_score: `28.55`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.7 | 28.55 | 63.22 | 49.23 | -1.3698 | 0.5452 | 0.6635 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.47 | 28.55 | 63.47 | 49.23 | -0.9304 | 0.5981 | 0.7339 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.6 | 28.55 | 63.52 | 49.23 | -1.2093 | 0.719 | 0.7462 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.02 | 28.55 | 63.98 | 49.23 | -0.4159 | 0.7437 | 0.8752 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
