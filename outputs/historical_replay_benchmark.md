# Historical Replay Benchmark

Generated at: `2026-08-07T13:42:49.096012+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.014536`
- secondary_mean_absolute_error: `0.012505`
- primary_error_advantage: `-0.002031`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.017316`
- secondary_mean_absolute_error: `0.016603`
- primary_error_advantage: `-0.000713`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.027488`
- secondary_mean_absolute_error: `0.026996`
- primary_error_advantage: `-0.000492`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.057508`
- secondary_mean_absolute_error: `0.053655`
- primary_error_advantage: `-0.003853`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.080501`
- secondary_mean_absolute_error: `0.081879`
- primary_error_advantage: `0.001378`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013296`, as_primary `0`, as_primary_hit `None`, avg `0.004038`, median `0.005105`
- 5d: sample `80`, direction_hit `0.7125`, path_mae `0.016751`, as_primary `0`, as_primary_hit `None`, avg `0.006371`, median `0.006292`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.024382`, as_primary `0`, as_primary_hit `None`, avg `0.008042`, median `0.00986`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.038498`, as_primary `0`, as_primary_hit `None`, avg `0.013946`, median `0.01616`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.065873`, as_primary `0`, as_primary_hit `None`, avg `0.025156`, median `0.044393`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.016511`, as_primary `60`, as_primary_hit `0.5833`, avg `0.004038`, median `0.005105`
- 5d: sample `80`, direction_hit `0.7125`, path_mae `0.021135`, as_primary `60`, as_primary_hit `0.7333`, avg `0.006371`, median `0.006292`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.032096`, as_primary `60`, as_primary_hit `0.6`, avg `0.008042`, median `0.00986`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.060342`, as_primary `60`, as_primary_hit `0.6833`, avg `0.013946`, median `0.01616`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.08209`, as_primary `60`, as_primary_hit `0.55`, avg `0.025156`, median `0.044393`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.013778`, as_primary `20`, as_primary_hit `0.75`, avg `0.004038`, median `0.005105`
- 5d: sample `80`, direction_hit `0.2875`, path_mae `0.017123`, as_primary `20`, as_primary_hit `0.65`, avg `0.006371`, median `0.006292`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.02878`, as_primary `20`, as_primary_hit `0.65`, avg `0.008042`, median `0.00986`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.071327`, as_primary `20`, as_primary_hit `0.75`, avg `0.013946`, median `0.01616`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.089275`, as_primary `20`, as_primary_hit `0.7`, avg `0.025156`, median `0.044393`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.012448`, as_primary `0`, as_primary_hit `None`, avg `0.004038`, median `0.005105`
- 5d: sample `80`, direction_hit `0.7125`, path_mae `0.014518`, as_primary `0`, as_primary_hit `None`, avg `0.006371`, median `0.006292`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.02194`, as_primary `0`, as_primary_hit `None`, avg `0.008042`, median `0.00986`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.036258`, as_primary `0`, as_primary_hit `None`, avg `0.013946`, median `0.01616`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.06298`, as_primary `0`, as_primary_hit `None`, avg `0.025156`, median `0.044393`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.014947`, avg `0.002017`, median `0.003213`
- 5d: sample `60`, primary_hit `0.7333`, primary_closer `0.5167`, primary_mae `0.016025`, avg `0.006481`, median `0.006292`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.026286`, avg `0.005287`, median `0.008249`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5333`, primary_mae `0.048981`, avg `0.008266`, median `0.015334`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.07438`, avg `0.015276`, median `0.031767`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.013303`, avg `0.0101`, median `0.011854`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.021187`, avg `0.006042`, median `0.008022`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.031095`, avg `0.016306`, median `0.011814`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.15`, primary_mae `0.083086`, avg `0.030987`, median `0.022345`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.098865`, avg `0.054799`, median `0.075516`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.014947`, avg `0.002017`, median `0.003213`
- 5d: sample `60`, primary_hit `0.7333`, primary_closer `0.5167`, primary_mae `0.016025`, avg `0.006481`, median `0.006292`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.026286`, avg `0.005287`, median `0.008249`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5333`, primary_mae `0.048981`, avg `0.008266`, median `0.015334`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.07438`, avg `0.015276`, median `0.031767`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.013303`, avg `0.0101`, median `0.011854`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.021187`, avg `0.006042`, median `0.008022`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.031095`, avg `0.016306`, median `0.011814`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.15`, primary_mae `0.083086`, avg `0.030987`, median `0.022345`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.098865`, avg `0.054799`, median `0.075516`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.016025, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.026286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.048981, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.07438, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012448, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016511, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014518, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021135, 'direction_hit_rate': 0.7125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.016025, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02194, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032096, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.026286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036258, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071327, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.048981, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06298, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.089275, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.07438, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.025605`, avg `-0.003813`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.02559`, avg `0.000899`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.034021`, avg `0.002265`, median `0.002208`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.062357`, avg `0.009259`, median `0.014663`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.106688`, avg `-0.012738`, median `-0.032183`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.020356`, avg `0.001449`, median `0.004081`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.020794`, avg `0.007192`, median `0.004667`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.028877`, avg `0.008881`, median `0.011059`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.051307`, avg `0.021596`, median `0.023697`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.084672`, avg `0.011327`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.011896`, avg `0.010245`, median `0.011854`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.023645`, avg `0.007391`, median `0.010594`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.030546`, avg `0.017876`, median `0.011814`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.079437`, avg `0.03733`, median `0.015461`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.091673`, avg `0.0516`, median `0.066875`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.014536`, avg `0.004038`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.5`, primary_mae `0.017316`, avg `0.006371`, median `0.006292`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.027488`, avg `0.008042`, median `0.00986`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.4375`, primary_mae `0.057508`, avg `0.013946`, median `0.01616`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.080501`, avg `0.025156`, median `0.044393`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.014536`, avg `0.004038`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.5`, primary_mae `0.017316`, avg `0.006371`, median `0.006292`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.027488`, avg `0.008042`, median `0.00986`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.4375`, primary_mae `0.057508`, avg `0.013946`, median `0.01616`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.080501`, avg `0.025156`, median `0.044393`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4`, primary_mae `0.014947`, avg `0.002017`, median `0.003213`
- 5d: sample `60`, primary_hit `0.7333`, primary_closer `0.5167`, primary_mae `0.016025`, avg `0.006481`, median `0.006292`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4667`, primary_mae `0.026286`, avg `0.005287`, median `0.008249`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.5333`, primary_mae `0.048981`, avg `0.008266`, median `0.015334`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.07438`, avg `0.015276`, median `0.031767`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.013303`, avg `0.0101`, median `0.011854`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.021187`, avg `0.006042`, median `0.008022`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.031095`, avg `0.016306`, median `0.011814`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.15`, primary_mae `0.083086`, avg `0.030987`, median `0.022345`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.098865`, avg `0.054799`, median `0.075516`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.014536`, avg `0.004038`, median `0.005105`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.5`, primary_mae `0.017316`, avg `0.006371`, median `0.006292`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.027488`, avg `0.008042`, median `0.00986`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.4375`, primary_mae `0.057508`, avg `0.013946`, median `0.01616`
- 60d: sample `80`, primary_hit `0.4875`, primary_closer `0.4625`, primary_mae `0.080501`, avg `0.025156`, median `0.044393`

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
