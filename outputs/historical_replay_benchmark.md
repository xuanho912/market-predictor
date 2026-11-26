# Historical Replay Benchmark

Generated at: `2026-11-26T03:46:38.539962+00:00`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.028667`
- secondary_mean_absolute_error: `0.022043`
- primary_error_advantage: `-0.006624`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.033722`
- secondary_mean_absolute_error: `0.027228`
- primary_error_advantage: `-0.006494`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.2625`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.056367`
- secondary_mean_absolute_error: `0.037219`
- primary_error_advantage: `-0.019148`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.2125`
- primary_mean_absolute_error: `0.110959`
- secondary_mean_absolute_error: `0.058115`
- primary_error_advantage: `-0.052844`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.093325`
- secondary_mean_absolute_error: `0.068662`
- primary_error_advantage: `-0.024663`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.020962`, as_primary `0`, as_primary_hit `None`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.027788`, as_primary `0`, as_primary_hit `None`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.03463`, as_primary `0`, as_primary_hit `None`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.053424`, as_primary `0`, as_primary_hit `None`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.067014`, as_primary `0`, as_primary_hit `None`, avg `0.04771`, median `0.066728`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.022058`, as_primary `0`, as_primary_hit `None`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.030379`, as_primary `0`, as_primary_hit `None`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.043922`, as_primary `0`, as_primary_hit `None`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.076968`, as_primary `0`, as_primary_hit `None`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.078019`, as_primary `0`, as_primary_hit `None`, avg `0.04771`, median `0.066728`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.028667`, as_primary `80`, as_primary_hit `0.575`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.033722`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.056367`, as_primary `80`, as_primary_hit `0.625`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.110959`, as_primary `80`, as_primary_hit `0.575`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.093325`, as_primary `80`, as_primary_hit `0.7625`, avg `0.04771`, median `0.066728`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.020405`, as_primary `0`, as_primary_hit `None`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.025412`, as_primary `0`, as_primary_hit `None`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.034549`, as_primary `0`, as_primary_hit `None`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.051917`, as_primary `0`, as_primary_hit `None`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.066651`, as_primary `0`, as_primary_hit `None`, avg `0.04771`, median `0.066728`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.4125`, primary_mae `0.028667`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.033722`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3125`, primary_mae `0.056367`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2125`, primary_mae `0.110959`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.3125`, primary_mae `0.093325`, avg `0.04771`, median `0.066728`

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
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.033708`, avg `0.009532`, median `0.017715`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.057076`, avg `0.014889`, median `0.026809`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.054515`, avg `0.028566`, median `0.048031`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.09021`, avg `0.00401`, median `-0.013772`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.092557`, avg `0.043661`, median `0.091177`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.026987`, avg `0.001175`, median `0.004064`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.025937`, avg `0.003097`, median `0.004301`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.3333`, primary_mae `0.056984`, avg `0.000218`, median `0.003723`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.1833`, primary_mae `0.117876`, avg `-0.002794`, median `0.010633`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.2833`, primary_mae `0.093581`, avg `0.049059`, median `0.063438`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026987, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.025937, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.054515, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.09021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.092557, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020405, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028667, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026987, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025412, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033722, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.025937, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.2625, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034549, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056367, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.054515, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.2125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051917, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.110959, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.09021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.066651, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.093325, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.092557, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.01774`, avg `-0.003275`, median `-0.003756`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.011576`, avg `-0.000897`, median `-0.002788`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.048735`, avg `-0.005409`, median `0.003793`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.071384`, avg `-0.027077`, median `-0.014372`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.03704`, avg `0.042088`, median `0.061251`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022125`, avg `0.001825`, median `0.001744`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.014523`, avg `0.001211`, median `-0.002788`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.041543`, avg `-0.001753`, median `-0.001702`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.081353`, avg `0.001105`, median `0.013048`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.040297`, avg `0.063008`, median `0.073009`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.033624`, avg `0.016219`, median `0.019346`
- 5d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.052943`, avg `0.025916`, median `0.026809`
- 10d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.051565`, avg `0.039368`, median `0.049419`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.093263`, avg `0.017617`, median `-0.005654`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.086203`, avg `0.051785`, median `0.091177`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.4125`, primary_mae `0.028667`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.033722`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3125`, primary_mae `0.056367`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2125`, primary_mae `0.110959`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.3125`, primary_mae `0.093325`, avg `0.04771`, median `0.066728`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.4125`, primary_mae `0.028667`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.033722`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3125`, primary_mae `0.056367`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2125`, primary_mae `0.110959`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.3125`, primary_mae `0.093325`, avg `0.04771`, median `0.066728`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.026987`, avg `0.001175`, median `0.004064`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.025937`, avg `0.003097`, median `0.004301`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.3333`, primary_mae `0.056984`, avg `0.000218`, median `0.003723`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.1833`, primary_mae `0.117876`, avg `-0.002794`, median `0.010633`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.2833`, primary_mae `0.093581`, avg `0.049059`, median `0.063438`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.033708`, avg `0.009532`, median `0.017715`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.057076`, avg `0.014889`, median `0.026809`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.054515`, avg `0.028566`, median `0.048031`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.09021`, avg `0.00401`, median `-0.013772`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.092557`, avg `0.043661`, median `0.091177`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.4125`, primary_mae `0.028667`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.033722`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3125`, primary_mae `0.056367`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2125`, primary_mae `0.110959`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.3125`, primary_mae `0.093325`, avg `0.04771`, median `0.066728`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.4125`, primary_mae `0.028667`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.033722`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3125`, primary_mae `0.056367`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2125`, primary_mae `0.110959`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.3125`, primary_mae `0.093325`, avg `0.04771`, median `0.066728`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.4125`, primary_mae `0.028667`, avg `0.003264`, median `0.007107`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.033722`, avg `0.006045`, median `0.004584`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.3125`, primary_mae `0.056367`, avg `0.007305`, median `0.008243`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.2125`, primary_mae `0.110959`, avg `-0.001093`, median `0.006438`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.3125`, primary_mae `0.093325`, avg `0.04771`, median `0.066728`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
