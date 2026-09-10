# Historical Replay Benchmark

Generated at: `2026-09-10T08:25:46.535547+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `not_proven_or_mixed`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.016173`
- secondary_mean_absolute_error: `0.012071`
- primary_error_advantage: `-0.004102`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.018079`
- secondary_mean_absolute_error: `0.014549`
- primary_error_advantage: `-0.00353`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.030414`
- secondary_mean_absolute_error: `0.022173`
- primary_error_advantage: `-0.008241`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.056674`
- secondary_mean_absolute_error: `0.033532`
- primary_error_advantage: `-0.023142`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.087958`
- secondary_mean_absolute_error: `0.058147`
- primary_error_advantage: `-0.029811`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.012203`, as_primary `0`, as_primary_hit `None`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.014869`, as_primary `0`, as_primary_hit `None`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.025316`, as_primary `0`, as_primary_hit `None`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.036218`, as_primary `0`, as_primary_hit `None`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.059138`, as_primary `0`, as_primary_hit `None`, avg `0.04334`, median `0.05856`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.014411`, as_primary `0`, as_primary_hit `None`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.017681`, as_primary `0`, as_primary_hit `None`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.036092`, as_primary `0`, as_primary_hit `None`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.052502`, as_primary `0`, as_primary_hit `None`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.069538`, as_primary `0`, as_primary_hit `None`, avg `0.04334`, median `0.05856`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.016173`, as_primary `80`, as_primary_hit `0.575`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.018079`, as_primary `80`, as_primary_hit `0.625`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.030414`, as_primary `80`, as_primary_hit `0.425`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.056674`, as_primary `80`, as_primary_hit `0.6625`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.2625`, path_mae `0.087958`, as_primary `80`, as_primary_hit `0.7375`, avg `0.04334`, median `0.05856`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.012071`, as_primary `0`, as_primary_hit `None`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.014549`, as_primary `0`, as_primary_hit `None`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.022173`, as_primary `0`, as_primary_hit `None`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.033532`, as_primary `0`, as_primary_hit `None`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, direction_hit `0.7375`, path_mae `0.058147`, as_primary `0`, as_primary_hit `None`, avg `0.04334`, median `0.05856`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.016173`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.018079`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030414`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.2875`, primary_mae `0.056674`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3`, primary_mae `0.087958`, avg `0.04334`, median `0.05856`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.013234`, avg `2.3e-05`, median `0.000609`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.3333`, primary_mae `0.014331`, avg `0.00035`, median `0.001723`
- 10d: sample `60`, primary_hit `0.6333`, primary_closer `0.3667`, primary_mae `0.025351`, avg `-0.00395`, median `-0.008001`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.2833`, primary_mae `0.05971`, avg `0.003482`, median `0.012243`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.2667`, primary_mae `0.093895`, avg `0.030861`, median `0.047025`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024991`, avg `0.00896`, median `0.010341`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.029321`, avg `0.011765`, median `0.011918`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.045601`, avg `0.021005`, median `0.019602`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.3`, primary_mae `0.047567`, avg `0.041845`, median `0.036414`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.070148`, avg `0.080777`, median `0.077217`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.013234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.014331, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.025351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070148, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012071, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016173, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.013234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014549, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018079, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3333, 'primary_mean_absolute_error': 0.014331, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022173, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036092, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.025351, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033532, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056674, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.047567, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058147, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087958, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070148, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.019442`, avg `-0.0016`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.014056`, avg `-0.007978`, median `-0.008697`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.032475`, avg `0.004226`, median `0.003189`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.064069`, avg `0.020874`, median `0.030181`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.127573`, avg `0.059214`, median `0.072376`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.018508`, avg `-0.005473`, median `-0.004159`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.017847`, avg `-0.010343`, median `-0.008697`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.028427`, avg `-0.002918`, median `-0.006514`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.059654`, avg `0.013856`, median `0.029731`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.115326`, avg `0.043117`, median `0.063523`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.009476`, avg `-0.000315`, median `-0.001535`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.010479`, avg `-0.004884`, median `-0.000876`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.025644`, avg `-0.005294`, median `-0.008001`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.072646`, avg `-0.001999`, median `0.015877`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.097228`, avg `0.033157`, median `0.060495`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.016173`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.018079`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030414`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.2875`, primary_mae `0.056674`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3`, primary_mae `0.087958`, avg `0.04334`, median `0.05856`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.016173`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.018079`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030414`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.2875`, primary_mae `0.056674`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3`, primary_mae `0.087958`, avg `0.04334`, median `0.05856`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.35`, primary_mae `0.016173`, avg `0.002258`, median `0.002198`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.3375`, primary_mae `0.018079`, avg `0.003204`, median `0.003417`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.030414`, avg `0.002289`, median `-0.006885`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.2875`, primary_mae `0.056674`, avg `0.013072`, median `0.020543`
- 60d: sample `80`, primary_hit `0.2625`, primary_closer `0.3`, primary_mae `0.087958`, avg `0.04334`, median `0.05856`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
