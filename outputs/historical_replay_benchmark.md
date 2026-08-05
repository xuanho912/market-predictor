# Historical Replay Benchmark

Generated at: `2026-08-05T14:36:10.501624+00:00`
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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.018209`
- secondary_mean_absolute_error: `0.016039`
- primary_error_advantage: `-0.00217`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.019467`
- secondary_mean_absolute_error: `0.017504`
- primary_error_advantage: `-0.001963`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.034487`
- secondary_mean_absolute_error: `0.030587`
- primary_error_advantage: `-0.0039`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.068528`
- secondary_mean_absolute_error: `0.062108`
- primary_error_advantage: `-0.00642`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.5875`
- primary_mean_absolute_error: `0.071118`
- secondary_mean_absolute_error: `0.075679`
- primary_error_advantage: `0.004561`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5875`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013982`, as_primary `0`, as_primary_hit `None`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.017227`, as_primary `0`, as_primary_hit `None`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.026716`, as_primary `0`, as_primary_hit `None`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.039546`, as_primary `0`, as_primary_hit `None`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.060274`, as_primary `0`, as_primary_hit `None`, avg `0.02527`, median `0.031767`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.017718`, as_primary `40`, as_primary_hit `0.65`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.022709`, as_primary `40`, as_primary_hit `0.675`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.036126`, as_primary `40`, as_primary_hit `0.575`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.065379`, as_primary `40`, as_primary_hit `0.725`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.082179`, as_primary `40`, as_primary_hit `0.65`, avg `0.02527`, median `0.031767`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.017813`, as_primary `40`, as_primary_hit `0.575`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, direction_hit `0.325`, path_mae `0.018814`, as_primary `40`, as_primary_hit `0.675`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.036414`, as_primary `40`, as_primary_hit `0.55`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.078515`, as_primary `40`, as_primary_hit `0.625`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.07429`, as_primary `40`, as_primary_hit `0.475`, avg `0.02527`, median `0.031767`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.01418`, as_primary `0`, as_primary_hit `None`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.015751`, as_primary `0`, as_primary_hit `None`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.024943`, as_primary `0`, as_primary_hit `None`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.038395`, as_primary `0`, as_primary_hit `None`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.05625`, as_primary `0`, as_primary_hit `None`, avg `0.02527`, median `0.031767`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4833`, primary_mae `0.017525`, avg `0.001022`, median `0.003213`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.015891`, avg `0.005339`, median `0.005323`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5333`, primary_mae `0.026474`, avg `0.003134`, median `0.005212`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.55`, primary_mae `0.054397`, avg `0.007017`, median `0.0135`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.65`, primary_mae `0.062902`, avg `0.015747`, median `0.024312`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.020261`, avg `0.005393`, median `0.010408`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.030197`, avg `0.002841`, median `0.005967`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.058526`, avg `0.008014`, median `0.011814`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.15`, primary_mae `0.110923`, avg `0.015932`, median `0.013042`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.095767`, avg `0.053839`, median `0.066875`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4833`, primary_mae `0.017525`, avg `0.001022`, median `0.003213`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.015891`, avg `0.005339`, median `0.005323`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5333`, primary_mae `0.026474`, avg `0.003134`, median `0.005212`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.55`, primary_mae `0.054397`, avg `0.007017`, median `0.0135`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.65`, primary_mae `0.062902`, avg `0.015747`, median `0.024312`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.020261`, avg `0.005393`, median `0.010408`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.030197`, avg `0.002841`, median `0.005967`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.058526`, avg `0.008014`, median `0.011814`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.15`, primary_mae `0.110923`, avg `0.015932`, median `0.013042`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.095767`, avg `0.053839`, median `0.066875`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.017525, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015891, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.026474, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.054397, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.062902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013982, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017813, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.017525, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015751, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022709, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.015891, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024943, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036414, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.026474, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038395, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078515, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.054397, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.5875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05625, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.082179, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.062902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.020385`, avg `-0.000325`, median `0.005338`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.01697`, avg `0.005691`, median `0.008933`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.022115`, avg `0.007415`, median `0.018359`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.049642`, avg `0.015667`, median `0.024592`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.096773`, avg `0.000291`, median `-0.02547`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.023628`, avg `-0.003988`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.020972`, avg `0.001356`, median `0.00171`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.027939`, avg `0.001371`, median `0.00381`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.057061`, avg `0.008247`, median `0.014663`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.088921`, avg `0.007334`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019978`, avg `0.00916`, median `0.010545`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.032384`, avg `0.007752`, median `0.010594`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.060672`, avg `0.018574`, median `0.011814`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.0625`, primary_mae `0.121128`, avg `0.02992`, median `0.013042`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.106666`, avg `0.061667`, median `0.075516`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4375`, primary_mae `0.018209`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.019467`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034487`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068528`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5875`, primary_mae `0.071118`, avg `0.02527`, median `0.031767`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4375`, primary_mae `0.018209`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.019467`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034487`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068528`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5875`, primary_mae `0.071118`, avg `0.02527`, median `0.031767`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4833`, primary_mae `0.017525`, avg `0.001022`, median `0.003213`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.5`, primary_mae `0.015891`, avg `0.005339`, median `0.005323`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5333`, primary_mae `0.026474`, avg `0.003134`, median `0.005212`
- 20d: sample `60`, primary_hit `0.6167`, primary_closer `0.55`, primary_mae `0.054397`, avg `0.007017`, median `0.0135`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.65`, primary_mae `0.062902`, avg `0.015747`, median `0.024312`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.020261`, avg `0.005393`, median `0.010408`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.030197`, avg `0.002841`, median `0.005967`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.058526`, avg `0.008014`, median `0.011814`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.15`, primary_mae `0.110923`, avg `0.015932`, median `0.013042`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.095767`, avg `0.053839`, median `0.066875`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4375`, primary_mae `0.018209`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.019467`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034487`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068528`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5875`, primary_mae `0.071118`, avg `0.02527`, median `0.031767`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.4375`, primary_mae `0.018209`, avg `0.002115`, median `0.004555`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.019467`, avg `0.004715`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.4625`, primary_mae `0.034487`, avg `0.004354`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.068528`, avg `0.009246`, median `0.0135`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.5875`, primary_mae `0.071118`, avg `0.02527`, median `0.031767`

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
