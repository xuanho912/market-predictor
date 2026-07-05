# Flow / Positioning Proxy Status

Generated at: `2026-07-05T16:09:17.127280+00:00`
Latest date: `2026-07-02`

## Summary

- flow_available: `True`
- flow_proxy_only: `True`
- true_flow_available: `False`
- average_flow_quality_score: `100.0`
- overall_flow_confirmation_score: `61.91`
- overall_flow_conflict_score: `61.98`

## Symbol Detail

| symbol | quality | confirmation | conflict | risk-on | risk-off | volume z | rel vol 5d | rel vol 20d | note |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SPY | 100.0 | 65.44 | 61.98 | 79.19 | 91.75 | -0.4992 | 1.0053 | 0.8929 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| QQQ | 100.0 | 61.15 | 61.98 | 77.78 | 91.75 | -0.2156 | 1.1344 | 0.9471 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| IWM | 100.0 | 58.4 | 61.98 | 76.88 | 91.75 | -1.2266 | 0.778 | 0.6967 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |
| DIA | 100.0 | 62.66 | 61.98 | 78.28 | 91.75 | -1.5013 | 0.8011 | 0.6403 | Proxy only: ETF volume, factor rotation, sector rotation, HYG/LQD, TLT and UUP. No true fund-flow or positioning feed. |

## Guardrail

- This is not true fund flow or true positioning.
- Do not use proxy flow as an execution input.
- Use it only to improve forecast scenario confirmation, conflict detection and confidence calibration.
