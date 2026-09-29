# Historical Replay Benchmark

Generated at: `2026-09-29T18:07:54.871280+00:00`
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
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.01838`
- secondary_mean_absolute_error: `0.015125`
- primary_error_advantage: `-0.003255`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.023925`
- secondary_mean_absolute_error: `0.017409`
- primary_error_advantage: `-0.006516`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.036049`
- secondary_mean_absolute_error: `0.025618`
- primary_error_advantage: `-0.010431`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.069565`
- secondary_mean_absolute_error: `0.039172`
- primary_error_advantage: `-0.030393`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1375`
- secondary_hit_rate: `0.8625`
- primary_vs_secondary_accuracy_spread: `-0.725`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.08774`
- secondary_mean_absolute_error: `0.056188`
- primary_error_advantage: `-0.031552`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015693`, as_primary `0`, as_primary_hit `None`, avg `-0.004028`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017754`, as_primary `0`, as_primary_hit `None`, avg `-0.007749`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.026134`, as_primary `0`, as_primary_hit `None`, avg `-0.00444`, median `8.3e-05`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.039651`, as_primary `0`, as_primary_hit `None`, avg `0.011093`, median `0.016235`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.054603`, as_primary `0`, as_primary_hit `None`, avg `0.060592`, median `0.075566`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015113`, as_primary `0`, as_primary_hit `None`, avg `-0.004028`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019562`, as_primary `0`, as_primary_hit `None`, avg `-0.007749`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.031113`, as_primary `0`, as_primary_hit `None`, avg `-0.00444`, median `8.3e-05`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.060137`, as_primary `0`, as_primary_hit `None`, avg `0.011093`, median `0.016235`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.060685`, as_primary `0`, as_primary_hit `None`, avg `0.060592`, median `0.075566`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.01838`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.004028`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.023925`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.007749`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.036049`, as_primary `80`, as_primary_hit `0.5`, avg `-0.00444`, median `8.3e-05`
- 20d: sample `80`, direction_hit `0.3875`, path_mae `0.069565`, as_primary `80`, as_primary_hit `0.6125`, avg `0.011093`, median `0.016235`
- 60d: sample `80`, direction_hit `0.1375`, path_mae `0.08774`, as_primary `80`, as_primary_hit `0.8625`, avg `0.060592`, median `0.075566`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.015125`, as_primary `0`, as_primary_hit `None`, avg `-0.004028`, median `-0.003098`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.017409`, as_primary `0`, as_primary_hit `None`, avg `-0.007749`, median `-0.004447`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.025618`, as_primary `0`, as_primary_hit `None`, avg `-0.00444`, median `8.3e-05`
- 20d: sample `80`, direction_hit `0.6125`, path_mae `0.039172`, as_primary `0`, as_primary_hit `None`, avg `0.011093`, median `0.016235`
- 60d: sample `80`, direction_hit `0.8625`, path_mae `0.056188`, as_primary `0`, as_primary_hit `None`, avg `0.060592`, median `0.075566`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.35`, primary_mae `0.01838`, avg `-0.004028`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.023925`, avg `-0.007749`, median `-0.004447`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.3375`, primary_mae `0.036049`, avg `-0.00444`, median `8.3e-05`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.069565`, avg `0.011093`, median `0.016235`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.25`, primary_mae `0.08774`, avg `0.060592`, median `0.075566`

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
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.021301`, avg `-0.007746`, median `-0.010153`
- 5d: sample `40`, primary_hit `0.725`, primary_closer `0.275`, primary_mae `0.027937`, avg `-0.012558`, median `-0.011651`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.35`, primary_mae `0.041907`, avg `-0.008462`, median `-0.006025`
- 20d: sample `40`, primary_hit `0.525`, primary_closer `0.275`, primary_mae `0.081867`, avg `0.005011`, median `-0.001058`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.225`, primary_mae `0.105346`, avg `0.070154`, median `0.104666`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.015458`, avg `-0.000309`, median `0.001753`
- 5d: sample `40`, primary_hit `0.4`, primary_closer `0.525`, primary_mae `0.019914`, avg `-0.00294`, median `0.001566`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.325`, primary_mae `0.030192`, avg `-0.000419`, median `0.005613`
- 20d: sample `40`, primary_hit `0.25`, primary_closer `0.225`, primary_mae `0.057263`, avg `0.017174`, median `0.024266`
- 60d: sample `40`, primary_hit `0.125`, primary_closer `0.275`, primary_mae `0.070135`, avg `0.05103`, median `0.055681`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015458, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.019914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.030192, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.057263, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.070135, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015113, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01838, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015458, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017409, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023925, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.019914, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025618, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036049, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.325, 'primary_mean_absolute_error': 0.030192, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039172, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069565, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.057263, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1375, 'secondary_hit_rate': 0.8625, 'primary_vs_secondary_accuracy_spread': -0.725, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054603, 'direction_hit_rate': 0.8625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08774, 'direction_hit_rate': 0.1375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.125, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.070135, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.017781`, avg `0.009635`, median `0.008516`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.026248`, avg `0.003391`, median `0.006826`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.035865`, avg `0.002911`, median `0.005974`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.054607`, avg `0.020574`, median `0.022849`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.04454`, avg `0.063318`, median `0.07166`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.018017`, avg `0.001926`, median `0.005108`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.026606`, avg `-0.000119`, median `0.006826`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.037036`, avg `-0.004031`, median `0.004006`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.051`, avg `0.013159`, median `0.017343`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.053146`, avg `0.049989`, median `0.056479`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.015723`, avg `-0.014152`, median `-0.012143`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.02159`, avg `-0.011909`, median `-0.01008`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.043546`, avg `0.001992`, median `0.001244`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.087864`, avg `0.015237`, median `0.016851`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.058408`, avg `0.10743`, median `0.133171`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.35`, primary_mae `0.01838`, avg `-0.004028`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.023925`, avg `-0.007749`, median `-0.004447`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.3375`, primary_mae `0.036049`, avg `-0.00444`, median `8.3e-05`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.069565`, avg `0.011093`, median `0.016235`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.25`, primary_mae `0.08774`, avg `0.060592`, median `0.075566`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.35`, primary_mae `0.01838`, avg `-0.004028`, median `-0.003098`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.4`, primary_mae `0.023925`, avg `-0.007749`, median `-0.004447`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.3375`, primary_mae `0.036049`, avg `-0.00444`, median `8.3e-05`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.25`, primary_mae `0.069565`, avg `0.011093`, median `0.016235`
- 60d: sample `80`, primary_hit `0.1375`, primary_closer `0.25`, primary_mae `0.08774`, avg `0.060592`, median `0.075566`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.325`, primary_mae `0.021304`, avg `-0.000698`, median `0.002181`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.3`, primary_mae `0.030376`, avg `-0.005716`, median `-0.002346`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.25`, primary_mae `0.039582`, avg `-0.00902`, median `-0.000315`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.275`, primary_mae `0.064717`, avg `0.004986`, median `0.009926`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.3`, primary_mae `0.099952`, avg `0.050769`, median `0.062563`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.015455`, avg `-0.007357`, median `-0.008025`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.017474`, avg `-0.009782`, median `-0.006281`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.032517`, avg `0.00014`, median `0.004921`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.225`, primary_mae `0.074414`, avg `0.017199`, median `0.030977`
- 60d: sample `40`, primary_hit `0.1`, primary_closer `0.2`, primary_mae `0.075529`, avg `0.070415`, median `0.076705`

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
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

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
