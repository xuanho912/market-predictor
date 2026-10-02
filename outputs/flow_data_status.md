# Flow / Positioning Proxy Status

Generated at: `2026-10-02T01:52:40.972212+00:00`
Latest date: `2026-10-01`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `66.58`
- overall_flow_conflict_score: `38.13`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.28 | 38.13 | 95.36 | 53.36 | 0.1986 | 1.0718 | 1.0593 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 68.55 | 38.13 | 97.09 | 53.36 | 0.3015 | 1.125 | 1.0764 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 67.24 | 38.13 | 96.66 | 53.36 | 2.1352 | 1.4443 | 1.4704 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 67.24 | 38.13 | 96.66 | 53.36 | 1.0289 | 1.6651 | 1.2934 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
