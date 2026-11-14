# Flow / Positioning Proxy Status

Generated at: `2026-11-14T03:06:45.271319+00:00`
Latest date: `2026-11-13`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.62`
- overall_flow_conflict_score: `55.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 66.07 | 55.63 | 79.54 | 85.09 | -0.3892 | 0.8472 | 0.7962 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 66.4 | 55.63 | 79.65 | 85.09 | -0.3139 | 0.8477 | 0.8262 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.35 | 55.63 | 79.31 | 85.09 | -0.7325 | 0.7598 | 0.7301 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.67 | 55.63 | 79.08 | 85.09 | -0.5375 | 0.8263 | 0.6683 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
