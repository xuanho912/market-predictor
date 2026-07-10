# Historical Replay Benchmark

Generated at: `2026-07-10T22:37:47.104437+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.0124`
- secondary_mean_absolute_error: `0.011602`
- primary_error_advantage: `-0.000798`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.016098`
- secondary_mean_absolute_error: `0.015822`
- primary_error_advantage: `-0.000276`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.024412`
- secondary_mean_absolute_error: `0.021601`
- primary_error_advantage: `-0.002811`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.047855`
- secondary_mean_absolute_error: `0.048899`
- primary_error_advantage: `0.001044`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.065629`
- secondary_mean_absolute_error: `0.062841`
- primary_error_advantage: `-0.002788`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012318`, as_primary `0`, as_primary_hit `None`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016048`, as_primary `0`, as_primary_hit `None`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.01952`, as_primary `0`, as_primary_hit `None`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.038009`, as_primary `0`, as_primary_hit `None`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.058437`, as_primary `0`, as_primary_hit `None`, avg `-0.000555`, median `-0.00053`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.0124`, as_primary `80`, as_primary_hit `0.5`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016098`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.024412`, as_primary `80`, as_primary_hit `0.525`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.047855`, as_primary `80`, as_primary_hit `0.6625`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.065629`, as_primary `80`, as_primary_hit `0.5`, avg `-0.000555`, median `-0.00053`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.012788`, as_primary `0`, as_primary_hit `None`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.018164`, as_primary `0`, as_primary_hit `None`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.025706`, as_primary `0`, as_primary_hit `None`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.071426`, as_primary `0`, as_primary_hit `None`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.082171`, as_primary `0`, as_primary_hit `None`, avg `-0.000555`, median `-0.00053`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.011573`, as_primary `0`, as_primary_hit `None`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.015751`, as_primary `0`, as_primary_hit `None`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.019326`, as_primary `0`, as_primary_hit `None`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.034882`, as_primary `0`, as_primary_hit `None`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, direction_hit `0.5`, path_mae `0.058474`, as_primary `0`, as_primary_hit `None`, avg `-0.000555`, median `-0.00053`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.012052`, avg `-0.003708`, median `-0.001834`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.5`, primary_mae `0.01517`, avg `-0.00525`, median `-0.002161`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.4667`, primary_mae `0.021295`, avg `-0.00509`, median `-0.003995`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5333`, primary_mae `0.041408`, avg `-0.004303`, median `0.01201`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4833`, primary_mae `0.06428`, avg `-0.00751`, median `-0.007976`

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.013445`, avg `0.002925`, median `0.004053`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.018883`, avg `0.002748`, median `0.007127`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.033761`, avg `0.015747`, median `0.007323`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.25`, primary_mae `0.067195`, avg `0.006217`, median `0.007476`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.069677`, avg `0.020311`, median `0.054132`

## Predictor Performance

### bounce_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.0124`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016098`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.024412`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4625`, primary_mae `0.047855`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065629`, avg `-0.000555`, median `-0.00053`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.0124, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5125, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.016098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.024412, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6625, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.047855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.065629, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.011573, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012788, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.0124, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015751, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018164, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5125, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.016098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019326, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025706, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.024412, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034882, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071426, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6625, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.047855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058437, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.082171, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.065629, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015163`, avg `-0.008752`, median `-0.00531`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.012495`, avg `-0.00855`, median `-0.006575`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.019455`, avg `-0.003031`, median `-0.010098`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.022728`, avg `0.018499`, median `0.025909`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065733`, avg `0.028022`, median `0.020575`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.01678`, avg `-0.008938`, median `-0.003968`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.019264`, avg `-0.008222`, median `-0.003481`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.02141`, avg `-0.0062`, median `-0.016124`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.043202`, avg `-8.1e-05`, median `0.012154`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.089815`, avg `0.004256`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.01678`, avg `-0.008938`, median `-0.003968`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.019264`, avg `-0.008222`, median `-0.003481`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.02141`, avg `-0.0062`, median `-0.016124`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.043202`, avg `-8.1e-05`, median `0.012154`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.089815`, avg `0.004256`, median `-0.012556`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.0124`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016098`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.024412`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4625`, primary_mae `0.047855`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065629`, avg `-0.000555`, median `-0.00053`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.0124`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016098`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.024412`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4625`, primary_mae `0.047855`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065629`, avg `-0.000555`, median `-0.00053`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.012052`, avg `-0.003708`, median `-0.001834`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.5`, primary_mae `0.01517`, avg `-0.00525`, median `-0.002161`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.4667`, primary_mae `0.021295`, avg `-0.00509`, median `-0.003995`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5333`, primary_mae `0.041408`, avg `-0.004303`, median `0.01201`
- 60d: sample `60`, primary_hit `0.45`, primary_closer `0.4833`, primary_mae `0.06428`, avg `-0.00751`, median `-0.007976`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.010944`, avg `-0.000348`, median `-0.001834`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.016169`, avg `-0.004995`, median `-0.005921`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.029243`, avg `-0.010905`, median `-0.015175`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.75`, primary_mae `0.054818`, avg `-0.020592`, median `0.003265`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.65`, primary_mae `0.052832`, avg `-0.014098`, median `-0.007976`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.0124`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016098`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.024412`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4625`, primary_mae `0.047855`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065629`, avg `-0.000555`, median `-0.00053`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.0124`, avg `-0.00205`, median `-8.6e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.475`, primary_mae `0.016098`, avg `-0.003251`, median `0.000837`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.024412`, avg `0.000119`, median `0.001939`
- 20d: sample `80`, primary_hit `0.6625`, primary_closer `0.4625`, primary_mae `0.047855`, avg `-0.001673`, median `0.009961`
- 60d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.065629`, avg `-0.000555`, median `-0.00053`

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
