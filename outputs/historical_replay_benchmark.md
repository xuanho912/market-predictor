# Historical Replay Benchmark

Generated at: `2026-11-19T02:06:29.782625+00:00`
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
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.02398`
- secondary_mean_absolute_error: `0.021124`
- primary_error_advantage: `-0.002856`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.027176`
- secondary_mean_absolute_error: `0.02463`
- primary_error_advantage: `-0.002546`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.053397`
- secondary_mean_absolute_error: `0.038224`
- primary_error_advantage: `-0.015173`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.087972`
- secondary_mean_absolute_error: `0.046953`
- primary_error_advantage: `-0.041019`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1375`
- secondary_hit_rate: `0.8625`
- primary_vs_secondary_accuracy_spread: `-0.725`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.08354`
- secondary_mean_absolute_error: `0.059698`
- primary_error_advantage: `-0.023842`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.022995`, as_primary `0`, as_primary_hit `None`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.025089`, as_primary `0`, as_primary_hit `None`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.038533`, as_primary `0`, as_primary_hit `None`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.04681`, as_primary `0`, as_primary_hit `None`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.059816`, as_primary `0`, as_primary_hit `None`, avg `0.100182`, median `0.10898`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.024249`, as_primary `0`, as_primary_hit `None`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.028082`, as_primary `0`, as_primary_hit `None`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.047448`, as_primary `0`, as_primary_hit `None`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.068671`, as_primary `0`, as_primary_hit `None`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.077022`, as_primary `0`, as_primary_hit `None`, avg `0.100182`, median `0.10898`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.02398`, as_primary `80`, as_primary_hit `0.525`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.027176`, as_primary `80`, as_primary_hit `0.4875`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.053397`, as_primary `80`, as_primary_hit `0.5875`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, direction_hit `0.25`, path_mae `0.087972`, as_primary `80`, as_primary_hit `0.75`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.08354`, as_primary `80`, as_primary_hit `0.8625`, avg `0.100182`, median `0.10898`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.021124`, as_primary `0`, as_primary_hit `None`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.02463`, as_primary `0`, as_primary_hit `None`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.038224`, as_primary `0`, as_primary_hit `None`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.046953`, as_primary `0`, as_primary_hit `None`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.059698`, as_primary `0`, as_primary_hit `None`, avg `0.100182`, median `0.10898`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.02398`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.027176`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.053397`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.2625`, primary_mae `0.087972`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.3375`, primary_mae `0.08354`, avg `0.100182`, median `0.10898`

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
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.021727`, avg `0.001497`, median `0.00162`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02448`, avg `0.007371`, median `0.000896`
- 10d: sample `40`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.052805`, avg `0.015943`, median `0.010811`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.275`, primary_mae `0.08985`, avg `0.040546`, median `0.048419`
- 60d: sample `40`, primary_hit `0.1`, primary_closer `0.35`, primary_mae `0.075371`, avg `0.114618`, median `0.104223`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.026233`, avg `0.003598`, median `0.000641`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.029873`, avg `0.001849`, median `-0.003377`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.053989`, avg `0.009293`, median `0.00796`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.25`, primary_mae `0.086095`, avg `0.027363`, median `0.039838`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.325`, primary_mae `0.091708`, avg `0.085746`, median `0.110325`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.021727, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02448, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.052805, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.086095, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.075371, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021124, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024249, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.021727, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02463, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028082, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02448, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038224, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053397, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.052805, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04681, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087972, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.086095, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1375, 'secondary_hit_rate': 0.8625, 'primary_vs_secondary_accuracy_spread': -0.725, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059698, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08354, 'direction_hit_rate': 0.1375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.075371, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020703`, avg `-0.000424`, median `-0.003865`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.021595`, avg `-0.005439`, median `-0.015102`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.047431`, avg `-0.002607`, median `-0.011075`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.070781`, avg `0.026848`, median `0.032046`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.129699`, avg `0.109967`, median `0.128694`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.025069`, avg `0.006828`, median `0.005197`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.031275`, avg `0.001453`, median `-0.006088`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.059628`, avg `0.008532`, median `0.008189`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.075519`, avg `0.028808`, median `0.038278`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.116651`, avg `0.085558`, median `0.118517`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.018897`, avg `-0.004425`, median `-0.005109`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.015575`, avg `-0.008585`, median `-0.013984`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.026819`, avg `-0.0049`, median `-0.004107`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.074596`, avg `0.029782`, median `0.035569`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.065126`, avg `0.074593`, median `0.079374`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.02398`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.027176`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.053397`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.2625`, primary_mae `0.087972`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.3375`, primary_mae `0.08354`, avg `0.100182`, median `0.10898`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.02398`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.027176`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.053397`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.2625`, primary_mae `0.087972`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.3375`, primary_mae `0.08354`, avg `0.100182`, median `0.10898`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.026233`, avg `0.003598`, median `0.000641`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.029873`, avg `0.001849`, median `-0.003377`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.35`, primary_mae `0.053989`, avg `0.009293`, median `0.00796`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.25`, primary_mae `0.086095`, avg `0.027363`, median `0.039838`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.325`, primary_mae `0.091708`, avg `0.085746`, median `0.110325`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.3667`, primary_mae `0.022337`, avg `0.001556`, median `0.000457`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.45`, primary_mae `0.025494`, avg `0.005531`, median `-0.001537`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.3333`, primary_mae `0.05064`, avg `0.013138`, median `0.010811`
- 20d: sample `60`, primary_hit `0.2333`, primary_closer `0.2667`, primary_mae `0.091606`, avg `0.035647`, median `0.045481`
- 60d: sample `60`, primary_hit `0.1`, primary_closer `0.3667`, primary_mae `0.071041`, avg `0.103383`, median `0.104223`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.02398`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.027176`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.053397`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.2625`, primary_mae `0.087972`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.3375`, primary_mae `0.08354`, avg `0.100182`, median `0.10898`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.02586`, avg `0.005221`, median `0.007232`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.030301`, avg `0.007953`, median `0.002636`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.3167`, primary_mae `0.06062`, avg `0.017366`, median `0.017994`
- 20d: sample `60`, primary_hit `0.25`, primary_closer `0.2667`, primary_mae `0.09283`, avg `0.037405`, median `0.045481`
- 60d: sample `60`, primary_hit `0.1167`, primary_closer `0.3667`, primary_mae `0.090398`, avg `0.110865`, median `0.113814`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.3875`, primary_mae `0.02398`, avg `0.002547`, median `0.00162`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.027176`, avg `0.00461`, median `-0.001537`
- 10d: sample `80`, primary_hit `0.4125`, primary_closer `0.35`, primary_mae `0.053397`, avg `0.012618`, median `0.010811`
- 20d: sample `80`, primary_hit `0.25`, primary_closer `0.2625`, primary_mae `0.087972`, avg `0.033954`, median `0.041276`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.3375`, primary_mae `0.08354`, avg `0.100182`, median `0.10898`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
