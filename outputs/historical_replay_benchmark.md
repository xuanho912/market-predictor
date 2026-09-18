# Historical Replay Benchmark

Generated at: `2026-09-18T16:27:50.293204+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.016708`
- secondary_mean_absolute_error: `0.015528`
- primary_error_advantage: `-0.00118`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.020951`
- secondary_mean_absolute_error: `0.017041`
- primary_error_advantage: `-0.00391`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.028344`
- secondary_mean_absolute_error: `0.023743`
- primary_error_advantage: `-0.004601`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.060343`
- secondary_mean_absolute_error: `0.037267`
- primary_error_advantage: `-0.023076`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.104503`
- secondary_mean_absolute_error: `0.065313`
- primary_error_advantage: `-0.03919`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015779`, as_primary `0`, as_primary_hit `None`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017859`, as_primary `0`, as_primary_hit `None`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.025966`, as_primary `0`, as_primary_hit `None`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.038668`, as_primary `0`, as_primary_hit `None`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.068421`, as_primary `0`, as_primary_hit `None`, avg `0.043609`, median `0.059722`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.017383`, as_primary `0`, as_primary_hit `None`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.020328`, as_primary `0`, as_primary_hit `None`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.036146`, as_primary `0`, as_primary_hit `None`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.060227`, as_primary `0`, as_primary_hit `None`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.081648`, as_primary `0`, as_primary_hit `None`, avg `0.043609`, median `0.059722`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.016708`, as_primary `80`, as_primary_hit `0.425`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.020951`, as_primary `80`, as_primary_hit `0.45`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.028344`, as_primary `80`, as_primary_hit `0.4`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.060343`, as_primary `80`, as_primary_hit `0.5875`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.104503`, as_primary `80`, as_primary_hit `0.75`, avg `0.043609`, median `0.059722`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015528`, as_primary `0`, as_primary_hit `None`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.017041`, as_primary `0`, as_primary_hit `None`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023743`, as_primary `0`, as_primary_hit `None`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.037267`, as_primary `0`, as_primary_hit `None`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.065313`, as_primary `0`, as_primary_hit `None`, avg `0.043609`, median `0.059722`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.016708`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.020951`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.028344`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.060343`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.104503`, avg `0.043609`, median `0.059722`

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
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.017652`, avg `-0.009384`, median `-0.010184`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.022756`, avg `-0.013428`, median `-0.017704`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.3667`, primary_mae `0.027503`, avg `-0.014174`, median `-0.016078`
- 20d: sample `60`, primary_hit `0.45`, primary_closer `0.2833`, primary_mae `0.067741`, avg `0.008418`, median `0.018008`
- 60d: sample `60`, primary_hit `0.2667`, primary_closer `0.2667`, primary_mae `0.114824`, avg `0.036328`, median `0.059313`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.65`, primary_mae `0.013875`, avg `0.001687`, median `0.009095`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.015537`, avg `0.004007`, median `0.00616`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.03087`, avg `0.012174`, median `0.012124`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.03815`, avg `0.021049`, median `0.012673`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.073539`, avg `0.065449`, median `0.062974`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.013875, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015537, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.027503, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.03815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.073539, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015528, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017383, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.013875, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017041, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020951, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015537, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023743, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036146, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.027503, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037267, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060343, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.03815, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065313, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.104503, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.073539, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.875`, primary_mae `0.007324`, avg `0.009739`, median `0.010341`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.012944`, avg `0.012684`, median `0.018767`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.033919`, avg `0.016277`, median `0.016207`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.040556`, avg `0.026304`, median `0.030279`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.070459`, avg `0.062563`, median `0.074898`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.6875`, primary_mae `0.014321`, avg `0.002621`, median `0.009121`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.5`, primary_mae `0.013875`, avg `0.006576`, median `0.00616`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.036452`, avg `0.016475`, median `0.016937`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.04307`, avg `0.026899`, median `0.015123`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.081809`, avg `0.070717`, median `0.069664`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.018975`, avg `-0.015812`, median `-0.016641`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.375`, primary_mae `0.023769`, avg `-0.02243`, median `-0.022951`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.4375`, primary_mae `0.029124`, avg `-0.032801`, median `-0.038715`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.07122`, avg `-0.020635`, median `-0.029855`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.157577`, avg `0.006742`, median `0.054522`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.016708`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.020951`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.028344`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.060343`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.104503`, avg `0.043609`, median `0.059722`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.016708`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.020951`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.028344`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.060343`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.104503`, avg `0.043609`, median `0.059722`

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
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.016708`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.020951`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.028344`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.060343`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.104503`, avg `0.043609`, median `0.059722`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.016708`, avg `-0.006617`, median `-0.00911`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3875`, primary_mae `0.020951`, avg `-0.009069`, median `-0.010108`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.3625`, primary_mae `0.028344`, avg `-0.007587`, median `-0.012286`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.325`, primary_mae `0.060343`, avg `0.011576`, median `0.015571`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.104503`, avg `0.043609`, median `0.059722`

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
