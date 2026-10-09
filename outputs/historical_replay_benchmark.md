# Historical Replay Benchmark

Generated at: `2026-10-09T00:43:05.730094+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `STRONG_HISTORICAL_ONLY`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.015039`
- secondary_mean_absolute_error: `0.016629`
- primary_error_advantage: `0.00159`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.019731`
- secondary_mean_absolute_error: `0.023635`
- primary_error_advantage: `0.003904`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.025157`
- secondary_mean_absolute_error: `0.030945`
- primary_error_advantage: `0.005788`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.625`
- primary_mean_absolute_error: `0.043213`
- secondary_mean_absolute_error: `0.058829`
- primary_error_advantage: `0.015616`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.65`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.0484`
- secondary_mean_absolute_error: `0.050888`
- primary_error_advantage: `0.002488`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01509`, as_primary `0`, as_primary_hit `None`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.020838`, as_primary `0`, as_primary_hit `None`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.02778`, as_primary `0`, as_primary_hit `None`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.039427`, as_primary `0`, as_primary_hit `None`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.044884`, as_primary `0`, as_primary_hit `None`, avg `0.085397`, median `0.098855`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015531`, as_primary `40`, as_primary_hit `0.7`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.024064`, as_primary `40`, as_primary_hit `0.625`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.032893`, as_primary `40`, as_primary_hit `0.725`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.05519`, as_primary `40`, as_primary_hit `0.875`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.049569`, as_primary `40`, as_primary_hit `0.95`, avg `0.085397`, median `0.098855`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016137`, as_primary `40`, as_primary_hit `0.475`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019302`, as_primary `40`, as_primary_hit `0.4`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.023209`, as_primary `40`, as_primary_hit `0.45`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.046853`, as_primary `40`, as_primary_hit `0.7`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, direction_hit `0.125`, path_mae `0.049718`, as_primary `40`, as_primary_hit `0.8`, avg `0.085397`, median `0.098855`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015237`, as_primary `0`, as_primary_hit `None`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019147`, as_primary `0`, as_primary_hit `None`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.023916`, as_primary `0`, as_primary_hit `None`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.032834`, as_primary `0`, as_primary_hit `None`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, direction_hit `0.875`, path_mae `0.04215`, as_primary `0`, as_primary_hit `None`, avg `0.085397`, median `0.098855`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.5375`, primary_mae `0.015039`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.5625`, primary_mae `0.019731`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5125`, primary_mae `0.025157`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.625`, primary_mae `0.043213`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.0484`, avg `0.085397`, median `0.098855`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.011739`, avg `0.00623`, median `0.012087`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017591`, avg `0.006387`, median `0.00893`
- 10d: sample `40`, primary_hit `0.725`, primary_closer `0.35`, primary_mae `0.021387`, avg `0.009033`, median `0.008792`
- 20d: sample `40`, primary_hit `0.875`, primary_closer `0.575`, primary_mae `0.033049`, avg `0.037132`, median `0.036235`
- 60d: sample `40`, primary_hit `0.95`, primary_closer `0.525`, primary_mae `0.028822`, avg `0.089717`, median `0.096338`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.01706`, avg `-0.003641`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.018283`, avg `-0.005618`, median `-0.006363`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.032076`, avg `-0.010428`, median `-0.023721`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.064078`, avg `-0.001691`, median `-0.008263`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.060637`, avg `0.089323`, median `0.108792`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019616`, avg `0.000819`, median `0.002703`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.6`, primary_mae `0.025461`, avg `0.000564`, median `-0.011716`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.025779`, avg `0.01076`, median `-0.000753`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.8`, primary_mae `0.042675`, avg `0.045287`, median `0.026541`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.075318`, avg `0.072833`, median `0.036672`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.011739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017591, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021387, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.875, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.033049, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.028822, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01509, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016137, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.011739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019147, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024064, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.017591, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023209, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032893, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021387, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032834, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05519, 'direction_hit_rate': 0.7875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.875, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.033049, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04215, 'direction_hit_rate': 0.875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049718, 'direction_hit_rate': 0.125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.028822, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.013099`, avg `0.010606`, median `0.016621`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.017173`, avg `0.014887`, median `0.012047`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.024824`, avg `0.016471`, median `0.017921`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.875`, primary_mae `0.021695`, avg `0.059849`, median `0.060676`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.015877`, avg `0.105861`, median `0.099778`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.013511`, avg `0.007015`, median `0.012449`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.022844`, avg `0.007893`, median `0.008828`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.028455`, avg `0.013055`, median `0.015682`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.625`, primary_mae `0.02968`, avg `0.051855`, median `0.058396`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.030045`, avg `0.090134`, median `0.09828`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.017117`, avg `-0.006681`, median `-0.011531`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.016708`, avg `-0.008955`, median `-0.009043`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.032044`, avg `-0.012151`, median `-0.028333`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.061409`, avg `-0.00484`, median `-0.016989`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.056501`, avg `0.091173`, median `0.108792`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.5375`, primary_mae `0.015039`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.5625`, primary_mae `0.019731`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5125`, primary_mae `0.025157`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.625`, primary_mae `0.043213`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.0484`, avg `0.085397`, median `0.098855`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.5375`, primary_mae `0.015039`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.5625`, primary_mae `0.019731`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5125`, primary_mae `0.025157`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.625`, primary_mae `0.043213`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.0484`, avg `0.085397`, median `0.098855`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.012101`, avg `0.008481`, median `0.012678`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.02018`, avg `0.00962`, median `0.009975`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.027224`, avg `0.01323`, median `0.013533`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.038555`, avg `0.042711`, median `0.040733`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.4`, primary_mae `0.025971`, avg `0.093442`, median `0.099615`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.018338`, avg `-0.001411`, median `-0.000629`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.625`, primary_mae `0.021872`, avg `-0.002527`, median `-0.008187`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.675`, primary_mae `0.028927`, avg `0.000166`, median `-0.007442`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.675`, primary_mae `0.053376`, avg `0.021798`, median `0.021077`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.067978`, avg `0.081078`, median `0.103937`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.5375`, primary_mae `0.015039`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.5625`, primary_mae `0.019731`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5125`, primary_mae `0.025157`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.625`, primary_mae `0.043213`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.0484`, avg `0.085397`, median `0.098855`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.5375`, primary_mae `0.015039`, avg `0.002409`, median `0.005428`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.5625`, primary_mae `0.019731`, avg `0.00193`, median `0.002671`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5125`, primary_mae `0.025157`, avg `0.0046`, median `0.004191`
- 20d: sample `80`, primary_hit `0.5875`, primary_closer `0.625`, primary_mae `0.043213`, avg `0.029465`, median `0.031783`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.0484`, avg `0.085397`, median `0.098855`

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
