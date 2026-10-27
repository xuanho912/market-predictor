# Historical Replay Benchmark

Generated at: `2026-10-27T00:58:29.165609+00:00`
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
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.021592`
- secondary_mean_absolute_error: `0.020254`
- primary_error_advantage: `-0.001338`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.03026`
- secondary_mean_absolute_error: `0.030123`
- primary_error_advantage: `-0.000137`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.049029`
- secondary_mean_absolute_error: `0.046287`
- primary_error_advantage: `-0.002742`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.066483`
- secondary_mean_absolute_error: `0.051017`
- primary_error_advantage: `-0.015466`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.175`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `-0.65`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.055776`
- secondary_mean_absolute_error: `0.055593`
- primary_error_advantage: `-0.000183`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.020273`, as_primary `0`, as_primary_hit `None`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025574`, as_primary `0`, as_primary_hit `None`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.03886`, as_primary `0`, as_primary_hit `None`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.040895`, as_primary `0`, as_primary_hit `None`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.048085`, as_primary `0`, as_primary_hit `None`, avg `0.064235`, median `0.065811`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.025419`, as_primary `0`, as_primary_hit `None`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.033341`, as_primary `0`, as_primary_hit `None`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.053389`, as_primary `0`, as_primary_hit `None`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.062773`, as_primary `0`, as_primary_hit `None`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.057368`, as_primary `0`, as_primary_hit `None`, avg `0.064235`, median `0.065811`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.021592`, as_primary `80`, as_primary_hit `0.6`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.03026`, as_primary `80`, as_primary_hit `0.55`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.049029`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.066483`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.055776`, as_primary `80`, as_primary_hit `0.825`, avg `0.064235`, median `0.065811`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.019014`, as_primary `0`, as_primary_hit `None`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025409`, as_primary `0`, as_primary_hit `None`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.036825`, as_primary `0`, as_primary_hit `None`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.040161`, as_primary `0`, as_primary_hit `None`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.046906`, as_primary `0`, as_primary_hit `None`, avg `0.064235`, median `0.065811`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.021592`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.03026`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.049029`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.066483`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.055776`, avg `0.064235`, median `0.065811`

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
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4833`, primary_mae `0.02095`, avg `0.003374`, median `0.005729`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.45`, primary_mae `0.030338`, avg `-0.000236`, median `0.006365`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.046845`, avg `-0.006047`, median `-0.004065`
- 20d: sample `60`, primary_hit `0.55`, primary_closer `0.3833`, primary_mae `0.061391`, avg `-0.009011`, median `-0.012786`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.4833`, primary_mae `0.063149`, avg `0.067299`, median `0.067564`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.023519`, avg `0.006135`, median `0.018118`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.030026`, avg `0.004539`, median `0.004099`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.055581`, avg `0.007323`, median `0.016614`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.081758`, avg `-0.006046`, median `0.007553`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.65`, primary_mae `0.033659`, avg `0.055044`, median `0.059547`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.02095, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.030026, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.046845, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.061391, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.033659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019014, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025419, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.02095, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025409, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033341, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.030026, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036825, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053389, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.046845, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040161, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066483, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.061391, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': -0.65, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.046906, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057368, 'direction_hit_rate': 0.825}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.033659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.875`, primary_mae `0.015458`, avg `-0.007794`, median `-0.010431`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.014932`, avg `-0.010277`, median `-0.015512`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.019419`, avg `-0.030498`, median `-0.04277`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.038525`, avg `-0.036915`, median `-0.039553`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.875`, primary_mae `0.038367`, avg `0.021487`, median `0.034011`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.6875`, primary_mae `0.013827`, avg `-0.000435`, median `-0.00419`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.6875`, primary_mae `0.018856`, avg `-0.004799`, median `-0.011914`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.027449`, avg `-0.018975`, median `-0.035039`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.052004`, avg `-0.022647`, median `-0.025949`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.6875`, primary_mae `0.040476`, avg `0.023626`, median `0.034011`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.030771`, avg `-0.001706`, median `0.004933`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.04191`, avg `-0.0038`, median `0.00779`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.047892`, avg `0.009686`, median `0.009633`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.053465`, avg `0.007882`, median `0.001969`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.064565`, avg `0.113365`, median `0.125416`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.021592`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.03026`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.049029`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.066483`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.055776`, avg `0.064235`, median `0.065811`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.021592`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.03026`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.049029`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.066483`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.055776`, avg `0.064235`, median `0.065811`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.4833`, primary_mae `0.018968`, avg `0.005326`, median `0.009909`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5167`, primary_mae `0.02611`, avg `0.001908`, median `0.002693`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.04989`, avg `-0.006378`, median `-0.013087`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.45`, primary_mae `0.071375`, avg `-0.013177`, median `-0.021284`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.5833`, primary_mae `0.053444`, avg `0.047991`, median `0.054327`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.029464`, avg `0.000277`, median `0.004933`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.042712`, avg `-0.001893`, median `0.010244`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.046448`, avg `0.008314`, median `0.010405`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.051806`, avg `0.006453`, median `0.001969`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.062775`, avg `0.112967`, median `0.111654`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.021592`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.03026`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.049029`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.066483`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.055776`, avg `0.064235`, median `0.065811`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.65`, primary_mae `0.012885`, avg `0.00202`, median `0.002787`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.65`, primary_mae `0.017892`, avg `-0.00453`, median `-0.009221`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.030126`, avg `-0.019777`, median `-0.032362`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.051279`, avg `-0.024884`, median `-0.025949`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.7`, primary_mae `0.038129`, avg `0.023385`, median `0.02325`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.021592`, avg `0.004064`, median `0.008374`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.03026`, avg `0.000958`, median `0.005702`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.45`, primary_mae `0.049029`, avg `-0.002705`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5375`, primary_closer `0.4`, primary_mae `0.066483`, avg `-0.00827`, median `-0.009627`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.525`, primary_mae `0.055776`, avg `0.064235`, median `0.065811`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
