# Flow / Positioning Proxy Status

Generated at: `2026-09-04T00:31:01.958703+00:00`
Latest date: `2026-09-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `57.79`
- overall_flow_conflict_score: `21.63`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 57.62 | 21.63 | 67.37 | 36.67 | -1.3956 | 0.8213 | 0.7927 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.25 | 21.63 | 65.6 | 36.67 | -1.2009 | 0.7789 | 0.748 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 60.02 | 21.63 | 68.15 | 36.67 | 1.5307 | 1.2878 | 1.3415 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.27 | 21.63 | 68.56 | 36.67 | 0.3898 | 1.314 | 1.0557 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
