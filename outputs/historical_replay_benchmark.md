# Historical Replay Benchmark

Generated at: `2026-10-26T18:44:22.954167+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.01754`
- secondary_mean_absolute_error: `0.015861`
- primary_error_advantage: `-0.001679`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.01959`
- secondary_mean_absolute_error: `0.016884`
- primary_error_advantage: `-0.002706`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.027525`
- secondary_mean_absolute_error: `0.025258`
- primary_error_advantage: `-0.002267`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.043043`
- secondary_mean_absolute_error: `0.040263`
- primary_error_advantage: `-0.00278`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.045971`
- secondary_mean_absolute_error: `0.044721`
- primary_error_advantage: `-0.00125`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01523`, as_primary `0`, as_primary_hit `None`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.016968`, as_primary `0`, as_primary_hit `None`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.021488`, as_primary `0`, as_primary_hit `None`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.030619`, as_primary `0`, as_primary_hit `None`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.038865`, as_primary `0`, as_primary_hit `None`, avg `0.041379`, median `0.04632`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015832`, as_primary `40`, as_primary_hit `0.575`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019038`, as_primary `40`, as_primary_hit `0.5`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.028294`, as_primary `40`, as_primary_hit `0.6`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.045341`, as_primary `40`, as_primary_hit `0.85`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.042709`, as_primary `40`, as_primary_hit `0.875`, avg `0.041379`, median `0.04632`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.017574`, as_primary `40`, as_primary_hit `0.6`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.017608`, as_primary `40`, as_primary_hit `0.65`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.027216`, as_primary `40`, as_primary_hit `0.725`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.04383`, as_primary `40`, as_primary_hit `0.575`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.048222`, as_primary `40`, as_primary_hit `0.775`, avg `0.041379`, median `0.04632`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015058`, as_primary `0`, as_primary_hit `None`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.016413`, as_primary `0`, as_primary_hit `None`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.020079`, as_primary `0`, as_primary_hit `None`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.027205`, as_primary `0`, as_primary_hit `None`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.037844`, as_primary `0`, as_primary_hit `None`, avg `0.041379`, median `0.04632`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.011803`, avg `0.002037`, median `0.005333`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.016278`, avg `0.002329`, median `0.004986`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.028417`, avg `0.00423`, median `0.007173`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.042722`, avg `0.015729`, median `0.019102`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.65`, primary_mae `0.041434`, avg `0.027671`, median `0.040761`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.019452`, avg `0.00497`, median `0.005755`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.45`, primary_mae `0.020694`, avg `0.006188`, median `0.009377`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.4167`, primary_mae `0.027228`, avg `0.014145`, median `0.011579`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.4333`, primary_mae `0.04315`, avg `0.019055`, median `0.022024`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.047483`, avg `0.045948`, median `0.052163`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.011803`, avg `0.002037`, median `0.005333`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.016278`, avg `0.002329`, median `0.004986`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.028417`, avg `0.00423`, median `0.007173`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.042722`, avg `0.015729`, median `0.019102`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.65`, primary_mae `0.041434`, avg `0.027671`, median `0.040761`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.01894`, avg `0.005974`, median `0.002901`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.026931`, avg `0.004551`, median `-0.003772`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.034214`, avg `0.017933`, median `0.014259`
- 20d: sample `20`, primary_hit `0.95`, primary_closer `0.35`, primary_mae `0.035541`, avg `0.03352`, median `0.028709`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.5`, primary_mae `0.028586`, avg `0.072656`, median `0.078007`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.019708`, avg `0.004468`, median `0.006024`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.017575`, avg `0.007007`, median `0.010334`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.4`, primary_mae `0.023734`, avg `0.012251`, median `0.011579`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.046955`, avg `0.011823`, median `0.003347`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.45`, primary_mae `0.056931`, avg `0.032594`, median `0.027512`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.011803, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.016278, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.023734, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035541, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.028586, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015058, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017574, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.011803, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016413, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019038, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.016278, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020079, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028294, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.023734, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027205, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045341, 'direction_hit_rate': 0.7125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035541, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037844, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048222, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.028586, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.011905`, avg `0.002738`, median `0.006323`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.015673`, avg `0.003635`, median `0.004986`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.030044`, avg `0.008584`, median `0.014419`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.036366`, avg `0.02459`, median `0.023499`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.041067`, avg `0.026024`, median `0.037084`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.011253`, avg `0.005612`, median `0.006547`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.015281`, avg `0.004939`, median `0.006642`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.028942`, avg `0.005282`, median `0.007954`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.042544`, avg `0.01674`, median `0.019102`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.625`, primary_mae `0.041081`, avg `0.027644`, median `0.039614`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.023469`, avg `0.003351`, median `-0.000483`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.021401`, avg `0.00347`, median `0.002887`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.031349`, avg `0.007115`, median `0.009787`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.044426`, avg `0.003933`, median `-0.004493`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.087355`, avg `0.055727`, median `0.041256`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01754`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.01959`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.027525`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.043043`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.045971`, avg `0.041379`, median `0.04632`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01754`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.01959`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.027525`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.043043`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.045971`, avg `0.041379`, median `0.04632`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.5167`, primary_mae `0.015474`, avg `0.004998`, median `0.006029`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4667`, primary_mae `0.018558`, avg `0.006528`, median `0.007155`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.027444`, avg `0.014118`, median `0.011971`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5`, primary_mae `0.04286`, avg `0.02311`, median `0.026442`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.034341`, avg `0.04192`, median `0.050464`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.023739`, avg `0.001952`, median `-0.001683`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022685`, avg `0.00131`, median `0.002887`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.027769`, avg `0.004311`, median `0.008601`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.043593`, avg `0.003566`, median `-0.004493`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.08086`, avg `0.039755`, median `0.031522`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01754`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.01959`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.027525`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.043043`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.045971`, avg `0.041379`, median `0.04632`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.475`, primary_mae `0.01754`, avg `0.004237`, median `0.005755`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4625`, primary_mae `0.01959`, avg `0.005223`, median `0.006772`
- 10d: sample `80`, primary_hit `0.4375`, primary_closer `0.4625`, primary_mae `0.027525`, avg `0.011666`, median `0.010267`
- 20d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.043043`, avg `0.018224`, median `0.019652`
- 60d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.045971`, avg `0.041379`, median `0.04632`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
