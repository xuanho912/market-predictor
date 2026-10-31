# Flow / Positioning Proxy Status

Generated at: `2026-10-31T02:17:50.244212+00:00`
Latest date: `2026-10-30`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.64`
- overall_flow_conflict_score: `71.37`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.76 | 71.37 | 74.27 | 100.0 | 2.7286 | 2.3634 | 2.0613 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.76 | 71.37 | 74.27 | 100.0 | 2.775 | 2.6101 | 2.3198 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.27 | 71.37 | 74.11 | 100.0 | -0.0762 | 1.2282 | 0.9667 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 63.76 | 71.37 | 74.27 | 100.0 | 1.9264 | 1.7574 | 1.4816 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
