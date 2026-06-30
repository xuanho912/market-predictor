# Historical Replay Benchmark

Generated at: `2026-06-30T05:19:52.803911+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `STRONG_HISTORICAL_ONLY`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.016273`
- secondary_mean_absolute_error: `0.017042`
- primary_error_advantage: `0.000769`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.020278`
- secondary_mean_absolute_error: `0.021396`
- primary_error_advantage: `0.001118`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5333`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.026573`
- secondary_mean_absolute_error: `0.030224`
- primary_error_advantage: `0.003651`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.375`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.049613`
- secondary_mean_absolute_error: `0.047668`
- primary_error_advantage: `-0.001945`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6333`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.072139`
- secondary_mean_absolute_error: `0.085595`
- primary_error_advantage: `0.013456`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014862`, as_primary `0`, as_primary_hit `None`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.018416`, as_primary `0`, as_primary_hit `None`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.022127`, as_primary `0`, as_primary_hit `None`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.030581`, as_primary `0`, as_primary_hit `None`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.058801`, as_primary `0`, as_primary_hit `None`, avg `0.038839`, median `0.048732`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.016546`, as_primary `40`, as_primary_hit `0.45`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.021306`, as_primary `40`, as_primary_hit `0.375`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.027131`, as_primary `40`, as_primary_hit `0.45`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.043936`, as_primary `40`, as_primary_hit `0.825`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.073559`, as_primary `40`, as_primary_hit `0.75`, avg `0.038839`, median `0.048732`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.016769`, as_primary `40`, as_primary_hit `0.325`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020368`, as_primary `40`, as_primary_hit `0.4`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.029667`, as_primary `40`, as_primary_hit `0.475`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.053345`, as_primary `40`, as_primary_hit `0.575`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.084175`, as_primary `40`, as_primary_hit `0.6`, avg `0.038839`, median `0.048732`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014481`, as_primary `0`, as_primary_hit `None`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.017637`, as_primary `0`, as_primary_hit `None`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.021166`, as_primary `0`, as_primary_hit `None`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.029755`, as_primary `0`, as_primary_hit `None`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.059052`, as_primary `0`, as_primary_hit `None`, avg `0.038839`, median `0.048732`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.6167`, primary_mae `0.016929`, avg `-0.001582`, median `-0.002593`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5333`, primary_mae `0.020812`, avg `-0.005453`, median `-0.008169`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.5667`, primary_mae `0.024208`, avg `0.001651`, median `-0.000741`
- 20d: sample `60`, primary_hit `0.7333`, primary_closer `0.6333`, primary_mae `0.043091`, avg `0.02192`, median `0.028709`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.077674`, avg `0.052753`, median `0.066423`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014306`, avg `-0.003795`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018676`, avg `-0.005946`, median `-0.005426`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.03367`, avg `-0.00758`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.069176`, avg `-0.003539`, median `0.013848`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.055533`, avg `-0.002904`, median `0.013327`

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
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014306`, avg `-0.003795`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018676`, avg `-0.005946`, median `-0.005426`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.03367`, avg `-0.00758`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.069176`, avg `-0.003539`, median `0.013848`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.055533`, avg `-0.002904`, median `0.013327`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.6167`, primary_mae `0.016929`, avg `-0.001582`, median `-0.002593`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5333`, primary_mae `0.020812`, avg `-0.005453`, median `-0.008169`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.5667`, primary_mae `0.024208`, avg `0.001651`, median `-0.000741`
- 20d: sample `60`, primary_hit `0.7333`, primary_closer `0.6333`, primary_mae `0.043091`, avg `0.02192`, median `0.028709`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.077674`, avg `0.052753`, median `0.066423`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014306, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018676, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.024208, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.6333, 'primary_mean_absolute_error': 0.043091, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014481, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016769, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.014306, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017637, 'direction_hit_rate': 0.3875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021306, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.018676, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021166, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029667, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.024208, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029755, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053345, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.6333, 'primary_mean_absolute_error': 0.043091, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058801, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084175, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.055533, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `1.0`, primary_closer `1.0`, primary_mae `0.008345`, avg `-0.009799`, median `-0.005627`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.016074`, avg `-0.017144`, median `-0.01542`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.023925`, avg `0.002552`, median `-0.001656`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.058362`, avg `0.017175`, median `0.007511`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.110158`, avg `0.070511`, median `0.024137`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.8125`, primary_closer `0.8125`, primary_mae `0.011975`, avg `-0.005121`, median `-0.00397`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.015737`, avg `-0.008106`, median `-0.006441`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.6875`, primary_mae `0.025148`, avg `0.00084`, median `-0.001656`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.061122`, avg `0.014676`, median `-0.002157`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.107399`, avg `0.067591`, median `0.071123`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.014402`, avg `-0.002252`, median `-0.00191`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.018689`, avg `-0.005432`, median `-0.005426`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.034825`, avg `-0.005891`, median `-0.004583`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.06948`, avg `-0.003116`, median `0.01201`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.063997`, avg `-0.014263`, median `-0.037245`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.016273`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.020278`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.026573`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.5375`, primary_mae `0.049613`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5375`, primary_mae `0.072139`, avg `0.038839`, median `0.048732`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.016273`, avg `-0.002135`, median `-0.002845`
- 5d: sample `80`, primary_hit `0.4875`, primary_closer `0.5125`, primary_mae `0.020278`, avg `-0.005576`, median `-0.007293`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.525`, primary_mae `0.026573`, avg `-0.000657`, median `-0.001449`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.5375`, primary_mae `0.049613`, avg `0.015555`, median `0.019104`
- 60d: sample `80`, primary_hit `0.575`, primary_closer `0.5375`, primary_mae `0.072139`, avg `0.038839`, median `0.048732`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.6167`, primary_mae `0.016929`, avg `-0.001582`, median `-0.002593`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5333`, primary_mae `0.020812`, avg `-0.005453`, median `-0.008169`
- 10d: sample `60`, primary_hit `0.45`, primary_closer `0.5667`, primary_mae `0.024208`, avg `0.001651`, median `-0.000741`
- 20d: sample `60`, primary_hit `0.7333`, primary_closer `0.6333`, primary_mae `0.043091`, avg `0.02192`, median `0.028709`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.077674`, avg `0.052753`, median `0.066423`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.014306`, avg `-0.003795`, median `-0.003287`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.018676`, avg `-0.005946`, median `-0.005426`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.03367`, avg `-0.00758`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.069176`, avg `-0.003539`, median `0.013848`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.055533`, avg `-0.002904`, median `0.013327`

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
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.575`, primary_mae `0.014494`, avg `-0.002372`, median `-0.003478`
- 5d: sample `40`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.01884`, avg `-0.004818`, median `-0.00538`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.029045`, avg `-0.00229`, median `-0.003859`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.425`, primary_mae `0.065159`, avg `0.006104`, median `0.01201`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.080284`, avg `0.034612`, median `0.034947`

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
