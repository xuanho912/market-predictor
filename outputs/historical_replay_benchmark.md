# Historical Replay Benchmark

Generated at: `2026-08-24T23:33:04.391349+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.019421`
- secondary_mean_absolute_error: `0.015297`
- primary_error_advantage: `-0.004124`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.020957`
- secondary_mean_absolute_error: `0.0192`
- primary_error_advantage: `-0.001757`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.028111`
- secondary_mean_absolute_error: `0.030214`
- primary_error_advantage: `0.002103`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.05608`
- secondary_mean_absolute_error: `0.039739`
- primary_error_advantage: `-0.016341`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.070203`
- secondary_mean_absolute_error: `0.055023`
- primary_error_advantage: `-0.01518`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014825`, as_primary `0`, as_primary_hit `None`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017533`, as_primary `0`, as_primary_hit `None`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.022623`, as_primary `0`, as_primary_hit `None`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.031125`, as_primary `0`, as_primary_hit `None`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.051792`, as_primary `0`, as_primary_hit `None`, avg `0.02577`, median `0.033835`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.015513`, as_primary `0`, as_primary_hit `None`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.019654`, as_primary `0`, as_primary_hit `None`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.032692`, as_primary `0`, as_primary_hit `None`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.043349`, as_primary `0`, as_primary_hit `None`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.061504`, as_primary `0`, as_primary_hit `None`, avg `0.02577`, median `0.033835`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.019421`, as_primary `80`, as_primary_hit `0.525`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020957`, as_primary `80`, as_primary_hit `0.5625`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.028111`, as_primary `80`, as_primary_hit `0.4875`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.05608`, as_primary `80`, as_primary_hit `0.625`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.070203`, as_primary `80`, as_primary_hit `0.6625`, avg `0.02577`, median `0.033835`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.014665`, as_primary `0`, as_primary_hit `None`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017294`, as_primary `0`, as_primary_hit `None`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.021523`, as_primary `0`, as_primary_hit `None`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.031533`, as_primary `0`, as_primary_hit `None`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.049054`, as_primary `0`, as_primary_hit `None`, avg `0.02577`, median `0.033835`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.019421`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.020957`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028111`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.05608`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.070203`, avg `0.02577`, median `0.033835`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.016031`, avg `0.000141`, median `0.000402`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.016841`, avg `0.001667`, median `0.001056`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.575`, primary_mae `0.028936`, avg `-0.001292`, median `-0.009582`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.068136`, avg `-0.007771`, median `-0.001572`
- 60d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.071203`, avg `-0.006079`, median `-0.003041`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.022811`, avg `0.000191`, median `0.001949`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.025073`, avg `-2.6e-05`, median `0.000311`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.027285`, avg `0.007503`, median `0.006375`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.044025`, avg `0.021023`, median `0.029731`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.069203`, avg `0.057618`, median `0.062955`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016841, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.027285, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.044025, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.069203, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014665, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019421, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017294, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020957, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016841, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021523, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032692, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.027285, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031125, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05608, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.044025, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049054, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070203, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.069203, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.024853`, avg `-0.006252`, median `0.001949`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.023852`, avg `-0.011032`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.026681`, avg `0.005548`, median `0.013417`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.056012`, avg `0.016823`, median `0.027848`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.104194`, avg `0.046649`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.028127`, avg `-0.002855`, median `0.001949`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.027381`, avg `-0.00797`, median `-0.006374`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.025604`, avg `0.007828`, median `0.009998`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.057922`, avg `0.021419`, median `0.029731`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.101576`, avg `0.044031`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.020784`, avg `0.006485`, median `0.010157`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.02608`, avg `0.00678`, median `0.004904`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.032603`, avg `0.012422`, median `0.017251`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.035388`, avg `0.026432`, median `0.028152`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.045225`, avg `0.081965`, median `0.071545`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.019421`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.020957`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028111`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.05608`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.070203`, avg `0.02577`, median `0.033835`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.019421`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.020957`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028111`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.05608`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.070203`, avg `0.02577`, median `0.033835`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.020983`, avg `-0.002336`, median `0.000402`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.020442`, avg `-0.004611`, median `0.000633`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.575`, primary_mae `0.024237`, avg `-0.003159`, median `-0.007623`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.060581`, avg `-0.001384`, median `0.009981`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.083553`, avg `0.013564`, median `0.020962`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.022811`, avg `0.000191`, median `0.001949`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.025073`, avg `-2.6e-05`, median `0.000311`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.027285`, avg `0.007503`, median `0.006375`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.044025`, avg `0.021023`, median `0.029731`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.069203`, avg `0.057618`, median `0.062955`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.019421`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.020957`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028111`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.05608`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.070203`, avg `0.02577`, median `0.033835`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4375`, primary_mae `0.019421`, avg `0.000166`, median `0.000684`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.45`, primary_mae `0.020957`, avg `0.000821`, median `0.000818`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.5`, primary_mae `0.028111`, avg `0.003106`, median `-0.001652`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.05608`, avg `0.006626`, median `0.016995`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.3875`, primary_mae `0.070203`, avg `0.02577`, median `0.033835`

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
