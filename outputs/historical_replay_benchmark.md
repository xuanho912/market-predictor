# Historical Replay Benchmark

Generated at: `2026-08-31T23:59:45.625386+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.018164`
- secondary_mean_absolute_error: `0.016646`
- primary_error_advantage: `-0.001518`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.022918`
- secondary_mean_absolute_error: `0.018235`
- primary_error_advantage: `-0.004683`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.034643`
- secondary_mean_absolute_error: `0.028672`
- primary_error_advantage: `-0.005971`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.051893`
- secondary_mean_absolute_error: `0.050196`
- primary_error_advantage: `-0.001697`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.080773`
- secondary_mean_absolute_error: `0.0763`
- primary_error_advantage: `-0.004473`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

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
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.016748`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.01976`, as_primary `60`, as_primary_hit `0.5`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.035399`, as_primary `60`, as_primary_hit `0.4`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.049705`, as_primary `60`, as_primary_hit `0.6667`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.072551`, as_primary `60`, as_primary_hit `0.7`, avg `0.028642`, median `0.031342`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.019403`, as_primary `20`, as_primary_hit `0.55`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.023098`, as_primary `20`, as_primary_hit `0.6`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.030432`, as_primary `20`, as_primary_hit `0.4`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.05833`, as_primary `20`, as_primary_hit `0.55`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.08544`, as_primary `20`, as_primary_hit `0.6`, avg `0.028642`, median `0.031342`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015992`, as_primary `0`, as_primary_hit `None`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.018028`, as_primary `0`, as_primary_hit `None`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023165`, as_primary `0`, as_primary_hit `None`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.032386`, as_primary `0`, as_primary_hit `None`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.057387`, as_primary `0`, as_primary_hit `None`, avg `0.028642`, median `0.031342`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.018164`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.022918`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.034643`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.051893`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.080773`, avg `0.028642`, median `0.031342`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.45`, primary_mae `0.019691`, avg `-2.5e-05`, median `0.000684`
- 5d: sample `60`, primary_hit `0.5`, primary_closer `0.3333`, primary_mae `0.025666`, avg `0.001102`, median `0.001271`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.3833`, primary_mae `0.039568`, avg `-0.002017`, median `-0.00936`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.4`, primary_mae `0.056194`, avg `0.005934`, median `0.011092`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.3833`, primary_mae `0.082227`, avg `0.025205`, median `0.021848`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.013582`, avg `-0.005118`, median `-0.004159`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.014673`, avg `-0.009827`, median `-0.010372`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.019869`, avg `-0.00125`, median `-0.006389`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.7`, primary_mae `0.03899`, avg `0.015702`, median `0.027848`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.076412`, avg `0.038952`, median `0.062395`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013582, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014673, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019869, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.03899, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.076412, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015938, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019403, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.013582, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018028, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023098, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.014673, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023165, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035399, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019869, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032386, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05833, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.03899, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057387, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08544, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.076412, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.011501`, avg `-0.008046`, median `-0.005597`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.01245`, avg `-0.008834`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.018462`, avg `0.005749`, median `0.013417`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.041233`, avg `0.010618`, median `0.027848`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.087332`, avg `0.023768`, median `0.037982`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.012359`, avg `-0.004529`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.01425`, avg `-0.007532`, median `-0.006113`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.625`, primary_mae `0.020646`, avg `0.001193`, median `-0.006389`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.04119`, avg `0.014213`, median `0.027848`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.08089`, avg `0.03554`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.027068`, avg `0.002577`, median `0.011157`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.033223`, avg `0.006062`, median `0.003855`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.035711`, avg `-0.002478`, median `-0.00147`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.069621`, avg `0.008519`, median `0.010724`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.095212`, avg `-0.00117`, median `0.010152`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.018164`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.022918`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.034643`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.051893`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.080773`, avg `0.028642`, median `0.031342`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.018164`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.022918`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.034643`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.051893`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.080773`, avg `0.028642`, median `0.031342`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.008081`, avg `-0.002536`, median `-0.002618`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.010443`, avg `-0.003361`, median `0.000781`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.028482`, avg `-0.00764`, median `-0.011447`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.044593`, avg `-0.008973`, median `0.001449`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.063478`, avg `0.015897`, median `0.018376`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.019193`, avg `-0.001109`, median `0.001944`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.024825`, avg `-0.002958`, median `-0.004402`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.038665`, avg `0.003474`, median `-0.003975`
- 20d: sample `40`, primary_hit `0.75`, primary_closer `0.425`, primary_mae `0.049807`, avg `0.021001`, median `0.025986`
- 60d: sample `40`, primary_hit `0.775`, primary_closer `0.475`, primary_mae `0.085753`, avg `0.054487`, median `0.064699`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.475`, primary_mae `0.018164`, avg `-0.001298`, median `-0.000413`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.375`, primary_mae `0.022918`, avg `-0.00163`, median `0.000482`
- 10d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.034643`, avg `-0.001826`, median `-0.007304`
- 20d: sample `80`, primary_hit `0.6125`, primary_closer `0.475`, primary_mae `0.051893`, avg `0.008376`, median `0.014891`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.45`, primary_mae `0.080773`, avg `0.028642`, median `0.031342`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.021525`, avg `-0.000885`, median `0.002335`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.3667`, primary_mae `0.027076`, avg `-0.001053`, median `0.000311`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.4833`, primary_mae `0.036697`, avg `0.000113`, median `-0.006304`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.054327`, avg `0.014159`, median `0.018714`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.4167`, primary_mae `0.086539`, avg `0.03289`, median `0.031342`

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
