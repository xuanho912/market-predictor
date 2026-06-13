# Label Definitions

Define labels before adding data. Keep threshold versions in metadata.

## Mandatory Labels

- `future_return_1d`
- `future_return_3d`
- `future_return_5d`
- `future_return_10d`
- `future_return_20d`
- `future_return_60d`
- `trend_label`
- `pullback_5d`
- `pullback_20d`
- `pullback_60d`
- `downside_continuation_10d`
- `downside_continuation_20d`
- `bounce_5d`
- `bounce_10d`
- `bounce_20d`
- `trend_reversal_20d`
- `trend_reversal_60d`
- `crash_risk_60d`
- `crash_risk_120d`
- `systemic_crisis_180d`

## Implementation Rules

- Use forward returns only for labels, never features.
- Shift labels forward after all features are timestamped.
- Purge or embargo overlapping samples when needed.
- Store label version, thresholds, horizon, and close convention.
- Evaluate bounce and reversal separately.
- Evaluate crash risk and systemic crisis separately.

## Suggested Baselines

`future_return_h`:

```text
close[t + h] / close[t] - 1
```

`pullback_h`:

```text
max_drawdown(close[t:t+h]) <= -threshold_h
```

`bounce_h`:

```text
prior_drawdown_20d <= -stress_threshold
and future_return_h >= bounce_threshold_h
```

`crash_risk_h`:

```text
max_drawdown(close[t:t+h]) <= -15%
```
