# Flow / Positioning Proxy Status

Generated at: `2026-11-19T20:40:46.146195+00:00`
Latest date: `2026-11-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `48.54`
- overall_flow_conflict_score: `63.53`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 48.56 | 63.53 | 63.11 | 94.65 | 0.1533 | 1.0179 | 1.0672 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 49.86 | 63.53 | 63.53 | 94.65 | 0.348 | 1.3256 | 1.1505 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 48.1 | 63.53 | 62.96 | 94.65 | 0.1099 | 1.0593 | 1.0331 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.63 | 63.53 | 62.8 | 94.65 | -0.0098 | 1.1827 | 1.0095 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
