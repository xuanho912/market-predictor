# Flow / Positioning Proxy Status

Generated at: `2026-07-14T14:16:43.596632+00:00`
Latest date: `2026-07-14`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.12`
- overall_flow_conflict_score: `31.94`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 46.56 | 31.94 | 55.56 | 52.09 | -2.8686 | 0.1621 | 0.1233 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 46.56 | 31.94 | 55.56 | 52.09 | -3.1389 | 0.2303 | 0.1838 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 41.68 | 31.94 | 53.96 | 52.09 | -2.4263 | 0.2491 | 0.1859 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 41.68 | 31.94 | 53.96 | 52.09 | -2.2115 | 0.3351 | 0.246 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
