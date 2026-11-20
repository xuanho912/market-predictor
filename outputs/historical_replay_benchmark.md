# Historical Replay Benchmark

Generated at: `2026-11-20T02:01:59.663222+00:00`
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
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.023043`
- secondary_mean_absolute_error: `0.020669`
- primary_error_advantage: `-0.002374`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.026302`
- secondary_mean_absolute_error: `0.025736`
- primary_error_advantage: `-0.000566`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.03825`
- secondary_mean_absolute_error: `0.03057`
- primary_error_advantage: `-0.00768`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.075`
- secondary_hit_rate: `0.925`
- primary_vs_secondary_accuracy_spread: `-0.85`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.062259`
- secondary_mean_absolute_error: `0.03433`
- primary_error_advantage: `-0.027929`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.075`
- secondary_hit_rate: `0.925`
- primary_vs_secondary_accuracy_spread: `-0.85`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.074884`
- secondary_mean_absolute_error: `0.044424`
- primary_error_advantage: `-0.03046`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.020686`, as_primary `0`, as_primary_hit `None`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025129`, as_primary `0`, as_primary_hit `None`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, direction_hit `0.75`, path_mae `0.032872`, as_primary `0`, as_primary_hit `None`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, direction_hit `0.925`, path_mae `0.035781`, as_primary `0`, as_primary_hit `None`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, direction_hit `0.925`, path_mae `0.043924`, as_primary `0`, as_primary_hit `None`, avg `0.137117`, median `0.130638`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.022782`, as_primary `0`, as_primary_hit `None`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.026911`, as_primary `0`, as_primary_hit `None`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, direction_hit `0.75`, path_mae `0.040687`, as_primary `0`, as_primary_hit `None`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, direction_hit `0.925`, path_mae `0.052882`, as_primary `0`, as_primary_hit `None`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, direction_hit `0.925`, path_mae `0.055142`, as_primary `0`, as_primary_hit `None`, avg `0.137117`, median `0.130638`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.023043`, as_primary `80`, as_primary_hit `0.625`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.026302`, as_primary `80`, as_primary_hit `0.55`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, direction_hit `0.25`, path_mae `0.03825`, as_primary `80`, as_primary_hit `0.75`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, direction_hit `0.075`, path_mae `0.062259`, as_primary `80`, as_primary_hit `0.925`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, direction_hit `0.075`, path_mae `0.074884`, as_primary `80`, as_primary_hit `0.925`, avg `0.137117`, median `0.130638`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.020669`, as_primary `0`, as_primary_hit `None`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025736`, as_primary `0`, as_primary_hit `None`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, direction_hit `0.75`, path_mae `0.03057`, as_primary `0`, as_primary_hit `None`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, direction_hit `0.925`, path_mae `0.03433`, as_primary `0`, as_primary_hit `None`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, direction_hit `0.925`, path_mae `0.044424`, as_primary `0`, as_primary_hit `None`, avg `0.137117`, median `0.130638`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.023043`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.026302`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, primary_hit `0.25`, primary_closer `0.3875`, primary_mae `0.03825`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.062259`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.074884`, avg `0.137117`, median `0.130638`

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
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.023043`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.026302`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, primary_hit `0.25`, primary_closer `0.3875`, primary_mae `0.03825`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.062259`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.074884`, avg `0.137117`, median `0.130638`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.023043, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.026302, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.03825, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.062259, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.074884, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020669, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023043, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.023043, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025129, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026911, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.026302, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03057, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040687, 'direction_hit_rate': 0.75}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.03825, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.075, 'secondary_hit_rate': 0.925, 'primary_vs_secondary_accuracy_spread': -0.85, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03433, 'direction_hit_rate': 0.925}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062259, 'direction_hit_rate': 0.075}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.062259, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.075, 'secondary_hit_rate': 0.925, 'primary_vs_secondary_accuracy_spread': -0.85, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043924, 'direction_hit_rate': 0.925}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074884, 'direction_hit_rate': 0.075}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.075, 'primary_closer_than_secondary_rate': 0.2375, 'primary_mean_absolute_error': 0.074884, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.018434`, avg `-0.005957`, median `-0.00959`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.01835`, avg `-0.007021`, median `-0.008184`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.022237`, avg `0.011987`, median `0.010916`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.074629`, avg `0.066842`, median `0.075302`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.049878`, avg `0.123538`, median `0.131952`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019312`, avg `0.00181`, median `0.001229`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.024055`, avg `0.002792`, median `-0.005659`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.032757`, avg `0.02306`, median `0.018154`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.066821`, avg `0.052148`, median `0.060248`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.049537`, avg `0.100886`, median `0.116909`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.0211`, avg `0.000368`, median `-0.000993`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.022284`, avg `2e-05`, median `-0.000667`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.03815`, avg `0.009774`, median `0.007697`
- 20d: sample `16`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.056027`, avg `0.049926`, median `0.049597`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.048265`, avg `0.091174`, median `0.100157`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.023043`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.026302`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, primary_hit `0.25`, primary_closer `0.3875`, primary_mae `0.03825`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.062259`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.074884`, avg `0.137117`, median `0.130638`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.023043`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.026302`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, primary_hit `0.25`, primary_closer `0.3875`, primary_mae `0.03825`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.062259`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.074884`, avg `0.137117`, median `0.130638`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.020587`, avg `0.00571`, median `0.009911`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02513`, avg `0.007988`, median `0.006398`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.030034`, avg `0.024138`, median `0.026455`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.061487`, avg `0.048166`, median `0.051337`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.3`, primary_mae `0.05173`, avg `0.094155`, median `0.116909`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.45`, primary_mae `0.022531`, avg `0.006859`, median `0.008088`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.5333`, primary_mae `0.024655`, avg `0.013292`, median `0.008449`
- 10d: sample `60`, primary_hit `0.25`, primary_closer `0.4167`, primary_mae `0.033091`, avg `0.032718`, median `0.035053`
- 20d: sample `60`, primary_hit `0.0833`, primary_closer `0.2333`, primary_mae `0.063241`, avg `0.069246`, median `0.062899`
- 60d: sample `60`, primary_hit `0.0833`, primary_closer `0.25`, primary_mae `0.076715`, avg `0.131328`, median `0.119395`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.023043`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.026302`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, primary_hit `0.25`, primary_closer `0.3875`, primary_mae `0.03825`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.062259`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.074884`, avg `0.137117`, median `0.130638`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.375`, primary_closer `0.4125`, primary_mae `0.023043`, avg `0.007862`, median `0.007522`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.5125`, primary_mae `0.026302`, avg `0.013062`, median `0.004007`
- 10d: sample `80`, primary_hit `0.25`, primary_closer `0.3875`, primary_mae `0.03825`, avg `0.032398`, median `0.03459`
- 20d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.062259`, avg `0.070886`, median `0.067355`
- 60d: sample `80`, primary_hit `0.075`, primary_closer `0.2375`, primary_mae `0.074884`, avg `0.137117`, median `0.130638`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
