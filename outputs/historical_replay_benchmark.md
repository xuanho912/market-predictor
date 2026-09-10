# Historical Replay Benchmark

Generated at: `2026-09-10T01:03:40.219858+00:00`
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
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.026179`
- secondary_mean_absolute_error: `0.018158`
- primary_error_advantage: `-0.008021`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.028711`
- secondary_mean_absolute_error: `0.020057`
- primary_error_advantage: `-0.008654`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.055606`
- secondary_mean_absolute_error: `0.033538`
- primary_error_advantage: `-0.022068`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.072783`
- secondary_mean_absolute_error: `0.042477`
- primary_error_advantage: `-0.030306`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.064143`
- secondary_mean_absolute_error: `0.052154`
- primary_error_advantage: `-0.011989`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.017746`, as_primary `0`, as_primary_hit `None`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.020073`, as_primary `0`, as_primary_hit `None`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.033129`, as_primary `0`, as_primary_hit `None`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.045189`, as_primary `0`, as_primary_hit `None`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.053209`, as_primary `0`, as_primary_hit `None`, avg `0.059372`, median `0.06681`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.019018`, as_primary `0`, as_primary_hit `None`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.02328`, as_primary `0`, as_primary_hit `None`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.039008`, as_primary `0`, as_primary_hit `None`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.062777`, as_primary `0`, as_primary_hit `None`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.056508`, as_primary `0`, as_primary_hit `None`, avg `0.059372`, median `0.06681`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.325`, path_mae `0.026179`, as_primary `80`, as_primary_hit `0.675`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, direction_hit `0.3`, path_mae `0.028711`, as_primary `80`, as_primary_hit `0.7`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.055606`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.072783`, as_primary `80`, as_primary_hit `0.6875`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.064143`, as_primary `80`, as_primary_hit `0.7875`, avg `0.059372`, median `0.06681`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.675`, path_mae `0.018158`, as_primary `0`, as_primary_hit `None`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, direction_hit `0.7`, path_mae `0.020057`, as_primary `0`, as_primary_hit `None`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.033538`, as_primary `0`, as_primary_hit `None`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.042477`, as_primary `0`, as_primary_hit `None`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.052154`, as_primary `0`, as_primary_hit `None`, avg `0.059372`, median `0.06681`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.026179`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.028711`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.055606`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.275`, primary_mae `0.072783`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3375`, primary_mae `0.064143`, avg `0.059372`, median `0.06681`

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
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.028074`, avg `0.00083`, median `0.002379`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.029804`, avg `0.00125`, median `0.007432`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.054288`, avg `-0.005877`, median `-0.00147`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.3`, primary_mae `0.065578`, avg `0.003685`, median `0.018545`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.068291`, avg `0.031482`, median `0.04549`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024284`, avg `0.011851`, median `0.018044`
- 5d: sample `40`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.027618`, avg `0.01836`, median `0.022151`
- 10d: sample `40`, primary_hit `0.275`, primary_closer `0.25`, primary_mae `0.056924`, avg `0.021588`, median `0.024407`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.079988`, avg `0.040549`, median `0.036318`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.35`, primary_mae `0.059996`, avg `0.087262`, median `0.093013`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.024284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.027618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.054288, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.065578, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.059996, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017746, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026179, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.024284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020057, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028711, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.027618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033129, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055606, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.054288, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042477, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072783, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.065578, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052154, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064143, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.059996, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017125`, avg `0.002422`, median `0.005307`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.020254`, avg `0.002383`, median `0.008828`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.032654`, avg `0.001255`, median `0.005316`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.088581`, avg `0.045109`, median `0.058396`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.073248`, avg `0.098577`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.021352`, avg `0.007425`, median `0.018713`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.025077`, avg `0.012215`, median `0.011781`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.040986`, avg `0.01564`, median `0.024318`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.089802`, avg `0.036433`, median `0.050926`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.058836`, avg `0.077797`, median `0.093013`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.030364`, avg `0.015827`, median `0.018551`
- 5d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.033404`, avg `0.023909`, median `0.025675`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.077957`, avg `0.031383`, median `0.047952`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.090738`, avg `0.064315`, median `0.056024`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.072497`, avg `0.107529`, median `0.147302`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.026179`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.028711`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.055606`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.275`, primary_mae `0.072783`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3375`, primary_mae `0.064143`, avg `0.059372`, median `0.06681`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.026179`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.028711`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.055606`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.275`, primary_mae `0.072783`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3375`, primary_mae `0.064143`, avg `0.059372`, median `0.06681`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.026179`, avg `0.006341`, median `0.012244`
- 5d: sample `80`, primary_hit `0.3`, primary_closer `0.325`, primary_mae `0.028711`, avg `0.009805`, median `0.013983`
- 10d: sample `80`, primary_hit `0.3875`, primary_closer `0.2875`, primary_mae `0.055606`, avg `0.007855`, median `0.015027`
- 20d: sample `80`, primary_hit `0.3125`, primary_closer `0.275`, primary_mae `0.072783`, avg `0.022117`, median `0.029226`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3375`, primary_mae `0.064143`, avg `0.059372`, median `0.06681`

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
