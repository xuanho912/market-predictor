# Flow / Positioning Proxy Status

Generated at: `2026-11-02T21:45:02.587917+00:00`
Latest date: `2026-11-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `63.94`
- overall_flow_conflict_score: `72.48`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 64.04 | 72.48 | 77.21 | 100.0 | 0.5655 | 1.1357 | 1.207 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 65.56 | 72.48 | 77.71 | 100.0 | 0.6904 | 1.1905 | 1.323 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 65.5 | 72.48 | 77.69 | 100.0 | -0.0258 | 1.2141 | 0.9954 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 60.64 | 72.48 | 76.1 | 100.0 | -0.0168 | 1.0579 | 0.9975 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
