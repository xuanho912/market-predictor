# Model Leaderboard

Generated at: `2026-06-15T10:30:26.186610+00:00`
Active model: `baseline_v1`

> This is forecast model validation, not execution guidance or portfolio accounting.

## Baseline Freeze

- model_version: `baseline_v1`
- frozen_components: `['scenario ranking', 'signal confirmation', 'historical analog engine', 'FRED rates/credit', 'breadth/internal resonance', 'VIX term / VVIX / SKEW', 'flow / positioning proxy', 'forecast accuracy ledger', 'historical replay benchmark']`
- alpha_v1_threshold: `0.32534311`
- past_forecast_policy: `Past rows are immutable. Pre-freeze rows keep their original model_version.`

## Validation Standards

- high_precision_standard: `not_yet_validated`
  - forward completed samples are below the minimum validation gate
  - MODERATE_EDGE / STRONG_EDGE samples are not yet proven better than NO_EDGE
  - 5d / 20d primary-path advantage is not yet forward validated
- stable_alpha_standard: `not_yet_validated`
  - forward-only samples are too small for stable alpha
  - Alpha v1 remains RESEARCH ALPHA CANDIDATE and cannot be upgraded by historical replay
- validated_forecasting_system_standard: `not_yet_validated`
  - forecast accuracy ledger has insufficient completed forward samples
  - no challenger has qualified for promotion against baseline_v1

## Best Model By Horizon

- 3d: `{'model_version': None, 'completed_count': 0, 'status': 'insufficient_forward_samples'}`
- 5d: `{'model_version': None, 'completed_count': 0, 'status': 'insufficient_forward_samples'}`
- 10d: `{'model_version': None, 'completed_count': 0, 'status': 'insufficient_forward_samples'}`
- 20d: `{'model_version': None, 'completed_count': 0, 'status': 'insufficient_forward_samples'}`
- 60d: `{'model_version': None, 'completed_count': 0, 'status': 'insufficient_forward_samples'}`

## Models

### baseline_v1
- role: `active_baseline`
- status: `tracking`
- total_forecasts: `4`
- pending_forecasts: `4`
- promotion_status: `active_model`
- reason: `Frozen current production model. Not a claim of high precision or stable alpha.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v2_options_flow
- role: `shadow_challenger`
- status: `tracking`
- total_forecasts: `4`
- pending_forecasts: `4`
- promotion_status: `insufficient_forward_evidence`
- reason: `Forward samples have not met promotion gates.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### market_intelligence_engine_v5
- role: `legacy_pre_baseline`
- status: `tracking`
- total_forecasts: `4`
- pending_forecasts: `4`
- promotion_status: `historical_only_not_validated`
- reason: `Pre-baseline records are preserved for audit only and cannot be renamed.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v2_put_call
- role: `registered_shadow_challenger`
- status: `blocked_missing_required_data`
- total_forecasts: `0`
- pending_forecasts: `0`
- promotion_status: `blocked_missing_required_data`
- reason: `Missing put_call_available; cannot generate this shadow forecast without stable real put/call ratio data.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v2_gamma_proxy
- role: `registered_shadow_challenger`
- status: `blocked_missing_required_data`
- total_forecasts: `0`
- pending_forecasts: `0`
- promotion_status: `blocked_missing_required_data`
- reason: `Missing gamma_available; cannot generate this shadow forecast without reliable gamma exposure source or defensible proxy.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v2_real_flow
- role: `registered_shadow_challenger`
- status: `blocked_missing_required_data`
- total_forecasts: `0`
- pending_forecasts: `0`
- promotion_status: `blocked_missing_required_data`
- reason: `Missing true_flow_available; cannot generate this shadow forecast without true flow / positioning feed.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v2_macro_event_risk
- role: `registered_shadow_challenger`
- status: `blocked_missing_required_data`
- total_forecasts: `0`
- pending_forecasts: `0`
- promotion_status: `blocked_missing_required_data`
- reason: `Missing macro_event_quality_available; cannot generate this shadow forecast without validated macro event quality data.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v3_full_options_flow
- role: `registered_shadow_challenger`
- status: `blocked_missing_required_data`
- total_forecasts: `0`
- pending_forecasts: `0`
- promotion_status: `blocked_missing_required_data`
- reason: `Missing put_call_available, gamma_available, true_flow_available, macro_event_quality_available; cannot generate this shadow forecast without all component challengers passing their own shadow validation gates.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

## Guardrails

- Alpha v1 threshold remains frozen at 0.32534311.
- Baseline v1 records are immutable except realized-outcome backfills.
- Challengers must run as shadow forecasts before replacing baseline.
- Historical replay cannot promote a model without forward validation.
- This system validates market probability paths, not execution guidance or portfolio accounting.
