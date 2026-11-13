# Flow / Positioning Proxy Status

Generated at: `2026-11-13T19:45:44.233921+00:00`
Latest date: `2026-11-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.8`
- overall_flow_conflict_score: `55.45`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.76 | 55.45 | 78.95 | 84.6 | -1.0594 | 0.4917 | 0.462 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.94 | 55.45 | 79.01 | 84.6 | -0.791 | 0.5974 | 0.5822 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.76 | 55.45 | 78.95 | 84.6 | -1.339 | 0.5284 | 0.5077 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.76 | 55.45 | 78.95 | 84.6 | -0.974 | 0.5029 | 0.4067 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
