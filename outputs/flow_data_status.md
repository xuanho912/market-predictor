# Flow / Positioning Proxy Status

Generated at: `2026-08-20T20:54:00.753033+00:00`
Latest date: `2026-08-20`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.58`
- overall_flow_conflict_score: `20.59`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 66.44 | 20.59 | 84.31 | 35.49 | -0.5004 | 1.0811 | 0.8542 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.6 | 20.59 | 84.03 | 35.49 | -0.687 | 0.944 | 0.7776 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 69.63 | 20.59 | 85.35 | 35.49 | 0.3811 | 1.3875 | 1.0766 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 64.66 | 20.59 | 83.72 | 35.49 | -0.7753 | 0.9607 | 0.6919 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
