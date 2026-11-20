# Flow / Positioning Proxy Status

Generated at: `2026-11-20T08:37:20.352042+00:00`
Latest date: `2026-11-19`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.89`
- overall_flow_conflict_score: `64.66`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 52.1 | 64.66 | 63.98 | 96.33 | 1.0499 | 1.4224 | 1.4912 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 52.1 | 64.66 | 63.98 | 96.33 | 0.8133 | 1.5842 | 1.3749 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 52.1 | 64.66 | 63.98 | 96.33 | 0.8879 | 1.331 | 1.298 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 51.27 | 64.66 | 63.71 | 96.33 | 0.4911 | 1.5146 | 1.2928 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
