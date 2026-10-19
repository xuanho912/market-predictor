# Flow / Positioning Proxy Status

Generated at: `2026-10-19T18:46:29.909542+00:00`
Latest date: `2026-10-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `44.59`
- overall_flow_conflict_score: `61.71`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 42.89 | 61.71 | 55.83 | 98.1 | -1.5058 | 0.5227 | 0.5171 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 44.79 | 61.71 | 56.46 | 98.1 | -0.7314 | 0.597 | 0.7395 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 42.89 | 61.71 | 55.83 | 98.1 | -1.9947 | 0.4397 | 0.5005 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 47.77 | 61.71 | 57.43 | 98.1 | -2.0311 | 0.4259 | 0.4748 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
