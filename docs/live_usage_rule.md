# Live Usage Rule For Alpha Candidate v1

## Scope

`bounce_probability_top_decile_v1` is a frozen research alpha candidate. It is not a broad market direction model and it is not a crisis-warning model.

## Allowed Interpretation

- Treat the signal only as a short-to-medium-term bounce / mean-reversion candidate.
- Use it only for SPY, QQQ, IWM, and DIA.
- Evaluate only the frozen horizons: 3d, 5d, 10d, 20d, and 60d.
- Keep every live signal in the forward-only validation log.

## Prohibited Interpretation

- Do not use this signal to forecast long-term market direction.
- Do not use this signal to initiate short exposure.
- Do not use `down_probability` or `crash_probability` as a substitute for risk management.
- Do not call this a confirmed alpha because the historical walk-forward slice looked strong.
- Do not change thresholds, features, or model parameters and keep the `alpha_v1` name.

## Paper Trading Gate

The signal may enter paper trading only after forward validation shows:

- enough completed post-freeze observations across symbols,
- positive average and median returns on the primary horizons,
- acceptable hit rates after costs,
- no collapse in a specific symbol or regime,
- no evidence that the signal is merely a weaker copy of simple mean reversion.

## Paper Trading Discipline

If the signal later enters paper trading:

- limit position size,
- define invalidation conditions before entry,
- record every trade assumption,
- include transaction costs and slippage,
- keep all missed, skipped, and failed signals in the audit trail,
- version any future change as `alpha_v2` or later.
