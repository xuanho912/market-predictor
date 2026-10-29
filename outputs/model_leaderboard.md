# Model Leaderboard

Generated at: `2026-10-29T10:26:47.384900+00:00`
Active model: `baseline_v1`

> This is forecast model validation, not execution guidance or portfolio accounting.

## Baseline Freeze

- model_version: `baseline_v1`
- frozen_components: `['scenario ranking', 'signal confirmation', 'historical analog engine', 'FRED rates/credit', 'breadth/internal resonance', 'VIX term / VVIX / SKEW', 'flow / positioning proxy', 'forecast accuracy ledger', 'historical replay benchmark']`
- alpha_v1_threshold: `0.32534311`
- past_forecast_policy: `Past rows are immutable. Pre-freeze rows keep their original model_version.`

## Validation Standards

- high_precision_standard: `not_yet_validated`
  - 5d / 20d primary-path advantage is not yet forward validated
- stable_alpha_standard: `not_yet_validated`
  - Alpha v1 remains RESEARCH ALPHA CANDIDATE and cannot be upgraded by historical replay
- validated_forecasting_system_standard: `not_yet_validated`
  - no challenger has qualified for promotion against baseline_v1

## Best Model By Horizon

- 3d: `{'model_version': 'market_intelligence_engine_v5', 'completed_count': 4, 'primary_hit_rate': 0.0, 'primary_mean_absolute_error': 0.009736}`
- 5d: `{'model_version': 'market_intelligence_engine_v5', 'completed_count': 4, 'primary_hit_rate': 0.75, 'primary_mean_absolute_error': 0.007474}`
- 10d: `{'model_version': 'market_intelligence_engine_v5', 'completed_count': 4, 'primary_hit_rate': 0.25, 'primary_mean_absolute_error': 0.008941}`
- 20d: `{'model_version': 'market_intelligence_engine_v5', 'completed_count': 4, 'primary_hit_rate': 0.0, 'primary_mean_absolute_error': 0.031809}`
- 60d: `{'model_version': 'market_intelligence_engine_v5', 'completed_count': 4, 'primary_hit_rate': 0.0, 'primary_mean_absolute_error': 0.041192}`

## Models

### baseline_v1
- role: `active_baseline`
- status: `tracking`
- total_forecasts: `384`
- pending_forecasts: `240`
- promotion_status: `active_model`
- reason: `Frozen current production model. Not a claim of high precision or stable alpha.`
- horizon_metrics:
  - 3d: `{'completed_count': 372, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.2608, 'secondary_hit_rate': 0.3011, 'primary_vs_secondary_accuracy_spread': -0.0403, 'primary_closer_than_secondary_rate': 0.379, 'primary_mean_absolute_error': 0.016508, 'primary_median_absolute_error': 0.013026, 'secondary_mean_absolute_error': 0.012457}`
  - 5d: `{'completed_count': 364, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.2555, 'secondary_hit_rate': 0.294, 'primary_vs_secondary_accuracy_spread': -0.0385, 'primary_closer_than_secondary_rate': 0.3681, 'primary_mean_absolute_error': 0.022622, 'primary_median_absolute_error': 0.019236, 'secondary_mean_absolute_error': 0.016247}`
  - 10d: `{'completed_count': 344, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.2297, 'secondary_hit_rate': 0.3372, 'primary_vs_secondary_accuracy_spread': -0.1076, 'primary_closer_than_secondary_rate': 0.3169, 'primary_mean_absolute_error': 0.03322, 'primary_median_absolute_error': 0.028313, 'secondary_mean_absolute_error': 0.021938}`
  - 20d: `{'completed_count': 304, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.1579, 'secondary_hit_rate': 0.2796, 'primary_vs_secondary_accuracy_spread': -0.1217, 'primary_closer_than_secondary_rate': 0.3191, 'primary_mean_absolute_error': 0.056748, 'primary_median_absolute_error': 0.054029, 'secondary_mean_absolute_error': 0.039089}`
  - 60d: `{'completed_count': 144, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.1181, 'secondary_hit_rate': 0.2222, 'primary_vs_secondary_accuracy_spread': -0.1042, 'primary_closer_than_secondary_rate': 0.4097, 'primary_mean_absolute_error': 0.072699, 'primary_median_absolute_error': 0.06687, 'secondary_mean_absolute_error': 0.055605}`

### challenger_v2_error_learning
- role: `shadow_challenger`
- status: `tracking`
- total_forecasts: `368`
- pending_forecasts: `368`
- promotion_status: `insufficient_forward_evidence`
- reason: `Forward samples have not met promotion gates.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v2_event_reaction_overlay
- role: `shadow_challenger`
- status: `tracking`
- total_forecasts: `332`
- pending_forecasts: `332`
- promotion_status: `insufficient_forward_evidence`
- reason: `Forward samples have not met promotion gates.`
- horizon_metrics:
  - 3d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 5d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 10d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 20d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`
  - 60d: `{'completed_count': 0, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': None, 'secondary_hit_rate': None, 'primary_vs_secondary_accuracy_spread': None, 'primary_closer_than_secondary_rate': None, 'primary_mean_absolute_error': None, 'primary_median_absolute_error': None, 'secondary_mean_absolute_error': None}`

### challenger_v2_options_flow
- role: `shadow_challenger`
- status: `tracking`
- total_forecasts: `384`
- pending_forecasts: `384`
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
- pending_forecasts: `0`
- promotion_status: `historical_only_not_validated`
- reason: `Pre-baseline records are preserved for audit only and cannot be renamed.`
- horizon_metrics:
  - 3d: `{'completed_count': 4, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': 0.0, 'secondary_hit_rate': 0.25, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.009736, 'primary_median_absolute_error': 0.007093, 'secondary_mean_absolute_error': 0.010119}`
  - 5d: `{'completed_count': 4, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.0, 'primary_vs_secondary_accuracy_spread': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.007474, 'primary_median_absolute_error': 0.007597, 'secondary_mean_absolute_error': 0.014221}`
  - 10d: `{'completed_count': 4, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.25, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.008941, 'primary_median_absolute_error': 0.006645, 'secondary_mean_absolute_error': 0.016161}`
  - 20d: `{'completed_count': 4, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': 0.0, 'secondary_hit_rate': 0.25, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.031809, 'primary_median_absolute_error': 0.032429, 'secondary_mean_absolute_error': 0.038434}`
  - 60d: `{'completed_count': 4, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': 0.0, 'secondary_hit_rate': 0.25, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.041192, 'primary_median_absolute_error': 0.042548, 'secondary_mean_absolute_error': 0.041237}`

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
