# Historical Replay Benchmark

Generated at: `2026-09-16T23:06:09.248158+00:00`
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
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.02084`
- secondary_mean_absolute_error: `0.01659`
- primary_error_advantage: `-0.00425`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.023372`
- secondary_mean_absolute_error: `0.018148`
- primary_error_advantage: `-0.005224`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.029905`
- secondary_mean_absolute_error: `0.025845`
- primary_error_advantage: `-0.00406`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.058988`
- secondary_mean_absolute_error: `0.035798`
- primary_error_advantage: `-0.02319`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.107518`
- secondary_mean_absolute_error: `0.071185`
- primary_error_advantage: `-0.036333`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.016475`, as_primary `0`, as_primary_hit `None`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.018433`, as_primary `0`, as_primary_hit `None`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.028834`, as_primary `0`, as_primary_hit `None`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, direction_hit `0.525`, path_mae `0.036184`, as_primary `0`, as_primary_hit `None`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.074988`, as_primary `0`, as_primary_hit `None`, avg `0.038468`, median `0.059251`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.018023`, as_primary `0`, as_primary_hit `None`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.024473`, as_primary `0`, as_primary_hit `None`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.041436`, as_primary `0`, as_primary_hit `None`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, direction_hit `0.525`, path_mae `0.05539`, as_primary `0`, as_primary_hit `None`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.080627`, as_primary `0`, as_primary_hit `None`, avg `0.038468`, median `0.059251`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.02084`, as_primary `80`, as_primary_hit `0.475`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.023372`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.029905`, as_primary `80`, as_primary_hit `0.4`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, direction_hit `0.475`, path_mae `0.058988`, as_primary `80`, as_primary_hit `0.525`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, direction_hit `0.2875`, path_mae `0.107518`, as_primary `80`, as_primary_hit `0.7125`, avg `0.038468`, median `0.059251`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.01659`, as_primary `0`, as_primary_hit `None`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.018148`, as_primary `0`, as_primary_hit `None`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.025845`, as_primary `0`, as_primary_hit `None`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, direction_hit `0.525`, path_mae `0.035798`, as_primary `0`, as_primary_hit `None`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.071185`, as_primary `0`, as_primary_hit `None`, avg `0.038468`, median `0.059251`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3625`, primary_mae `0.02084`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.023372`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.029905`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.058988`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3375`, primary_mae `0.107518`, avg `0.038468`, median `0.059251`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3625`, primary_mae `0.02084`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.023372`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.029905`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.058988`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3375`, primary_mae `0.107518`, avg `0.038468`, median `0.059251`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.02084, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5125, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023372, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.029905, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.058988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2875, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.107518, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016475, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02084, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.02084, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018148, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024473, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5125, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023372, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025845, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041436, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.029905, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035798, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058988, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.058988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071185, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.107518, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2875, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.107518, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.023212`, avg `-0.004233`, median `-0.005846`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.023746`, avg `-0.009463`, median `-0.010036`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.020022`, avg `-0.001061`, median `-0.005954`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.056171`, avg `0.026282`, median `0.024576`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.092055`, avg `0.040031`, median `0.044859`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.02509`, avg `-0.002437`, median `0.000341`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.022426`, avg `-0.008025`, median `0.000647`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.017918`, avg `-0.006025`, median `-0.008236`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.05594`, avg `0.02605`, median `0.030181`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.102369`, avg `0.050624`, median `0.072376`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.024997`, avg `-0.003872`, median `-0.00059`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.037118`, avg `-0.005841`, median `0.000234`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.042417`, avg `-0.014562`, median `-0.029632`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.072114`, avg `-0.00963`, median `-0.019222`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.189422`, avg `0.009259`, median `0.054522`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3625`, primary_mae `0.02084`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.023372`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.029905`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.058988`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3375`, primary_mae `0.107518`, avg `0.038468`, median `0.059251`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3625`, primary_mae `0.02084`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.023372`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.029905`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.058988`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3375`, primary_mae `0.107518`, avg `0.038468`, median `0.059251`

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
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.3625`, primary_mae `0.02084`, avg `-0.00367`, median `-0.001727`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.35`, primary_mae `0.023372`, avg `-0.005472`, median `-0.001281`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.029905`, avg `-0.006405`, median `-0.014131`
- 20d: sample `80`, primary_hit `0.475`, primary_closer `0.3`, primary_mae `0.058988`, avg `0.008931`, median `0.002079`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.3375`, primary_mae `0.107518`, avg `0.038468`, median `0.059251`

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
