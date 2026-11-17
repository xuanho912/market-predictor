# Flow / Positioning Proxy Status

Generated at: `2026-11-17T04:50:57.609179+00:00`
Latest date: `2026-11-16`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.23`
- overall_flow_conflict_score: `69.01`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.84 | 69.01 | 80.54 | 100.0 | 0.9221 | 1.6733 | 1.471 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 59.39 | 69.01 | 78.43 | 100.0 | -0.2858 | 0.9819 | 0.8673 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.5 | 69.01 | 79.45 | 100.0 | 0.2693 | 1.1892 | 1.1028 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.18 | 69.01 | 79.01 | 100.0 | 0.0189 | 1.382 | 1.0276 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
