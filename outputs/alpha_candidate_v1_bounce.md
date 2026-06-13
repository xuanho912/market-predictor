# Alpha Candidate v1: Bounce Probability Top Decile

## Frozen Signal

- Signal name: `bounce_probability_top_decile_v1`
- Version: `alpha_v1`
- Frozen on: 2026-06-13
- Frozen threshold used for forward validation: `0.32534311`
- Threshold source: 90th percentile of unique symbol-date `bounce_probability` values from the historical walk-forward prediction log available at freeze time.

## Signal Definition

When a supported symbol's `bounce_probability` is in the top decile of the frozen historical walk-forward prediction distribution, generate a long-bounce candidate signal.

This is a short-to-medium-term bounce / mean-reversion research signal. It is not a long-term direction signal and it is not a crisis-warning signal.

## Instruments

- SPY
- QQQ
- IWM
- DIA

## Observation Horizons

- 3d
- 5d
- 10d
- 20d
- 60d

## Prohibited Changes

- Do not reselect the threshold.
- Do not retune the model.
- Do not modify the rule because future performance is poor.
- Do not add new features and claim the result is still `alpha_v1`.
- Do not use future data to recompute the threshold.
- Do not use `down_probability` or `crash_probability` as part of this alpha.

## Current Status

`RESEARCH ALPHA CANDIDATE`

This candidate is not a stable tradable alpha. It must pass forward-only validation before paper trading is considered.
