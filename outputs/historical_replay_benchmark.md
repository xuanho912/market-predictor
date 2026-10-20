# Historical Replay Benchmark

Generated at: `2026-10-20T01:31:00.411175+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.017176`
- secondary_mean_absolute_error: `0.016361`
- primary_error_advantage: `-0.000815`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.021146`
- secondary_mean_absolute_error: `0.018422`
- primary_error_advantage: `-0.002724`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.026018`
- secondary_mean_absolute_error: `0.023658`
- primary_error_advantage: `-0.00236`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.043633`
- secondary_mean_absolute_error: `0.026821`
- primary_error_advantage: `-0.016812`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1375`
- secondary_hit_rate: `0.8625`
- primary_vs_secondary_accuracy_spread: `-0.725`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.044046`
- secondary_mean_absolute_error: `0.042655`
- primary_error_advantage: `-0.001391`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.01667`, as_primary `0`, as_primary_hit `None`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018975`, as_primary `0`, as_primary_hit `None`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.023965`, as_primary `0`, as_primary_hit `None`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.02878`, as_primary `0`, as_primary_hit `None`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.046431`, as_primary `0`, as_primary_hit `None`, avg `0.087294`, median `0.091749`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017628`, as_primary `0`, as_primary_hit `None`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.021`, as_primary `0`, as_primary_hit `None`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.027286`, as_primary `0`, as_primary_hit `None`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.039017`, as_primary `0`, as_primary_hit `None`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.054349`, as_primary `0`, as_primary_hit `None`, avg `0.087294`, median `0.091749`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.017176`, as_primary `80`, as_primary_hit `0.55`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.021146`, as_primary `80`, as_primary_hit `0.5625`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.026018`, as_primary `80`, as_primary_hit `0.65`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.043633`, as_primary `80`, as_primary_hit `0.7875`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.044046`, as_primary `80`, as_primary_hit `0.8625`, avg `0.087294`, median `0.091749`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.016361`, as_primary `0`, as_primary_hit `None`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.018422`, as_primary `0`, as_primary_hit `None`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.023658`, as_primary `0`, as_primary_hit `None`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.026821`, as_primary `0`, as_primary_hit `None`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.042655`, as_primary `0`, as_primary_hit `None`, avg `0.087294`, median `0.091749`

## Edge Status Performance

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.022256`, avg `-0.002622`, median `-0.010472`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.026525`, avg `-0.000557`, median `-0.005714`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.035278`, avg `0.002279`, median `0.004113`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.053352`, avg `0.025945`, median `0.019809`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.055315`, avg `0.09766`, median `0.113341`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.3`, primary_closer `0.575`, primary_mae `0.012096`, avg `0.005901`, median `0.007355`
- 5d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.015767`, avg `0.008222`, median `0.011847`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.016757`, avg `0.012288`, median `0.0165`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.175`, primary_mae `0.033914`, avg `0.032776`, median `0.03415`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.525`, primary_mae `0.032777`, avg `0.076928`, median `0.084258`

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
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.022256`, avg `-0.002622`, median `-0.010472`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.026525`, avg `-0.000557`, median `-0.005714`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.035278`, avg `0.002279`, median `0.004113`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.053352`, avg `0.025945`, median `0.019809`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.055315`, avg `0.09766`, median `0.113341`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.3`, primary_closer `0.575`, primary_mae `0.012096`, avg `0.005901`, median `0.007355`
- 5d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.015767`, avg `0.008222`, median `0.011847`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.016757`, avg `0.012288`, median `0.0165`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.175`, primary_mae `0.033914`, avg `0.032776`, median `0.03415`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.525`, primary_mae `0.032777`, avg `0.076928`, median `0.084258`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.012096, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016757, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.175, 'primary_mean_absolute_error': 0.033914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.032777, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016361, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017628, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.012096, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018422, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021146, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023658, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027286, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.016757, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026821, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043633, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.175, 'primary_mean_absolute_error': 0.033914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1375, 'secondary_hit_rate': 0.8625, 'primary_vs_secondary_accuracy_spread': -0.725, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042655, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054349, 'direction_hit_rate': 0.8625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.032777, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.019283`, avg `-0.000905`, median `-0.001624`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.014644`, avg `0.00475`, median `0.008828`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017632`, avg `0.0103`, median `0.013415`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.051832`, avg `0.047185`, median `0.050926`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.049763`, avg `0.080594`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.016885`, avg `0.006072`, median `0.008014`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.017524`, avg `0.007277`, median `0.008828`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.020643`, avg `0.009984`, median `0.014434`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.044915`, avg `0.04018`, median `0.041075`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.048543`, avg `0.075344`, median `0.093308`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.023643`, avg `-0.005154`, median `-0.012312`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.025035`, avg `-0.004448`, median `-0.014292`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.019278`, avg `0.008138`, median `0.007002`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.028201`, avg `0.022831`, median `0.01416`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.064749`, avg `0.057248`, median `0.068484`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.017176`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.021146`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.026018`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, primary_hit `0.2125`, primary_closer `0.275`, primary_mae `0.043633`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4875`, primary_mae `0.044046`, avg `0.087294`, median `0.091749`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.017176`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.021146`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.026018`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, primary_hit `0.2125`, primary_closer `0.275`, primary_mae `0.043633`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4875`, primary_mae `0.044046`, avg `0.087294`, median `0.091749`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.3`, primary_closer `0.575`, primary_mae `0.012096`, avg `0.005901`, median `0.007355`
- 5d: sample `40`, primary_hit `0.325`, primary_closer `0.4`, primary_mae `0.015767`, avg `0.008222`, median `0.011847`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.016757`, avg `0.012288`, median `0.0165`
- 20d: sample `40`, primary_hit `0.15`, primary_closer `0.175`, primary_mae `0.033914`, avg `0.032776`, median `0.03415`
- 60d: sample `40`, primary_hit `0.075`, primary_closer `0.525`, primary_mae `0.032777`, avg `0.076928`, median `0.084258`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.022256`, avg `-0.002622`, median `-0.010472`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.026525`, avg `-0.000557`, median `-0.005714`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.035278`, avg `0.002279`, median `0.004113`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.053352`, avg `0.025945`, median `0.019809`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.45`, primary_mae `0.055315`, avg `0.09766`, median `0.113341`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.017176`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.021146`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.026018`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, primary_hit `0.2125`, primary_closer `0.275`, primary_mae `0.043633`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4875`, primary_mae `0.044046`, avg `0.087294`, median `0.091749`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.017176`, avg `0.00164`, median `0.003839`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.4125`, primary_mae `0.021146`, avg `0.003833`, median `0.005322`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.026018`, avg `0.007284`, median `0.011917`
- 20d: sample `80`, primary_hit `0.2125`, primary_closer `0.275`, primary_mae `0.043633`, avg `0.02936`, median `0.032626`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.4875`, primary_mae `0.044046`, avg `0.087294`, median `0.091749`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
