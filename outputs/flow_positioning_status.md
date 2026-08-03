# Flow / Positioning Proxy Status

Generated at: `2026-08-03T22:38:16.073087+00:00`
Latest date: `2026-08-03`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.73`
- overall_flow_conflict_score: `31.24`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.27 | 31.24 | 63.97 | 53.86 | 0.3726 | 0.8998 | 1.0818 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.68 | 31.24 | 63.78 | 53.86 | 0.1768 | 0.7947 | 1.0629 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.69 | 31.24 | 63.45 | 53.86 | -0.0147 | 0.8752 | 1.0041 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.27 | 31.24 | 63.97 | 53.86 | 0.2953 | 0.8881 | 1.0951 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
