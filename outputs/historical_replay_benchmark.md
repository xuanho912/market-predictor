# Historical Replay Benchmark

Generated at: `2026-10-21T23:36:15.405239+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.475`
- secondary_hit_rate: `0.525`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.013846`
- secondary_mean_absolute_error: `0.012897`
- primary_error_advantage: `-0.000949`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.0125`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.018671`
- secondary_mean_absolute_error: `0.017237`
- primary_error_advantage: `-0.001434`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.02917`
- secondary_mean_absolute_error: `0.02289`
- primary_error_advantage: `-0.00628`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.045231`
- secondary_mean_absolute_error: `0.030966`
- primary_error_advantage: `-0.014265`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.075626`
- secondary_mean_absolute_error: `0.068963`
- primary_error_advantage: `-0.006663`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.012815`, as_primary `0`, as_primary_hit `None`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.017105`, as_primary `0`, as_primary_hit `None`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.02259`, as_primary `0`, as_primary_hit `None`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.02585`, as_primary `0`, as_primary_hit `None`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.061126`, as_primary `0`, as_primary_hit `None`, avg `0.027313`, median `0.026933`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013651`, as_primary `0`, as_primary_hit `None`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019219`, as_primary `0`, as_primary_hit `None`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.026366`, as_primary `0`, as_primary_hit `None`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.037464`, as_primary `0`, as_primary_hit `None`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.074499`, as_primary `0`, as_primary_hit `None`, avg `0.027313`, median `0.026933`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013846`, as_primary `80`, as_primary_hit `0.525`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.018671`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.02917`, as_primary `80`, as_primary_hit `0.5`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.045231`, as_primary `80`, as_primary_hit `0.7125`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.075626`, as_primary `80`, as_primary_hit `0.6375`, avg `0.027313`, median `0.026933`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.01274`, as_primary `0`, as_primary_hit `None`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.016762`, as_primary `0`, as_primary_hit `None`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.022066`, as_primary `0`, as_primary_hit `None`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.02546`, as_primary `0`, as_primary_hit `None`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.059551`, as_primary `0`, as_primary_hit `None`, avg `0.027313`, median `0.026933`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.011873`, avg `-0.002522`, median `0.000184`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.015376`, avg `-0.002873`, median `-0.001055`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.019382`, avg `0.000875`, median `0.001074`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.040082`, avg `0.016259`, median `0.02136`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.086585`, avg `0.014636`, median `0.018211`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.015819`, avg `0.000707`, median `0.005393`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.021965`, avg `-8.5e-05`, median `-0.00019`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.038958`, avg `-0.000549`, median `-0.003246`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.050379`, avg `0.016672`, median `0.019406`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.064667`, avg `0.03999`, median `0.030028`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.007842`, avg `0.003461`, median `0.004629`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.012904`, avg `0.003273`, median `0.005606`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.02279`, avg `0.004048`, median `0.009234`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.031895`, avg `0.01205`, median `0.014043`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.080139`, avg `-0.001706`, median `0.002733`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018827`, avg `-0.000154`, median `-0.003812`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.02382`, avg `-0.00171`, median `-0.010047`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.037663`, avg `-0.003986`, median `-0.01452`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.043082`, avg `0.012875`, median `0.018905`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.5`, primary_mae `0.037182`, avg `0.039032`, median `0.035618`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.525`, primary_closer `0.375`, primary_mae `0.014357`, avg `-0.003468`, median `-0.00264`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.375`, primary_mae `0.018979`, avg `-0.00374`, median `-0.002989`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.028113`, avg `0.000295`, median `-0.004481`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.3`, primary_mae `0.052973`, avg `0.020468`, median `0.024592`
- 60d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.092592`, avg `0.035963`, median `0.030329`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.007842, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.012904, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.02279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.031895, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.037182, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01274, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013846, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.007842, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.0125, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016762, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019219, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.012904, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022066, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02917, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.02279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02546, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045231, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.031895, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059551, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075626, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.037182, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.014987`, avg `-0.011386`, median `-0.009739`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.016786`, avg `-0.008748`, median `-0.008736`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.013381`, avg `-0.00992`, median `-0.016542`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.034923`, avg `0.002441`, median `0.006586`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.068826`, avg `0.00059`, median `0.004851`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.016124`, avg `-0.006966`, median `-0.007945`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.018104`, avg `-0.005472`, median `-0.003481`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.018702`, avg `-2.4e-05`, median `-0.004544`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.052587`, avg `0.024006`, median `0.030181`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.104601`, avg `0.041518`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.018541`, avg `-0.001635`, median `-0.012031`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.023249`, avg `-0.002002`, median `-0.016722`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.035641`, avg `-0.004521`, median `-0.017369`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.041885`, avg `0.010665`, median `0.018905`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.037875`, avg `0.04258`, median `0.03947`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### low_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.013846`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018671`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.02917`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2875`, primary_mae `0.045231`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.45`, primary_mae `0.075626`, avg `0.027313`, median `0.026933`

### fred_available
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_missing
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.013846`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018671`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.02917`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2875`, primary_mae `0.045231`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.45`, primary_mae `0.075626`, avg `0.027313`, median `0.026933`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.011873`, avg `-0.002522`, median `0.000184`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.015376`, avg `-0.002873`, median `-0.001055`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.019382`, avg `0.000875`, median `0.001074`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.040082`, avg `0.016259`, median `0.02136`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.45`, primary_mae `0.086585`, avg `0.014636`, median `0.018211`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.015819`, avg `0.000707`, median `0.005393`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.021965`, avg `-8.5e-05`, median `-0.00019`
- 10d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.038958`, avg `-0.000549`, median `-0.003246`
- 20d: sample `40`, primary_hit `0.3`, primary_closer `0.225`, primary_mae `0.050379`, avg `0.016672`, median `0.019406`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.064667`, avg `0.03999`, median `0.030028`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.013846`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.018671`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.02917`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2875`, primary_mae `0.045231`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, primary_hit `0.3625`, primary_closer `0.45`, primary_mae `0.075626`, avg `0.027313`, median `0.026933`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
