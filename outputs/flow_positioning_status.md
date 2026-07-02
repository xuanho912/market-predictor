# Flow / Positioning Proxy Status

Generated at: `2026-07-02T05:12:05.170582+00:00`
Latest date: `2026-07-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `60.13`
- overall_flow_conflict_score: `46.96`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 60.58 | 46.96 | 75.33 | 70.29 | -1.1919 | 0.7918 | 0.7376 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.78 | 46.96 | 75.39 | 70.29 | -0.8453 | 0.8519 | 0.7557 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 59.95 | 46.96 | 75.12 | 70.29 | -1.421 | 0.7138 | 0.6795 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.23 | 46.96 | 74.88 | 70.29 | -1.6426 | 0.747 | 0.6139 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
