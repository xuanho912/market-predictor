# Flow / Positioning Proxy Status

Generated at: `2026-08-17T23:10:43.441503+00:00`
Latest date: `2026-08-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `75.54`
- overall_flow_conflict_score: `18.71`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 73.72 | 18.71 | 100.0 | 32.25 | -0.9933 | 0.9449 | 0.7094 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 77.33 | 18.71 | 100.0 | 32.25 | -1.0397 | 0.9326 | 0.6651 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 77.71 | 18.71 | 100.0 | 32.25 | -1.0878 | 0.9506 | 0.7081 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 73.39 | 18.71 | 100.0 | 32.25 | -0.8906 | 0.9353 | 0.6728 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
