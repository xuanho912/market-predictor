# Flow / Positioning Proxy Status

Generated at: `2026-07-31T14:38:18.447287+00:00`
Latest date: `2026-07-31`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `47.64`
- overall_flow_conflict_score: `36.42`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 48.86 | 36.42 | 57.67 | 59.82 | -2.5545 | 0.2716 | 0.3081 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 48.86 | 36.42 | 57.67 | 59.82 | -1.6855 | 0.3649 | 0.4735 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 43.98 | 36.42 | 56.07 | 59.82 | -2.3893 | 0.3612 | 0.3922 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 48.86 | 36.42 | 57.67 | 59.82 | -1.9271 | 0.296 | 0.3568 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
