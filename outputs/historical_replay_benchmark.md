# Historical Replay Benchmark

Generated at: `2026-10-02T01:53:04.242997+00:00`
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
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.019113`
- secondary_mean_absolute_error: `0.016046`
- primary_error_advantage: `-0.003067`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.024554`
- secondary_mean_absolute_error: `0.019141`
- primary_error_advantage: `-0.005413`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.040597`
- secondary_mean_absolute_error: `0.027337`
- primary_error_advantage: `-0.01326`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.2625`
- primary_mean_absolute_error: `0.074116`
- secondary_mean_absolute_error: `0.041462`
- primary_error_advantage: `-0.032654`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.175`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `-0.65`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.08013`
- secondary_mean_absolute_error: `0.053337`
- primary_error_advantage: `-0.026793`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.016346`, as_primary `0`, as_primary_hit `None`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019067`, as_primary `0`, as_primary_hit `None`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.027473`, as_primary `0`, as_primary_hit `None`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.041323`, as_primary `0`, as_primary_hit `None`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.051758`, as_primary `0`, as_primary_hit `None`, avg `0.052756`, median `0.059117`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.015746`, as_primary `0`, as_primary_hit `None`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.020076`, as_primary `0`, as_primary_hit `None`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.032229`, as_primary `0`, as_primary_hit `None`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.062236`, as_primary `0`, as_primary_hit `None`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.05975`, as_primary `0`, as_primary_hit `None`, avg `0.052756`, median `0.059117`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.019113`, as_primary `80`, as_primary_hit `0.425`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.024554`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.040597`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, direction_hit `0.4125`, path_mae `0.074116`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.08013`, as_primary `80`, as_primary_hit `0.825`, avg `0.052756`, median `0.059117`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.016046`, as_primary `0`, as_primary_hit `None`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019141`, as_primary `0`, as_primary_hit `None`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.027337`, as_primary `0`, as_primary_hit `None`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, direction_hit `0.5875`, path_mae `0.041462`, as_primary `0`, as_primary_hit `None`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.053337`, as_primary `0`, as_primary_hit `None`, avg `0.052756`, median `0.059117`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.019113`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.024554`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3125`, primary_mae `0.040597`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.2625`, primary_mae `0.074116`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.08013`, avg `0.052756`, median `0.059117`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.35`, primary_mae `0.024403`, avg `-0.010127`, median `-0.010184`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.3`, primary_mae `0.028943`, avg `-0.012407`, median `-0.012577`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.35`, primary_mae `0.047299`, avg `-0.007289`, median `-0.008236`
- 20d: sample `40`, primary_hit `0.5`, primary_closer `0.275`, primary_mae `0.083721`, avg `0.004152`, median `0.007148`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.095501`, avg `0.066739`, median `0.096101`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.013823`, avg `0.000453`, median `0.001753`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.020166`, avg `-0.003881`, median `0.001207`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.275`, primary_mae `0.033894`, avg `-0.003147`, median `0.005613`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.25`, primary_mae `0.06451`, avg `0.007887`, median `0.015571`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.064759`, avg `0.038774`, median `0.044525`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.013823, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.020166, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.033894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.06451, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.064759, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015746, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019113, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.013823, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019067, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024554, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.020166, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027337, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040597, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.033894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.2625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041323, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074116, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.06451, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': -0.65, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051758, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08013, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.175, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.064759, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.010758`, avg `-0.001851`, median `0.000125`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.016374`, avg `-0.000166`, median `0.005565`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.03567`, avg `0.011474`, median `0.013429`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.09987`, avg `0.036437`, median `0.033594`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.076812`, avg `0.04395`, median `0.04613`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.009273`, avg `-0.000165`, median `-0.002438`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.013708`, avg `-0.003477`, median `0.000899`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.029528`, avg `0.002341`, median `0.006069`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.080841`, avg `0.014918`, median `0.020612`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.067559`, avg `0.029504`, median `0.032017`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.025107`, avg `-0.006581`, median `-0.005846`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.033007`, avg `-0.014391`, median `-0.013247`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.042177`, avg `-0.014893`, median `-0.012632`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.088476`, avg `0.005701`, median `0.019252`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.136895`, avg `0.046363`, median `0.065914`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.019113`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.024554`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3125`, primary_mae `0.040597`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.2625`, primary_mae `0.074116`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.08013`, avg `0.052756`, median `0.059117`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.019113`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.024554`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3125`, primary_mae `0.040597`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.2625`, primary_mae `0.074116`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.08013`, avg `0.052756`, median `0.059117`

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
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.019113`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.024554`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3125`, primary_mae `0.040597`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.2625`, primary_mae `0.074116`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.08013`, avg `0.052756`, median `0.059117`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.575`, primary_closer `0.375`, primary_mae `0.019113`, avg `-0.004837`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.024554`, avg `-0.008144`, median `-0.007462`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.3125`, primary_mae `0.040597`, avg `-0.005218`, median `0.001002`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.2625`, primary_mae `0.074116`, avg `0.006019`, median `0.015082`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.275`, primary_mae `0.08013`, avg `0.052756`, median `0.059117`

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
