# Historical Replay Benchmark

Generated at: `2026-11-06T19:28:11.092003+00:00`
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
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.02466`
- secondary_mean_absolute_error: `0.022032`
- primary_error_advantage: `-0.002628`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.033375`
- secondary_mean_absolute_error: `0.02658`
- primary_error_advantage: `-0.006795`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.060401`
- secondary_mean_absolute_error: `0.045102`
- primary_error_advantage: `-0.015299`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.091966`
- secondary_mean_absolute_error: `0.051835`
- primary_error_advantage: `-0.040131`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.087958`
- secondary_mean_absolute_error: `0.055172`
- primary_error_advantage: `-0.032786`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.019385`, as_primary `0`, as_primary_hit `None`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.024484`, as_primary `0`, as_primary_hit `None`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.038566`, as_primary `0`, as_primary_hit `None`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.044602`, as_primary `0`, as_primary_hit `None`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.053719`, as_primary `0`, as_primary_hit `None`, avg `0.04898`, median `0.070461`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.023487`, as_primary `0`, as_primary_hit `None`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.030158`, as_primary `0`, as_primary_hit `None`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.049956`, as_primary `0`, as_primary_hit `None`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.063539`, as_primary `0`, as_primary_hit `None`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.055458`, as_primary `0`, as_primary_hit `None`, avg `0.04898`, median `0.070461`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.02466`, as_primary `80`, as_primary_hit `0.65`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.033375`, as_primary `80`, as_primary_hit `0.625`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.060401`, as_primary `80`, as_primary_hit `0.65`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.091966`, as_primary `80`, as_primary_hit `0.7125`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.087958`, as_primary `80`, as_primary_hit `0.8125`, avg `0.04898`, median `0.070461`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.019101`, as_primary `0`, as_primary_hit `None`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.023638`, as_primary `0`, as_primary_hit `None`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.038597`, as_primary `0`, as_primary_hit `None`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.045745`, as_primary `0`, as_primary_hit `None`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.052091`, as_primary `0`, as_primary_hit `None`, avg `0.04898`, median `0.070461`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.02466`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.033375`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.060401`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.091966`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.087958`, avg `0.04898`, median `0.070461`

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
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.02466`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.033375`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.060401`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.091966`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.087958`, avg `0.04898`, median `0.070461`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.02466, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.033375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.060401, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2875, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.091966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.1875, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.087958, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019101, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02466, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.02466, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023638, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033375, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.033375, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038566, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060401, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.060401, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044602, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.091966, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2875, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.091966, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052091, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.087958, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.1875, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.087958, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.019777`, avg `0.005652`, median `0.012206`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.021613`, avg `0.007707`, median `0.011845`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.040083`, avg `0.009064`, median `0.003439`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.050935`, avg `0.027152`, median `0.028912`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.057718`, avg `0.04327`, median `0.042816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.020424`, avg `0.005525`, median `0.008712`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.023591`, avg `0.008346`, median `0.011845`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.043024`, avg `0.015055`, median `0.012995`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.056425`, avg `0.029606`, median `0.040851`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.058957`, avg `0.038852`, median `0.044167`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.018543`, avg `0.006245`, median `0.009859`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.023272`, avg `0.023279`, median `0.021051`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.063395`, avg `0.022611`, median `0.044876`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.098676`, avg `0.041676`, median `0.067551`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.089488`, avg `0.068512`, median `0.084854`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.02466`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.033375`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.060401`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.091966`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.087958`, avg `0.04898`, median `0.070461`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.02466`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.033375`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.060401`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.091966`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.087958`, avg `0.04898`, median `0.070461`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.4`, primary_mae `0.026937`, avg `0.00362`, median `0.007407`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.3833`, primary_mae `0.036969`, avg `0.003719`, median `0.011033`
- 10d: sample `60`, primary_hit `0.3833`, primary_closer `0.4333`, primary_mae `0.058326`, avg `0.007698`, median `0.011784`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.25`, primary_mae `0.088893`, avg `0.021181`, median `0.02893`
- 60d: sample `60`, primary_hit `0.1833`, primary_closer `0.3`, primary_mae `0.087717`, avg `0.044208`, median `0.067281`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.01783`, avg `0.009075`, median `0.011882`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.022591`, avg `0.026537`, median `0.025793`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.066626`, avg `0.030343`, median `0.049243`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.101186`, avg `0.04642`, median `0.067551`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.088683`, avg `0.063296`, median `0.086717`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.02466`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.033375`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.060401`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.091966`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.087958`, avg `0.04898`, median `0.070461`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3167`, primary_closer `0.4833`, primary_mae `0.021486`, avg `0.008395`, median `0.011369`
- 5d: sample `60`, primary_hit `0.3333`, primary_closer `0.4833`, primary_mae `0.021831`, avg `0.016303`, median `0.014593`
- 10d: sample `60`, primary_hit `0.3167`, primary_closer `0.4`, primary_mae `0.053645`, avg `0.020553`, median `0.028603`
- 20d: sample `60`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.083376`, avg `0.035133`, median `0.052537`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.2833`, primary_mae `0.064805`, avg `0.060748`, median `0.074488`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.02466`, avg `0.004984`, median `0.008997`
- 5d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.033375`, avg `0.009424`, median `0.01341`
- 10d: sample `80`, primary_hit `0.3375`, primary_closer `0.375`, primary_mae `0.060401`, avg `0.01336`, median `0.023707`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.091966`, avg `0.027491`, median `0.040269`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.275`, primary_mae `0.087958`, avg `0.04898`, median `0.070461`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
