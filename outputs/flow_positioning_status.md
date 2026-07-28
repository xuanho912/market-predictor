# Flow / Positioning Proxy Status

Generated at: `2026-07-28T21:37:26.358805+00:00`
Latest date: `2026-07-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.09`
- overall_flow_conflict_score: `53.73`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.52 | 53.73 | 66.21 | 92.65 | -0.6311 | 0.9793 | 0.8784 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 62.86 | 53.73 | 68.28 | 92.65 | 1.4388 | 1.3282 | 1.3141 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.25 | 53.73 | 66.44 | 92.65 | -0.2725 | 0.944 | 0.9444 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 67.74 | 53.73 | 69.88 | 92.65 | 1.8209 | 1.3172 | 1.2857 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
