# Historical Replay Benchmark

Generated at: `2026-11-06T11:31:47.859195+00:00`
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
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.033758`
- secondary_mean_absolute_error: `0.025755`
- primary_error_advantage: `-0.008003`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.038169`
- secondary_mean_absolute_error: `0.027839`
- primary_error_advantage: `-0.01033`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.2625`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.070022`
- secondary_mean_absolute_error: `0.047335`
- primary_error_advantage: `-0.022687`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.133198`
- secondary_mean_absolute_error: `0.066784`
- primary_error_advantage: `-0.066414`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.113015`
- secondary_mean_absolute_error: `0.071052`
- primary_error_advantage: `-0.041963`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.026129`, as_primary `0`, as_primary_hit `None`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.027025`, as_primary `0`, as_primary_hit `None`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.043508`, as_primary `0`, as_primary_hit `None`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.062973`, as_primary `0`, as_primary_hit `None`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.068402`, as_primary `0`, as_primary_hit `None`, avg `0.033874`, median `0.05716`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.026993`, as_primary `0`, as_primary_hit `None`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.027758`, as_primary `0`, as_primary_hit `None`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.049583`, as_primary `0`, as_primary_hit `None`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.074753`, as_primary `0`, as_primary_hit `None`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.078185`, as_primary `0`, as_primary_hit `None`, avg `0.033874`, median `0.05716`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.033758`, as_primary `80`, as_primary_hit `0.65`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.038169`, as_primary `80`, as_primary_hit `0.65`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.070022`, as_primary `80`, as_primary_hit `0.625`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.133198`, as_primary `80`, as_primary_hit `0.675`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.113015`, as_primary `80`, as_primary_hit `0.725`, avg `0.033874`, median `0.05716`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.024751`, as_primary `0`, as_primary_hit `None`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.026226`, as_primary `0`, as_primary_hit `None`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.04308`, as_primary `0`, as_primary_hit `None`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.060645`, as_primary `0`, as_primary_hit `None`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.069593`, as_primary `0`, as_primary_hit `None`, avg `0.033874`, median `0.05716`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.033758`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.038169`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.070022`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2375`, primary_mae `0.133198`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.2625`, primary_mae `0.113015`, avg `0.033874`, median `0.05716`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.033758`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.038169`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.070022`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2375`, primary_mae `0.133198`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.2625`, primary_mae `0.113015`, avg `0.033874`, median `0.05716`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.033758, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.038169, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.070022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.133198, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.113015, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024751, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033758, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.033758, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026226, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038169, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.038169, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.2625, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04308, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070022, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.070022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060645, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.133198, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.133198, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.068402, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.113015, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.113015, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.03729`, avg `0.003923`, median `0.012206`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.034621`, avg `0.013152`, median `0.015572`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.076615`, avg `0.001856`, median `0.024584`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.156728`, avg `-0.020003`, median `0.034635`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.091641`, avg `0.019104`, median `0.048774`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.037098`, avg `0.007993`, median `0.012472`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.034521`, avg `0.015094`, median `0.021231`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.073583`, avg `0.010895`, median `0.024584`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.146512`, avg `-0.005964`, median `0.015394`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.083523`, avg `0.017807`, median `0.043392`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.026373`, avg `-0.000953`, median `0.011882`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.020853`, avg `0.020467`, median `0.01808`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.059213`, avg `0.043616`, median `0.053885`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.125`, primary_mae `0.079003`, avg `0.064567`, median `0.069806`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.125`, primary_mae `0.111195`, avg `0.103483`, median `0.119951`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.033758`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.038169`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.070022`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2375`, primary_mae `0.133198`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.2625`, primary_mae `0.113015`, avg `0.033874`, median `0.05716`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.033758`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.038169`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.070022`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2375`, primary_mae `0.133198`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.2625`, primary_mae `0.113015`, avg `0.033874`, median `0.05716`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.035993`, avg `0.003389`, median `0.010573`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.3333`, primary_mae `0.043785`, avg `0.004052`, median `0.011845`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.3833`, primary_mae `0.073764`, avg `0.000531`, median `0.011637`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.2333`, primary_mae `0.153177`, avg `-0.009587`, median `0.015394`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.2667`, primary_mae `0.114943`, avg `0.019639`, median `0.052261`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.02705`, avg `0.005181`, median `0.01219`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.02132`, avg `0.021497`, median `0.01808`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.058794`, avg `0.039454`, median `0.053885`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.25`, primary_mae `0.073262`, avg `0.05151`, median `0.066144`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.107233`, avg `0.076579`, median `0.107445`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.033758`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.038169`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.070022`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2375`, primary_mae `0.133198`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.2625`, primary_mae `0.113015`, avg `0.033874`, median `0.05716`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.033758`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.038169`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.070022`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2375`, primary_mae `0.133198`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.2625`, primary_mae `0.113015`, avg `0.033874`, median `0.05716`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.033758`, avg `0.003837`, median `0.011369`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.038169`, avg `0.008413`, median `0.012755`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3375`, primary_mae `0.070022`, avg `0.010262`, median `0.020457`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.2375`, primary_mae `0.133198`, avg `0.005687`, median `0.031212`
- 60d: sample `80`, primary_hit `0.275`, primary_closer `0.2625`, primary_mae `0.113015`, avg `0.033874`, median `0.05716`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
