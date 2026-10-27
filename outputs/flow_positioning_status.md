# Flow / Positioning Proxy Status

Generated at: `2026-10-27T18:03:49.669280+00:00`
Latest date: `2026-10-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.0`
- overall_flow_conflict_score: `63.97`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 54.22 | 63.97 | 64.19 | 100.0 | -1.8229 | 0.3941 | 0.3666 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.22 | 63.97 | 64.19 | 100.0 | -1.2158 | 0.5209 | 0.5469 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.22 | 63.97 | 64.19 | 100.0 | -1.7696 | 0.563 | 0.467 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 49.34 | 63.97 | 62.59 | 100.0 | -1.9772 | 0.5617 | 0.482 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
