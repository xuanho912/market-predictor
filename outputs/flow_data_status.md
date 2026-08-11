# Flow / Positioning Proxy Status

Generated at: `2026-08-11T21:12:38.763808+00:00`
Latest date: `2026-08-11`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.67`
- overall_flow_conflict_score: `18.98`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.02 | 18.98 | 68.68 | 32.73 | -1.1411 | 0.7702 | 0.7319 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 55.68 | 18.98 | 68.57 | 32.73 | -1.0413 | 0.7886 | 0.7007 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.46 | 18.98 | 68.5 | 32.73 | -1.423 | 0.821 | 0.6806 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 55.51 | 18.98 | 68.51 | 32.73 | -0.9269 | 0.644 | 0.6851 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
