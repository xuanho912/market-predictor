# Historical Replay Benchmark

Generated at: `2026-07-08T14:43:53.673775+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.6875`
- primary_mean_absolute_error: `0.015198`
- secondary_mean_absolute_error: `0.019566`
- primary_error_advantage: `0.004368`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.6875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.019208`
- secondary_mean_absolute_error: `0.020996`
- primary_error_advantage: `0.001788`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.023404`
- secondary_mean_absolute_error: `0.023497`
- primary_error_advantage: `9.3e-05`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.725`
- secondary_hit_rate: `0.275`
- primary_vs_secondary_accuracy_spread: `0.45`
- primary_closer_than_secondary_rate: `0.6125`
- primary_mean_absolute_error: `0.040641`
- secondary_mean_absolute_error: `0.054219`
- primary_error_advantage: `0.013578`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.6125`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.063999`
- secondary_mean_absolute_error: `0.071938`
- primary_error_advantage: `0.007939`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014549`, as_primary `0`, as_primary_hit `None`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017496`, as_primary `0`, as_primary_hit `None`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.020133`, as_primary `0`, as_primary_hit `None`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.02717`, as_primary `0`, as_primary_hit `None`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.056`, as_primary `0`, as_primary_hit `None`, avg `0.016763`, median `0.024773`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.015198`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019208`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.023404`, as_primary `80`, as_primary_hit `0.45`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.040641`, as_primary `80`, as_primary_hit `0.725`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.063999`, as_primary `80`, as_primary_hit `0.5625`, avg `0.016763`, median `0.024773`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.019566`, as_primary `0`, as_primary_hit `None`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.020996`, as_primary `0`, as_primary_hit `None`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.023497`, as_primary `0`, as_primary_hit `None`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.054219`, as_primary `0`, as_primary_hit `None`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.071938`, as_primary `0`, as_primary_hit `None`, avg `0.016763`, median `0.024773`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.014048`, as_primary `0`, as_primary_hit `None`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.016767`, as_primary `0`, as_primary_hit `None`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.019098`, as_primary `0`, as_primary_hit `None`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.02662`, as_primary `0`, as_primary_hit `None`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.054753`, as_primary `0`, as_primary_hit `None`, avg `0.016763`, median `0.024773`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.6875`, primary_mae `0.015198`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.019208`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.023404`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, primary_hit `0.725`, primary_closer `0.6125`, primary_mae `0.040641`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.063999`, avg `0.016763`, median `0.024773`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.9`, primary_mae `0.008132`, avg `-0.004469`, median `-0.004035`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.65`, primary_mae `0.011431`, avg `-0.002489`, median `0.001088`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.65`, primary_mae `0.015357`, avg `-0.009484`, median `-0.010461`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.039915`, avg `-0.00884`, median `-0.000984`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.057894`, avg `-0.019681`, median `-0.025523`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.6167`, primary_mae `0.017554`, avg `-0.001052`, median `0.001151`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.5167`, primary_mae `0.0218`, avg `-0.003113`, median `-0.002066`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.4667`, primary_mae `0.026087`, avg `0.001792`, median `-7.9e-05`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.5667`, primary_mae `0.040883`, avg `0.017502`, median `0.020313`
- 60d: sample `60`, primary_hit `0.6333`, primary_closer `0.55`, primary_mae `0.066034`, avg `0.028911`, median `0.044873`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.9, 'primary_mean_absolute_error': 0.008132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011431, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.015357, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.039915, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.057894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.6875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014048, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019566, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.9, 'primary_mean_absolute_error': 0.008132, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016767, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020996, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.011431, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019098, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023497, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.015357, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.275, 'primary_vs_secondary_accuracy_spread': 0.45, 'primary_closer_than_secondary_rate': 0.6125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02662, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054219, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.039915, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054753, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071938, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.057894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.015486`, avg `-0.006276`, median `-5e-05`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.019083`, avg `-0.010574`, median `-0.014548`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022643`, avg `-0.001552`, median `-0.003208`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.02801`, avg `0.038788`, median `0.038728`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.75`, primary_mae `0.041937`, avg `0.090405`, median `0.10056`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.018717`, avg `-0.004526`, median `-5e-05`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.020105`, avg `-0.009902`, median `-0.012995`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022132`, avg `-0.001246`, median `-0.00362`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.625`, primary_mae `0.037109`, avg `0.028809`, median `0.032598`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.6875`, primary_mae `0.058554`, avg `0.072136`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.018717`, avg `-0.004526`, median `-5e-05`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.020105`, avg `-0.009902`, median `-0.012995`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.022132`, avg `-0.001246`, median `-0.00362`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.625`, primary_mae `0.037109`, avg `0.028809`, median `0.032598`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.6875`, primary_mae `0.058554`, avg `0.072136`, median `0.088952`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.6875`, primary_mae `0.015198`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.019208`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.023404`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, primary_hit `0.725`, primary_closer `0.6125`, primary_mae `0.040641`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.063999`, avg `0.016763`, median `0.024773`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.6875`, primary_mae `0.015198`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.019208`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.023404`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, primary_hit `0.725`, primary_closer `0.6125`, primary_mae `0.040641`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.063999`, avg `0.016763`, median `0.024773`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.6875`, primary_mae `0.015198`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.019208`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.023404`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, primary_hit `0.725`, primary_closer `0.6125`, primary_mae `0.040641`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.063999`, avg `0.016763`, median `0.024773`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.6875`, primary_mae `0.015198`, avg `-0.001906`, median `-0.000944`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.019208`, avg `-0.002957`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.023404`, avg `-0.001027`, median `-0.004577`
- 20d: sample `80`, primary_hit `0.725`, primary_closer `0.6125`, primary_mae `0.040641`, avg `0.010917`, median `0.013584`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.063999`, avg `0.016763`, median `0.024773`

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
