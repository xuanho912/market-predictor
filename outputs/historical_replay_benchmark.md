# Historical Replay Benchmark

Generated at: `2026-07-24T04:37:10.854728+00:00`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.027011`
- secondary_mean_absolute_error: `0.018697`
- primary_error_advantage: `-0.008314`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.031637`
- secondary_mean_absolute_error: `0.021996`
- primary_error_advantage: `-0.009641`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.032306`
- secondary_mean_absolute_error: `0.025029`
- primary_error_advantage: `-0.007277`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.072874`
- secondary_mean_absolute_error: `0.043665`
- primary_error_advantage: `-0.029209`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.118457`
- secondary_mean_absolute_error: `0.081766`
- primary_error_advantage: `-0.036691`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.01848`, as_primary `0`, as_primary_hit `None`, avg `-0.001731`, median `0.001872`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.02117`, as_primary `0`, as_primary_hit `None`, avg `-0.001378`, median `0.001877`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.023674`, as_primary `0`, as_primary_hit `None`, avg `0.006932`, median `0.008678`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.037246`, as_primary `0`, as_primary_hit `None`, avg `0.019995`, median `0.026059`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.074359`, as_primary `0`, as_primary_hit `None`, avg `0.030618`, median `0.058049`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.019029`, as_primary `0`, as_primary_hit `None`, avg `-0.001731`, median `0.001872`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.026029`, as_primary `0`, as_primary_hit `None`, avg `-0.001378`, median `0.001877`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.027548`, as_primary `0`, as_primary_hit `None`, avg `0.006932`, median `0.008678`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.057185`, as_primary `0`, as_primary_hit `None`, avg `0.019995`, median `0.026059`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.08724`, as_primary `0`, as_primary_hit `None`, avg `0.030618`, median `0.058049`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.027011`, as_primary `80`, as_primary_hit `0.575`, avg `-0.001731`, median `0.001872`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.031637`, as_primary `80`, as_primary_hit `0.525`, avg `-0.001378`, median `0.001877`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.032306`, as_primary `80`, as_primary_hit `0.6`, avg `0.006932`, median `0.008678`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.072874`, as_primary `80`, as_primary_hit `0.7`, avg `0.019995`, median `0.026059`
- 60d: sample `80`, direction_hit `0.3125`, path_mae `0.118457`, as_primary `80`, as_primary_hit `0.6875`, avg `0.030618`, median `0.058049`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.018671`, as_primary `0`, as_primary_hit `None`, avg `-0.001731`, median `0.001872`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.021133`, as_primary `0`, as_primary_hit `None`, avg `-0.001378`, median `0.001877`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.023184`, as_primary `0`, as_primary_hit `None`, avg `0.006932`, median `0.008678`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.037026`, as_primary `0`, as_primary_hit `None`, avg `0.019995`, median `0.026059`
- 60d: sample `80`, direction_hit `0.6875`, path_mae `0.075089`, as_primary `0`, as_primary_hit `None`, avg `0.030618`, median `0.058049`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3125`, primary_mae `0.027011`, avg `-0.001731`, median `0.001872`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.031637`, avg `-0.001378`, median `0.001877`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4125`, primary_mae `0.032306`, avg `0.006932`, median `0.008678`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.3125`, primary_mae `0.072874`, avg `0.019995`, median `0.026059`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.118457`, avg `0.030618`, median `0.058049`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.031896`, avg `-0.00081`, median `0.005771`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.037751`, avg `0.002143`, median `0.001164`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.3`, primary_mae `0.043432`, avg `0.01512`, median `0.023221`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.081274`, avg `0.025661`, median `0.045498`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.152593`, avg `0.022739`, median `0.066969`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.022126`, avg `-0.002652`, median `0.001302`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.025523`, avg `-0.004899`, median `0.002038`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.021179`, avg `-0.001255`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.064474`, avg `0.014329`, median `0.020147`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.4`, primary_mae `0.084321`, avg `0.038497`, median `0.052147`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.022126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.021179, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.064474, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.084321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01848, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027011, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.022126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021133, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031637, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025523, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023184, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032306, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.021179, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037026, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072874, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.064474, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074359, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.118457, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.084321, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.022391`, avg `-0.01363`, median `-0.018199`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.025902`, avg `-0.025133`, median `-0.031479`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.012388`, avg `-0.011762`, median `-0.009593`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.057216`, avg `-0.007317`, median `-0.006533`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.083528`, avg `0.011993`, median `0.004276`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.026234`, avg `-0.006839`, median `0.000341`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.031511`, avg `-0.013914`, median `-0.006529`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.018068`, avg `-0.004444`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.069003`, avg `0.01574`, median `0.024617`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.10725`, avg `0.049448`, median `0.054967`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.034104`, avg `0.003632`, median `0.008962`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.034101`, avg `0.015533`, median `0.015645`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.037829`, avg `0.030219`, median `0.031352`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.064637`, avg `0.048117`, median `0.052213`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.137832`, avg `0.037926`, median `0.073766`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3125`, primary_mae `0.027011`, avg `-0.001731`, median `0.001872`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.031637`, avg `-0.001378`, median `0.001877`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4125`, primary_mae `0.032306`, avg `0.006932`, median `0.008678`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.3125`, primary_mae `0.072874`, avg `0.019995`, median `0.026059`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.118457`, avg `0.030618`, median `0.058049`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3125`, primary_mae `0.027011`, avg `-0.001731`, median `0.001872`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.031637`, avg `-0.001378`, median `0.001877`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.4125`, primary_mae `0.032306`, avg `0.006932`, median `0.008678`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.3125`, primary_mae `0.072874`, avg `0.019995`, median `0.026059`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.118457`, avg `0.030618`, median `0.058049`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.022126`, avg `-0.002652`, median `0.001302`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.025523`, avg `-0.004899`, median `0.002038`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.021179`, avg `-0.001255`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.35`, primary_mae `0.064474`, avg `0.014329`, median `0.020147`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.4`, primary_mae `0.084321`, avg `0.038497`, median `0.052147`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.031896`, avg `-0.00081`, median `0.005771`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.037751`, avg `0.002143`, median `0.001164`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.3`, primary_mae `0.043432`, avg `0.01512`, median `0.023221`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.081274`, avg `0.025661`, median `0.045498`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.152593`, avg `0.022739`, median `0.066969`

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
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.25`, primary_mae `0.031179`, avg `-0.004072`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.042902`, avg `-0.009801`, median `-0.007423`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.048947`, avg `0.000397`, median `0.0115`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.097466`, avg `0.00178`, median `0.014631`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.162204`, avg `-0.004543`, median `0.028631`

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
