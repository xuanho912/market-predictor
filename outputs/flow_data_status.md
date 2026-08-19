# Flow / Positioning Proxy Status

Generated at: `2026-08-19T20:52:29.682801+00:00`
Latest date: `2026-08-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `64.17`
- overall_flow_conflict_score: `18.85`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.75 | 18.85 | 82.64 | 32.49 | -1.0524 | 0.9378 | 0.7183 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.06 | 18.85 | 83.07 | 32.49 | -0.5768 | 1.0427 | 0.8368 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 63.78 | 18.85 | 82.65 | 32.49 | -1.013 | 0.9325 | 0.7206 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.11 | 18.85 | 82.75 | 32.49 | -0.6704 | 1.0361 | 0.7505 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
