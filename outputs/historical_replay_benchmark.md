# Historical Replay Benchmark

Generated at: `2026-07-17T14:06:34.711854+00:00`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.01946`
- secondary_mean_absolute_error: `0.014128`
- primary_error_advantage: `-0.005332`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.023382`
- secondary_mean_absolute_error: `0.017439`
- primary_error_advantage: `-0.005943`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.225`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.02605`
- secondary_mean_absolute_error: `0.030499`
- primary_error_advantage: `0.004449`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.056209`
- secondary_mean_absolute_error: `0.044287`
- primary_error_advantage: `-0.011922`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.085423`
- secondary_mean_absolute_error: `0.073693`
- primary_error_advantage: `-0.01173`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.013541`, as_primary `0`, as_primary_hit `None`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.016351`, as_primary `0`, as_primary_hit `None`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.024922`, as_primary `0`, as_primary_hit `None`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.030433`, as_primary `0`, as_primary_hit `None`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.062604`, as_primary `0`, as_primary_hit `None`, avg `0.032065`, median `0.044937`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.014128`, as_primary `0`, as_primary_hit `None`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.017439`, as_primary `0`, as_primary_hit `None`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.030499`, as_primary `0`, as_primary_hit `None`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.044287`, as_primary `0`, as_primary_hit `None`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.073693`, as_primary `0`, as_primary_hit `None`, avg `0.032065`, median `0.044937`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.01946`, as_primary `80`, as_primary_hit `0.575`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.023382`, as_primary `80`, as_primary_hit `0.5625`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.02605`, as_primary `80`, as_primary_hit `0.4`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.056209`, as_primary `80`, as_primary_hit `0.7125`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.085423`, as_primary `80`, as_primary_hit `0.6125`, avg `0.032065`, median `0.044937`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.01273`, as_primary `0`, as_primary_hit `None`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.015684`, as_primary `0`, as_primary_hit `None`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023742`, as_primary `0`, as_primary_hit `None`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.030409`, as_primary `0`, as_primary_hit `None`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.061993`, as_primary `0`, as_primary_hit `None`, avg `0.032065`, median `0.044937`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3625`, primary_mae `0.01946`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.023382`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.02605`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.4125`, primary_mae `0.056209`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.085423`, avg `0.032065`, median `0.044937`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.3833`, primary_mae `0.020184`, avg `-0.002572`, median `0.000933`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.026301`, avg `-0.0008`, median `0.002095`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.5833`, primary_mae `0.026559`, avg `0.000516`, median `-0.004843`
- 20d: sample `60`, primary_hit `0.2167`, primary_closer `0.45`, primary_mae `0.052231`, avg `0.019926`, median `0.019949`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4`, primary_mae `0.092177`, avg `0.043201`, median `0.06313`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.017286`, avg `0.001143`, median `0.001417`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.014627`, avg `0.001259`, median `0.00278`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.024525`, avg `-0.008901`, median `-0.013311`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.068141`, avg `-0.009632`, median `0.001741`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.065161`, avg `-0.001341`, median `-0.019635`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.017286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014627, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.024525, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.052231, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.065161, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01273, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01946, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.017286, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015684, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023382, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.014627, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023742, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030499, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.024525, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030409, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056209, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2167, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.052231, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061993, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.085423, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.065161, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.026249`, avg `0.002832`, median `0.008701`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.125`, primary_mae `0.039229`, avg `-0.000744`, median `0.001165`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.023732`, avg `-0.004297`, median `-0.015682`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.038378`, avg `0.008811`, median `0.00391`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.087706`, avg `0.027216`, median `0.054932`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.025397`, avg `-0.000601`, median `0.004891`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.125`, primary_mae `0.036146`, avg `-0.000741`, median `0.002095`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.019255`, avg `-0.012555`, median `-0.019607`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.043995`, avg `0.015249`, median `0.008514`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.104018`, avg `0.0497`, median `0.101391`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.017526`, avg `0.002365`, median `0.001417`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.01338`, avg `0.002139`, median `0.002044`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.028436`, avg `-0.004017`, median `-0.007304`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.069069`, avg `-0.006208`, median `0.001741`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.076003`, avg `0.011128`, median `0.013899`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3625`, primary_mae `0.01946`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.023382`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.02605`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.4125`, primary_mae `0.056209`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.085423`, avg `0.032065`, median `0.044937`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3625`, primary_mae `0.01946`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.023382`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.02605`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.4125`, primary_mae `0.056209`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.085423`, avg `0.032065`, median `0.044937`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3625`, primary_mae `0.01946`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.023382`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.02605`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.4125`, primary_mae `0.056209`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.085423`, avg `0.032065`, median `0.044937`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.015942`, avg `-0.001009`, median `0.000374`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.016146`, avg `0.000905`, median `0.001894`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.55`, primary_mae `0.028613`, avg `0.000126`, median `-0.002875`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.375`, primary_mae `0.053133`, avg `0.010364`, median `0.012341`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.066139`, avg `0.024275`, median `0.038298`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.3625`, primary_mae `0.01946`, avg `-0.001643`, median `0.000944`
- 5d: sample `80`, primary_hit `0.4375`, primary_closer `0.3375`, primary_mae `0.023382`, avg `-0.000285`, median `0.002469`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.02605`, avg `-0.001838`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.4125`, primary_mae `0.056209`, avg `0.012537`, median `0.01416`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.085423`, avg `0.032065`, median `0.044937`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
