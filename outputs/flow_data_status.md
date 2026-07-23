# Flow / Positioning Proxy Status

Generated at: `2026-07-23T06:19:48.115774+00:00`
Latest date: `2026-07-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.03`
- overall_flow_conflict_score: `36.4`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.18 | 36.4 | 63.48 | 62.77 | -1.6489 | 0.6879 | 0.65 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.43 | 36.4 | 63.24 | 62.77 | -1.7352 | 0.6182 | 0.5821 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.24 | 36.4 | 64.16 | 62.77 | -0.5954 | 0.8615 | 0.838 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 57.29 | 36.4 | 64.18 | 62.77 | -0.6114 | 0.9547 | 0.8425 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
