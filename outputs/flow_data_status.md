# Flow / Positioning Proxy Status

Generated at: `2026-10-23T17:11:34.407034+00:00`
Latest date: `2026-10-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `53.06`
- overall_flow_conflict_score: `68.29`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 50.4 | 68.29 | 64.54 | 100.0 | -1.8274 | 0.3541 | 0.3895 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 50.4 | 68.29 | 64.54 | 100.0 | -1.3664 | 0.383 | 0.4821 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 55.28 | 68.29 | 66.14 | 100.0 | -2.0314 | 0.4439 | 0.4196 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.17 | 68.29 | 66.43 | 100.0 | -1.4087 | 0.6405 | 0.6471 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
