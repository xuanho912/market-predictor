# Model Leaderboard

Generated at: `2026-09-11T01:02:30.160040+00:00`
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
  - Alpha v1 remains RESEARCH ALPHA CANDIDATE and cannot be upgraded by historical replay
- validated_forecasting_system_standard: `not_yet_validated`
  - forecast accuracy ledger has insufficient completed forward samples
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
- total_forecasts: `248`
- pending_forecasts: `240`
- promotion_status: `active_model`
- reason: `Frozen current production model. Not a claim of high precision or stable alpha.`
- horizon_metrics:
  - 3d: `{'completed_count': 236, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.2585, 'secondary_hit_rate': 0.3432, 'primary_vs_secondary_accuracy_spread': -0.0847, 'primary_closer_than_secondary_rate': 0.3983, 'primary_mean_absolute_error': 0.016042, 'primary_median_absolute_error': 0.012132, 'secondary_mean_absolute_error': 0.012577}`
  - 5d: `{'completed_count': 228, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.2325, 'secondary_hit_rate': 0.307, 'primary_vs_secondary_accuracy_spread': -0.0746, 'primary_closer_than_secondary_rate': 0.3904, 'primary_mean_absolute_error': 0.022381, 'primary_median_absolute_error': 0.0176, 'secondary_mean_absolute_error': 0.016435}`
  - 10d: `{'completed_count': 208, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.2067, 'secondary_hit_rate': 0.3365, 'primary_vs_secondary_accuracy_spread': -0.1298, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.034719, 'primary_median_absolute_error': 0.029068, 'secondary_mean_absolute_error': 0.022205}`
  - 20d: `{'completed_count': 168, 'sample_gate': 'stronger_evidence', 'primary_hit_rate': 0.1071, 'secondary_hit_rate': 0.2857, 'primary_vs_secondary_accuracy_spread': -0.1786, 'primary_closer_than_secondary_rate': 0.2381, 'primary_mean_absolute_error': 0.061512, 'primary_median_absolute_error': 0.063114, 'secondary_mean_absolute_error': 0.035066}`
  - 60d: `{'completed_count': 8, 'sample_gate': 'insufficient_samples', 'primary_hit_rate': 0.0, 'secondary_hit_rate': 0.25, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.064784, 'primary_median_absolute_error': 0.052891, 'secondary_mean_absolute_error': 0.037988}`

### challenger_v2_error_learning
- role: `shadow_challenger`
- status: `tracking`
- total_forecasts: `232`
- pending_forecasts: `232`
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
- total_forecasts: `196`
- pending_forecasts: `196`
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
- total_forecasts: `248`
- pending_forecasts: `248`
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
