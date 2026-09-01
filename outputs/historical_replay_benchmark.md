# Historical Replay Benchmark

Generated at: `2026-09-01T01:30:34.753447+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.019403`
- secondary_mean_absolute_error: `0.016748`
- primary_error_advantage: `-0.002655`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.023098`
- secondary_mean_absolute_error: `0.01976`
- primary_error_advantage: `-0.003338`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.030432`
- secondary_mean_absolute_error: `0.035399`
- primary_error_advantage: `0.004967`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.05833`
- secondary_mean_absolute_error: `0.049705`
- primary_error_advantage: `-0.008625`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.08544`
- secondary_mean_absolute_error: `0.072551`
- primary_error_advantage: `-0.012889`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015938`, as_primary `0`, as_primary_hit `None`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.018236`, as_primary `0`, as_primary_hit `None`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.025566`, as_primary `0`, as_primary_hit `None`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.033272`, as_primary `0`, as_primary_hit `None`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.060582`, as_primary `0`, as_primary_hit `None`, avg `0.028642`, median `0.031342`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.016748`, as_primary `0`, as_primary_hit `None`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.01976`, as_primary `0`, as_primary_hit `None`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.035399`, as_primary `0`, as_primary_hit `None`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.049705`, as_primary `0`, as_primary_hit `None`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.072551`, as_primary `0`, as_primary_hit `None`, avg `0.028642`, median `0.031342`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.019403`, as_primary `80`, as_primary_hit `0.5`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.023098`, as_primary `80`, as_primary_hit `0.525`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.030432`, as_primary `80`, as_primary_hit `0.4`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.05833`, as_primary `80`, as_primary_hit `0.6375`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.08544`, as_primary `80`, as_primary_hit `0.675`, avg `0.028642`, median `0.031342`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015992`, as_primary `0`, as_primary_hit `None`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.018028`, as_primary `0`, as_primary_hit `None`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023165`, as_primary `0`, as_primary_hit `None`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.032386`, as_primary `0`, as_primary_hit `None`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.057387`, as_primary `0`, as_primary_hit `None`, avg `0.028642`, median `0.031342`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.017141`, avg `-0.001585`, median `-0.001535`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.020272`, avg `-0.003092`, median `-0.001116`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.5667`, primary_mae `0.029656`, avg `-0.000231`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.4167`, primary_mae `0.056652`, avg `0.01101`, median `0.018121`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.08455`, avg `0.041623`, median `0.05856`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.026188`, avg `-0.000438`, median `0.006871`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.031578`, avg `0.002755`, median `0.001494`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.03276`, avg `-0.00661`, median `-0.008899`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.063366`, avg `0.000474`, median `0.004283`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.088111`, avg `-0.010302`, median `0.007994`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.017721`, avg `0.000182`, median `-0.000413`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022998`, avg `0.000275`, median `0.001088`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.65`, primary_mae `0.033609`, avg `0.000279`, median `-0.00936`
- 20d: sample `40`, primary_hit `0.375`, primary_closer `0.475`, primary_mae `0.057563`, avg `0.008664`, median `0.013025`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.575`, primary_mae `0.071656`, avg `0.042959`, median `0.055734`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.026188`, avg `-0.000438`, median `0.006871`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.031578`, avg `0.002755`, median `0.001494`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.03276`, avg `-0.00661`, median `-0.008899`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.063366`, avg `0.000474`, median `0.004283`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.088111`, avg `-0.010302`, median `0.007994`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.015981`, avg `-0.005118`, median `-0.004159`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.014818`, avg `-0.009827`, median `-0.010372`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.02175`, avg `-0.00125`, median `-0.006389`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.3`, primary_mae `0.054829`, avg `0.015702`, median `0.027848`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.110339`, avg `0.038952`, median `0.062395`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015981, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.02175, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.054829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.071656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015938, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019403, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.015981, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018028, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023098, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023165, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035399, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.02175, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032386, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05833, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.054829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057387, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08544, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.071656, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.012653`, avg `-0.008046`, median `-0.005597`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.011044`, avg `-0.008834`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.026972`, avg `0.005749`, median `0.013417`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.049508`, avg `0.010618`, median `0.027848`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.099444`, avg `0.023768`, median `0.037982`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.015941`, avg `-0.004529`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.015602`, avg `-0.007532`, median `-0.006113`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.023575`, avg `0.001193`, median `-0.006389`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.054101`, avg `0.014213`, median `0.027848`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.107812`, avg `0.03554`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.027068`, avg `0.002577`, median `0.011157`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.033223`, avg `0.006062`, median `0.003855`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.035711`, avg `-0.002478`, median `-0.00147`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.069621`, avg `0.008519`, median `0.010724`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.095212`, avg `-0.00117`, median `0.010152`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.019403`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023098`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5625`, primary_mae `0.030432`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.05833`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.45`, primary_mae `0.08544`, avg `0.028642`, median `0.031342`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.019403`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023098`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5625`, primary_mae `0.030432`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.05833`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.45`, primary_mae `0.08544`, avg `0.028642`, median `0.031342`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.008136`, avg `-0.002536`, median `-0.002618`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.010317`, avg `-0.003361`, median `0.000781`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.021057`, avg `-0.00764`, median `-0.011447`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.060026`, avg `-0.008973`, median `0.001449`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.083327`, avg `0.015897`, median `0.018376`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.021643`, avg `-0.001109`, median `0.001944`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.025249`, avg `-0.002958`, median `-0.004402`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.033956`, avg `0.003474`, median `-0.003975`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.425`, primary_mae `0.054965`, avg `0.021001`, median `0.025986`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.525`, primary_mae `0.085162`, avg `0.054487`, median `0.064699`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.019403`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023098`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.5625`, primary_mae `0.030432`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.05833`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.45`, primary_mae `0.08544`, avg `0.028642`, median `0.031342`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.023158`, avg `-0.000885`, median `0.002335`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4`, primary_mae `0.027358`, avg `-0.001053`, median `0.000311`
- 10d: sample `60`, primary_hit `0.5667`, primary_closer `0.5167`, primary_mae `0.033557`, avg `0.000113`, median `-0.006304`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.4333`, primary_mae `0.057765`, avg `0.014159`, median `0.018714`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.45`, primary_mae `0.086145`, avg `0.03289`, median `0.031342`

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
