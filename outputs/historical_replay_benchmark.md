# Historical Replay Benchmark

Generated at: `2026-07-22T14:25:09.894740+00:00`
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
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.018268`
- secondary_mean_absolute_error: `0.017189`
- primary_error_advantage: `-0.001079`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.022798`
- secondary_mean_absolute_error: `0.019264`
- primary_error_advantage: `-0.003534`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.028286`
- secondary_mean_absolute_error: `0.025768`
- primary_error_advantage: `-0.002518`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.071414`
- secondary_mean_absolute_error: `0.049945`
- primary_error_advantage: `-0.021469`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.108987`
- secondary_mean_absolute_error: `0.083708`
- primary_error_advantage: `-0.025279`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.01526`, as_primary `0`, as_primary_hit `None`, avg `-0.005694`, median `-0.004449`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.017532`, as_primary `0`, as_primary_hit `None`, avg `-0.006382`, median `-0.004781`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.022344`, as_primary `0`, as_primary_hit `None`, avg `-0.00373`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.037779`, as_primary `0`, as_primary_hit `None`, avg `0.002745`, median `0.01543`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.072888`, as_primary `0`, as_primary_hit `None`, avg `0.002526`, median `0.008264`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.017323`, as_primary `0`, as_primary_hit `None`, avg `-0.005694`, median `-0.004449`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.02046`, as_primary `0`, as_primary_hit `None`, avg `-0.006382`, median `-0.004781`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.029276`, as_primary `0`, as_primary_hit `None`, avg `-0.00373`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.051868`, as_primary `0`, as_primary_hit `None`, avg `0.002745`, median `0.01543`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.086623`, as_primary `0`, as_primary_hit `None`, avg `0.002526`, median `0.008264`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.018268`, as_primary `80`, as_primary_hit `0.425`, avg `-0.005694`, median `-0.004449`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.022798`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.006382`, median `-0.004781`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.028286`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.00373`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.071414`, as_primary `80`, as_primary_hit `0.6375`, avg `0.002745`, median `0.01543`
- 60d: sample `80`, direction_hit `0.475`, path_mae `0.108987`, as_primary `80`, as_primary_hit `0.525`, avg `0.002526`, median `0.008264`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.014856`, as_primary `0`, as_primary_hit `None`, avg `-0.005694`, median `-0.004449`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.017085`, as_primary `0`, as_primary_hit `None`, avg `-0.006382`, median `-0.004781`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.02098`, as_primary `0`, as_primary_hit `None`, avg `-0.00373`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.038206`, as_primary `0`, as_primary_hit `None`, avg `0.002745`, median `0.01543`
- 60d: sample `80`, direction_hit `0.525`, path_mae `0.072894`, as_primary `0`, as_primary_hit `None`, avg `0.002526`, median `0.008264`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.021541`, avg `-0.011343`, median `-0.012958`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.029001`, avg `-0.011905`, median `-0.01025`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.025402`, avg `-0.003471`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.078029`, avg `0.01147`, median `0.020913`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.112937`, avg `0.036482`, median `0.052632`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.017177`, avg `-0.003811`, median `-0.002029`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.35`, primary_mae `0.02073`, avg `-0.004541`, median `-0.004366`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.4`, primary_mae `0.029247`, avg `-0.003817`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.3`, primary_mae `0.069208`, avg `-0.000163`, median `0.007712`
- 60d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.10767`, avg `-0.008793`, median `-0.003444`

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
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.017177`, avg `-0.003811`, median `-0.002029`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.35`, primary_mae `0.02073`, avg `-0.004541`, median `-0.004366`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.4`, primary_mae `0.029247`, avg `-0.003817`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.3`, primary_mae `0.069208`, avg `-0.000163`, median `0.007712`
- 60d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.10767`, avg `-0.008793`, median `-0.003444`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.021541`, avg `-0.011343`, median `-0.012958`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.029001`, avg `-0.011905`, median `-0.01025`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.025402`, avg `-0.003471`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.078029`, avg `0.01147`, median `0.020913`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.112937`, avg `0.036482`, median `0.052632`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.017177, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02073, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.025402, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.069208, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.10767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014856, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018268, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.017177, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017085, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022798, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02073, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02098, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029276, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.025402, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037779, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071414, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.069208, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072888, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.108987, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.10767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016968`, avg `-0.020804`, median `-0.031812`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.020585`, avg `-0.028823`, median `-0.028941`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.014361`, avg `-0.016415`, median `-0.019121`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.065782`, avg `-0.00875`, median `0.01014`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.09873`, avg `0.011496`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.0214`, avg `-0.012659`, median `-0.018199`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.026228`, avg `-0.016367`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.023613`, avg `-0.004553`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.082286`, avg `0.015139`, median `0.023936`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.122014`, avg `0.043762`, median `0.059313`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.024094`, avg `-0.002333`, median `-0.003808`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.023043`, avg `-0.003449`, median `-0.008875`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.027239`, avg `0.011196`, median `0.015719`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.046934`, avg `0.029049`, median `0.033856`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.094246`, avg `0.022781`, median `0.056527`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.018268`, avg `-0.005694`, median `-0.004449`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.022798`, avg `-0.006382`, median `-0.004781`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.028286`, avg `-0.00373`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.071414`, avg `0.002745`, median `0.01543`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.108987`, avg `0.002526`, median `0.008264`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.018268`, avg `-0.005694`, median `-0.004449`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.022798`, avg `-0.006382`, median `-0.004781`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.028286`, avg `-0.00373`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.071414`, avg `0.002745`, median `0.01543`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.108987`, avg `0.002526`, median `0.008264`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.575`, primary_mae `0.017202`, avg `-0.00981`, median `-0.009234`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.02243`, avg `-0.01046`, median `-0.005451`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.525`, primary_mae `0.023298`, avg `-0.008048`, median `-0.010971`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.071787`, avg `-0.001684`, median `-0.000495`
- 60d: sample `40`, primary_hit `0.45`, primary_closer `0.475`, primary_mae `0.090632`, avg `0.017319`, median `0.018124`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.026842`, avg `-0.002054`, median `0.002036`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.025412`, avg `-0.002018`, median `-0.007626`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.029119`, avg `0.012609`, median `0.01787`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.25`, primary_mae `0.047445`, avg `0.025881`, median `0.033856`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.09107`, avg `0.013798`, median `0.031665`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.018268`, avg `-0.005694`, median `-0.004449`
- 5d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.022798`, avg `-0.006382`, median `-0.004781`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.028286`, avg `-0.00373`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.071414`, avg `0.002745`, median `0.01543`
- 60d: sample `80`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.108987`, avg `0.002526`, median `0.008264`

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
