# Historical Replay Benchmark

Generated at: `2026-10-22T01:22:29.244648+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.016057`
- secondary_mean_absolute_error: `0.015102`
- primary_error_advantage: `-0.000955`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.021961`
- secondary_mean_absolute_error: `0.020702`
- primary_error_advantage: `-0.001259`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.040894`
- secondary_mean_absolute_error: `0.034128`
- primary_error_advantage: `-0.006766`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.045884`
- secondary_mean_absolute_error: `0.041258`
- primary_error_advantage: `-0.004626`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.065346`
- secondary_mean_absolute_error: `0.054398`
- primary_error_advantage: `-0.010948`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.0149`, as_primary `0`, as_primary_hit `None`, avg `0.005491`, median `0.010316`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.020105`, as_primary `0`, as_primary_hit `None`, avg `0.004286`, median `0.00989`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.034458`, as_primary `0`, as_primary_hit `None`, avg `0.003188`, median `0.010795`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.03525`, as_primary `0`, as_primary_hit `None`, avg `0.014122`, median `0.023203`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.051992`, as_primary `0`, as_primary_hit `None`, avg `0.060515`, median `0.06755`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.015975`, as_primary `40`, as_primary_hit `0.75`, avg `0.005491`, median `0.010316`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022771`, as_primary `40`, as_primary_hit `0.725`, avg `0.004286`, median `0.00989`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.039929`, as_primary `40`, as_primary_hit `0.625`, avg `0.003188`, median `0.010795`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.048793`, as_primary `40`, as_primary_hit `0.75`, avg `0.014122`, median `0.023203`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.055499`, as_primary `40`, as_primary_hit `0.85`, avg `0.060515`, median `0.06755`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.325`, path_mae `0.018325`, as_primary `40`, as_primary_hit `0.6`, avg `0.005491`, median `0.010316`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.023011`, as_primary `40`, as_primary_hit `0.575`, avg `0.004286`, median `0.00989`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.044341`, as_primary `40`, as_primary_hit `0.525`, avg `0.003188`, median `0.010795`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.05818`, as_primary `40`, as_primary_hit `0.625`, avg `0.014122`, median `0.023203`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.068279`, as_primary `40`, as_primary_hit `0.725`, avg `0.060515`, median `0.06755`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.014969`, as_primary `0`, as_primary_hit `None`, avg `0.005491`, median `0.010316`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.020554`, as_primary `0`, as_primary_hit `None`, avg `0.004286`, median `0.00989`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.032553`, as_primary `0`, as_primary_hit `None`, avg `0.003188`, median `0.010795`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.033779`, as_primary `0`, as_primary_hit `None`, avg `0.014122`, median `0.023203`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.051901`, as_primary `0`, as_primary_hit `None`, avg `0.060515`, median `0.06755`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.75`, primary_closer `0.575`, primary_mae `0.011768`, avg `0.009866`, median `0.013714`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.375`, primary_mae `0.02068`, avg `0.011206`, median `0.012522`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.03103`, avg `0.010313`, median `0.018774`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.575`, primary_mae `0.037165`, avg `0.021968`, median `0.030087`
- 60d: sample `40`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.037701`, avg `0.064851`, median `0.074798`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.020346`, avg `0.001116`, median `0.007933`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.023242`, avg `-0.002634`, median `0.006593`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.050758`, avg `-0.003938`, median `0.000942`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.054604`, avg `0.006276`, median `0.005514`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.092992`, avg `0.056178`, median `0.064205`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.012071`, avg `0.005098`, median `0.006729`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.022173`, avg `0.005918`, median `0.010662`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.035111`, avg `0.002113`, median `0.008378`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.033913`, avg `0.003087`, median `0.024588`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.034604`, avg `0.051692`, median `0.04783`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.020346`, avg `0.001116`, median `0.007933`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.023242`, avg `-0.002634`, median `0.006593`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.050758`, avg `-0.003938`, median `0.000942`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.054604`, avg `0.006276`, median `0.005514`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.092992`, avg `0.056178`, median `0.064205`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.75`, primary_mae `0.011466`, avg `0.014633`, median `0.020444`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.019186`, avg `0.016494`, median `0.016307`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.026949`, avg `0.018513`, median `0.028693`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.6`, primary_mae `0.040416`, avg `0.04085`, median `0.050926`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.6`, primary_mae `0.040798`, avg `0.07801`, median `0.093013`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.011466, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019186, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.026949, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.033913, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.034604, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0149, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018325, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.011466, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020105, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023011, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019186, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032553, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044341, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.026949, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033779, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05818, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.033913, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051901, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068279, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.034604, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.011301`, avg `0.015298`, median `0.021989`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.015121`, avg `0.020091`, median `0.024074`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.021157`, avg `0.021892`, median `0.036558`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.034031`, avg `0.047512`, median `0.060676`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.032927`, avg `0.079695`, median `0.093013`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.011661`, avg `0.014897`, median `0.020793`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.018607`, avg `0.017678`, median `0.016307`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.02441`, avg `0.021437`, median `0.030411`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.039023`, avg `0.042512`, median `0.03908`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.5625`, primary_mae `0.044684`, avg `0.069284`, median `0.088751`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.015335`, avg `0.00368`, median `0.010829`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.6875`, primary_mae `0.020495`, avg `0.001116`, median `0.011314`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018885`, avg `0.002639`, median `0.000568`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.030815`, avg `0.006442`, median `0.003139`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.103136`, avg `0.053829`, median `0.043938`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### low_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.016057`, avg `0.005491`, median `0.010316`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.021961`, avg `0.004286`, median `0.00989`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.040894`, avg `0.003188`, median `0.010795`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.045884`, avg `0.014122`, median `0.023203`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.065346`, avg `0.060515`, median `0.06755`

### fred_available
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_missing
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.016057`, avg `0.005491`, median `0.010316`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.021961`, avg `0.004286`, median `0.00989`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.040894`, avg `0.003188`, median `0.010795`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.045884`, avg `0.014122`, median `0.023203`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.065346`, avg `0.060515`, median `0.06755`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.75`, primary_closer `0.575`, primary_mae `0.011768`, avg `0.009866`, median `0.013714`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.375`, primary_mae `0.02068`, avg `0.011206`, median `0.012522`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.03103`, avg `0.010313`, median `0.018774`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.575`, primary_mae `0.037165`, avg `0.021968`, median `0.030087`
- 60d: sample `40`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.037701`, avg `0.064851`, median `0.074798`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.020346`, avg `0.001116`, median `0.007933`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.023242`, avg `-0.002634`, median `0.006593`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.050758`, avg `-0.003938`, median `0.000942`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.054604`, avg `0.006276`, median `0.005514`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.325`, primary_mae `0.092992`, avg `0.056178`, median `0.064205`

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
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.012071`, avg `0.005098`, median `0.006729`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.022173`, avg `0.005918`, median `0.010662`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.035111`, avg `0.002113`, median `0.008378`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.033913`, avg `0.003087`, median `0.024588`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.034604`, avg `0.051692`, median `0.04783`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.016057`, avg `0.005491`, median `0.010316`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.45`, primary_mae `0.021961`, avg `0.004286`, median `0.00989`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.4625`, primary_mae `0.040894`, avg `0.003188`, median `0.010795`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.045884`, avg `0.014122`, median `0.023203`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.4125`, primary_mae `0.065346`, avg `0.060515`, median `0.06755`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
