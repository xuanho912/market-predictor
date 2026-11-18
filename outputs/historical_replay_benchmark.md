# Historical Replay Benchmark

Generated at: `2026-11-18T20:35:04.546778+00:00`
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
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.030501`
- secondary_mean_absolute_error: `0.022044`
- primary_error_advantage: `-0.008457`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.029625`
- secondary_mean_absolute_error: `0.023116`
- primary_error_advantage: `-0.006509`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.2875`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.040111`
- secondary_mean_absolute_error: `0.029308`
- primary_error_advantage: `-0.010803`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.071328`
- secondary_mean_absolute_error: `0.039553`
- primary_error_advantage: `-0.031775`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.069825`
- secondary_mean_absolute_error: `0.063167`
- primary_error_advantage: `-0.006658`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.022563`, as_primary `0`, as_primary_hit `None`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.02398`, as_primary `0`, as_primary_hit `None`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.030937`, as_primary `0`, as_primary_hit `None`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.039107`, as_primary `0`, as_primary_hit `None`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.062751`, as_primary `0`, as_primary_hit `None`, avg `0.049258`, median `0.063438`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.024156`, as_primary `0`, as_primary_hit `None`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.026974`, as_primary `0`, as_primary_hit `None`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.03624`, as_primary `0`, as_primary_hit `None`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.059458`, as_primary `0`, as_primary_hit `None`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.066352`, as_primary `0`, as_primary_hit `None`, avg `0.049258`, median `0.063438`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.030501`, as_primary `80`, as_primary_hit `0.6`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.029625`, as_primary `80`, as_primary_hit `0.65`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.040111`, as_primary `80`, as_primary_hit `0.6375`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.071328`, as_primary `80`, as_primary_hit `0.65`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.069825`, as_primary `80`, as_primary_hit `0.7`, avg `0.049258`, median `0.063438`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.022044`, as_primary `0`, as_primary_hit `None`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.023116`, as_primary `0`, as_primary_hit `None`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.029308`, as_primary `0`, as_primary_hit `None`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.039553`, as_primary `0`, as_primary_hit `None`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.063167`, as_primary `0`, as_primary_hit `None`, avg `0.049258`, median `0.063438`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.030501`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.029625`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.3625`, primary_mae `0.040111`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.2625`, primary_mae `0.071328`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3875`, primary_mae `0.069825`, avg `0.049258`, median `0.063438`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.030541`, avg `0.010136`, median `0.021132`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.034331`, avg `0.018545`, median `0.023522`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.033388`, avg `0.029711`, median `0.032681`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.083598`, avg `0.004734`, median `0.001335`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.081325`, avg `0.039985`, median `0.06725`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.3167`, primary_mae `0.030487`, avg `0.006103`, median `0.008272`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.3833`, primary_mae `0.028057`, avg `0.006196`, median `0.0034`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.042352`, avg `0.007985`, median `0.005498`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.25`, primary_mae `0.067238`, avg `0.018567`, median `0.030451`
- 60d: sample `60`, primary_hit `0.2667`, primary_closer `0.3833`, primary_mae `0.065991`, avg `0.05235`, median `0.063438`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.030487, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.028057, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.033388, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.067238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.065991, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022044, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030501, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.030487, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023116, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029625, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.028057, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.2875, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029308, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040111, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.033388, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039107, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071328, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.067238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062751, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069825, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.065991, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.049299`, avg `0.018561`, median `0.024622`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.05663`, avg `0.023159`, median `0.025062`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.095705`, avg `0.030345`, median `0.010784`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.122515`, avg `0.046688`, median `0.035916`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.102955`, avg `0.104204`, median `0.122708`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.049501`, avg `0.016653`, median `0.024622`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.055374`, avg `0.016657`, median `0.023063`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.088797`, avg `0.020531`, median `0.009806`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.0625`, primary_mae `0.114155`, avg `0.038328`, median `0.036063`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.087636`, avg `0.088161`, median `0.119256`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.02566`, avg `0.013337`, median `0.021132`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.035409`, avg `0.019667`, median `0.028679`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.035101`, avg `0.029394`, median `0.032681`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.079946`, avg `0.003196`, median `-0.010667`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.078243`, avg `0.049422`, median `0.06725`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.030501`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.029625`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.3625`, primary_mae `0.040111`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.2625`, primary_mae `0.071328`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3875`, primary_mae `0.069825`, avg `0.049258`, median `0.063438`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.030501`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.029625`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.3625`, primary_mae `0.040111`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.2625`, primary_mae `0.071328`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3875`, primary_mae `0.069825`, avg `0.049258`, median `0.063438`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.3167`, primary_mae `0.030487`, avg `0.006103`, median `0.008272`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.3833`, primary_mae `0.028057`, avg `0.006196`, median `0.0034`
- 10d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.042352`, avg `0.007985`, median `0.005498`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.25`, primary_mae `0.067238`, avg `0.018567`, median `0.030451`
- 60d: sample `60`, primary_hit `0.2667`, primary_closer `0.3833`, primary_mae `0.065991`, avg `0.05235`, median `0.063438`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.030541`, avg `0.010136`, median `0.021132`
- 5d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.034331`, avg `0.018545`, median `0.023522`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.3`, primary_mae `0.033388`, avg `0.029711`, median `0.032681`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.083598`, avg `0.004734`, median `0.001335`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.081325`, avg `0.039985`, median `0.06725`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.030501`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.029625`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.3625`, primary_mae `0.040111`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.2625`, primary_mae `0.071328`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3875`, primary_mae `0.069825`, avg `0.049258`, median `0.063438`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.030501`, avg `0.007111`, median `0.011864`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.029625`, avg `0.009283`, median `0.009509`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.3625`, primary_mae `0.040111`, avg `0.013417`, median `0.012538`
- 20d: sample `80`, primary_hit `0.35`, primary_closer `0.2625`, primary_mae `0.071328`, avg `0.015109`, median `0.028827`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.3875`, primary_mae `0.069825`, avg `0.049258`, median `0.063438`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
