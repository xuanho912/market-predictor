# Flow / Positioning Proxy Status

Generated at: `2026-06-25T23:56:17.156150+00:00`
Latest date: `2026-06-25`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `65.21`
- overall_flow_conflict_score: `31.83`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 61.65 | 31.83 | 86.48 | 44.37 | -0.8007 | 0.6999 | 0.7781 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 63.56 | 31.83 | 87.1 | 44.37 | -0.1759 | 0.9677 | 0.9522 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 67.75 | 31.83 | 88.48 | 44.37 | -0.49 | 0.8699 | 0.8897 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 67.88 | 31.83 | 88.52 | 44.37 | -0.5137 | 0.8409 | 0.9015 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
