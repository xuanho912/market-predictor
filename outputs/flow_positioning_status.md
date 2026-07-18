# Flow / Positioning Proxy Status

Generated at: `2026-07-18T00:04:06.322453+00:00`
Latest date: `2026-07-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `58.77`
- overall_flow_conflict_score: `49.0`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.94 | 49.0 | 67.05 | 81.17 | 0.8089 | 1.4495 | 1.1443 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.78 | 49.0 | 67.66 | 81.17 | 1.4301 | 1.6325 | 1.2889 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.36 | 49.0 | 67.19 | 81.17 | 0.8388 | 1.469 | 1.1774 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.02 | 49.0 | 66.09 | 81.17 | 0.1061 | 1.3214 | 1.0028 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
