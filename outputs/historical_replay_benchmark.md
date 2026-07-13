# Historical Replay Benchmark

Generated at: `2026-07-13T15:14:56.697009+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.016057`
- secondary_mean_absolute_error: `0.01418`
- primary_error_advantage: `-0.001877`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.020541`
- secondary_mean_absolute_error: `0.01713`
- primary_error_advantage: `-0.003411`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.027726`
- secondary_mean_absolute_error: `0.025184`
- primary_error_advantage: `-0.002542`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2625`
- secondary_hit_rate: `0.7375`
- primary_vs_secondary_accuracy_spread: `-0.475`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.063183`
- secondary_mean_absolute_error: `0.044924`
- primary_error_advantage: `-0.018259`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.091875`
- secondary_mean_absolute_error: `0.084438`
- primary_error_advantage: `-0.007437`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.01473`, as_primary `0`, as_primary_hit `None`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.016725`, as_primary `0`, as_primary_hit `None`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.022121`, as_primary `0`, as_primary_hit `None`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.031057`, as_primary `0`, as_primary_hit `None`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.068537`, as_primary `0`, as_primary_hit `None`, avg `0.019293`, median `0.035204`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.01418`, as_primary `0`, as_primary_hit `None`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.01713`, as_primary `0`, as_primary_hit `None`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.025184`, as_primary `0`, as_primary_hit `None`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.044924`, as_primary `0`, as_primary_hit `None`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.084438`, as_primary `0`, as_primary_hit `None`, avg `0.019293`, median `0.035204`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.016057`, as_primary `80`, as_primary_hit `0.5`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.020541`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.027726`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, direction_hit `0.2625`, path_mae `0.063183`, as_primary `80`, as_primary_hit `0.7375`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.091875`, as_primary `80`, as_primary_hit `0.6125`, avg `0.019293`, median `0.035204`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.01405`, as_primary `0`, as_primary_hit `None`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.016366`, as_primary `0`, as_primary_hit `None`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.021855`, as_primary `0`, as_primary_hit `None`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, direction_hit `0.7375`, path_mae `0.031224`, as_primary `0`, as_primary_hit `None`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.067664`, as_primary `0`, as_primary_hit `None`, avg `0.019293`, median `0.035204`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.016057`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.020541`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.027726`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.4125`, primary_mae `0.063183`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.091875`, avg `0.019293`, median `0.035204`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.011222`, avg `-0.002049`, median `-0.000282`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.014406`, avg `-0.002572`, median `0.002596`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.023641`, avg `-0.004448`, median `0.001074`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.054689`, avg `0.002021`, median `0.011472`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.071303`, avg `-0.019017`, median `-0.022824`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.017669`, avg `-0.004502`, median `6.2e-05`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.3667`, primary_mae `0.022586`, avg `-0.005575`, median `-0.001999`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.4833`, primary_mae `0.029088`, avg `-0.001395`, median `-0.006514`
- 20d: sample `60`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.066014`, avg `0.015065`, median `0.019949`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.45`, primary_mae `0.098732`, avg `0.032063`, median `0.047308`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.011222, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014406, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023641, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.054689, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.071303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01405, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016057, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.011222, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016366, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020541, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014406, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021855, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027726, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.023641, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_vs_secondary_accuracy_spread': -0.475, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031057, 'direction_hit_rate': 0.7375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.063183, 'direction_hit_rate': 0.2625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.054689, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067664, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.091875, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.071303, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.013309`, avg `-0.001674`, median `-0.006771`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.015835`, avg `-0.004666`, median `-0.013748`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.030516`, avg `0.004835`, median `0.008455`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.063621`, avg `0.025259`, median `0.013099`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.042252`, avg `-0.006529`, median `-0.012825`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.016055`, avg `-0.005566`, median `-0.006771`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017215`, avg `-0.002364`, median `-0.003138`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.031191`, avg `0.007372`, median `0.008455`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.060813`, avg `0.02245`, median `0.009478`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.6875`, primary_mae `0.070303`, avg `0.029785`, median `0.031665`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.021006`, avg `-0.009939`, median `-0.005846`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.028792`, avg `-0.012476`, median `-0.012112`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.023868`, avg `-0.006986`, median `-0.009221`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.077228`, avg `0.017836`, median `0.023936`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.132416`, avg `0.058256`, median `0.066096`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.016057`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.020541`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.027726`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.4125`, primary_mae `0.063183`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.091875`, avg `0.019293`, median `0.035204`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.016057`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.020541`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.027726`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.4125`, primary_mae `0.063183`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.091875`, avg `0.019293`, median `0.035204`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.013207`, avg `-0.002826`, median `-0.000421`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.016766`, avg `-0.003007`, median `0.001204`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.028219`, avg `0.002221`, median `0.002812`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.425`, primary_mae `0.060158`, avg `0.009034`, median `0.010966`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.55`, primary_mae `0.07369`, avg `0.006889`, median `0.018893`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4167`, primary_mae `0.015578`, avg `-0.004893`, median `-0.00205`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.4333`, primary_mae `0.020529`, avg `-0.006387`, median `-0.003038`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.026488`, avg `-0.002078`, median `-0.003423`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.4`, primary_mae `0.063871`, avg `0.010185`, median `0.015831`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.4833`, primary_mae `0.087765`, avg `0.017749`, median `0.035204`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.016057`, avg `-0.003889`, median `6.2e-05`
- 5d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.020541`, avg `-0.004824`, median `-0.000392`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.45`, primary_mae `0.027726`, avg `-0.002159`, median `-0.002469`
- 20d: sample `80`, primary_hit `0.2625`, primary_closer `0.4125`, primary_mae `0.063183`, avg `0.011804`, median `0.017969`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.091875`, avg `0.019293`, median `0.035204`

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
