# Flow / Positioning Proxy Status

Generated at: `2026-07-02T23:42:22.156226+00:00`
Latest date: `2026-07-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.19`
- overall_flow_conflict_score: `61.98`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 63.62 | 61.98 | 78.59 | 91.75 | -1.1639 | 0.8193 | 0.7277 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 60.92 | 61.98 | 77.71 | 91.75 | -0.2844 | 1.109 | 0.9259 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.23 | 61.98 | 76.83 | 91.75 | -1.2834 | 0.7608 | 0.6813 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 61.99 | 61.98 | 78.06 | 91.75 | -1.7126 | 0.7243 | 0.5789 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
