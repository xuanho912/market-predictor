# Historical Replay Benchmark

Generated at: `2026-08-18T20:47:18.770588+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `60`
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
- sample_size: `60`
- primary_hit_rate: `0.3667`
- secondary_hit_rate: `0.6333`
- primary_vs_secondary_accuracy_spread: `-0.2667`
- primary_closer_than_secondary_rate: `0.4667`
- primary_mean_absolute_error: `0.018076`
- secondary_mean_absolute_error: `0.016768`
- primary_error_advantage: `-0.001308`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `60`
- primary_hit_rate: `0.4167`
- secondary_hit_rate: `0.5833`
- primary_vs_secondary_accuracy_spread: `-0.1667`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.023316`
- secondary_mean_absolute_error: `0.025208`
- primary_error_advantage: `0.001892`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `60`
- primary_hit_rate: `0.3667`
- secondary_hit_rate: `0.6333`
- primary_vs_secondary_accuracy_spread: `-0.2667`
- primary_closer_than_secondary_rate: `0.4167`
- primary_mean_absolute_error: `0.040888`
- secondary_mean_absolute_error: `0.035518`
- primary_error_advantage: `-0.00537`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.475`

### 20d
- sample_size: `60`
- primary_hit_rate: `0.3167`
- secondary_hit_rate: `0.6833`
- primary_vs_secondary_accuracy_spread: `-0.3667`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.087739`
- secondary_mean_absolute_error: `0.062856`
- primary_error_advantage: `-0.024883`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `60`
- primary_hit_rate: `0.3167`
- secondary_hit_rate: `0.6833`
- primary_vs_secondary_accuracy_spread: `-0.3667`
- primary_closer_than_secondary_rate: `0.4167`
- primary_mean_absolute_error: `0.104891`
- secondary_mean_absolute_error: `0.084555`
- primary_error_advantage: `-0.020336`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6333`, path_mae `0.015063`, as_primary `0`, as_primary_hit `None`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, direction_hit `0.5833`, path_mae `0.022671`, as_primary `0`, as_primary_hit `None`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, direction_hit `0.6333`, path_mae `0.029437`, as_primary `0`, as_primary_hit `None`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, direction_hit `0.6833`, path_mae `0.050026`, as_primary `0`, as_primary_hit `None`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, direction_hit `0.6833`, path_mae `0.076352`, as_primary `0`, as_primary_hit `None`, avg `0.025764`, median `0.049838`

### bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6333`, path_mae `0.018987`, as_primary `0`, as_primary_hit `None`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, direction_hit `0.5833`, path_mae `0.031623`, as_primary `0`, as_primary_hit `None`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, direction_hit `0.6333`, path_mae `0.043317`, as_primary `0`, as_primary_hit `None`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, direction_hit `0.6833`, path_mae `0.079695`, as_primary `0`, as_primary_hit `None`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, direction_hit `0.6833`, path_mae `0.093288`, as_primary `0`, as_primary_hit `None`, avg `0.025764`, median `0.049838`

### failed_bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.3667`, path_mae `0.018076`, as_primary `60`, as_primary_hit `0.6333`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, direction_hit `0.4167`, path_mae `0.023316`, as_primary `60`, as_primary_hit `0.5833`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, direction_hit `0.3667`, path_mae `0.040888`, as_primary `60`, as_primary_hit `0.6333`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, direction_hit `0.3167`, path_mae `0.087739`, as_primary `60`, as_primary_hit `0.6833`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, direction_hit `0.3167`, path_mae `0.104891`, as_primary `60`, as_primary_hit `0.6833`, avg `0.025764`, median `0.049838`

### analog_average_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6333`, path_mae `0.014994`, as_primary `0`, as_primary_hit `None`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, direction_hit `0.5833`, path_mae `0.019211`, as_primary `0`, as_primary_hit `None`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, direction_hit `0.6333`, path_mae `0.027193`, as_primary `0`, as_primary_hit `None`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, direction_hit `0.6833`, path_mae `0.046659`, as_primary `0`, as_primary_hit `None`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, direction_hit `0.6833`, path_mae `0.076711`, as_primary `0`, as_primary_hit `None`, avg `0.025764`, median `0.049838`

## Edge Status Performance

