# Flow / Positioning Proxy Status

Generated at: `2026-10-23T23:17:48.406082+00:00`
Latest date: `2026-10-23`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.78`
- overall_flow_conflict_score: `68.18`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 53.25 | 68.18 | 65.67 | 100.0 | -0.6218 | 0.739 | 0.813 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 53.27 | 68.18 | 65.68 | 100.0 | -0.5254 | 0.6466 | 0.8149 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.01 | 68.18 | 67.24 | 100.0 | -0.7845 | 0.8489 | 0.8026 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.59 | 68.18 | 67.42 | 100.0 | -0.6254 | 0.8464 | 0.8552 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
