# Historical Replay Benchmark

Generated at: `2026-11-03T19:31:53.980090+00:00`
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
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.023258`
- secondary_mean_absolute_error: `0.019755`
- primary_error_advantage: `-0.003503`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.022328`
- secondary_mean_absolute_error: `0.02491`
- primary_error_advantage: `0.002582`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.3625`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.041403`
- secondary_mean_absolute_error: `0.036345`
- primary_error_advantage: `-0.005058`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.059343`
- secondary_mean_absolute_error: `0.046006`
- primary_error_advantage: `-0.013337`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.051429`
- secondary_mean_absolute_error: `0.035522`
- primary_error_advantage: `-0.015907`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018637`, as_primary `0`, as_primary_hit `None`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.022837`, as_primary `0`, as_primary_hit `None`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.028556`, as_primary `0`, as_primary_hit `None`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.034792`, as_primary `0`, as_primary_hit `None`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.031557`, as_primary `0`, as_primary_hit `None`, avg `0.049481`, median `0.062627`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.021708`, as_primary `0`, as_primary_hit `None`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.028239`, as_primary `0`, as_primary_hit `None`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.040963`, as_primary `0`, as_primary_hit `None`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.05109`, as_primary `0`, as_primary_hit `None`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.036402`, as_primary `0`, as_primary_hit `None`, avg `0.049481`, median `0.062627`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.023258`, as_primary `80`, as_primary_hit `0.525`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.022328`, as_primary `80`, as_primary_hit `0.55`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, direction_hit `0.3125`, path_mae `0.041403`, as_primary `80`, as_primary_hit `0.675`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.059343`, as_primary `80`, as_primary_hit `0.725`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.051429`, as_primary `80`, as_primary_hit `0.8125`, avg `0.049481`, median `0.062627`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.018164`, as_primary `0`, as_primary_hit `None`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.020542`, as_primary `0`, as_primary_hit `None`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.026803`, as_primary `0`, as_primary_hit `None`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.034091`, as_primary `0`, as_primary_hit `None`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.032508`, as_primary `0`, as_primary_hit `None`, avg `0.049481`, median `0.062627`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023258`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022328`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4625`, primary_mae `0.041403`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.059343`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.051429`, avg `0.049481`, median `0.062627`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.020341`, avg `0.004619`, median `0.005282`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.6`, primary_mae `0.019422`, avg `0.005992`, median `0.001621`
- 10d: sample `40`, primary_hit `0.375`, primary_closer `0.45`, primary_mae `0.039902`, avg `0.013482`, median `0.012086`
- 20d: sample `40`, primary_hit `0.225`, primary_closer `0.425`, primary_mae `0.050619`, avg `0.028677`, median `0.02893`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.3`, primary_mae `0.052363`, avg `0.058036`, median `0.070341`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.026174`, avg `-0.000861`, median `0.001007`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.025234`, avg `0.009433`, median `0.006927`
- 10d: sample `40`, primary_hit `0.25`, primary_closer `0.475`, primary_mae `0.042905`, avg `0.018955`, median `0.021357`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.068068`, avg `0.029365`, median `0.042071`
- 60d: sample `40`, primary_hit `0.25`, primary_closer `0.325`, primary_mae `0.050495`, avg `0.040925`, median `0.055914`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.020341, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019422, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.039902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.050619, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.050495, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018164, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023258, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.020341, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020542, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028239, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.019422, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.3625, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026803, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041403, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.039902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034091, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059343, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.050619, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031557, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051429, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.050495, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.01279`, avg `-0.00054`, median `-0.004204`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.015358`, avg `0.000936`, median `-0.009913`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.037499`, avg `-0.002318`, median `-0.003361`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.044313`, avg `0.018122`, median `0.017025`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.057133`, avg `0.027743`, median `0.040761`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.014451`, avg `-0.00025`, median `-0.004204`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.018393`, avg `0.005943`, median `0.007025`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.042445`, avg `0.007934`, median `0.003439`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.055408`, avg `0.026743`, median `0.029737`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.07293`, avg `0.047041`, median `0.048488`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.035365`, avg `-0.000824`, median `-0.002931`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.030354`, avg `0.014105`, median `0.00445`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.055818`, avg `0.026595`, median `0.029836`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.069076`, avg `0.050242`, median `0.054498`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.0552`, avg `0.052694`, median `0.068874`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023258`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022328`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4625`, primary_mae `0.041403`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.059343`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.051429`, avg `0.049481`, median `0.062627`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023258`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022328`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4625`, primary_mae `0.041403`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.059343`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.051429`, avg `0.049481`, median `0.062627`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.4667`, primary_mae `0.020532`, avg `0.004093`, median `0.006024`
- 5d: sample `60`, primary_hit `0.4333`, primary_closer `0.55`, primary_mae `0.020752`, avg `0.008069`, median `0.010052`
- 10d: sample `60`, primary_hit `0.3167`, primary_closer `0.5167`, primary_mae `0.037677`, avg `0.014629`, median `0.014924`
- 20d: sample `60`, primary_hit `0.3`, primary_closer `0.4333`, primary_mae `0.057276`, avg `0.024344`, median `0.02893`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.3333`, primary_mae `0.051217`, avg `0.047535`, median `0.056753`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.031436`, avg `-0.004762`, median `-0.008464`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.027057`, avg `0.006643`, median `-0.001204`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.052581`, avg `0.020986`, median `0.029242`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.065546`, avg `0.043052`, median `0.053281`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.052065`, avg `0.055319`, median `0.069033`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023258`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022328`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4625`, primary_mae `0.041403`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.059343`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.051429`, avg `0.049481`, median `0.062627`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023258`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022328`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4625`, primary_mae `0.041403`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.059343`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.051429`, avg `0.049481`, median `0.062627`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.023258`, avg `0.001879`, median `0.002857`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022328`, avg `0.007712`, median `0.005661`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.4625`, primary_mae `0.041403`, avg `0.016218`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.375`, primary_mae `0.059343`, avg `0.029021`, median `0.031427`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.051429`, avg `0.049481`, median `0.062627`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
