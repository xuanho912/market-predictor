# Flow / Positioning Proxy Status

Generated at: `2026-09-25T17:15:20.321319+00:00`
Latest date: `2026-09-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.83`
- overall_flow_conflict_score: `36.43`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 58.04 | 36.43 | 82.83 | 53.57 | -2.35 | 0.3749 | 0.4287 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 58.06 | 36.43 | 82.84 | 53.57 | -1.9694 | 0.4762 | 0.5685 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 53.16 | 36.43 | 81.23 | 53.57 | -2.0934 | 0.4769 | 0.5427 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 58.04 | 36.43 | 82.83 | 53.57 | -1.6016 | 0.5569 | 0.5278 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