### RISK_WARNING
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4667`, primary_mae `0.018076`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.023316`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.040888`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3`, primary_mae `0.087739`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.104891`, avg `0.025764`, median `0.049838`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4667`, primary_mae `0.018076`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.023316`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.040888`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3`, primary_mae `0.087739`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.104891`, avg `0.025764`, median `0.049838`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.018076, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023316, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.040888, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.087739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.104891, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3667, 'secondary_hit_rate': 0.6333, 'primary_vs_secondary_accuracy_spread': -0.2667, 'primary_closer_than_secondary_rate': 0.4667, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.014994, 'direction_hit_rate': 0.6333}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.018987, 'direction_hit_rate': 0.6333}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.018076, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4167, 'secondary_hit_rate': 0.5833, 'primary_vs_secondary_accuracy_spread': -0.1667, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.019211, 'direction_hit_rate': 0.5833}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.031623, 'direction_hit_rate': 0.5833}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.023316, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3667, 'secondary_hit_rate': 0.6333, 'primary_vs_secondary_accuracy_spread': -0.2667, 'primary_closer_than_secondary_rate': 0.4167, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.027193, 'direction_hit_rate': 0.6333}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.043317, 'direction_hit_rate': 0.6333}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.040888, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3167, 'secondary_hit_rate': 0.6833, 'primary_vs_secondary_accuracy_spread': -0.3667, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.046659, 'direction_hit_rate': 0.6833}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.087739, 'direction_hit_rate': 0.3167}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.087739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3167, 'secondary_hit_rate': 0.6833, 'primary_vs_secondary_accuracy_spread': -0.3667, 'primary_closer_than_secondary_rate': 0.4167, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 60, 'path_mean_absolute_error': 0.076352, 'direction_hit_rate': 0.6833}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.104891, 'direction_hit_rate': 0.3167}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.104891, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `6`
- 3d: sample `6`, primary_hit `0.1667`, primary_closer `0.3333`, primary_mae `0.028736`, avg `0.001102`, median `0.010792`
- 5d: sample `6`, primary_hit `0.3333`, primary_closer `0.5`, primary_mae `0.016314`, avg `0.003127`, median `0.007128`
- 10d: sample `6`, primary_hit `0.1667`, primary_closer `0.5`, primary_mae `0.02911`, avg `0.007415`, median `0.01307`
- 20d: sample `6`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.068809`, avg `-0.00051`, median `0.008581`
- 60d: sample `6`, primary_hit `0.3333`, primary_closer `0.3333`, primary_mae `0.09431`, avg `0.033664`, median `0.056402`

### top_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.5`, primary_closer `0.5833`, primary_mae `0.02243`, avg `-0.001697`, median `-0.000883`
- 5d: sample `12`, primary_hit `0.4167`, primary_closer `0.6667`, primary_mae `0.018182`, avg `0.002807`, median `0.004667`
- 10d: sample `12`, primary_hit `0.25`, primary_closer `0.4167`, primary_mae `0.028006`, avg `0.008679`, median `0.011059`
- 20d: sample `12`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.077967`, avg `0.015205`, median `0.023697`
- 60d: sample `12`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.082774`, avg `0.011186`, median `0.005143`

### bottom_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.016033`, avg `0.010091`, median `0.010987`
- 5d: sample `12`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.025564`, avg `0.006862`, median `0.001259`
- 10d: sample `12`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.044478`, avg `0.015595`, median `0.013627`
- 20d: sample `12`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.087056`, avg `0.030006`, median `0.013042`
- 60d: sample `12`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.068019`, avg `0.052973`, median `0.040994`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4667`, primary_mae `0.018076`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.023316`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.040888`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3`, primary_mae `0.087739`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.104891`, avg `0.025764`, median `0.049838`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4667`, primary_mae `0.018076`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.023316`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.040888`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3`, primary_mae `0.087739`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.104891`, avg `0.025764`, median `0.049838`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.5`, primary_mae `0.022379`, avg `0.001631`, median `0.005338`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.6`, primary_mae `0.020556`, avg `0.003688`, median `0.004667`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.45`, primary_mae `0.030595`, avg `0.005895`, median `0.011059`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.076135`, avg `0.01096`, median `0.015956`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.092979`, avg `0.004284`, median `0.005143`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.45`, primary_mae `0.01422`, avg `0.006735`, median `0.007773`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.022367`, avg `0.004066`, median `0.00322`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.040788`, avg `0.016672`, median `0.014273`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.08328`, avg `0.032569`, median `0.013689`
- 60d: sample `20`, primary_hit `0.2`, primary_closer `0.5`, primary_mae `0.063545`, avg `0.056577`, median `0.048545`

### options_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4667`, primary_mae `0.018076`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.023316`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.040888`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3`, primary_mae `0.087739`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.104891`, avg `0.025764`, median `0.049838`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.4667`, primary_mae `0.018076`, avg `0.005308`, median `0.009598`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.5`, primary_mae `0.023316`, avg `0.00455`, median `0.005053`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.4167`, primary_mae `0.040888`, avg `0.008113`, median `0.01093`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3`, primary_mae `0.087739`, avg `0.014812`, median `0.015068`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4167`, primary_mae `0.104891`, avg `0.025764`, median `0.049838`

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
