# Historical Replay Benchmark

Generated at: `2026-08-04T14:42:29.352562+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `not_proven_or_mixed`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.015423`
- secondary_mean_absolute_error: `0.014135`
- primary_error_advantage: `-0.001288`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.020456`
- secondary_mean_absolute_error: `0.017733`
- primary_error_advantage: `-0.002723`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.031367`
- secondary_mean_absolute_error: `0.029255`
- primary_error_advantage: `-0.002112`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.525`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.067426`
- secondary_mean_absolute_error: `0.053609`
- primary_error_advantage: `-0.013817`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.096607`
- secondary_mean_absolute_error: `0.083151`
- primary_error_advantage: `-0.013456`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.013166`, as_primary `0`, as_primary_hit `None`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.015646`, as_primary `0`, as_primary_hit `None`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.023783`, as_primary `0`, as_primary_hit `None`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.035595`, as_primary `0`, as_primary_hit `None`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.072108`, as_primary `0`, as_primary_hit `None`, avg `0.008387`, median `0.018893`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.014182`, as_primary `20`, as_primary_hit `0.5`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.017674`, as_primary `20`, as_primary_hit `0.8`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.029316`, as_primary `20`, as_primary_hit `0.4`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.051882`, as_primary `20`, as_primary_hit `0.5`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.086068`, as_primary `20`, as_primary_hit `0.3`, avg `0.008387`, median `0.018893`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.015376`, as_primary `60`, as_primary_hit `0.7`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, direction_hit `0.325`, path_mae `0.020515`, as_primary `60`, as_primary_hit `0.6333`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.031305`, as_primary `60`, as_primary_hit `0.5167`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.069154`, as_primary `60`, as_primary_hit `0.6667`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.09369`, as_primary `60`, as_primary_hit `0.6167`, avg `0.008387`, median `0.018893`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.012415`, as_primary `0`, as_primary_hit `None`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.014707`, as_primary `0`, as_primary_hit `None`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.022645`, as_primary `0`, as_primary_hit `None`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.035325`, as_primary `0`, as_primary_hit `None`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.068255`, as_primary `0`, as_primary_hit `None`, avg `0.008387`, median `0.018893`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.015423`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.020456`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.525`, primary_mae `0.031367`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.067426`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4625`, primary_mae `0.096607`, avg `0.008387`, median `0.018893`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4`, primary_closer `0.3833`, primary_mae `0.014438`, avg `-2.1e-05`, median `0.001778`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.4`, primary_mae `0.018951`, avg `0.000616`, median `0.003922`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.4833`, primary_mae `0.029021`, avg `-0.002971`, median `-0.006514`
- 20d: sample `60`, primary_hit `0.4333`, primary_closer `0.4167`, primary_mae `0.064848`, avg `-0.005198`, median `0.006152`
- 60d: sample `60`, primary_hit `0.3833`, primary_closer `0.4167`, primary_mae `0.097627`, avg `-0.001988`, median `-0.004291`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.2`, primary_closer `0.5`, primary_mae `0.018378`, avg `0.009928`, median `0.010894`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.02497`, avg `0.009158`, median `0.011214`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.65`, primary_mae `0.038404`, avg `0.016853`, median `0.016937`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.075159`, avg `0.024102`, median `0.029945`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.6`, primary_mae `0.093545`, avg `0.039514`, median `0.052729`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.014438, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018951, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.029021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.064848, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.093545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012415, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015376, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.014438, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014707, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020515, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018951, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022645, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031305, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.029021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035325, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069154, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.064848, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068255, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.09369, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.093545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.014238`, avg `0.002372`, median `0.004282`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024487`, avg `0.010834`, median `0.018318`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.052064`, avg `0.01183`, median `0.013511`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.0`, primary_mae `0.111865`, avg `0.014043`, median `0.015241`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.157522`, avg `0.047567`, median `0.06708`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.013928`, avg `0.005824`, median `0.006103`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.025554`, avg `0.009207`, median `0.014435`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.058639`, avg `0.006546`, median `0.014766`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.110998`, avg `-0.000641`, median `0.014549`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.152382`, avg `0.037111`, median `0.060238`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.5`, primary_mae `0.018137`, avg `0.008894`, median `0.010894`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.024449`, avg `0.007363`, median `0.011214`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.036356`, avg `0.016305`, median `0.016937`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.068427`, avg `0.027478`, median `0.029945`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.085834`, avg `0.032687`, median `0.03285`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.015423`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.020456`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.525`, primary_mae `0.031367`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.067426`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4625`, primary_mae `0.096607`, avg `0.008387`, median `0.018893`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.015423`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.020456`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.525`, primary_mae `0.031367`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.067426`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4625`, primary_mae `0.096607`, avg `0.008387`, median `0.018893`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.014865`, avg `-0.003106`, median `0.000402`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.4`, primary_mae `0.017017`, avg `-0.002478`, median `0.00235`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.018041`, avg `-0.004757`, median `-0.008765`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.048561`, avg `-0.002031`, median `0.000884`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.076455`, avg `-0.005946`, median `-0.019292`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.2`, primary_closer `0.5`, primary_mae `0.018378`, avg `0.009928`, median `0.010894`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.02497`, avg `0.009158`, median `0.011214`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.65`, primary_mae `0.038404`, avg `0.016853`, median `0.016937`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.075159`, avg `0.024102`, median `0.029945`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.6`, primary_mae `0.093545`, avg `0.039514`, median `0.052729`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.015423`, avg `0.002466`, median `0.004555`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.4125`, primary_mae `0.020456`, avg `0.002752`, median `0.00461`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.525`, primary_mae `0.031367`, avg `0.001985`, median `-0.001861`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.067426`, avg `0.002127`, median `0.009961`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.4625`, primary_mae `0.096607`, avg `0.008387`, median `0.018893`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.009093`, avg `-0.002088`, median `-0.00051`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.55`, primary_mae `0.008924`, avg `0.003889`, median `0.00454`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.013804`, avg `-0.00226`, median `-0.004581`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.029727`, avg `-0.001858`, median `0.000176`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.058527`, avg `-0.014294`, median `-0.024343`

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
