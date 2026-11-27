# Flow / Positioning Proxy Status

Generated at: `2026-11-27T21:20:11.706052+00:00`
Latest date: `2026-11-27`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.21`
- overall_flow_conflict_score: `68.41`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.45 | 68.41 | 70.26 | 100.0 | -0.8945 | 0.427 | 0.5956 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.13 | 68.41 | 70.15 | 100.0 | -1.0214 | 0.4058 | 0.5498 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.13 | 68.41 | 70.15 | 100.0 | -1.333 | 0.3868 | 0.4987 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.13 | 68.41 | 70.15 | 100.0 | -1.0408 | 0.456 | 0.5018 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
