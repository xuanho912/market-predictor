# Historical Replay Benchmark

Generated at: `2026-06-17T00:01:37.258618+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.01558`
- secondary_mean_absolute_error: `0.014047`
- primary_error_advantage: `-0.001533`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.021482`
- secondary_mean_absolute_error: `0.019206`
- primary_error_advantage: `-0.002276`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.026339`
- secondary_mean_absolute_error: `0.02202`
- primary_error_advantage: `-0.004319`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.047724`
- secondary_mean_absolute_error: `0.035668`
- primary_error_advantage: `-0.012056`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.073669`
- secondary_mean_absolute_error: `0.053337`
- primary_error_advantage: `-0.020332`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.014865`, as_primary `0`, as_primary_hit `None`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.020426`, as_primary `0`, as_primary_hit `None`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.022049`, as_primary `0`, as_primary_hit `None`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.030609`, as_primary `0`, as_primary_hit `None`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.057102`, as_primary `0`, as_primary_hit `None`, avg `0.033499`, median `0.039902`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.01558`, as_primary `80`, as_primary_hit `0.65`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.021482`, as_primary `80`, as_primary_hit `0.65`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.026339`, as_primary `80`, as_primary_hit `0.65`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.047724`, as_primary `80`, as_primary_hit `0.7625`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.073669`, as_primary `80`, as_primary_hit `0.6375`, avg `0.033499`, median `0.039902`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.35`, path_mae `0.015887`, as_primary `0`, as_primary_hit `None`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.020963`, as_primary `0`, as_primary_hit `None`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.029568`, as_primary `0`, as_primary_hit `None`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, direction_hit `0.2375`, path_mae `0.058266`, as_primary `0`, as_primary_hit `None`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.071585`, as_primary `0`, as_primary_hit `None`, avg `0.033499`, median `0.039902`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.65`, path_mae `0.014021`, as_primary `0`, as_primary_hit `None`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.018878`, as_primary `0`, as_primary_hit `None`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.02147`, as_primary `0`, as_primary_hit `None`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, direction_hit `0.7625`, path_mae `0.029045`, as_primary `0`, as_primary_hit `None`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.053517`, as_primary `0`, as_primary_hit `None`, avg `0.033499`, median `0.039902`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.3875`, primary_mae `0.01558`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.3625`, primary_mae `0.021482`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.026339`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.375`, primary_mae `0.047724`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.3375`, primary_mae `0.073669`, avg `0.033499`, median `0.039902`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.013355`, avg `0.005987`, median `0.004273`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.35`, primary_mae `0.016251`, avg `0.007343`, median `0.005768`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.015859`, avg `0.008283`, median `0.008571`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.040735`, avg `0.009779`, median `0.012734`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.064063`, avg `-0.008234`, median `-0.018485`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4`, primary_mae `0.016322`, avg `0.005926`, median `0.008474`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.3667`, primary_mae `0.023226`, avg `0.006981`, median `0.00776`
- 10d: sample `60`, primary_hit `0.65`, primary_closer `0.3833`, primary_mae `0.029833`, avg `0.012066`, median `0.013904`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.2833`, primary_mae `0.050054`, avg `0.019673`, median `0.026158`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.3333`, primary_mae `0.07687`, avg `0.04741`, median `0.058606`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013355, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.016251, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015859, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.040735, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.064063, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014021, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015887, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.013355, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018878, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021482, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.016251, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02147, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029568, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.015859, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029045, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058266, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.040735, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053517, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073669, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.064063, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.024104`, avg `-0.009751`, median `-0.008976`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.03097`, avg `-0.01508`, median `-0.014993`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.01702`, avg `0.009728`, median `0.010282`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.0`, primary_mae `0.03193`, avg `0.023574`, median `0.028979`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.046388`, avg `0.041325`, median `0.055714`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.021717`, avg `-0.003178`, median `-0.006094`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.02739`, avg `-0.00634`, median `-0.011576`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021989`, avg `0.010873`, median `0.006918`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.1875`, primary_mae `0.031499`, avg `0.028146`, median `0.030181`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.046651`, avg `0.043905`, median `0.055714`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.021717`, avg `-0.003178`, median `-0.006094`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.02739`, avg `-0.00634`, median `-0.011576`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021989`, avg `0.010873`, median `0.006918`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.1875`, primary_mae `0.031499`, avg `0.028146`, median `0.030181`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.046651`, avg `0.043905`, median `0.055714`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.3875`, primary_mae `0.01558`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.3625`, primary_mae `0.021482`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.026339`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.375`, primary_mae `0.047724`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.3375`, primary_mae `0.073669`, avg `0.033499`, median `0.039902`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.3875`, primary_mae `0.01558`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.3625`, primary_mae `0.021482`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.026339`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.375`, primary_mae `0.047724`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.3375`, primary_mae `0.073669`, avg `0.033499`, median `0.039902`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.3875`, primary_mae `0.01558`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.3625`, primary_mae `0.021482`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.026339`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.375`, primary_mae `0.047724`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.3375`, primary_mae `0.073669`, avg `0.033499`, median `0.039902`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.3875`, primary_mae `0.01558`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.3625`, primary_mae `0.021482`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.026339`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.375`, primary_mae `0.047724`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.3375`, primary_mae `0.073669`, avg `0.033499`, median `0.039902`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.65`, primary_closer `0.3875`, primary_mae `0.01558`, avg `0.005941`, median `0.006714`
- 5d: sample `80`, primary_hit `0.65`, primary_closer `0.3625`, primary_mae `0.021482`, avg `0.007072`, median `0.006888`
- 10d: sample `80`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.026339`, avg `0.01112`, median `0.012934`
- 20d: sample `80`, primary_hit `0.7625`, primary_closer `0.375`, primary_mae `0.047724`, avg `0.0172`, median `0.020645`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.3375`, primary_mae `0.073669`, avg `0.033499`, median `0.039902`

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
