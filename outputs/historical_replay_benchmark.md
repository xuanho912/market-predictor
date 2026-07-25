# Historical Replay Benchmark

Generated at: `2026-07-25T06:08:31.241990+00:00`
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
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.016459`
- secondary_mean_absolute_error: `0.015834`
- primary_error_advantage: `-0.000625`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.021067`
- secondary_mean_absolute_error: `0.018914`
- primary_error_advantage: `-0.002153`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.021749`
- secondary_mean_absolute_error: `0.018399`
- primary_error_advantage: `-0.00335`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.575`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.15`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `-0.7`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.043287`
- secondary_mean_absolute_error: `0.030878`
- primary_error_advantage: `-0.012409`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.072484`
- secondary_mean_absolute_error: `0.063466`
- primary_error_advantage: `-0.009018`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.625`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015769`, as_primary `0`, as_primary_hit `None`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.019094`, as_primary `0`, as_primary_hit `None`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, direction_hit `0.8125`, path_mae `0.01881`, as_primary `0`, as_primary_hit `None`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.026064`, as_primary `0`, as_primary_hit `None`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.0611`, as_primary `0`, as_primary_hit `None`, avg `0.049675`, median `0.075617`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016232`, as_primary `0`, as_primary_hit `None`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.01948`, as_primary `0`, as_primary_hit `None`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, direction_hit `0.8125`, path_mae `0.019967`, as_primary `0`, as_primary_hit `None`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.038568`, as_primary `0`, as_primary_hit `None`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.066887`, as_primary `0`, as_primary_hit `None`, avg `0.049675`, median `0.075617`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.016459`, as_primary `80`, as_primary_hit `0.5875`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, direction_hit `0.4125`, path_mae `0.021067`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, direction_hit `0.1875`, path_mae `0.021749`, as_primary `80`, as_primary_hit `0.8125`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, direction_hit `0.15`, path_mae `0.043287`, as_primary `80`, as_primary_hit `0.85`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, direction_hit `0.2`, path_mae `0.072484`, as_primary `80`, as_primary_hit `0.8`, avg `0.049675`, median `0.075617`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015818`, as_primary `0`, as_primary_hit `None`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, direction_hit `0.5875`, path_mae `0.018981`, as_primary `0`, as_primary_hit `None`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, direction_hit `0.8125`, path_mae `0.018132`, as_primary `0`, as_primary_hit `None`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.024734`, as_primary `0`, as_primary_hit `None`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, direction_hit `0.8`, path_mae `0.061896`, as_primary `0`, as_primary_hit `None`, avg `0.049675`, median `0.075617`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.016459`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.021067`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, primary_hit `0.1875`, primary_closer `0.4875`, primary_mae `0.021749`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.3375`, primary_mae `0.043287`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4875`, primary_mae `0.072484`, avg `0.049675`, median `0.075617`

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
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.02025`, avg `0.008003`, median `0.005731`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.02435`, avg `0.010348`, median `0.004361`
- 10d: sample `20`, primary_hit `0.15`, primary_closer `0.55`, primary_mae `0.016101`, avg `0.021144`, median `0.026765`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.3`, primary_mae `0.036794`, avg `0.034589`, median `0.031544`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.0918`, avg `0.013373`, median `0.060674`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.015195`, avg `0.001634`, median `0.004149`
- 5d: sample `60`, primary_hit `0.4`, primary_closer `0.4167`, primary_mae `0.019973`, avg `0.005633`, median `0.00805`
- 10d: sample `60`, primary_hit `0.2`, primary_closer `0.4667`, primary_mae `0.023631`, avg `0.015459`, median `0.01712`
- 20d: sample `60`, primary_hit `0.1667`, primary_closer `0.35`, primary_mae `0.045451`, avg `0.030438`, median `0.033589`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.5333`, primary_mae `0.066046`, avg `0.061776`, median `0.084258`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.015195, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.019973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036794, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.066046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015769, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016459, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.015195, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018981, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021067, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.019973, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018132, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021749, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.016101, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': -0.7, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024734, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043287, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.036794, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0611, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072484, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.066046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.016338`, avg `0.00231`, median `0.005341`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.012766`, avg `0.011766`, median `0.015644`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.016653`, avg `0.011279`, median `0.01205`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.039227`, avg `0.034564`, median `0.031643`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.75`, primary_mae `0.028094`, avg `0.096074`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.015141`, avg `0.005983`, median `0.006481`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.018946`, avg `0.011442`, median `0.015644`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.022218`, avg `0.016669`, median `0.02208`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.039015`, avg `0.031943`, median `0.029448`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.6875`, primary_mae `0.03014`, avg `0.097066`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.018903`, avg `0.010381`, median `0.011826`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.022013`, avg `0.013863`, median `0.008083`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.013269`, avg `0.020487`, median `0.029526`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.036613`, avg `0.033881`, median `0.037526`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.098626`, avg `-1.2e-05`, median `0.060674`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.016459`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.021067`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, primary_hit `0.1875`, primary_closer `0.4875`, primary_mae `0.021749`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.3375`, primary_mae `0.043287`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4875`, primary_mae `0.072484`, avg `0.049675`, median `0.075617`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.016459`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.021067`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, primary_hit `0.1875`, primary_closer `0.4875`, primary_mae `0.021749`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.3375`, primary_mae `0.043287`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4875`, primary_mae `0.072484`, avg `0.049675`, median `0.075617`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.013698`, avg `0.004306`, median `0.005602`
- 5d: sample `40`, primary_hit `0.325`, primary_closer `0.425`, primary_mae `0.01636`, avg `0.008969`, median `0.009975`
- 10d: sample `40`, primary_hit `0.175`, primary_closer `0.575`, primary_mae `0.016292`, avg `0.014466`, median `0.013673`
- 20d: sample `40`, primary_hit `0.175`, primary_closer `0.45`, primary_mae `0.038508`, avg `0.030712`, median `0.031465`
- 60d: sample `40`, primary_hit `0.025`, primary_closer `0.625`, primary_mae `0.030308`, avg `0.086127`, median `0.084449`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.475`, primary_mae `0.01922`, avg `0.002147`, median `6.5e-05`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.025774`, avg `0.004653`, median `0.000911`
- 10d: sample `40`, primary_hit `0.2`, primary_closer `0.4`, primary_mae `0.027206`, avg `0.019294`, median `0.024783`
- 20d: sample `40`, primary_hit `0.125`, primary_closer `0.225`, primary_mae `0.048066`, avg `0.032239`, median `0.033971`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.114661`, avg `0.013223`, median `0.060674`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.45`, primary_mae `0.016459`, avg `0.003227`, median `0.004149`
- 5d: sample `80`, primary_hit `0.4125`, primary_closer `0.4125`, primary_mae `0.021067`, avg `0.006811`, median `0.007278`
- 10d: sample `80`, primary_hit `0.1875`, primary_closer `0.4875`, primary_mae `0.021749`, avg `0.01688`, median `0.019753`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.3375`, primary_mae `0.043287`, avg `0.031476`, median `0.033589`
- 60d: sample `80`, primary_hit `0.2`, primary_closer `0.4875`, primary_mae `0.072484`, avg `0.049675`, median `0.075617`

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
