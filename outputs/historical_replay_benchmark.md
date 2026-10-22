# Historical Replay Benchmark

Generated at: `2026-10-22T06:10:47.946473+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.013692`
- secondary_mean_absolute_error: `0.013051`
- primary_error_advantage: `-0.000641`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.1625`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.018854`
- secondary_mean_absolute_error: `0.017053`
- primary_error_advantage: `-0.001801`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.02789`
- secondary_mean_absolute_error: `0.02417`
- primary_error_advantage: `-0.00372`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.043701`
- secondary_mean_absolute_error: `0.032496`
- primary_error_advantage: `-0.011205`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.075194`
- secondary_mean_absolute_error: `0.069394`
- primary_error_advantage: `-0.0058`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

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
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.013651`, as_primary `20`, as_primary_hit `0.65`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.019219`, as_primary `20`, as_primary_hit `0.65`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.026366`, as_primary `20`, as_primary_hit `0.7`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.037464`, as_primary `20`, as_primary_hit `0.7`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.074499`, as_primary `20`, as_primary_hit `0.55`, avg `0.027313`, median `0.026933`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.475`, path_mae `0.013846`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, direction_hit `0.5`, path_mae `0.018671`, as_primary `60`, as_primary_hit `0.4333`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.02917`, as_primary `60`, as_primary_hit `0.4333`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.045231`, as_primary `60`, as_primary_hit `0.7167`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.075626`, as_primary `60`, as_primary_hit `0.6667`, avg `0.027313`, median `0.026933`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.525`, path_mae `0.01274`, as_primary `0`, as_primary_hit `None`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.016762`, as_primary `0`, as_primary_hit `None`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, direction_hit `0.5`, path_mae `0.022066`, as_primary `0`, as_primary_hit `None`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.02546`, as_primary `0`, as_primary_hit `None`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.059551`, as_primary `0`, as_primary_hit `None`, avg `0.027313`, median `0.026933`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.013692`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4375`, primary_mae `0.018854`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.02789`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.043701`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.075194`, avg `0.027313`, median `0.026933`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.65`, primary_mae `0.007225`, avg `0.003461`, median `0.004629`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.013638`, avg `0.003273`, median `0.005606`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.017669`, avg `0.004048`, median `0.009234`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.025775`, avg `0.01205`, median `0.014043`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.078412`, avg `-0.001706`, median `0.002733`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018827`, avg `-0.000154`, median `-0.003812`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.02382`, avg `-0.00171`, median `-0.010047`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.037663`, avg `-0.003986`, median `-0.01452`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.043082`, avg `0.012875`, median `0.018905`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.5`, primary_mae `0.037182`, avg `0.039032`, median `0.035618`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.015904`, avg `-0.008505`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.017848`, avg `-0.00902`, median `-0.006388`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.015974`, avg `-0.002297`, median `-0.006389`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.048269`, avg `0.020468`, median `0.027848`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.093031`, avg `0.030979`, median `0.037982`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.012811`, avg `0.001568`, median `0.007433`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.020111`, avg `0.00154`, median `0.00026`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.040253`, avg `0.002888`, median `0.00564`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.25`, primary_mae `0.057676`, avg `0.020469`, median `0.019406`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.092152`, avg `0.040948`, median `0.027501`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.007225, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015974, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.025775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.037182, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01274, 'direction_hit_rate': 0.525}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013846, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.007225, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.1625, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016762, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019219, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.013638, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022066, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02917, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015974, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02546, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.045231, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.025775, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059551, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075626, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.037182, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.008677`, avg `0.006601`, median `0.009432`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.009932`, avg `0.009886`, median `0.009916`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.008513`, avg `0.013971`, median `0.015958`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.028564`, avg `0.00811`, median `0.010374`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.077611`, avg `0.005145`, median `0.006035`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.007581`, avg `0.005159`, median `0.00646`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.011586`, avg `0.006326`, median `0.008361`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.014384`, avg `0.008171`, median `0.011607`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.6875`, primary_mae `0.023268`, avg `0.014846`, median `0.017299`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.072213`, avg `0.008513`, median `0.020606`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.018541`, avg `-0.001635`, median `-0.012031`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.023249`, avg `-0.002002`, median `-0.016722`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.035641`, avg `-0.004521`, median `-0.017369`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.1875`, primary_mae `0.041885`, avg `0.010665`, median `0.018905`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.037875`, avg `0.04258`, median `0.03947`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.013692`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4375`, primary_mae `0.018854`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.02789`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.043701`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.075194`, avg `0.027313`, median `0.026933`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.013692`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4375`, primary_mae `0.018854`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.02789`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.043701`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.075194`, avg `0.027313`, median `0.026933`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.011564`, avg `-0.002522`, median `0.000184`
- 5d: sample `40`, primary_hit `0.65`, primary_closer `0.475`, primary_mae `0.015743`, avg `-0.002873`, median `-0.001055`
- 10d: sample `40`, primary_hit `0.7`, primary_closer `0.575`, primary_mae `0.016822`, avg `0.000875`, median `0.001074`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.037022`, avg `0.016259`, median `0.02136`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.5`, primary_mae `0.085722`, avg `0.014636`, median `0.018211`

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
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.013692`, avg `-0.000907`, median `0.001788`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4375`, primary_mae `0.018854`, avg `-0.001479`, median `-0.00019`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.02789`, avg `0.000163`, median `-5.7e-05`
- 20d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.043701`, avg `0.016466`, median `0.019807`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.475`, primary_mae `0.075194`, avg `0.027313`, median `0.026933`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
