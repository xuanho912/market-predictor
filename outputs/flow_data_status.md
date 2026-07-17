# Flow / Positioning Proxy Status

Generated at: `2026-07-17T14:06:13.575369+00:00`
Latest date: `2026-07-17`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `56.67`
- overall_flow_conflict_score: `57.14`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 56.67 | 57.14 | 69.51 | 92.5 | -2.7849 | 0.2454 | 0.1936 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 56.67 | 57.14 | 69.51 | 92.5 | -2.6981 | 0.3838 | 0.3026 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 56.67 | 57.14 | 69.51 | 92.5 | -2.4721 | 0.2757 | 0.2209 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 56.67 | 57.14 | 69.51 | 92.5 | -1.8266 | 0.5144 | 0.3902 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
