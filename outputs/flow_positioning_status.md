# Flow / Positioning Proxy Status

Generated at: `2026-08-05T04:34:16.113499+00:00`
Latest date: `2026-08-04`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `74.96`
- overall_flow_conflict_score: `20.44`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 76.35 | 20.44 | 84.59 | 35.24 | 1.6794 | 1.124 | 1.4244 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 76.35 | 20.44 | 84.59 | 35.24 | 1.5347 | 1.0971 | 1.4535 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 70.8 | 20.44 | 82.77 | 35.24 | -0.2731 | 0.8127 | 0.9504 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 76.35 | 20.44 | 84.59 | 35.24 | 2.265 | 1.3922 | 1.7637 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
