# Flow / Positioning Proxy Status

Generated at: `2026-08-28T15:41:38.033160+00:00`
Latest date: `2026-08-28`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `69.06`
- overall_flow_conflict_score: `20.48`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 70.28 | 20.48 | 93.24 | 35.32 | -2.2749 | 0.3897 | 0.3082 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 70.28 | 20.48 | 93.24 | 35.32 | -1.8922 | 0.464 | 0.3916 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.4 | 20.48 | 91.64 | 35.32 | -2.1512 | 0.5283 | 0.4594 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 70.28 | 20.48 | 93.24 | 35.32 | -1.5066 | 0.4559 | 0.3933 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
