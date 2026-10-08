# Historical Replay Benchmark

Generated at: `2026-10-08T00:33:01.809138+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.015941`
- secondary_mean_absolute_error: `0.015348`
- primary_error_advantage: `-0.000593`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.017943`
- secondary_mean_absolute_error: `0.019861`
- primary_error_advantage: `0.001918`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.022257`
- secondary_mean_absolute_error: `0.025081`
- primary_error_advantage: `0.002824`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.044661`
- secondary_mean_absolute_error: `0.043645`
- primary_error_advantage: `-0.001016`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.9125`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.048412`
- secondary_mean_absolute_error: `0.043837`
- primary_error_advantage: `-0.004575`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014172`, as_primary `0`, as_primary_hit `None`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018258`, as_primary `0`, as_primary_hit `None`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.022574`, as_primary `0`, as_primary_hit `None`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.033239`, as_primary `0`, as_primary_hit `None`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.040408`, as_primary `0`, as_primary_hit `None`, avg `0.088511`, median `0.101639`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014924`, as_primary `20`, as_primary_hit `0.75`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.020539`, as_primary `20`, as_primary_hit `0.65`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.026725`, as_primary `20`, as_primary_hit `0.75`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.047272`, as_primary `20`, as_primary_hit `0.8`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.044255`, as_primary `20`, as_primary_hit `0.95`, avg `0.088511`, median `0.101639`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.016143`, as_primary `60`, as_primary_hit `0.4`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.017336`, as_primary `60`, as_primary_hit `0.3833`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.020738`, as_primary `60`, as_primary_hit `0.5167`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, direction_hit `0.25`, path_mae `0.045539`, as_primary `60`, as_primary_hit `0.7333`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, direction_hit `0.0875`, path_mae `0.048321`, as_primary `60`, as_primary_hit `0.9`, avg `0.088511`, median `0.101639`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.01448`, as_primary `0`, as_primary_hit `None`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.016676`, as_primary `0`, as_primary_hit `None`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.019821`, as_primary `0`, as_primary_hit `None`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.029871`, as_primary `0`, as_primary_hit `None`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.04083`, as_primary `0`, as_primary_hit `None`, avg `0.088511`, median `0.101639`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.525`, primary_mae `0.015941`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017943`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.022257`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4875`, primary_mae `0.044661`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.048412`, avg `0.088511`, median `0.101639`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.011871`, avg `0.00829`, median `0.012678`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019546`, avg `0.009507`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.025646`, avg `0.012823`, median `0.013533`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.041508`, avg `0.038432`, median `0.036235`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.45`, primary_mae `0.028097`, avg `0.095195`, median `0.099778`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.020021`, avg `-0.008586`, median `-0.010622`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.021078`, avg `-0.005507`, median `-0.005714`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.031489`, avg `-0.003067`, median `-0.006948`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.065097`, avg `-0.008393`, median `-0.016989`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.055622`, avg `0.094735`, median `0.114142`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.015935`, avg `-0.003485`, median `-0.002734`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.015574`, avg `-0.003882`, median `-0.010492`
- 10d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.015947`, avg `0.001596`, median `0.003261`
- 20d: sample `40`, primary_hit `0.125`, primary_closer `0.55`, primary_mae `0.03602`, avg `0.032032`, median `0.030725`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.475`, primary_mae `0.054964`, avg `0.082056`, median `0.088395`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011871, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015574, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.015947, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.03602, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.028097, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014172, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016143, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011871, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016676, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020539, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015574, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019821, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026725, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.015947, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029871, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047272, 'direction_hit_rate': 0.75}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.03602, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.9125, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040408, 'direction_hit_rate': 0.9125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048321, 'direction_hit_rate': 0.0875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.028097, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.01533`, avg `0.000456`, median `0.003357`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.024824`, avg `-0.000705`, median `0.002343`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.03386`, avg `0.00041`, median `0.006274`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.045157`, avg `0.033377`, median `0.040733`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.016155`, avg `0.107041`, median `0.104666`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.012051`, avg `0.007228`, median `0.012449`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.018261`, avg `0.009494`, median `0.009975`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.024834`, avg `0.012625`, median `0.016702`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.045607`, avg `0.033802`, median `0.032756`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.02017`, avg `0.101518`, median `0.104666`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.019801`, avg `-0.00852`, median `-0.010622`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.022331`, avg `-0.004212`, median `-0.005714`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.037396`, avg `0.001542`, median `0.001244`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.076622`, avg `0.002792`, median `0.0259`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.4375`, primary_mae `0.039096`, avg `0.112221`, median `0.115176`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.525`, primary_mae `0.015941`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017943`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.022257`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4875`, primary_mae `0.044661`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.048412`, avg `0.088511`, median `0.101639`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.525`, primary_mae `0.015941`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017943`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.022257`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4875`, primary_mae `0.044661`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.048412`, avg `0.088511`, median `0.101639`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.011871`, avg `0.00829`, median `0.012678`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.019546`, avg `0.009507`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.025646`, avg `0.012823`, median `0.013533`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.041508`, avg `0.038432`, median `0.036235`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.45`, primary_mae `0.028097`, avg `0.095195`, median `0.099778`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.019179`, avg `-0.0075`, median `-0.010063`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.55`, primary_mae `0.018848`, avg `-0.006024`, median `-0.010492`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.675`, primary_mae `0.0251`, avg `-0.001292`, median `-0.005399`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.65`, primary_mae `0.046961`, avg `0.013785`, median `0.026541`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.45`, primary_mae `0.064592`, avg `0.084123`, median `0.108609`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.525`, primary_mae `0.015941`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017943`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.022257`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4875`, primary_mae `0.044661`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.048412`, avg `0.088511`, median `0.101639`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.525`, primary_mae `0.015941`, avg `-0.001816`, median `-0.001142`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017943`, avg `-0.000941`, median `-0.004376`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.022257`, avg `0.003237`, median `0.003868`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.4875`, primary_mae `0.044661`, avg `0.023526`, median `0.030406`
- 60d: sample `80`, primary_hit `0.3125`, primary_closer `0.45`, primary_mae `0.048412`, avg `0.088511`, median `0.101639`

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
