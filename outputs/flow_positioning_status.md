# Flow / Positioning Proxy Status

Generated at: `2026-08-18T20:46:59.151591+00:00`
Latest date: `2026-08-18`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.53`
- overall_flow_conflict_score: `20.47`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.37 | 20.47 | 73.6 | 35.29 | -0.8372 | 1.0362 | 0.7696 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 67.65 | 20.47 | 75.66 | 35.29 | 0.6495 | 1.7097 | 1.2264 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.22 | 20.47 | 73.88 | 35.29 | -0.5765 | 1.1464 | 0.8474 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.9 | 20.47 | 74.1 | 35.29 | -0.2559 | 1.3423 | 0.9088 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
