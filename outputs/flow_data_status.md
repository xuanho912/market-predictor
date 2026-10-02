# Flow / Positioning Proxy Status

Generated at: `2026-10-02T01:37:08.676079+00:00`
Latest date: `2026-10-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.59`
- overall_flow_conflict_score: `38.13`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 67.24 | 38.13 | 96.66 | 53.36 | 1.7921 | 1.4432 | 1.4132 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.98 | 38.13 | 96.24 | 53.36 | -0.4751 | 0.9244 | 0.896 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 61.27 | 38.13 | 94.7 | 53.36 | -0.4655 | 0.875 | 0.912 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 59.87 | 38.13 | 94.24 | 53.36 | -0.8071 | 0.9153 | 0.7846 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
