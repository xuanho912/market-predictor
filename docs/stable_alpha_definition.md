# Stable Alpha Definition

Stable alpha is not a single good historical replay, a one-off backtest, or a visually persuasive dashboard. In this project it means a forecast component has shown repeatable forward-only information advantage after the rule and model version were frozen.

## Stable Alpha Standard

A forecast component or model can be considered stable alpha only when:

- Forward-only samples are sufficient.
- At least one core horizon remains stable after enough observations mature.
- The result is not driven by only one symbol.
- The signal does not completely fail in most market regimes.
- Performance is not dominated by a few extreme outliers.
- Primary / secondary scenario ranking shows stable information advantage.
- Confidence level has positive relationship with realized performance.
- Overfitting risk is controlled through versioned challenger comparison.
- Model upgrades are fully traceable.
- Historical replay is treated as research context, not proof.

## Minimum Forward Evidence

The minimum sample gate is:

- `3d` completed samples >= 20
- `5d` completed samples >= 20
- `10d` completed samples >= 30
- `20d` completed samples >= 50
- `60d` completed samples >= 50, preferably 100+

Stable alpha also requires cross-checks:

- By symbol: SPY / QQQ / IWM / DIA
- By horizon: 3d / 5d / 10d / 20d / 60d
- By regime: risk-on, risk-off, oversold bounce, recovery, panic, sideways
- By confidence bucket
- By signal confirmation bucket
- By data completeness bucket

## Alpha v1 Status

Alpha v1 remains:

```text
RESEARCH ALPHA CANDIDATE
```

Frozen rule:

- Signal: `bounce_probability_top_decile_v1`
- Threshold: `0.32534311`
- Use: bounce scenario input / forecast signal only

Alpha v1 must not be upgraded to confirmed alpha unless forward-only evidence satisfies the stable alpha standard. Historical replay, historical analogs, or one strong historical period are not enough.

## Current Status

Current status: `not_yet_validated`.

Reason:

- Forward completed samples are insufficient.
- `baseline_v1` has no matured forward sample set yet.
- No challenger has passed promotion gates against `baseline_v1`.

## Non-Goals

Stable alpha does not mean:

- Trading automation.
- Execution recommendation.
- Position sizing.
- Broker integration.
- Paper portfolio accounting.

This project validates market probability paths only.

