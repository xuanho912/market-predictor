# Historical Replay Benchmark

Generated at: `2026-10-21T17:21:26.162453+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.012497`
- secondary_mean_absolute_error: `0.012402`
- primary_error_advantage: `-9.5e-05`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.1125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.017782`
- secondary_mean_absolute_error: `0.016453`
- primary_error_advantage: `-0.001329`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.028285`
- secondary_mean_absolute_error: `0.025834`
- primary_error_advantage: `-0.002451`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.042703`
- secondary_mean_absolute_error: `0.030687`
- primary_error_advantage: `-0.012016`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.072468`
- secondary_mean_absolute_error: `0.065094`
- primary_error_advantage: `-0.007374`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.012405`, as_primary `0`, as_primary_hit `None`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016676`, as_primary `0`, as_primary_hit `None`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.022796`, as_primary `0`, as_primary_hit `None`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.025053`, as_primary `0`, as_primary_hit `None`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.057983`, as_primary `0`, as_primary_hit `None`, avg `0.032419`, median `0.033671`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.013106`, as_primary `20`, as_primary_hit `0.65`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.018632`, as_primary `20`, as_primary_hit `0.65`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.02596`, as_primary `20`, as_primary_hit `0.75`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.036403`, as_primary `20`, as_primary_hit `0.75`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.06938`, as_primary `20`, as_primary_hit `0.6`, avg `0.032419`, median `0.033671`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.012493`, as_primary `60`, as_primary_hit `0.5`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.017463`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.031367`, as_primary `60`, as_primary_hit `0.4833`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.043454`, as_primary `60`, as_primary_hit `0.7333`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.073049`, as_primary `60`, as_primary_hit `0.7`, avg `0.032419`, median `0.033671`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.012343`, as_primary `0`, as_primary_hit `None`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.016309`, as_primary `0`, as_primary_hit `None`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.022407`, as_primary `0`, as_primary_hit `None`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.024503`, as_primary `0`, as_primary_hit `None`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.057581`, as_primary `0`, as_primary_hit `None`, avg `0.032419`, median `0.033671`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.009562`, avg `-0.001027`, median `0.001546`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.013232`, avg `-0.000808`, median `0.00171`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.65`, primary_mae `0.016852`, avg `0.003259`, median `0.006005`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.035483`, avg `0.018673`, median `0.023144`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.077979`, avg `0.021943`, median `0.033172`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.015433`, avg `0.000808`, median `0.005393`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.022331`, avg `0.000281`, median `0.00026`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.325`, primary_mae `0.039718`, avg `0.000212`, median `0.002512`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.049922`, avg `0.016215`, median `0.01868`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.425`, primary_mae `0.066957`, avg `0.042894`, median `0.036417`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.00748`, avg `0.003206`, median `0.004629`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.013524`, avg `0.003388`, median `0.005606`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.016282`, avg `0.005435`, median `0.010338`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.023682`, avg `0.014143`, median `0.014043`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.070596`, avg `0.00611`, median `0.014514`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018541`, avg `-0.00044`, median `-0.003812`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.023942`, avg `-0.001588`, median `-0.010047`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.037887`, avg `-0.003762`, median `-0.01452`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.043019`, avg `0.012812`, median `0.018905`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.5`, primary_mae `0.037168`, avg `0.039017`, median `0.035618`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.011983`, avg `-0.001602`, median `0.000649`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.01683`, avg `-0.001427`, median `-0.00019`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.029486`, avg `0.002634`, median `0.002512`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.275`, primary_mae `0.052055`, avg `0.021411`, median `0.027848`
- 60d: sample `40`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.091054`, avg `0.042274`, median `0.052365`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.00748, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013524, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.016282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023682, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.037168, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012343, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013106, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.00748, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.1125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016309, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018632, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013524, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022407, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031367, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.016282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024503, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043454, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023682, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057581, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073049, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.037168, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.015937`, avg `-0.008856`, median `-0.009739`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.016766`, avg `-0.007496`, median `-0.008736`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.017728`, avg `-0.004284`, median `-0.012789`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.040442`, avg `0.010284`, median `0.019745`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.066116`, avg `0.004041`, median `0.004851`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.012013`, avg `-0.007617`, median `-0.009708`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.012948`, avg `-0.00639`, median `-0.004713`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016983`, avg `-0.00107`, median `-0.006514`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.046867`, avg `0.021772`, median `0.027848`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.081941`, avg `0.031978`, median `0.037982`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.017077`, avg `-0.003566`, median `-0.01228`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02467`, avg `-0.002073`, median `-0.004664`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.038416`, avg `-0.004691`, median `-0.01452`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.1875`, primary_mae `0.0453`, avg `0.014768`, median `0.019252`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.041859`, avg `0.040108`, median `0.03947`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### low_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.012497`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017782`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.028285`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.042703`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.072468`, avg `0.032419`, median `0.033671`

### fred_available
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_missing
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.012497`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017782`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.028285`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.042703`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.072468`, avg `0.032419`, median `0.033671`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.009562`, avg `-0.001027`, median `0.001546`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.013232`, avg `-0.000808`, median `0.00171`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.65`, primary_mae `0.016852`, avg `0.003259`, median `0.006005`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.035483`, avg `0.018673`, median `0.023144`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.077979`, avg `0.021943`, median `0.033172`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.015433`, avg `0.000808`, median `0.005393`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.022331`, avg `0.000281`, median `0.00026`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.325`, primary_mae `0.039718`, avg `0.000212`, median `0.002512`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.049922`, avg `0.016215`, median `0.01868`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.425`, primary_mae `0.066957`, avg `0.042894`, median `0.036417`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.012497`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017782`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.028285`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.042703`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.072468`, avg `0.032419`, median `0.033671`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.012497`, avg `-0.00011`, median `0.002179`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.4125`, primary_mae `0.017782`, avg `-0.000264`, median `0.000467`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.028285`, avg `0.001735`, median `0.004733`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3125`, primary_mae `0.042703`, avg `0.017444`, median `0.02136`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.072468`, avg `0.032419`, median `0.033671`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
