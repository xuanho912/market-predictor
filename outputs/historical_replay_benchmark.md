# Historical Replay Benchmark

Generated at: `2026-09-23T06:21:11.573787+00:00`
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
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.020975`
- secondary_mean_absolute_error: `0.016931`
- primary_error_advantage: `-0.004044`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.024549`
- secondary_mean_absolute_error: `0.020699`
- primary_error_advantage: `-0.00385`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.036164`
- secondary_mean_absolute_error: `0.032269`
- primary_error_advantage: `-0.003895`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7875`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.057691`
- secondary_mean_absolute_error: `0.037231`
- primary_error_advantage: `-0.02046`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.825`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.059683`
- secondary_mean_absolute_error: `0.054203`
- primary_error_advantage: `-0.00548`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.017467`, as_primary `0`, as_primary_hit `None`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.021313`, as_primary `0`, as_primary_hit `None`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.031932`, as_primary `0`, as_primary_hit `None`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.040336`, as_primary `0`, as_primary_hit `None`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.052612`, as_primary `0`, as_primary_hit `None`, avg `0.066044`, median `0.079292`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.020975`, as_primary `80`, as_primary_hit `0.625`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.024549`, as_primary `80`, as_primary_hit `0.6125`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.036164`, as_primary `80`, as_primary_hit `0.6125`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.057691`, as_primary `80`, as_primary_hit `0.7875`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.059683`, as_primary `80`, as_primary_hit `0.825`, avg `0.066044`, median `0.079292`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.020938`, as_primary `0`, as_primary_hit `None`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.026388`, as_primary `0`, as_primary_hit `None`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.3875`, path_mae `0.044611`, as_primary `0`, as_primary_hit `None`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.2125`, path_mae `0.061416`, as_primary `0`, as_primary_hit `None`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.071006`, as_primary `0`, as_primary_hit `None`, avg `0.066044`, median `0.079292`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.016931`, as_primary `0`, as_primary_hit `None`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020699`, as_primary `0`, as_primary_hit `None`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, direction_hit `0.6125`, path_mae `0.032269`, as_primary `0`, as_primary_hit `None`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, direction_hit `0.7875`, path_mae `0.037231`, as_primary `0`, as_primary_hit `None`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.054203`, as_primary `0`, as_primary_hit `None`, avg `0.066044`, median `0.079292`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.020975`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.024549`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.036164`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.7875`, primary_closer `0.3125`, primary_mae `0.057691`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.825`, primary_closer `0.45`, primary_mae `0.059683`, avg `0.066044`, median `0.079292`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.014328`, avg `0.005695`, median `0.012244`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.018492`, avg `0.005954`, median `0.00893`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.025542`, avg `0.005065`, median `0.011325`
- 20d: sample `40`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.039922`, avg `0.030073`, median `0.033275`
- 60d: sample `40`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.040481`, avg `0.067004`, median `0.082331`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.027621`, avg `0.004952`, median `0.008122`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.030606`, avg `0.00577`, median `0.013359`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.046786`, avg `0.012294`, median `0.021158`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.275`, primary_mae `0.07546`, avg `0.032613`, median `0.028464`
- 60d: sample `40`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.078885`, avg `0.065084`, median `0.07206`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.014328, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018492, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.025542, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.039922, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.040481, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016931, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020975, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.014328, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020699, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026388, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.018492, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031932, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044611, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.025542, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7875, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037231, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061416, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.039922, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.825, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052612, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071006, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.040481, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.011579`, avg `0.010261`, median `0.018969`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.01755`, avg `0.011464`, median `0.011781`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.024499`, avg `0.014702`, median `0.017921`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.02051`, avg `0.059682`, median `0.060676`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.032522`, avg `0.089216`, median `0.099778`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.012056`, avg `0.011069`, median `0.017922`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.375`, primary_mae `0.017239`, avg `0.01426`, median `0.014527`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.021077`, avg `0.020542`, median `0.024318`
- 20d: sample `16`, primary_hit `1.0`, primary_closer `0.4375`, primary_mae `0.02813`, avg `0.053405`, median `0.058396`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.039723`, avg `0.080457`, median `0.096338`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.5625`, primary_mae `0.012056`, avg `0.011069`, median `0.017922`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.375`, primary_mae `0.017239`, avg `0.01426`, median `0.014527`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.021077`, avg `0.020542`, median `0.024318`
- 20d: sample `16`, primary_hit `1.0`, primary_closer `0.4375`, primary_mae `0.02813`, avg `0.053405`, median `0.058396`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.039723`, avg `0.080457`, median `0.096338`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.020975`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.024549`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.036164`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.7875`, primary_closer `0.3125`, primary_mae `0.057691`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.825`, primary_closer `0.45`, primary_mae `0.059683`, avg `0.066044`, median `0.079292`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.020975`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.024549`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.036164`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.7875`, primary_closer `0.3125`, primary_mae `0.057691`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.825`, primary_closer `0.45`, primary_mae `0.059683`, avg `0.066044`, median `0.079292`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014696`, avg `0.000998`, median `0.002973`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016454`, avg `-0.000165`, median `0.001407`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.023246`, avg `-0.004112`, median `0.004006`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.042735`, avg `0.01599`, median `0.030823`
- 60d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.038033`, avg `0.058882`, median `0.064839`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.020975`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.024549`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.036164`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.7875`, primary_closer `0.3125`, primary_mae `0.057691`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.825`, primary_closer `0.45`, primary_mae `0.059683`, avg `0.066044`, median `0.079292`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.020975`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.024549`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.036164`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.7875`, primary_closer `0.3125`, primary_mae `0.057691`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.825`, primary_closer `0.45`, primary_mae `0.059683`, avg `0.066044`, median `0.079292`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.020975`, avg `0.005324`, median `0.010835`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3875`, primary_mae `0.024549`, avg `0.005862`, median `0.010881`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.036164`, avg `0.008679`, median `0.011917`
- 20d: sample `80`, primary_hit `0.7875`, primary_closer `0.3125`, primary_mae `0.057691`, avg `0.031343`, median `0.032626`
- 60d: sample `80`, primary_hit `0.825`, primary_closer `0.45`, primary_mae `0.059683`, avg `0.066044`, median `0.079292`

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
