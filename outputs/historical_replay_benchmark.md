# Historical Replay Benchmark

Generated at: `2026-11-19T20:41:08.637087+00:00`
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
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.024285`
- secondary_mean_absolute_error: `0.020816`
- primary_error_advantage: `-0.003469`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.025096`
- secondary_mean_absolute_error: `0.022749`
- primary_error_advantage: `-0.002347`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.042553`
- secondary_mean_absolute_error: `0.032021`
- primary_error_advantage: `-0.010532`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.07796`
- secondary_mean_absolute_error: `0.043927`
- primary_error_advantage: `-0.034033`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.083146`
- secondary_mean_absolute_error: `0.077129`
- primary_error_advantage: `-0.006017`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.021291`, as_primary `0`, as_primary_hit `None`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022917`, as_primary `0`, as_primary_hit `None`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.033522`, as_primary `0`, as_primary_hit `None`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.046151`, as_primary `0`, as_primary_hit `None`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.079265`, as_primary `0`, as_primary_hit `None`, avg `0.042044`, median `0.052222`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.021234`, as_primary `0`, as_primary_hit `None`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022841`, as_primary `0`, as_primary_hit `None`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.040872`, as_primary `0`, as_primary_hit `None`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.07108`, as_primary `0`, as_primary_hit `None`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.097629`, as_primary `0`, as_primary_hit `None`, avg `0.042044`, median `0.052222`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.024285`, as_primary `80`, as_primary_hit `0.6`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.025096`, as_primary `80`, as_primary_hit `0.65`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.042553`, as_primary `80`, as_primary_hit `0.675`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.07796`, as_primary `80`, as_primary_hit `0.7`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.083146`, as_primary `80`, as_primary_hit `0.5875`, avg `0.042044`, median `0.052222`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.020816`, as_primary `0`, as_primary_hit `None`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022749`, as_primary `0`, as_primary_hit `None`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.032021`, as_primary `0`, as_primary_hit `None`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.043927`, as_primary `0`, as_primary_hit `None`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.077129`, as_primary `0`, as_primary_hit `None`, avg `0.042044`, median `0.052222`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.024285`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.025096`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.042553`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.07796`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4375`, primary_mae `0.083146`, avg `0.042044`, median `0.052222`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.032362`, avg `-0.008456`, median `-0.010844`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.031387`, avg `0.001592`, median `0.005446`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.05652`, avg `0.01681`, median `0.019434`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.129831`, avg `0.014404`, median `0.02439`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.102128`, avg `-0.002585`, median `-0.021408`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.3667`, primary_mae `0.021592`, avg `0.011075`, median `0.009541`
- 5d: sample `60`, primary_hit `0.3167`, primary_closer `0.4333`, primary_mae `0.022998`, avg `0.011463`, median `0.010702`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.3667`, primary_mae `0.037897`, avg `0.018856`, median `0.013914`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.25`, primary_mae `0.06067`, avg `0.035528`, median `0.0388`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.4167`, primary_mae `0.076819`, avg `0.05692`, median `0.066693`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.021592, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.022998, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.037897, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.06067, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.076819, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020816, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024285, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.021592, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022749, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025096, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.022998, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032021, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042553, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.037897, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043927, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07796, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.06067, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077129, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.097629, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.076819, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.030385`, avg `0.019725`, median `0.019594`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.025122`, avg `0.018908`, median `0.016938`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.050607`, avg `0.04092`, median `0.042409`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.070919`, avg `0.068048`, median `0.056364`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.102287`, avg `0.076573`, median `0.084187`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.024842`, avg `0.016637`, median `0.010315`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.030324`, avg `0.01856`, median `0.029084`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.05617`, avg `0.043375`, median `0.049918`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.069336`, avg `0.065802`, median `0.059804`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.107673`, avg `0.105608`, median `0.128786`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.036173`, avg `-0.003303`, median `-0.001755`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.033441`, avg `0.006989`, median `0.010878`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.054202`, avg `0.029764`, median `0.019434`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.130695`, avg `0.029897`, median `0.040222`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.076849`, avg `-0.009305`, median `-0.034156`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.024285`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.025096`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.042553`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.07796`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4375`, primary_mae `0.083146`, avg `0.042044`, median `0.052222`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.024285`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.025096`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.042553`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.07796`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4375`, primary_mae `0.083146`, avg `0.042044`, median `0.052222`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.022427`, avg `0.005083`, median `0.008011`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.018503`, avg `0.00361`, median `0.004974`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.028917`, avg `0.001335`, median `-0.000779`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.062013`, avg `0.010842`, median `0.008148`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.067694`, avg `0.020845`, median `0.000212`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.3833`, primary_mae `0.022868`, avg `0.001499`, median `0.006403`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.4333`, primary_mae `0.021939`, avg `0.003329`, median `0.005446`
- 10d: sample `60`, primary_hit `0.3833`, primary_closer `0.35`, primary_mae `0.036173`, avg `0.009901`, median `0.007697`
- 20d: sample `60`, primary_hit `0.3667`, primary_closer `0.2667`, primary_mae `0.07935`, avg `0.018931`, median `0.028101`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.075798`, avg `0.022998`, median `0.003033`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.024285`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.025096`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.042553`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.07796`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4375`, primary_mae `0.083146`, avg `0.042044`, median `0.052222`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4`, primary_closer `0.375`, primary_mae `0.024285`, avg `0.006192`, median `0.00813`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.425`, primary_mae `0.025096`, avg `0.008995`, median `0.009149`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.042553`, avg `0.018345`, median `0.016032`
- 20d: sample `80`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.07796`, avg `0.030247`, median `0.03791`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.4375`, primary_mae `0.083146`, avg `0.042044`, median `0.052222`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
