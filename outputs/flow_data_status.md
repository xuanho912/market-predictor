# Flow / Positioning Proxy Status

Generated at: `2026-10-31T01:11:19.235162+00:00`
Latest date: `2026-10-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `59.77`
- overall_flow_conflict_score: `71.37`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.87 | 71.37 | 72.99 | 100.0 | 0.2367 | 1.1317 | 1.0597 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.5 | 71.37 | 72.87 | 100.0 | 0.1226 | 1.0101 | 1.0462 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.21 | 71.37 | 73.76 | 100.0 | -0.3971 | 1.0869 | 0.8699 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.5 | 71.37 | 72.21 | 100.0 | -0.4265 | 1.094 | 0.8854 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
