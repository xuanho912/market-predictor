# Historical Replay Benchmark

Generated at: `2026-11-22T19:44:10.541682+00:00`
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
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.045479`
- secondary_mean_absolute_error: `0.030556`
- primary_error_advantage: `-0.014923`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.225`
- primary_mean_absolute_error: `0.06199`
- secondary_mean_absolute_error: `0.036464`
- primary_error_advantage: `-0.025526`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.094469`
- secondary_mean_absolute_error: `0.054373`
- primary_error_advantage: `-0.040096`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.1875`
- primary_mean_absolute_error: `0.156165`
- secondary_mean_absolute_error: `0.076981`
- primary_error_advantage: `-0.079184`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.151464`
- secondary_mean_absolute_error: `0.10603`
- primary_error_advantage: `-0.045434`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.031748`, as_primary `0`, as_primary_hit `None`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.036985`, as_primary `0`, as_primary_hit `None`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.053762`, as_primary `0`, as_primary_hit `None`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.075953`, as_primary `0`, as_primary_hit `None`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.104737`, as_primary `0`, as_primary_hit `None`, avg `0.027625`, median `0.051113`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.030527`, as_primary `0`, as_primary_hit `None`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.038272`, as_primary `0`, as_primary_hit `None`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.065814`, as_primary `0`, as_primary_hit `None`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.100838`, as_primary `0`, as_primary_hit `None`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.135583`, as_primary `0`, as_primary_hit `None`, avg `0.027625`, median `0.051113`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.045479`, as_primary `80`, as_primary_hit `0.6`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, direction_hit `0.325`, path_mae `0.06199`, as_primary `80`, as_primary_hit `0.675`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.094469`, as_primary `80`, as_primary_hit `0.6`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.156165`, as_primary `80`, as_primary_hit `0.6625`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, direction_hit `0.4`, path_mae `0.151464`, as_primary `80`, as_primary_hit `0.6`, avg `0.027625`, median `0.051113`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.030556`, as_primary `0`, as_primary_hit `None`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.036464`, as_primary `0`, as_primary_hit `None`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.054373`, as_primary `0`, as_primary_hit `None`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.076981`, as_primary `0`, as_primary_hit `None`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, direction_hit `0.6`, path_mae `0.10603`, as_primary `0`, as_primary_hit `None`, avg `0.027625`, median `0.051113`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.2625`, primary_mae `0.045479`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.225`, primary_mae `0.06199`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.094469`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.1875`, primary_mae `0.156165`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.151464`, avg `0.027625`, median `0.051113`

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
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.2625`, primary_mae `0.045479`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.225`, primary_mae `0.06199`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.094469`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.1875`, primary_mae `0.156165`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.151464`, avg `0.027625`, median `0.051113`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.045479, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.06199, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.094469, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.1875, 'primary_mean_absolute_error': 0.156165, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.151464, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030527, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045479, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.2625, 'primary_mean_absolute_error': 0.045479, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.225, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036464, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06199, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.06199, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053762, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.094469, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.094469, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.1875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075953, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.156165, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3375, 'primary_closer_than_secondary_rate': 0.1875, 'primary_mean_absolute_error': 0.156165, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.104737, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.151464, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.151464, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.028388`, avg `-0.00248`, median `-0.000439`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.028847`, avg `0.00833`, median `0.012765`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.060949`, avg `-0.007933`, median `0.013247`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.121002`, avg `-0.04067`, median `0.004182`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.042862`, avg `-0.008509`, median `-0.004316`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.031311`, avg `0.005235`, median `0.007977`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.023552`, avg `0.008174`, median `0.006663`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.057152`, avg `0.003931`, median `0.018028`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.125592`, avg `-0.004297`, median `0.02099`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.052794`, avg `0.01493`, median `0.003033`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.051137`, avg `-0.012222`, median `0.008886`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.079363`, avg `-0.017279`, median `0.008898`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.13155`, avg `-0.011037`, median `0.003849`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.206318`, avg `-0.037937`, median `0.006263`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.249415`, avg `-0.005964`, median `0.032603`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.2625`, primary_mae `0.045479`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.225`, primary_mae `0.06199`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.094469`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.1875`, primary_mae `0.156165`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.151464`, avg `0.027625`, median `0.051113`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.2625`, primary_mae `0.045479`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.225`, primary_mae `0.06199`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.094469`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.1875`, primary_mae `0.156165`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.151464`, avg `0.027625`, median `0.051113`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.2333`, primary_mae `0.045186`, avg `0.000527`, median `0.010624`
- 5d: sample `60`, primary_hit `0.3`, primary_closer `0.2167`, primary_mae `0.055245`, avg `0.002049`, median `0.012731`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.2667`, primary_mae `0.079932`, avg `0.004084`, median `0.019008`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.15`, primary_mae `0.137821`, avg `0.010326`, median `0.034467`
- 60d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.112322`, avg `0.030161`, median `0.052907`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.2625`, primary_mae `0.045479`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.225`, primary_mae `0.06199`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.094469`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.1875`, primary_mae `0.156165`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.151464`, avg `0.027625`, median `0.051113`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.2625`, primary_mae `0.045479`, avg `-0.00198`, median `0.0101`
- 5d: sample `80`, primary_hit `0.325`, primary_closer `0.225`, primary_mae `0.06199`, avg `-0.002307`, median `0.012707`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.094469`, avg `-0.002173`, median `0.019008`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.1875`, primary_mae `0.156165`, avg `-7.8e-05`, median `0.031811`
- 60d: sample `80`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.151464`, avg `0.027625`, median `0.051113`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
