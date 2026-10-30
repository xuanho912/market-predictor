# Flow / Positioning Proxy Status

Generated at: `2026-10-30T23:56:49.788972+00:00`
Latest date: `2026-10-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.62`
- overall_flow_conflict_score: `71.37`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.76 | 71.37 | 74.27 | 100.0 | 2.7086 | 2.3487 | 2.0484 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.76 | 71.37 | 74.27 | 100.0 | 2.7628 | 2.5992 | 2.3102 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.19 | 71.37 | 74.08 | 100.0 | -0.1004 | 1.2196 | 0.9599 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.76 | 71.37 | 74.27 | 100.0 | 1.541 | 1.6213 | 1.3669 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
