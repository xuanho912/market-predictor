# Historical Replay Benchmark

Generated at: `2026-08-19T13:11:38.836457+00:00`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.018011`
- secondary_mean_absolute_error: `0.015805`
- primary_error_advantage: `-0.002206`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.021936`
- secondary_mean_absolute_error: `0.020501`
- primary_error_advantage: `-0.001435`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.035643`
- secondary_mean_absolute_error: `0.029775`
- primary_error_advantage: `-0.005868`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.072031`
- secondary_mean_absolute_error: `0.053466`
- primary_error_advantage: `-0.018565`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.087404`
- secondary_mean_absolute_error: `0.070372`
- primary_error_advantage: `-0.017032`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.014793`, as_primary `0`, as_primary_hit `None`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.020751`, as_primary `0`, as_primary_hit `None`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.025861`, as_primary `0`, as_primary_hit `None`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.043143`, as_primary `0`, as_primary_hit `None`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.067285`, as_primary `0`, as_primary_hit `None`, avg `0.032187`, median `0.045588`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.017873`, as_primary `20`, as_primary_hit `0.55`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.027944`, as_primary `20`, as_primary_hit `0.6`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.03667`, as_primary `20`, as_primary_hit `0.7`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.065236`, as_primary `20`, as_primary_hit `0.8`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.083742`, as_primary `20`, as_primary_hit `0.55`, avg `0.032187`, median `0.045588`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.018214`, as_primary `60`, as_primary_hit `0.6667`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.01982`, as_primary `60`, as_primary_hit `0.6333`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.034956`, as_primary `60`, as_primary_hit `0.6167`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.073633`, as_primary `60`, as_primary_hit `0.7`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.084671`, as_primary `60`, as_primary_hit `0.7167`, avg `0.032187`, median `0.045588`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.014392`, as_primary `0`, as_primary_hit `None`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.017253`, as_primary `0`, as_primary_hit `None`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.023713`, as_primary `0`, as_primary_hit `None`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.039105`, as_primary `0`, as_primary_hit `None`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.064576`, as_primary `0`, as_primary_hit `None`, avg `0.032187`, median `0.045588`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018011`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.021936`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.035643`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.072031`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.087404`, avg `0.032187`, median `0.045588`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018011`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.021936`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.035643`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.072031`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.087404`, avg `0.032187`, median `0.045588`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.021936, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.035643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.072031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.087404, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014392, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018214, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3875, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018011, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017253, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027944, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.4875, 'primary_mean_absolute_error': 0.021936, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023713, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03667, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.035643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039105, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073633, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.072031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064576, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084671, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4125, 'primary_mean_absolute_error': 0.087404, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.017358`, avg `0.004628`, median `0.005338`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.025506`, avg `0.003822`, median `0.004667`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.02456`, avg `0.010374`, median `0.011059`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.054598`, avg `0.016632`, median `0.015956`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.085629`, avg `0.01085`, median `-0.025539`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.023436`, avg `-0.000393`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.026563`, avg `0.005531`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.02696`, avg `0.01176`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.625`, primary_mae `0.050723`, avg `0.023687`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.07842`, avg `0.018535`, median `0.012785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.017463`, avg `0.008672`, median `0.009593`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.023803`, avg `0.001605`, median `-0.000777`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.042882`, avg `0.016726`, median `0.016311`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.09213`, avg `0.039041`, median `0.028759`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.061346`, avg `0.053778`, median `0.033928`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018011`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.021936`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.035643`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.072031`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.087404`, avg `0.032187`, median `0.045588`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018011`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.021936`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.035643`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.072031`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.087404`, avg `0.032187`, median `0.045588`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.019223`, avg `0.000638`, median `0.004273`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.5`, primary_mae `0.018381`, avg `0.005932`, median `0.006888`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.024039`, avg `0.006977`, median `0.011059`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.45`, primary_mae `0.047094`, avg `0.016735`, median `0.023144`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.061798`, avg `0.0228`, median `0.024312`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.015968`, avg `0.008956`, median `0.010408`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.023957`, avg `0.004673`, median `0.001259`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.043213`, avg `0.019097`, median `0.016311`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.090133`, avg `0.039422`, median `0.028759`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.45`, primary_mae `0.067872`, avg `0.066715`, median `0.06367`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018011`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.021936`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.035643`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.072031`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.087404`, avg `0.032187`, median `0.045588`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.018011`, avg `0.004448`, median `0.006639`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4875`, primary_mae `0.021936`, avg `0.005608`, median `0.005323`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.035643`, avg `0.008706`, median `0.011297`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.3875`, primary_mae `0.072031`, avg `0.01845`, median `0.022248`
- 60d: sample `80`, primary_hit `0.35`, primary_closer `0.4125`, primary_mae `0.087404`, avg `0.032187`, median `0.045588`

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
