# Flow / Positioning Proxy Status

Generated at: `2026-07-08T14:43:27.804280+00:00`
Latest date: `2026-07-08`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `51.37`
- overall_flow_conflict_score: `47.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 51.37 | 47.83 | 66.8 | 70.88 | -2.8337 | 0.2264 | 0.1854 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 51.37 | 47.83 | 66.8 | 70.88 | -2.4618 | 0.2803 | 0.227 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 51.37 | 47.83 | 66.8 | 70.88 | -2.2941 | 0.3348 | 0.2361 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 51.37 | 47.83 | 66.8 | 70.88 | -2.3121 | 0.3764 | 0.2647 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
