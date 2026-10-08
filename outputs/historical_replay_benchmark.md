# Historical Replay Benchmark

Generated at: `2026-10-08T02:42:39.176794+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.01938`
- secondary_mean_absolute_error: `0.015807`
- primary_error_advantage: `-0.003573`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.0242`
- secondary_mean_absolute_error: `0.019792`
- primary_error_advantage: `-0.004408`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.041965`
- secondary_mean_absolute_error: `0.030582`
- primary_error_advantage: `-0.011383`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.079031`
- secondary_mean_absolute_error: `0.059062`
- primary_error_advantage: `-0.019969`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.076002`
- secondary_mean_absolute_error: `0.057144`
- primary_error_advantage: `-0.018858`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016574`, as_primary `0`, as_primary_hit `None`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.019019`, as_primary `0`, as_primary_hit `None`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.029201`, as_primary `0`, as_primary_hit `None`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.043085`, as_primary `0`, as_primary_hit `None`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.050721`, as_primary `0`, as_primary_hit `None`, avg `0.040374`, median `0.052147`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.015796`, as_primary `0`, as_primary_hit `None`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.019642`, as_primary `0`, as_primary_hit `None`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.033709`, as_primary `0`, as_primary_hit `None`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.061239`, as_primary `0`, as_primary_hit `None`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.056432`, as_primary `0`, as_primary_hit `None`, avg `0.040374`, median `0.052147`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.01938`, as_primary `80`, as_primary_hit `0.4125`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.0242`, as_primary `80`, as_primary_hit `0.425`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.041965`, as_primary `80`, as_primary_hit `0.45`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.079031`, as_primary `80`, as_primary_hit `0.5625`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.076002`, as_primary `80`, as_primary_hit `0.8`, avg `0.040374`, median `0.052147`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.01576`, as_primary `0`, as_primary_hit `None`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.018991`, as_primary `0`, as_primary_hit `None`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.028786`, as_primary `0`, as_primary_hit `None`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.043562`, as_primary `0`, as_primary_hit `None`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.052561`, as_primary `0`, as_primary_hit `None`, avg `0.040374`, median `0.052147`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.01938`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.0242`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.041965`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.079031`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.076002`, avg `0.040374`, median `0.052147`

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
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.01938`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.0242`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.041965`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.079031`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.076002`, avg `0.040374`, median `0.052147`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5875, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.01938, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.0242, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.041965, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.079031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.076002, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01576, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01938, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5875, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.01938, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018991, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0242, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.0242, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028786, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041965, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.041965, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043085, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079031, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.079031, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050721, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076002, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.076002, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.026372`, avg `-0.009683`, median `-0.011802`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.040421`, avg `-0.014553`, median `-0.01059`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.046232`, avg `-0.017771`, median `-0.015896`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.085191`, avg `-0.01538`, median `-0.000101`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.105094`, avg `-0.046636`, median `-0.048596`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.021033`, avg `-0.013234`, median `-0.018481`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.034076`, avg `-0.016786`, median `-0.020293`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.1875`, primary_mae `0.04419`, avg `-0.019747`, median `-0.017516`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.09019`, avg `-0.007454`, median `0.008742`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.11288`, avg `-0.00716`, median `0.041125`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.022013`, avg `-0.011073`, median `-0.010304`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.022341`, avg `-0.008207`, median `-0.008295`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.05656`, avg `0.000678`, median `0.013888`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.09744`, avg `0.022119`, median `0.03756`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.098812`, avg `0.098011`, median `0.115176`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.01938`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.0242`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.041965`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.079031`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.076002`, avg `0.040374`, median `0.052147`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.01938`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.0242`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.041965`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.079031`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.076002`, avg `0.040374`, median `0.052147`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.022288`, avg `-0.011521`, median `-0.015558`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.03381`, avg `-0.016712`, median `-0.020293`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.3`, primary_mae `0.039488`, avg `-0.027701`, median `-0.024563`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.080913`, avg `-0.017425`, median `-0.001627`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.109247`, avg `-0.001741`, median `0.035253`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.275`, primary_mae `0.017415`, avg `-0.005378`, median `-0.003662`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.017864`, avg `-0.005366`, median `-0.004042`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.042785`, avg `-0.00209`, median `0.005455`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.087409`, avg `0.009355`, median `0.025964`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.175`, primary_mae `0.07587`, avg `0.053794`, median `0.05712`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.01938`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.0242`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.041965`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.079031`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.076002`, avg `0.040374`, median `0.052147`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.35`, primary_mae `0.01938`, avg `-0.00571`, median `-0.003835`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.0242`, avg `-0.008308`, median `-0.007022`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.041965`, avg `-0.010635`, median `-0.008269`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.079031`, avg `0.001424`, median `0.014286`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.076002`, avg `0.040374`, median `0.052147`

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
