# Historical Replay Benchmark

Generated at: `2026-08-03T15:24:04.971505+00:00`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.017575`
- secondary_mean_absolute_error: `0.015885`
- primary_error_advantage: `-0.00169`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.022289`
- secondary_mean_absolute_error: `0.018064`
- primary_error_advantage: `-0.004225`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3625`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.033734`
- secondary_mean_absolute_error: `0.025405`
- primary_error_advantage: `-0.008329`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.064505`
- secondary_mean_absolute_error: `0.052316`
- primary_error_advantage: `-0.012189`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.097325`
- secondary_mean_absolute_error: `0.08251`
- primary_error_advantage: `-0.014815`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.015659`, as_primary `0`, as_primary_hit `None`, avg `0.000712`, median `0.000983`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.017569`, as_primary `0`, as_primary_hit `None`, avg `0.000313`, median `0.002728`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.021684`, as_primary `0`, as_primary_hit `None`, avg `0.00197`, median `-0.006304`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.034622`, as_primary `0`, as_primary_hit `None`, avg `0.006879`, median `0.007717`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.067321`, as_primary `0`, as_primary_hit `None`, avg `0.008614`, median `0.015082`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017232`, as_primary `20`, as_primary_hit `0.55`, avg `0.000712`, median `0.000983`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.020913`, as_primary `20`, as_primary_hit `0.7`, avg `0.000313`, median `0.002728`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.029462`, as_primary `20`, as_primary_hit `0.2`, avg `0.00197`, median `-0.006304`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.057393`, as_primary `20`, as_primary_hit `0.3`, avg `0.006879`, median `0.007717`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.082384`, as_primary `20`, as_primary_hit `0.4`, avg `0.008614`, median `0.015082`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.017128`, as_primary `60`, as_primary_hit `0.55`, avg `0.000712`, median `0.000983`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.02204`, as_primary `60`, as_primary_hit `0.5667`, avg `0.000313`, median `0.002728`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.032198`, as_primary `60`, as_primary_hit `0.5`, avg `0.00197`, median `-0.006304`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.065681`, as_primary `60`, as_primary_hit `0.65`, avg `0.006879`, median `0.007717`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.099786`, as_primary `60`, as_primary_hit `0.6167`, avg `0.008614`, median `0.015082`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.014969`, as_primary `0`, as_primary_hit `None`, avg `0.000712`, median `0.000983`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.016885`, as_primary `0`, as_primary_hit `None`, avg `0.000313`, median `0.002728`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.021149`, as_primary `0`, as_primary_hit `None`, avg `0.00197`, median `-0.006304`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.034933`, as_primary `0`, as_primary_hit `None`, avg `0.006879`, median `0.007717`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.067491`, as_primary `0`, as_primary_hit `None`, avg `0.008614`, median `0.015082`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.021154`, avg `-0.005927`, median `-0.00023`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.023806`, avg `-0.01222`, median `-0.002934`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.4`, primary_mae `0.018803`, avg `-0.010729`, median `-0.010944`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.065405`, avg `-0.004193`, median `-0.001662`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.09654`, avg `0.004561`, median `0.005177`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.016383`, avg `0.002925`, median `0.001383`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.3667`, primary_mae `0.021783`, avg `0.004491`, median `0.00461`
- 10d: sample `60`, primary_hit `0.3`, primary_closer `0.3833`, primary_mae `0.038711`, avg `0.006203`, median `-0.000717`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.4`, primary_mae `0.064206`, avg `0.010569`, median `0.0112`
- 60d: sample `60`, primary_hit `0.3667`, primary_closer `0.4`, primary_mae `0.097587`, avg `0.009964`, median `0.029534`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.45`, primary_mae `0.015956`, avg `-0.00122`, median `0.000402`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.3833`, primary_mae `0.017585`, avg `-0.001256`, median `0.002073`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.026447`, avg `-0.004606`, median `-0.008492`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.4667`, primary_mae `0.061829`, avg `-0.005522`, median `-0.001662`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.5167`, primary_mae `0.09254`, avg `-0.007591`, median `-0.003444`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.022435`, avg `0.006509`, median `0.009444`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.036401`, avg `0.005021`, median `0.009055`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.055595`, avg `0.021698`, median `0.027594`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.072536`, avg `0.044082`, median `0.047846`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.11168`, avg `0.057228`, median `0.072959`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015956, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.017585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.026447, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.061829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.09254, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014969, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017232, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015956, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016885, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02204, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.017585, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021149, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032198, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.026447, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034622, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065681, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.061829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067321, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.099786, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.09254, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.014843`, avg `-0.017072`, median `-0.016048`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.020318`, avg `-0.02328`, median `-0.019178`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.015878`, avg `-0.01468`, median `-0.016542`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065804`, avg `-0.011897`, median `-0.006591`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.096399`, avg `-0.006141`, median `-0.021705`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.021528`, avg `-0.00798`, median `-0.003521`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024936`, avg `-0.013215`, median `-0.002011`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.018733`, avg `-0.010703`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.06359`, avg `-0.007255`, median `-0.001662`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.09492`, avg `0.001181`, median `0.005177`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.021763`, avg `0.007474`, median `0.009444`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.034153`, avg `0.006926`, median `0.009055`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.054367`, avg `0.026059`, median `0.027594`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.067401`, avg `0.044679`, median `0.047846`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.113632`, avg `0.059784`, median `0.084587`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.017575`, avg `0.000712`, median `0.000983`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.3625`, primary_mae `0.022289`, avg `0.000313`, median `0.002728`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.033734`, avg `0.00197`, median `-0.006304`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.4125`, primary_mae `0.064505`, avg `0.006879`, median `0.007717`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.097325`, avg `0.008614`, median `0.015082`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.017575`, avg `0.000712`, median `0.000983`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.3625`, primary_mae `0.022289`, avg `0.000313`, median `0.002728`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.033734`, avg `0.00197`, median `-0.006304`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.4125`, primary_mae `0.064505`, avg `0.006879`, median `0.007717`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.097325`, avg `0.008614`, median `0.015082`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.325`, primary_mae `0.017463`, avg `-0.003421`, median `0.000402`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.3`, primary_mae `0.017959`, avg `-0.005944`, median `0.001032`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.019304`, avg `-0.010903`, median `-0.011907`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.050347`, avg `-0.00777`, median `-0.005975`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.6`, primary_mae `0.071219`, avg `-0.000181`, median `-0.004291`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.022435`, avg `0.006509`, median `0.009444`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.036401`, avg `0.005021`, median `0.009055`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.055595`, avg `0.021698`, median `0.027594`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.072536`, avg `0.044082`, median `0.047846`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.11168`, avg `0.057228`, median `0.072959`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.017575`, avg `0.000712`, median `0.000983`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.3625`, primary_mae `0.022289`, avg `0.000313`, median `0.002728`
- 10d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.033734`, avg `0.00197`, median `-0.006304`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.4125`, primary_mae `0.064505`, avg `0.006879`, median `0.007717`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.097325`, avg `0.008614`, median `0.015082`

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
