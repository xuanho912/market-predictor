# Historical Replay Benchmark

Generated at: `2026-09-21T18:16:05.870306+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'medium', 'reasons': ['high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.014938`
- secondary_mean_absolute_error: `0.015315`
- primary_error_advantage: `0.000377`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.6`
- primary_mean_absolute_error: `0.018219`
- secondary_mean_absolute_error: `0.020969`
- primary_error_advantage: `0.00275`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6667`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.325`
- primary_vs_secondary_accuracy_spread: `0.35`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.020931`
- secondary_mean_absolute_error: `0.027375`
- primary_error_advantage: `0.006444`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.060508`
- secondary_mean_absolute_error: `0.064321`
- primary_error_advantage: `0.003813`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.085629`
- secondary_mean_absolute_error: `0.082537`
- primary_error_advantage: `-0.003092`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.014559`, as_primary `0`, as_primary_hit `None`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.018354`, as_primary `0`, as_primary_hit `None`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.020513`, as_primary `0`, as_primary_hit `None`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.039705`, as_primary `0`, as_primary_hit `None`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.063284`, as_primary `0`, as_primary_hit `None`, avg `0.026113`, median `0.035204`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015315`, as_primary `0`, as_primary_hit `None`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.020969`, as_primary `0`, as_primary_hit `None`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.027375`, as_primary `0`, as_primary_hit `None`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.064321`, as_primary `0`, as_primary_hit `None`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.082537`, as_primary `0`, as_primary_hit `None`, avg `0.026113`, median `0.035204`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014938`, as_primary `80`, as_primary_hit `0.4`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.018219`, as_primary `80`, as_primary_hit `0.4`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.020931`, as_primary `80`, as_primary_hit `0.325`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.4625`, path_mae `0.060508`, as_primary `80`, as_primary_hit `0.5375`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.085629`, as_primary `80`, as_primary_hit `0.7`, avg `0.026113`, median `0.035204`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.013845`, as_primary `0`, as_primary_hit `None`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.01643`, as_primary `0`, as_primary_hit `None`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.017112`, as_primary `0`, as_primary_hit `None`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, direction_hit `0.5375`, path_mae `0.036924`, as_primary `0`, as_primary_hit `None`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.061554`, as_primary `0`, as_primary_hit `None`, avg `0.026113`, median `0.035204`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.014938`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018219`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.020931`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.5375`, primary_mae `0.060508`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.525`, primary_mae `0.085629`, avg `0.026113`, median `0.035204`

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
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.3`, primary_mae `0.013183`, avg `-0.005826`, median `-0.003921`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.4`, primary_mae `0.019621`, avg `-0.015981`, median `-0.014968`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.45`, primary_mae `0.021046`, avg `-0.029747`, median `-0.032528`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.075119`, avg `-0.012529`, median `-0.029855`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.122561`, avg `0.010433`, median `0.033887`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.015523`, avg `-0.004237`, median `-0.003662`
- 5d: sample `60`, primary_hit `0.5167`, primary_closer `0.6667`, primary_mae `0.017751`, avg `-0.006795`, median `-0.003`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.6167`, primary_mae `0.020893`, avg `-0.002526`, median `-0.007068`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.055638`, avg `0.013906`, median `0.015722`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.55`, primary_mae `0.073318`, avg `0.03134`, median `0.035204`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.013183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.6667, 'primary_mean_absolute_error': 0.017751, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.6167, 'primary_mean_absolute_error': 0.020893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2833, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.073318, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013845, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015315, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.013183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.6, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01643, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020969, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.6667, 'primary_mean_absolute_error': 0.017751, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.325, 'primary_vs_secondary_accuracy_spread': 0.35, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017112, 'direction_hit_rate': 0.325}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027375, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.6167, 'primary_mean_absolute_error': 0.020893, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036924, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064321, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061554, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.085629, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2833, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.073318, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.013085`, avg `-0.018856`, median `-0.016078`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.017873`, avg `-0.01519`, median `-0.02258`
- 10d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.018077`, avg `-0.015127`, median `-0.016097`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.080534`, avg `0.017035`, median `0.025462`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.127938`, avg `0.034259`, median `0.059414`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.023117`, avg `-0.008711`, median `-0.009708`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.025483`, avg `-0.012095`, median `-0.01025`
- 10d: sample `16`, primary_hit `0.8125`, primary_closer `0.375`, primary_mae `0.024829`, avg `-0.008624`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.08143`, avg `0.011013`, median `0.020913`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.134408`, avg `0.035483`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.010998`, avg `-0.007394`, median `-0.005111`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.018959`, avg `-0.018186`, median `-0.023937`
- 10d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.017032`, avg `-0.034878`, median `-0.038709`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.076092`, avg `-0.012774`, median `-0.029855`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.127772`, avg `0.009779`, median `0.039551`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.014938`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018219`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.020931`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.5375`, primary_mae `0.060508`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.525`, primary_mae `0.085629`, avg `0.026113`, median `0.035204`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.014938`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018219`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.020931`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.5375`, primary_mae `0.060508`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.525`, primary_mae `0.085629`, avg `0.026113`, median `0.035204`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.7`, primary_mae `0.014473`, avg `-0.00612`, median `-0.008299`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.7`, primary_mae `0.014134`, avg `-0.008182`, median `-0.0084`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.7`, primary_mae `0.014999`, avg `-0.005703`, median `-0.008001`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.034353`, avg `0.014509`, median `0.017343`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.049405`, avg `0.036506`, median `0.058786`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.014938`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018219`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.020931`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.5375`, primary_mae `0.060508`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.525`, primary_mae `0.085629`, avg `0.026113`, median `0.035204`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.014938`, avg `-0.004634`, median `-0.003749`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.018219`, avg `-0.009092`, median `-0.009037`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.020931`, avg `-0.009331`, median `-0.010971`
- 20d: sample `80`, primary_hit `0.4625`, primary_closer `0.5375`, primary_mae `0.060508`, avg `0.007297`, median `0.010094`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.525`, primary_mae `0.085629`, avg `0.026113`, median `0.035204`

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
