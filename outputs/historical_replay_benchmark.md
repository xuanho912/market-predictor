# Historical Replay Benchmark

Generated at: `2026-11-28T20:07:01.714284+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.024039`
- secondary_mean_absolute_error: `0.021677`
- primary_error_advantage: `-0.002362`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.625`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.025571`
- secondary_mean_absolute_error: `0.02416`
- primary_error_advantage: `-0.001411`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.02729`
- secondary_mean_absolute_error: `0.030543`
- primary_error_advantage: `0.003253`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.054863`
- secondary_mean_absolute_error: `0.058268`
- primary_error_advantage: `0.003405`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.625`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.077828`
- secondary_mean_absolute_error: `0.091948`
- primary_error_advantage: `0.01412`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.020844`, as_primary `0`, as_primary_hit `None`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.021983`, as_primary `0`, as_primary_hit `None`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.026822`, as_primary `0`, as_primary_hit `None`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, direction_hit `0.5`, path_mae `0.041349`, as_primary `0`, as_primary_hit `None`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.074`, as_primary `0`, as_primary_hit `None`, avg `0.014162`, median `-0.005128`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.021691`, as_primary `20`, as_primary_hit `0.3`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.024044`, as_primary `20`, as_primary_hit `0.3`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.035109`, as_primary `20`, as_primary_hit `0.4`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, direction_hit `0.5`, path_mae `0.06589`, as_primary `20`, as_primary_hit `0.6`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.090286`, as_primary `20`, as_primary_hit `0.55`, avg `0.014162`, median `-0.005128`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.024171`, as_primary `60`, as_primary_hit `0.4`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.02643`, as_primary `60`, as_primary_hit `0.4667`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.027386`, as_primary `60`, as_primary_hit `0.5`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, direction_hit `0.5`, path_mae `0.056184`, as_primary `60`, as_primary_hit `0.4667`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.084521`, as_primary `60`, as_primary_hit `0.4667`, avg `0.014162`, median `-0.005128`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.019796`, as_primary `0`, as_primary_hit `None`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.021401`, as_primary `0`, as_primary_hit `None`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.024186`, as_primary `0`, as_primary_hit `None`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, direction_hit `0.5`, path_mae `0.036969`, as_primary `0`, as_primary_hit `None`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.071049`, as_primary `0`, as_primary_hit `None`, avg `0.014162`, median `-0.005128`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.024039`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.025571`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.02729`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.054863`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.525`, primary_mae `0.077828`, avg `0.014162`, median `-0.005128`

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
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.042855`, avg `-0.00131`, median `-0.006572`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.043566`, avg `0.009367`, median `0.013291`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.042137`, avg `0.021954`, median `0.017852`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.064708`, avg `-0.008983`, median `-0.018312`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.100061`, avg `-0.002749`, median `-0.004011`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.6`, primary_mae `0.017767`, avg `-0.004188`, median `-0.007334`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.5333`, primary_mae `0.019573`, avg `-0.007168`, median `-0.007072`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.022341`, avg `-0.001891`, median `-0.004392`
- 20d: sample `60`, primary_hit `0.5167`, primary_closer `0.6167`, primary_mae `0.051581`, avg `0.008222`, median `0.00354`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5667`, primary_mae `0.070417`, avg `0.019799`, median `-0.005128`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.019573, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.022341, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.6167, 'primary_mean_absolute_error': 0.051581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.070417, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019796, 'direction_hit_rate': 0.375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024171, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.017767, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021401, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02643, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.019573, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024186, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035109, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.022341, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036969, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.06589, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.6167, 'primary_mean_absolute_error': 0.051581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071049, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090286, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.070417, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.875`, primary_mae `0.012941`, avg `-0.010295`, median `-0.008299`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.013159`, avg `-0.013203`, median `-0.016563`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015394`, avg `-0.012174`, median `-0.012647`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0413`, avg `0.003577`, median `0.013767`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.065733`, avg `0.008535`, median `-0.014935`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.75`, primary_mae `0.015008`, avg `-0.006441`, median `-0.008299`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.013239`, avg `-0.010284`, median `-0.009646`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.01151`, avg `-0.008019`, median `-0.003586`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.045921`, avg `-0.001044`, median `0.001105`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.062622`, avg `0.011409`, median `-0.005861`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.038385`, avg `-0.005124`, median `-0.008749`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.038662`, avg `0.003236`, median `0.000426`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.042662`, avg `0.014985`, median `0.010963`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.061477`, avg `-0.012878`, median `-0.018312`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.099782`, avg `-0.005048`, median `-0.004011`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.024039`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.025571`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.02729`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.054863`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.525`, primary_mae `0.077828`, avg `0.014162`, median `-0.005128`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.024039`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.025571`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.02729`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.054863`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.525`, primary_mae `0.077828`, avg `0.014162`, median `-0.005128`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.6`, primary_mae `0.017767`, avg `-0.004188`, median `-0.007334`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.5333`, primary_mae `0.019573`, avg `-0.007168`, median `-0.007072`
- 10d: sample `60`, primary_hit `0.5`, primary_closer `0.5167`, primary_mae `0.022341`, avg `-0.001891`, median `-0.004392`
- 20d: sample `60`, primary_hit `0.5167`, primary_closer `0.6167`, primary_mae `0.051581`, avg `0.008222`, median `0.00354`
- 60d: sample `60`, primary_hit `0.55`, primary_closer `0.5667`, primary_mae `0.070417`, avg `0.019799`, median `-0.005128`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.042855`, avg `-0.00131`, median `-0.006572`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.043566`, avg `0.009367`, median `0.013291`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.5`, primary_mae `0.042137`, avg `0.021954`, median `0.017852`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.064708`, avg `-0.008983`, median `-0.018312`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.100061`, avg `-0.002749`, median `-0.004011`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.024039`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.025571`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.02729`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.054863`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.525`, primary_mae `0.077828`, avg `0.014162`, median `-0.005128`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.024039`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.025571`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.02729`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.054863`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.525`, primary_mae `0.077828`, avg `0.014162`, median `-0.005128`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.525`, primary_closer `0.5375`, primary_mae `0.024039`, avg `-0.003468`, median `-0.007334`
- 5d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.025571`, avg `-0.003034`, median `-0.006344`
- 10d: sample `80`, primary_hit `0.475`, primary_closer `0.5125`, primary_mae `0.02729`, avg `0.004071`, median `-0.001997`
- 20d: sample `80`, primary_hit `0.55`, primary_closer `0.5375`, primary_mae `0.054863`, avg `0.003921`, median `-0.000647`
- 60d: sample `80`, primary_hit `0.5375`, primary_closer `0.525`, primary_mae `0.077828`, avg `0.014162`, median `-0.005128`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
