# Flow / Positioning Proxy Status

Generated at: `2026-07-29T00:09:18.608784+00:00`
Latest date: `2026-07-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.26`
- overall_flow_conflict_score: `49.27`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.69 | 49.27 | 66.34 | 84.95 | -0.6311 | 0.9793 | 0.8784 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.03 | 49.27 | 68.42 | 84.95 | 1.4388 | 1.3282 | 1.3141 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.41 | 49.27 | 66.58 | 84.95 | -0.2725 | 0.944 | 0.9444 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 67.91 | 49.27 | 70.02 | 84.95 | 1.8209 | 1.3172 | 1.2857 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
