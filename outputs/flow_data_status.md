# Flow / Positioning Proxy Status

Generated at: `2026-07-22T22:38:51.772290+00:00`
Latest date: `2026-07-22`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `55.87`
- overall_flow_conflict_score: `36.4`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 55.07 | 36.4 | 63.45 | 62.77 | -1.6906 | 0.6774 | 0.6401 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 54.29 | 36.4 | 63.19 | 62.77 | -1.7802 | 0.605 | 0.5696 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 57.13 | 36.4 | 64.12 | 62.77 | -0.6337 | 0.8513 | 0.828 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.98 | 36.4 | 64.07 | 62.77 | -0.7324 | 0.9224 | 0.814 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
