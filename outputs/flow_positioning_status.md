# Flow / Positioning Proxy Status

Generated at: `2026-07-29T14:33:47.650853+00:00`
Latest date: `2026-07-29`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `54.71`
- overall_flow_conflict_score: `60.22`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 54.65 | 60.22 | 67.56 | 100.0 | -3.2205 | 0.2084 | 0.2006 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.65 | 60.22 | 67.56 | 100.0 | -2.5692 | 0.2628 | 0.2814 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 54.65 | 60.22 | 67.56 | 100.0 | -2.9451 | 0.3195 | 0.3299 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 54.91 | 60.22 | 67.64 | 100.0 | -1.9039 | 0.5401 | 0.5896 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
