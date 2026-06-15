# Flow / Positioning Proxy Status

Generated at: `2026-06-15T13:55:19.311080+00:00`
Latest date: `2026-06-15`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.27`
- overall_flow_conflict_score: `23.77`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 75.27 | 23.77 | 100.0 | 36.27 | -2.3484 | 0.0889 | 0.1117 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 75.27 | 23.77 | 100.0 | 36.27 | -1.8323 | 0.116 | 0.1572 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 75.27 | 23.77 | 100.0 | 36.27 | -2.9047 | 0.1061 | 0.1312 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 75.27 | 23.77 | 100.0 | 36.27 | -2.807 | 0.1833 | 0.2079 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
