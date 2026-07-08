# Historical Replay Benchmark

Generated at: `2026-07-08T21:39:03.322855+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.014558`
- secondary_mean_absolute_error: `0.012941`
- primary_error_advantage: `-0.001617`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.018167`
- secondary_mean_absolute_error: `0.015246`
- primary_error_advantage: `-0.002921`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.023419`
- secondary_mean_absolute_error: `0.021129`
- primary_error_advantage: `-0.00229`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.042939`
- secondary_mean_absolute_error: `0.050137`
- primary_error_advantage: `0.007198`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.062909`
- secondary_mean_absolute_error: `0.054585`
- primary_error_advantage: `-0.008324`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.013115`, as_primary `0`, as_primary_hit `None`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.015993`, as_primary `0`, as_primary_hit `None`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.019947`, as_primary `0`, as_primary_hit `None`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.029009`, as_primary `0`, as_primary_hit `None`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.053222`, as_primary `0`, as_primary_hit `None`, avg `0.016077`, median `0.021735`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014558`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.018167`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.023419`, as_primary `80`, as_primary_hit `0.475`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.042939`, as_primary `80`, as_primary_hit `0.6875`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.062909`, as_primary `80`, as_primary_hit `0.575`, avg `0.016077`, median `0.021735`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.013223`, as_primary `0`, as_primary_hit `None`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.01578`, as_primary `0`, as_primary_hit `None`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.023337`, as_primary `0`, as_primary_hit `None`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.062362`, as_primary `0`, as_primary_hit `None`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, direction_hit `0.425`, path_mae `0.064771`, as_primary `0`, as_primary_hit `None`, avg `0.016077`, median `0.021735`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.012795`, as_primary `0`, as_primary_hit `None`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.015079`, as_primary `0`, as_primary_hit `None`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.018962`, as_primary `0`, as_primary_hit `None`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.029366`, as_primary `0`, as_primary_hit `None`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, direction_hit `0.575`, path_mae `0.051308`, as_primary `0`, as_primary_hit `None`, avg `0.016077`, median `0.021735`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.014279`, avg `-0.000989`, median `-0.001297`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.019888`, avg `-0.001796`, median `-0.000554`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.027969`, avg `-0.001642`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.6`, primary_closer `0.75`, primary_mae `0.048173`, avg `-0.004668`, median `0.005514`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.064761`, avg `-0.009562`, median `-0.014755`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.014836`, avg `0.00041`, median `0.00217`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.4`, primary_mae `0.016446`, avg `-0.001874`, median `0.001606`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.018868`, avg `0.003134`, median `-7.9e-05`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.037706`, avg `0.017386`, median `0.020913`
- 60d: sample `40`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.061057`, avg `0.041715`, median `0.052162`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.008589`, avg `-0.001519`, median `-0.001297`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.65`, primary_mae `0.010693`, avg `-0.001297`, median `0.001088`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.01537`, avg `-0.007083`, median `-0.008952`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.7`, primary_mae `0.040765`, avg `-0.009691`, median `-0.005516`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.055886`, avg `-0.016172`, median `-0.025523`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.016547`, avg `0.00012`, median `0.001778`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.020658`, avg `-0.002014`, median `-0.000848`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.026102`, avg `0.003356`, median `0.001752`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.4667`, primary_mae `0.043664`, avg `0.011709`, median `0.018375`
- 60d: sample `60`, primary_hit `0.6333`, primary_closer `0.3833`, primary_mae `0.065251`, avg `0.026826`, median `0.041234`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.008589, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.010693, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.01537, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.040765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.055886, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012795, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014558, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.008589, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015079, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018167, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.010693, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018962, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023419, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.01537, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029009, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062362, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.040765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051308, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064771, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.055886, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.021792`, avg `-0.014051`, median `-0.008899`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024863`, avg `-0.017492`, median `-0.014548`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.024002`, avg `-0.006656`, median `-0.00918`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.125`, primary_mae `0.044372`, avg `0.01926`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.066675`, avg `0.061772`, median `0.076071`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.018793`, avg `-0.00612`, median `-0.001735`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.021178`, avg `-0.010974`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021728`, avg `0.000329`, median `-0.003208`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.037582`, avg `0.028336`, median `0.031427`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.4375`, primary_mae `0.057942`, avg `0.072748`, median `0.093846`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.020453`, avg `-0.002653`, median `-0.005902`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.031454`, avg `-0.006684`, median `-0.013748`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.04359`, avg `0.001133`, median `-0.00374`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.875`, primary_mae `0.053423`, avg `0.003117`, median `0.009478`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.069685`, avg `0.004431`, median `-0.011052`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.014558`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.018167`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023419`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.525`, primary_mae `0.042939`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.3875`, primary_mae `0.062909`, avg `0.016077`, median `0.021735`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.014558`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.018167`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023419`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.525`, primary_mae `0.042939`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.3875`, primary_mae `0.062909`, avg `0.016077`, median `0.021735`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.014558`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.018167`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023419`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.525`, primary_mae `0.042939`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.3875`, primary_mae `0.062909`, avg `0.016077`, median `0.021735`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5125`, primary_closer `0.425`, primary_mae `0.014558`, avg `-0.00029`, median `0.000463`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.018167`, avg `-0.001835`, median `0.000448`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.4875`, primary_mae `0.023419`, avg `0.000746`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.525`, primary_mae `0.042939`, avg `0.006359`, median `0.013418`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.3875`, primary_mae `0.062909`, avg `0.016077`, median `0.021735`

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
