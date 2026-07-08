# Model Promotion Rules

Generated at: `2026-07-08T21:39:03.347132+00:00`

## Minimum Forward Sample Gates

- 3d: `>= 20` completed samples
- 5d: `>= 20` completed samples
- 10d: `>= 30` completed samples
- 20d: `>= 50` completed samples
- 60d: `>= 50` completed samples

## Required Majority Wins

- primary scenario hit rate
- primary vs secondary accuracy spread
- mean absolute path error
- median absolute path error
- high confidence accuracy
- signal confirmation top 10% performance
- edge status performance
- calibration quality
- max adverse path control

## Current Promotion Status

### challenger_v2_options_flow
- status: `insufficient_forward_evidence`
- eligible: `False`
- reason: `Forward validation sample gates are not met.`
- wins_vs_baseline: `0`
- failed_gates: `['3d', '5d', '10d', '20d', '60d']`

### challenger_v2_put_call
- status: `blocked_missing_required_data`
- eligible: `False`
- reason: `Missing put_call_available; cannot generate this shadow forecast without stable real put/call ratio data.`
- wins_vs_baseline: `0`
- failed_gates: `['put_call_available']`

### challenger_v2_gamma_proxy
- status: `blocked_missing_required_data`
- eligible: `False`
- reason: `Missing gamma_available; cannot generate this shadow forecast without reliable gamma exposure source or defensible proxy.`
- wins_vs_baseline: `0`
- failed_gates: `['gamma_available']`

### challenger_v2_real_flow
- status: `blocked_missing_required_data`
- eligible: `False`
- reason: `Missing true_flow_available; cannot generate this shadow forecast without true flow / positioning feed.`
- wins_vs_baseline: `0`
- failed_gates: `['true_flow_available']`

### challenger_v2_macro_event_risk
- status: `blocked_missing_required_data`
- eligible: `False`
- reason: `Missing macro_event_quality_available; cannot generate this shadow forecast without validated macro event quality data.`
- wins_vs_baseline: `0`
- failed_gates: `['macro_event_quality_available']`

### challenger_v2_error_learning
- status: `insufficient_forward_evidence`
- eligible: `False`
- reason: `Forward validation sample gates are not met.`
- wins_vs_baseline: `0`
- failed_gates: `['3d', '5d', '10d', '20d', '60d']`

### challenger_v2_event_reaction_overlay
- status: `insufficient_forward_evidence`
- eligible: `False`
- reason: `Forward validation sample gates are not met.`
- wins_vs_baseline: `0`
- failed_gates: `['3d', '5d', '10d', '20d', '60d']`

### challenger_v3_full_options_flow
- status: `blocked_missing_required_data`
- eligible: `False`
- reason: `Missing put_call_available, gamma_available, true_flow_available, macro_event_quality_available; cannot generate this shadow forecast without all component challengers passing their own shadow validation gates.`
- wins_vs_baseline: `0`
- failed_gates: `['put_call_available', 'gamma_available', 'true_flow_available', 'macro_event_quality_available']`

## Validation Standards

- high_precision_standard: `not_yet_validated`
  - forward completed samples are below the minimum validation gate
  - MODERATE_EDGE / STRONG_EDGE samples are not yet proven better than NO_EDGE
  - 5d / 20d primary-path advantage is not yet forward validated
- stable_alpha_standard: `not_yet_validated`
  - Alpha v1 remains RESEARCH ALPHA CANDIDATE and cannot be upgraded by historical replay
- validated_forecasting_system_standard: `not_yet_validated`
  - forecast accuracy ledger has insufficient completed forward samples
  - no challenger has qualified for promotion against baseline_v1
## Non-Negotiable Rules

- Alpha v1 threshold remains frozen at 0.32534311.
- Baseline v1 records are immutable except realized-outcome backfills.
- Challengers must run as shadow forecasts before replacing baseline.
- Historical replay cannot promote a model without forward validation.
- This system validates market probability paths, not execution guidance or portfolio accounting.
- If a challenger only wins one horizon while degrading others, it cannot be promoted.
- Historical replay can create research priority, not active-model promotion.
- Only forward validation can promote a challenger to active_model.
