# Historical Replay Benchmark

Generated at: `2026-07-30T14:35:12.305011+00:00`
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
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.018358`
- secondary_mean_absolute_error: `0.014182`
- primary_error_advantage: `-0.004176`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.025371`
- secondary_mean_absolute_error: `0.018311`
- primary_error_advantage: `-0.00706`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.035982`
- secondary_mean_absolute_error: `0.029677`
- primary_error_advantage: `-0.006305`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.7`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.070329`
- secondary_mean_absolute_error: `0.045544`
- primary_error_advantage: `-0.024785`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.10616`
- secondary_mean_absolute_error: `0.079264`
- primary_error_advantage: `-0.026896`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.01371`, as_primary `0`, as_primary_hit `None`, avg `0.00332`, median `0.002204`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.017225`, as_primary `0`, as_primary_hit `None`, avg `0.002853`, median `0.002061`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.025745`, as_primary `0`, as_primary_hit `None`, avg `0.001863`, median `-0.001634`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.037445`, as_primary `0`, as_primary_hit `None`, avg `0.013795`, median `0.019503`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.069452`, as_primary `0`, as_primary_hit `None`, avg `0.015028`, median `0.019404`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.016425`, as_primary `0`, as_primary_hit `None`, avg `0.00332`, median `0.002204`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.022271`, as_primary `0`, as_primary_hit `None`, avg `0.002853`, median `0.002061`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.035147`, as_primary `0`, as_primary_hit `None`, avg `0.001863`, median `-0.001634`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.05981`, as_primary `0`, as_primary_hit `None`, avg `0.013795`, median `0.019503`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.088056`, as_primary `0`, as_primary_hit `None`, avg `0.015028`, median `0.019404`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.018358`, as_primary `80`, as_primary_hit `0.625`, avg `0.00332`, median `0.002204`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.025371`, as_primary `80`, as_primary_hit `0.6125`, avg `0.002853`, median `0.002061`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.035982`, as_primary `80`, as_primary_hit `0.4625`, avg `0.001863`, median `-0.001634`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.070329`, as_primary `80`, as_primary_hit `0.6375`, avg `0.013795`, median `0.019503`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.10616`, as_primary `80`, as_primary_hit `0.5625`, avg `0.015028`, median `0.019404`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013512`, as_primary `0`, as_primary_hit `None`, avg `0.00332`, median `0.002204`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.01727`, as_primary `0`, as_primary_hit `None`, avg `0.002853`, median `0.002061`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.024961`, as_primary `0`, as_primary_hit `None`, avg `0.001863`, median `-0.001634`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.036977`, as_primary `0`, as_primary_hit `None`, avg `0.013795`, median `0.019503`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.068858`, as_primary `0`, as_primary_hit `None`, avg `0.015028`, median `0.019404`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.027652`, avg `0.001415`, median `0.00525`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.029906`, avg `-0.004395`, median `0.001655`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.019536`, avg `-0.002636`, median `-0.006514`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.053728`, avg `0.019939`, median `0.024617`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.0884`, avg `0.033758`, median `0.041779`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.01526`, avg `0.003955`, median `0.001312`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.3`, primary_mae `0.02386`, avg `0.005269`, median `0.002175`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.041465`, avg `0.003363`, median `0.000596`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.2833`, primary_mae `0.075863`, avg `0.011747`, median `0.018088`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.3333`, primary_mae `0.11208`, avg `0.008785`, median `0.009818`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.01526`, avg `0.003955`, median `0.001312`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.3`, primary_mae `0.02386`, avg `0.005269`, median `0.002175`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.041465`, avg `0.003363`, median `0.000596`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.2833`, primary_mae `0.075863`, avg `0.011747`, median `0.018088`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.3333`, primary_mae `0.11208`, avg `0.008785`, median `0.009818`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.027652`, avg `0.001415`, median `0.00525`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.029906`, avg `-0.004395`, median `0.001655`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.019536`, avg `-0.002636`, median `-0.006514`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.053728`, avg `0.019939`, median `0.024617`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.0884`, avg `0.033758`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.01526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.02386, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.019536, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.053728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.0884, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013512, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018358, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.01526, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017225, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025371, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.02386, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024961, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035982, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.019536, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036977, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070329, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.053728, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068858, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.10616, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.0884, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019066`, avg `-0.014954`, median `-0.018199`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.021219`, avg `-0.022298`, median `-0.026961`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.015388`, avg `-0.005325`, median `-0.007383`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.048592`, avg `0.011513`, median `0.01014`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.084068`, avg `0.033239`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.025931`, avg `-0.001604`, median `0.003063`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.029032`, avg `-0.006805`, median `0.001215`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.019366`, avg `-0.000868`, median `-0.006514`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.055466`, avg `0.021143`, median `0.024617`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.095829`, avg `0.044249`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.012466`, avg `-0.000715`, median `0.000402`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.011056`, avg `-0.00365`, median `0.000725`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.021526`, avg `-0.009053`, median `-0.011447`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.062125`, avg `-0.01252`, median `-0.005975`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.066507`, avg `0.005933`, median `-0.010173`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.3625`, primary_mae `0.018358`, avg `0.00332`, median `0.002204`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.025371`, avg `0.002853`, median `0.002061`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.035982`, avg `0.001863`, median `-0.001634`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.070329`, avg `0.013795`, median `0.019503`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.3625`, primary_mae `0.10616`, avg `0.015028`, median `0.019404`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.3625`, primary_mae `0.018358`, avg `0.00332`, median `0.002204`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.025371`, avg `0.002853`, median `0.002061`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.035982`, avg `0.001863`, median `-0.001634`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.070329`, avg `0.013795`, median `0.019503`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.3625`, primary_mae `0.10616`, avg `0.015028`, median `0.019404`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.020279`, avg `0.00107`, median `0.001633`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.325`, primary_mae `0.020488`, avg `-0.002856`, median `0.001195`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.625`, primary_mae `0.020263`, avg `-0.00619`, median `-0.007623`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.055663`, avg `0.001297`, median `-0.001803`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.074572`, avg `0.015565`, median `0.001845`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.016437`, avg `0.00557`, median `0.005771`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.275`, primary_mae `0.030254`, avg `0.008563`, median `0.004576`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.3`, primary_mae `0.051702`, avg `0.009917`, median `0.019744`
- 20d: sample `40`, primary_hit `0.175`, primary_closer `0.25`, primary_mae `0.084996`, avg `0.026294`, median `0.041488`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.137748`, avg `0.014492`, median `0.030832`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.3625`, primary_mae `0.018358`, avg `0.00332`, median `0.002204`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3`, primary_mae `0.025371`, avg `0.002853`, median `0.002061`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.035982`, avg `0.001863`, median `-0.001634`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.070329`, avg `0.013795`, median `0.019503`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.3625`, primary_mae `0.10616`, avg `0.015028`, median `0.019404`

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
