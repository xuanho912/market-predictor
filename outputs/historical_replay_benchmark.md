# Historical Replay Benchmark

Generated at: `2026-09-11T00:39:57.493372+00:00`
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
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.026379`
- secondary_mean_absolute_error: `0.018291`
- primary_error_advantage: `-0.008088`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.027762`
- secondary_mean_absolute_error: `0.021772`
- primary_error_advantage: `-0.00599`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3125`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `-0.375`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.040023`
- secondary_mean_absolute_error: `0.027269`
- primary_error_advantage: `-0.012754`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `-0.6`
- primary_closer_than_secondary_rate: `0.2125`
- primary_mean_absolute_error: `0.061639`
- secondary_mean_absolute_error: `0.032613`
- primary_error_advantage: `-0.029026`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.079912`
- secondary_mean_absolute_error: `0.061223`
- primary_error_advantage: `-0.018689`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6875`, path_mae `0.018089`, as_primary `0`, as_primary_hit `None`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.021988`, as_primary `0`, as_primary_hit `None`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.027608`, as_primary `0`, as_primary_hit `None`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.034233`, as_primary `0`, as_primary_hit `None`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.061081`, as_primary `0`, as_primary_hit `None`, avg `0.065843`, median `0.082944`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6875`, path_mae `0.019128`, as_primary `0`, as_primary_hit `None`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.025749`, as_primary `0`, as_primary_hit `None`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.033639`, as_primary `0`, as_primary_hit `None`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.050406`, as_primary `0`, as_primary_hit `None`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.064555`, as_primary `0`, as_primary_hit `None`, avg `0.065843`, median `0.082944`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3125`, path_mae `0.026379`, as_primary `80`, as_primary_hit `0.6875`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.027762`, as_primary `80`, as_primary_hit `0.6125`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, direction_hit `0.3125`, path_mae `0.040023`, as_primary `80`, as_primary_hit `0.6875`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, direction_hit `0.2`, path_mae `0.061639`, as_primary `80`, as_primary_hit `0.8`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.079912`, as_primary `80`, as_primary_hit `0.7875`, avg `0.065843`, median `0.082944`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6875`, path_mae `0.018291`, as_primary `0`, as_primary_hit `None`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.021772`, as_primary `0`, as_primary_hit `None`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, direction_hit `0.6875`, path_mae `0.027269`, as_primary `0`, as_primary_hit `None`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.032613`, as_primary `0`, as_primary_hit `None`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.061223`, as_primary `0`, as_primary_hit `None`, avg `0.065843`, median `0.082944`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.026379`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.027762`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.040023`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.2125`, primary_mae `0.061639`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.375`, primary_mae `0.079912`, avg `0.065843`, median `0.082944`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3333`, primary_closer `0.25`, primary_mae `0.031719`, avg `0.007815`, median `0.015898`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.3333`, primary_mae `0.032398`, avg `0.009329`, median `0.013228`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.3167`, primary_mae `0.048166`, avg `0.017121`, median `0.020752`
- 20d: sample `60`, primary_hit `0.2333`, primary_closer `0.2167`, primary_mae `0.070413`, avg `0.032147`, median `0.034715`
- 60d: sample `60`, primary_hit `0.2167`, primary_closer `0.4`, primary_mae `0.086063`, avg `0.064512`, median `0.087043`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.010361`, avg `0.004002`, median `0.004678`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.013854`, avg `0.004183`, median `0.010518`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.4`, primary_mae `0.015591`, avg `0.006692`, median `0.008213`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.2`, primary_mae `0.035316`, avg `0.032367`, median `0.034657`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.06146`, avg `0.069835`, median `0.07602`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.010361, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.013854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015591, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.035316, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.06146, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018089, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026379, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.010361, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021772, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027762, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.013854, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': -0.375, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027269, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040023, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.015591, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': -0.6, 'primary_closer_than_secondary_rate': 0.2125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032613, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061639, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.035316, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061081, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079912, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.06146, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.013995`, avg `-0.003677`, median `-0.001624`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.016837`, avg `0.00159`, median `0.006272`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.018378`, avg `0.010867`, median `0.015682`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.0`, primary_mae `0.0829`, avg `0.042186`, median `0.050926`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.75`, primary_mae `0.040823`, avg `0.097429`, median `0.110832`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.021811`, avg `0.006352`, median `0.014733`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.022137`, avg `0.010781`, median `0.014527`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.018258`, avg `0.014194`, median `0.016718`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.0625`, primary_mae `0.074103`, avg `0.023147`, median `0.027267`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.625`, primary_mae `0.043295`, avg `0.082143`, median `0.099675`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.0625`, primary_closer `0.125`, primary_mae `0.031013`, avg `0.02027`, median `0.024148`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.03558`, avg `0.023292`, median `0.029291`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.072275`, avg `0.032756`, median `0.038479`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.081616`, avg `0.060252`, median `0.055203`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.4375`, primary_mae `0.096542`, avg `0.086869`, median `0.128949`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.026379`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.027762`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.040023`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.2125`, primary_mae `0.061639`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.375`, primary_mae `0.079912`, avg `0.065843`, median `0.082944`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.026379`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.027762`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.040023`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.2125`, primary_mae `0.061639`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.375`, primary_mae `0.079912`, avg `0.065843`, median `0.082944`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.026379`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.027762`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.040023`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.2125`, primary_mae `0.061639`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.375`, primary_mae `0.079912`, avg `0.065843`, median `0.082944`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3125`, primary_closer `0.325`, primary_mae `0.026379`, avg `0.006862`, median `0.012505`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4`, primary_mae `0.027762`, avg `0.008042`, median `0.012744`
- 10d: sample `80`, primary_hit `0.3125`, primary_closer `0.3375`, primary_mae `0.040023`, avg `0.014514`, median `0.01712`
- 20d: sample `80`, primary_hit `0.2`, primary_closer `0.2125`, primary_mae `0.061639`, avg `0.032202`, median `0.034715`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.375`, primary_mae `0.079912`, avg `0.065843`, median `0.082944`

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
