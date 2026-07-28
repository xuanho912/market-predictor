# Historical Replay Benchmark

Generated at: `2026-07-28T06:16:08.678944+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.023261`
- secondary_mean_absolute_error: `0.020152`
- primary_error_advantage: `-0.003109`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.029641`
- secondary_mean_absolute_error: `0.023195`
- primary_error_advantage: `-0.006446`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.035441`
- secondary_mean_absolute_error: `0.027319`
- primary_error_advantage: `-0.008122`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.076798`
- secondary_mean_absolute_error: `0.047412`
- primary_error_advantage: `-0.029386`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.110279`
- secondary_mean_absolute_error: `0.074421`
- primary_error_advantage: `-0.035858`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.018875`, as_primary `0`, as_primary_hit `None`, avg `-0.002834`, median `0.000952`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.022198`, as_primary `0`, as_primary_hit `None`, avg `-0.004229`, median `0.000725`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.024224`, as_primary `0`, as_primary_hit `None`, avg `0.004217`, median `0.004904`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.039105`, as_primary `0`, as_primary_hit `None`, avg `0.01495`, median `0.020543`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.067561`, as_primary `0`, as_primary_hit `None`, avg `0.027205`, median `0.049461`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.020163`, as_primary `0`, as_primary_hit `None`, avg `-0.002834`, median `0.000952`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.026451`, as_primary `0`, as_primary_hit `None`, avg `-0.004229`, median `0.000725`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.029416`, as_primary `0`, as_primary_hit `None`, avg `0.004217`, median `0.004904`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.057285`, as_primary `0`, as_primary_hit `None`, avg `0.01495`, median `0.020543`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.075296`, as_primary `0`, as_primary_hit `None`, avg `0.027205`, median `0.049461`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.023261`, as_primary `80`, as_primary_hit `0.55`, avg `-0.002834`, median `0.000952`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.029641`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.004229`, median `0.000725`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.035441`, as_primary `80`, as_primary_hit `0.55`, avg `0.004217`, median `0.004904`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.076798`, as_primary `80`, as_primary_hit `0.65`, avg `0.01495`, median `0.020543`
- 60d: sample `80`, direction_hit `0.35`, path_mae `0.110279`, as_primary `80`, as_primary_hit `0.65`, avg `0.027205`, median `0.049461`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.019574`, as_primary `0`, as_primary_hit `None`, avg `-0.002834`, median `0.000952`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021888`, as_primary `0`, as_primary_hit `None`, avg `-0.004229`, median `0.000725`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.023796`, as_primary `0`, as_primary_hit `None`, avg `0.004217`, median `0.004904`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.040548`, as_primary `0`, as_primary_hit `None`, avg `0.01495`, median `0.020543`
- 60d: sample `80`, direction_hit `0.65`, path_mae `0.067081`, as_primary `0`, as_primary_hit `None`, avg `0.027205`, median `0.049461`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.023261`, avg `-0.002834`, median `0.000952`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3875`, primary_mae `0.029641`, avg `-0.004229`, median `0.000725`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.035441`, avg `0.004217`, median `0.004904`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.076798`, avg `0.01495`, median `0.020543`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.110279`, avg `0.027205`, median `0.049461`

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
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.024876`, avg `0.000121`, median `0.004834`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.033756`, avg `0.00108`, median `0.003601`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.051269`, avg `0.012998`, median `0.023232`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.090842`, avg `0.018713`, median `0.042225`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.225`, primary_mae `0.137674`, avg `0.02059`, median `0.05682`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.021647`, avg `-0.005789`, median `0.000684`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.025526`, avg `-0.009539`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019613`, avg `-0.004565`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.062754`, avg `0.011187`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.082885`, avg `0.033821`, median `0.04627`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.025526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.019613, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.062754, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.082885, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018875, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023261, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021888, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029641, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.025526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023796, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035441, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.019613, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039105, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076798, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.062754, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067081, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.110279, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.082885, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.013252`, avg `-0.003324`, median `0.000684`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.011631`, avg `-0.007791`, median `-0.002888`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022176`, avg `-0.000342`, median `-0.003431`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.052539`, avg `0.012209`, median `0.009143`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.053158`, avg `0.031452`, median `0.045303`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.012326`, avg `-0.002301`, median `0.000952`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.013817`, avg `-0.001174`, median `0.000725`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.025713`, avg `-0.000985`, median `-0.003431`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.057854`, avg `0.006746`, median `0.017821`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.057468`, avg `0.022772`, median `0.039695`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.023591`, avg `-0.006218`, median `-0.003306`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.040063`, avg `-0.009526`, median `-0.007423`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.049413`, avg `0.00258`, median `0.016209`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.099184`, avg `0.002111`, median `0.017443`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.156408`, avg `-0.00768`, median `0.002694`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.023261`, avg `-0.002834`, median `0.000952`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3875`, primary_mae `0.029641`, avg `-0.004229`, median `0.000725`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.035441`, avg `0.004217`, median `0.004904`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.076798`, avg `0.01495`, median `0.020543`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.110279`, avg `0.027205`, median `0.049461`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.023261`, avg `-0.002834`, median `0.000952`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.3875`, primary_mae `0.029641`, avg `-0.004229`, median `0.000725`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.035441`, avg `0.004217`, median `0.004904`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.076798`, avg `0.01495`, median `0.020543`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.3125`, primary_mae `0.110279`, avg `0.027205`, median `0.049461`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.021647`, avg `-0.005789`, median `0.000684`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.5`, primary_mae `0.025526`, avg `-0.009539`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019613`, avg `-0.004565`, median `-0.007064`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.062754`, avg `0.011187`, median `0.019669`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.082885`, avg `0.033821`, median `0.04627`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.024876`, avg `0.000121`, median `0.004834`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.275`, primary_mae `0.033756`, avg `0.00108`, median `0.003601`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.051269`, avg `0.012998`, median `0.023232`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.090842`, avg `0.018713`, median `0.042225`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.225`, primary_mae `0.137674`, avg `0.02059`, median `0.05682`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.021948`, avg `-0.000592`, median `0.001272`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.3667`, primary_mae `0.027716`, avg `-0.000552`, median `0.001877`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.3667`, primary_mae `0.041877`, avg `0.007167`, median `0.017341`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.35`, primary_mae `0.078845`, avg `0.014442`, median `0.019748`
- 60d: sample `60`, primary_hit `0.3833`, primary_closer `0.3167`, primary_mae `0.108833`, avg `0.020103`, median `0.039695`

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
