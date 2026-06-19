# Historical Replay Benchmark

Generated at: `2026-06-19T00:14:33.947132+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.015712`
- secondary_mean_absolute_error: `0.013384`
- primary_error_advantage: `-0.002328`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.018883`
- secondary_mean_absolute_error: `0.017828`
- primary_error_advantage: `-0.001055`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.02881`
- secondary_mean_absolute_error: `0.023964`
- primary_error_advantage: `-0.004846`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.051367`
- secondary_mean_absolute_error: `0.045861`
- primary_error_advantage: `-0.005506`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.061009`
- secondary_mean_absolute_error: `0.059522`
- primary_error_advantage: `-0.001487`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.013802`, as_primary `0`, as_primary_hit `None`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.017366`, as_primary `0`, as_primary_hit `None`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.022881`, as_primary `0`, as_primary_hit `None`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.030609`, as_primary `0`, as_primary_hit `None`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.049586`, as_primary `0`, as_primary_hit `None`, avg `0.023666`, median `0.032753`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.015217`, as_primary `40`, as_primary_hit `0.525`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.019446`, as_primary `40`, as_primary_hit `0.525`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.025935`, as_primary `40`, as_primary_hit `0.425`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.044396`, as_primary `40`, as_primary_hit `0.6`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.062487`, as_primary `40`, as_primary_hit `0.55`, avg `0.023666`, median `0.032753`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.013879`, as_primary `40`, as_primary_hit `0.575`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.017357`, as_primary `40`, as_primary_hit `0.525`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027966`, as_primary `40`, as_primary_hit `0.525`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.058365`, as_primary `40`, as_primary_hit `0.7`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.061508`, as_primary `40`, as_primary_hit `0.7`, avg `0.023666`, median `0.032753`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.013071`, as_primary `0`, as_primary_hit `None`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.016261`, as_primary `0`, as_primary_hit `None`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.021487`, as_primary `0`, as_primary_hit `None`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.029346`, as_primary `0`, as_primary_hit `None`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.04845`, as_primary `0`, as_primary_hit `None`, avg `0.023666`, median `0.032753`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015712`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018883`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02881`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.051367`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.061009`, avg `0.023666`, median `0.032753`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.012075`, avg `0.003297`, median `0.004273`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.018933`, avg `0.002489`, median `0.00548`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.031815`, avg `-0.001131`, median `0.002638`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.067477`, avg `-0.006365`, median `0.004456`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.06917`, avg `-0.002772`, median `-0.00576`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.01935`, avg `0.00058`, median `0.000418`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.018832`, avg `-0.00193`, median `-0.004234`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.025804`, avg `0.002287`, median `-0.00223`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.275`, primary_mae `0.035257`, avg `0.014554`, median `0.018729`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.052848`, avg `0.050104`, median `0.068676`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012075, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018832, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.025804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.035257, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.052848, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013071, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015217, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012075, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016261, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019446, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018832, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021487, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027966, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.025804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029346, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058365, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.035257, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04845, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062487, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.052848, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.012911`, avg `-0.007525`, median `-0.006094`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.011872`, avg `-0.014321`, median `-0.014993`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015178`, avg `0.007866`, median `0.006918`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.019757`, avg `0.026213`, median `0.028979`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.0463`, avg `0.060567`, median `0.073193`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.019189`, avg `-0.000697`, median `0.002901`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.01648`, avg `-0.006766`, median `-0.010753`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015337`, avg `0.004651`, median `0.00206`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.022335`, avg `0.025369`, median `0.028445`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.048012`, avg `0.055638`, median `0.06667`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.015551`, avg `0.005487`, median `0.009853`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.022402`, avg `0.003385`, median `0.010985`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.039492`, avg `-0.005765`, median `-0.001926`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.097415`, avg `-0.013095`, median `-0.000686`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.08346`, avg `0.020501`, median `0.0031`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015712`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018883`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02881`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.051367`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.061009`, avg `0.023666`, median `0.032753`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015712`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018883`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02881`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.051367`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.061009`, avg `0.023666`, median `0.032753`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.014484`, avg `0.002161`, median `0.002578`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.018559`, avg `0.001757`, median `0.002655`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.027709`, avg `-0.000675`, median `-0.004932`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.041172`, avg `-0.001072`, median `0.005284`
- 60d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.055324`, avg `0.010983`, median `0.02685`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.01694`, avg `0.001716`, median `0.004084`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.019206`, avg `-0.001199`, median `0.000733`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.02991`, avg `0.001831`, median `0.003601`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.061563`, avg `0.009262`, median `0.025671`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.066694`, avg `0.036348`, median `0.051141`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015712`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018883`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02881`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.051367`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.061009`, avg `0.023666`, median `0.032753`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.015712`, avg `0.001938`, median `0.003268`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018883`, avg `0.000279`, median `0.001938`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02881`, avg `0.000578`, median `-0.001708`
- 20d: sample `80`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.051367`, avg `0.004095`, median `0.01579`
- 60d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.061009`, avg `0.023666`, median `0.032753`

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
