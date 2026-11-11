# Historical Replay Benchmark

Generated at: `2026-11-11T11:29:26.523129+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.019496`
- secondary_mean_absolute_error: `0.020476`
- primary_error_advantage: `0.00098`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.6125`
- primary_mean_absolute_error: `0.020747`
- secondary_mean_absolute_error: `0.025224`
- primary_error_advantage: `0.004477`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.0375`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.042802`
- secondary_mean_absolute_error: `0.041126`
- primary_error_advantage: `-0.001676`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.057818`
- secondary_mean_absolute_error: `0.045923`
- primary_error_advantage: `-0.011895`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.050335`
- secondary_mean_absolute_error: `0.052243`
- primary_error_advantage: `0.001908`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.018122`, as_primary `0`, as_primary_hit `None`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.021253`, as_primary `0`, as_primary_hit `None`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.030247`, as_primary `0`, as_primary_hit `None`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.03122`, as_primary `0`, as_primary_hit `None`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.036425`, as_primary `0`, as_primary_hit `None`, avg `0.051751`, median `0.06611`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.020488`, as_primary `20`, as_primary_hit `0.55`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.02503`, as_primary `20`, as_primary_hit `0.55`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.036107`, as_primary `20`, as_primary_hit `0.8`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.047355`, as_primary `20`, as_primary_hit `0.7`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.045247`, as_primary `20`, as_primary_hit `0.75`, avg `0.051751`, median `0.06611`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.019528`, as_primary `60`, as_primary_hit `0.55`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020866`, as_primary `60`, as_primary_hit `0.5667`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.046868`, as_primary `60`, as_primary_hit `0.6167`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.060037`, as_primary `60`, as_primary_hit `0.75`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, direction_hit `0.15`, path_mae `0.059017`, as_primary `60`, as_primary_hit `0.8833`, avg `0.051751`, median `0.06611`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017192`, as_primary `0`, as_primary_hit `None`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019698`, as_primary `0`, as_primary_hit `None`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.028631`, as_primary `0`, as_primary_hit `None`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.031126`, as_primary `0`, as_primary_hit `None`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.037283`, as_primary `0`, as_primary_hit `None`, avg `0.051751`, median `0.06611`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.5667`, primary_mae `0.019659`, avg `0.001162`, median `0.002094`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.6333`, primary_mae `0.021043`, avg `0.002148`, median `0.000861`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.5833`, primary_mae `0.034658`, avg `0.011377`, median `0.012736`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.4667`, primary_mae `0.051159`, avg `0.020572`, median `0.025425`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.5167`, primary_mae `0.059581`, avg `0.044117`, median `0.055914`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.019005`, avg `0.005067`, median `0.008431`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.019858`, avg `0.014461`, median `0.006467`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.067234`, avg `0.013376`, median `0.030746`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.15`, primary_mae `0.077793`, avg `0.023544`, median `0.038327`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.45`, primary_mae `0.022597`, avg `0.074653`, median `0.072384`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.019005`, avg `0.005067`, median `0.008431`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.019858`, avg `0.014461`, median `0.006467`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.067234`, avg `0.013376`, median `0.030746`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.15`, primary_mae `0.077793`, avg `0.023544`, median `0.038327`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.45`, primary_mae `0.022597`, avg `0.074653`, median `0.072384`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.022427`, avg `0.001476`, median `0.002296`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.6`, primary_mae `0.022727`, avg `0.002056`, median `-0.002209`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.625`, primary_mae `0.03259`, avg `0.015274`, median `0.016246`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.050867`, avg `0.022665`, median `0.026077`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.062318`, avg `0.045006`, median `0.062248`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.65`, primary_mae `0.014123`, avg `0.000536`, median `0.000265`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.7`, primary_mae `0.017675`, avg `0.002332`, median `0.00645`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.038793`, avg `0.003583`, median `0.005314`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.051743`, avg `0.016386`, median `0.023053`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.5`, primary_mae `0.054108`, avg `0.042339`, median `0.047138`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.014123, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.017675, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.03259, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.050867, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.022597, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017192, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020488, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.014123, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.6125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019698, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02503, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.017675, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.0375, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028631, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046868, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.03259, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031126, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060037, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.050867, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036425, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059017, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.022597, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.016951`, avg `0.008091`, median `0.016333`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.024834`, avg `0.021151`, median `0.026904`
- 10d: sample `8`, primary_hit `1.0`, primary_closer `0.875`, primary_mae `0.018861`, avg `0.04168`, median `0.04932`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.013099`, avg `0.056508`, median `0.054962`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.03108`, avg `0.071794`, median `0.065415`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020801`, avg `-0.001`, median `-0.001364`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.025519`, avg `0.005898`, median `0.006717`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.032762`, avg `0.018755`, median `0.021014`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.042301`, avg `0.027064`, median `0.033185`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.059015`, avg `0.04082`, median `0.055914`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.01943`, avg `0.002953`, median `0.004416`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.018219`, avg `0.01305`, median `0.005214`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.067362`, avg `0.010186`, median `0.034572`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.070561`, avg `0.014215`, median `0.02456`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.014451`, avg `0.075021`, median `0.072384`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5625`, primary_mae `0.019496`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.6125`, primary_mae `0.020747`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.042802`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3875`, primary_mae `0.057818`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.5`, primary_mae `0.050335`, avg `0.051751`, median `0.06611`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5625`, primary_mae `0.019496`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.6125`, primary_mae `0.020747`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.042802`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3875`, primary_mae `0.057818`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.5`, primary_mae `0.050335`, avg `0.051751`, median `0.06611`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.5667`, primary_mae `0.019659`, avg `0.001162`, median `0.002094`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.6333`, primary_mae `0.021043`, avg `0.002148`, median `0.000861`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.5833`, primary_mae `0.034658`, avg `0.011377`, median `0.012736`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.4667`, primary_mae `0.051159`, avg `0.020572`, median `0.025425`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.5167`, primary_mae `0.059581`, avg `0.044117`, median `0.055914`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.019005`, avg `0.005067`, median `0.008431`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.019858`, avg `0.014461`, median `0.006467`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.067234`, avg `0.013376`, median `0.030746`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.15`, primary_mae `0.077793`, avg `0.023544`, median `0.038327`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.45`, primary_mae `0.022597`, avg `0.074653`, median `0.072384`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5625`, primary_mae `0.019496`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.6125`, primary_mae `0.020747`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.042802`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3875`, primary_mae `0.057818`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.5`, primary_mae `0.050335`, avg `0.051751`, median `0.06611`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.5625`, primary_mae `0.019496`, avg `0.002138`, median `0.002327`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.6125`, primary_mae `0.020747`, avg `0.005226`, median `0.004111`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.042802`, avg `0.011877`, median `0.016246`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3875`, primary_mae `0.057818`, avg `0.021315`, median `0.027618`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.5`, primary_mae `0.050335`, avg `0.051751`, median `0.06611`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
