# Flow / Positioning Proxy Status

Generated at: `2026-10-02T17:54:38.810345+00:00`
Latest date: `2026-10-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `62.23`
- overall_flow_conflict_score: `36.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 59.66 | 36.83 | 96.31 | 51.12 | -1.8533 | 0.5958 | 0.5868 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.58 | 36.83 | 98.25 | 51.12 | -1.5436 | 0.6961 | 0.6812 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 62.75 | 36.83 | 97.32 | 51.12 | -0.7189 | 0.8276 | 0.8684 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.94 | 36.83 | 96.73 | 51.12 | -1.036 | 0.8202 | 0.7031 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
