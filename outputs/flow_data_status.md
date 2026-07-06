# Flow / Positioning Proxy Status

Generated at: `2026-07-06T14:44:14.716700+00:00`
Latest date: `2026-07-06`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.48`
- overall_flow_conflict_score: `44.97`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.7 | 44.97 | 67.88 | 67.89 | -2.8237 | 0.1859 | 0.1663 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.7 | 44.97 | 67.88 | 67.89 | -2.3386 | 0.2258 | 0.1877 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 47.82 | 44.97 | 66.28 | 67.89 | -2.6701 | 0.1987 | 0.1718 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 52.7 | 44.97 | 67.88 | 67.89 | -2.4432 | 0.3586 | 0.264 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
