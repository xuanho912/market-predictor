# Flow / Positioning Proxy Status

Generated at: `2026-06-16T13:41:40.977283+00:00`
Latest date: `2026-06-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.27`
- overall_flow_conflict_score: `28.43`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 75.27 | 28.43 | 100.0 | 40.18 | -2.4774 | 0.0327 | 0.0411 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.27 | 28.43 | 100.0 | 40.18 | -1.9883 | 0.0476 | 0.0647 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 75.27 | 28.43 | 100.0 | 40.18 | -2.9905 | 0.0516 | 0.0639 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.27 | 28.43 | 100.0 | 40.18 | -2.9848 | 0.099 | 0.1142 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
