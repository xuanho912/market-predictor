# Forecast Usage Rule For Alpha Candidate v1

## Scope

`bounce_probability_top_decile_v1` is a frozen research alpha candidate. In this project it is a forecast signal and bounce-scenario input, not an execution input.

The product is a Market Prediction Dashboard. It predicts and explains broad-market probability paths; it does not automate orders, simulate orders, recommend execution, or connect to brokers.

## Allowed Interpretation

- Treat the signal only as evidence for a short-to-medium-term bounce scenario.
- Use it only for SPY, QQQ, IWM, and DIA forecast validation.
- Evaluate only the frozen horizons: 3d, 5d, 10d, 20d, and 60d.
- Keep every forecast signal in the forward-only validation log.
- Track realized forward returns, scenario hit rate, calibration quality, and whether the primary path was closer to reality than the secondary path.

## Prohibited Interpretation

- Do not treat this signal as an execution recommendation.
- Do not use this signal to forecast long-term market direction.
- Do not use `down_probability` or `crash_probability` as order triggers.
- Do not call this a confirmed alpha because a historical walk-forward slice looked strong.
- Do not change thresholds, features, or model parameters and keep the `alpha_v1` name.

## Forecast Validation Gate

The signal can only be considered a stronger forecast component after forward validation shows:

- enough completed post-freeze observations across symbols,
- stable prediction accuracy across the primary horizons,
- primary scenario hit rate better than secondary/risk paths,
- high-confidence forecasts outperforming low-confidence forecasts,
- no collapse in a specific symbol or regime,
- no evidence that the signal is merely a weaker copy of simple mean reversion.

## Forecast Discipline

Every generated forecast signal must:

- preserve the frozen Alpha v1 threshold,
- record forecast start date and forecast horizon,
- record the primary, secondary, and risk scenarios,
- define invalidation conditions before realized outcomes arrive,
- keep missed, skipped, failed, and completed forecast observations in the audit trail,
- version any future rule change as `alpha_v2` or later.
