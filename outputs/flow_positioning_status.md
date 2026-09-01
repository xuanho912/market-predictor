# Flow / Positioning Proxy Status

Generated at: `2026-09-01T01:48:59.776350+00:00`
Latest date: `2026-08-31`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.11`
- overall_flow_conflict_score: `21.48`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.37 | 21.48 | 78.37 | 37.03 | -0.0055 | 1.2086 | 0.9721 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.23 | 21.48 | 78.32 | 37.03 | -0.0825 | 1.1035 | 0.9591 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.8 | 21.48 | 78.51 | 37.03 | 1.3152 | 1.4685 | 1.2438 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.04 | 21.48 | 75.31 | 37.03 | -1.2163 | 0.5952 | 0.5101 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
