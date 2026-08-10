# Historical Replay Benchmark

Generated at: `2026-08-10T23:48:56.662930+00:00`
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
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.016277`
- secondary_mean_absolute_error: `0.018168`
- primary_error_advantage: `0.001891`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.020197`
- secondary_mean_absolute_error: `0.020935`
- primary_error_advantage: `0.000738`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.033241`
- secondary_mean_absolute_error: `0.03545`
- primary_error_advantage: `0.002209`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.062058`
- secondary_mean_absolute_error: `0.062874`
- primary_error_advantage: `0.000816`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.077962`
- secondary_mean_absolute_error: `0.083421`
- primary_error_advantage: `0.005459`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014441`, as_primary `0`, as_primary_hit `None`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.018986`, as_primary `0`, as_primary_hit `None`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.027447`, as_primary `0`, as_primary_hit `None`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.045052`, as_primary `0`, as_primary_hit `None`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.075791`, as_primary `0`, as_primary_hit `None`, avg `0.012992`, median `0.019108`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.015351`, as_primary `60`, as_primary_hit `0.5833`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.023333`, as_primary `60`, as_primary_hit `0.7`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.035389`, as_primary `60`, as_primary_hit `0.5333`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.064109`, as_primary `60`, as_primary_hit `0.6333`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.083941`, as_primary `60`, as_primary_hit `0.4833`, avg `0.012992`, median `0.019108`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.021989`, as_primary `20`, as_primary_hit `0.75`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, direction_hit `0.325`, path_mae `0.022615`, as_primary `20`, as_primary_hit `0.6`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.040345`, as_primary `20`, as_primary_hit `0.6`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.081898`, as_primary `20`, as_primary_hit `0.7`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.089088`, as_primary `20`, as_primary_hit `0.7`, avg `0.012992`, median `0.019108`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014412`, as_primary `0`, as_primary_hit `None`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, direction_hit `0.675`, path_mae `0.017224`, as_primary `0`, as_primary_hit `None`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.026055`, as_primary `0`, as_primary_hit `None`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.041555`, as_primary `0`, as_primary_hit `None`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.067332`, as_primary `0`, as_primary_hit `None`, avg `0.012992`, median `0.019108`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5375`, primary_mae `0.016277`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5375`, primary_mae `0.020197`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.033241`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.062058`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.077962`, avg `0.012992`, median `0.019108`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.5667`, primary_mae `0.015`, avg `0.003183`, median `0.004555`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.6167`, primary_mae `0.018489`, avg `0.004662`, median `0.006047`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.5333`, primary_mae `0.034943`, avg `0.002572`, median `0.003776`
- 20d: sample `60`, primary_hit `0.4833`, primary_closer `0.5167`, primary_mae `0.064405`, avg `0.000736`, median `0.011557`
- 60d: sample `60`, primary_hit `0.4167`, primary_closer `0.5167`, primary_mae `0.07896`, avg `0.012723`, median `0.021115`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.020109`, avg `-0.001874`, median `0.002617`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.025322`, avg `0.002691`, median `0.003509`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.028135`, avg `0.007331`, median `0.011059`
- 20d: sample `20`, primary_hit `0.75`, primary_closer `0.2`, primary_mae `0.055018`, avg `0.016395`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.07497`, avg `0.013799`, median `0.003555`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.015, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.6167, 'primary_mean_absolute_error': 0.018489, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.028135, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.055018, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.07497, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014412, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021989, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.015, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017224, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023333, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.6167, 'primary_mean_absolute_error': 0.018489, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026055, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040345, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.028135, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041555, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.081898, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.055018, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067332, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.089088, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.07497, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.023836`, avg `-0.007498`, median `-0.002198`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.025753`, avg `-0.001465`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.030351`, avg `0.001015`, median `0.002208`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.064627`, avg `0.00323`, median `0.014663`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.074477`, avg `0.003476`, median `-0.009359`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.020577`, avg `-0.003334`, median `0.002617`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.025632`, avg `0.000704`, median `0.003509`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.027857`, avg `0.006211`, median `0.011059`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.1875`, primary_mae `0.059417`, avg `0.010668`, median `0.02136`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.073416`, avg `0.013362`, median `-0.004019`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.020577`, avg `-0.003334`, median `0.002617`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.025632`, avg `0.000704`, median `0.003509`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.027857`, avg `0.006211`, median `0.011059`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.1875`, primary_mae `0.059417`, avg `0.010668`, median `0.02136`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.073416`, avg `0.013362`, median `-0.004019`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5375`, primary_mae `0.016277`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5375`, primary_mae `0.020197`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.033241`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.062058`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.077962`, avg `0.012992`, median `0.019108`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5375`, primary_mae `0.016277`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5375`, primary_mae `0.020197`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.033241`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.062058`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.077962`, avg `0.012992`, median `0.019108`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.015179`, avg `-0.003516`, median `-0.00051`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.525`, primary_mae `0.018098`, avg `0.001585`, median `0.003509`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.475`, primary_mae `0.022978`, avg `0.002816`, median `0.004492`
- 20d: sample `40`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.046647`, avg `0.003674`, median `0.012734`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.070994`, avg `0.001165`, median `-0.017782`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.023379`, avg `0.007129`, median `0.010987`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.028881`, avg `0.003877`, median `0.005967`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.052707`, avg `0.01225`, median `0.013627`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.091862`, avg `0.025182`, median `0.020351`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.088113`, avg `0.056405`, median `0.052729`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5375`, primary_mae `0.016277`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5375`, primary_mae `0.020197`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.033241`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.062058`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.077962`, avg `0.012992`, median `0.019108`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5375`, primary_mae `0.016277`, avg `0.001919`, median `0.004273`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.5375`, primary_mae `0.020197`, avg `0.004169`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.033241`, avg `0.003762`, median `0.006542`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.062058`, avg `0.004651`, median `0.013528`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.4875`, primary_mae `0.077962`, avg `0.012992`, median `0.019108`

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
