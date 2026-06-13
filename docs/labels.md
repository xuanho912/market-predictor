# Label Definitions

Labels must be defined before collecting or adding indicators. All labels are evaluated using information after the forecast timestamp, while features must only use information available at or before the forecast timestamp.

## Return Labels

`future_return_{horizon}`:

- `future_return_1d`
- `future_return_3d`
- `future_return_5d`
- `future_return_10d`
- `future_return_20d`
- `future_return_60d`

Definition:

```text
future_return_h = close[t + h] / close[t] - 1
```

Use adjusted index levels or total-return series consistently. Do not mix price-return and total-return labels without a label version change.

## Trend Label

`trend_label` has three classes:

- `up`
- `down`
- `sideways`

Baseline definition:

```text
up       if future_return_20d >= +2.5% and realized_vol_20d is not extreme
down     if future_return_20d <= -2.5%
sideways otherwise
```

Thresholds are configuration values and must be versioned.

## Pullback Labels

- `pullback_5d`
- `pullback_20d`
- `pullback_60d`

Definition:

```text
pullback_h = max_drawdown(close[t:t+h]) <= -threshold_h
```

Use lower thresholds for shorter horizons and higher thresholds for longer horizons.

## Downside Continuation Labels

- `downside_continuation_10d`
- `downside_continuation_20d`

Definition:

```text
downside_continuation_h = prior_return_20d < 0 and future_return_h < -threshold_h
```

This label is only meaningful when the market is already in a decline or stress regime.

## Bounce Labels

- `bounce_5d`
- `bounce_10d`
- `bounce_20d`

Definition:

```text
bounce_h = prior_drawdown_20d <= -stress_threshold and future_return_h >= bounce_threshold_h
```

Bounce labels should be evaluated separately from durable trend reversals.

## Trend Reversal Labels

- `trend_reversal_20d`
- `trend_reversal_60d`

Definition:

```text
trend_reversal_h =
  prior_trend in {up, down}
  and future_trend over h changes sign
  and move exceeds reversal_threshold_h
```

Require confirmation rules to avoid labeling ordinary noise as a reversal.

## Crash and Crisis Labels

- `crash_risk_60d`
- `crash_risk_120d`
- `systemic_crisis_180d`

Baseline crash definition:

```text
crash_risk_h = max_drawdown(close[t:t+h]) <= -15%
```

Baseline systemic crisis definition:

```text
systemic_crisis_180d =
  equity_drawdown <= -20%
  and at least two of:
    credit_spread_stress
    funding_liquidity_stress
    bank_underperformance
    volatility_regime_break
    macro_growth_shock
```

All thresholds must be stored in label metadata and tested for sensitivity.
