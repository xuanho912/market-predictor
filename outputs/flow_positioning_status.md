# Flow / Positioning Proxy Status

Generated at: `2026-10-15T23:10:56.110455+00:00`
Latest date: `2026-10-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `50.41`
- overall_flow_conflict_score: `41.06`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.62 | 41.06 | 55.08 | 62.68 | 0.0757 | 1.314 | 1.0135 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.32 | 41.06 | 56.62 | 62.68 | 1.4639 | 1.3848 | 1.4247 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.1 | 41.06 | 56.55 | 62.68 | 1.0324 | 1.165 | 1.2519 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.62 | 41.06 | 57.04 | 62.68 | 0.3807 | 1.0501 | 1.0616 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
