# Historical Replay Benchmark

Generated at: `2026-08-13T23:29:28.101116+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `20`
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
- sample_size: `20`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.022698`
- secondary_mean_absolute_error: `0.01454`
- primary_error_advantage: `-0.008158`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 5d
- sample_size: `20`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2`
- primary_mean_absolute_error: `0.040953`
- secondary_mean_absolute_error: `0.021795`
- primary_error_advantage: `-0.019158`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.2`

### 10d
- sample_size: `20`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.059336`
- secondary_mean_absolute_error: `0.033978`
- primary_error_advantage: `-0.025358`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `20`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2`
- primary_mean_absolute_error: `0.118384`
- secondary_mean_absolute_error: `0.059791`
- primary_error_advantage: `-0.058593`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.2`

### 60d
- sample_size: `20`
- primary_hit_rate: `0.8`
- secondary_hit_rate: `0.8`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.093365`
- secondary_mean_absolute_error: `0.064742`
- primary_error_advantage: `-0.028623`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

## Scenario Type Performance

### base_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.65`, path_mae `0.01803`, as_primary `0`, as_primary_hit `None`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, direction_hit `0.55`, path_mae `0.029822`, as_primary `0`, as_primary_hit `None`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, direction_hit `0.55`, path_mae `0.03771`, as_primary `0`, as_primary_hit `None`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, direction_hit `0.6`, path_mae `0.072069`, as_primary `0`, as_primary_hit `None`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, direction_hit `0.8`, path_mae `0.065937`, as_primary `0`, as_primary_hit `None`, avg `0.052484`, median `0.06367`

### bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.65`, path_mae `0.022698`, as_primary `20`, as_primary_hit `0.65`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, direction_hit `0.55`, path_mae `0.040953`, as_primary `20`, as_primary_hit `0.55`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, direction_hit `0.55`, path_mae `0.059336`, as_primary `20`, as_primary_hit `0.55`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, direction_hit `0.6`, path_mae `0.118384`, as_primary `20`, as_primary_hit `0.6`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, direction_hit `0.8`, path_mae `0.093365`, as_primary `20`, as_primary_hit `0.8`, avg `0.052484`, median `0.06367`

### failed_bounce_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.35`, path_mae `0.014605`, as_primary `0`, as_primary_hit `None`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, direction_hit `0.45`, path_mae `0.02203`, as_primary `0`, as_primary_hit `None`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, direction_hit `0.45`, path_mae `0.051225`, as_primary `0`, as_primary_hit `None`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, direction_hit `0.4`, path_mae `0.112465`, as_primary `0`, as_primary_hit `None`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, direction_hit `0.2`, path_mae `0.092366`, as_primary `0`, as_primary_hit `None`, avg `0.052484`, median `0.06367`

### analog_average_path
- sample_size: `20`
- 3d: sample `20`, direction_hit `0.65`, path_mae `0.01454`, as_primary `0`, as_primary_hit `None`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, direction_hit `0.55`, path_mae `0.021795`, as_primary `0`, as_primary_hit `None`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, direction_hit `0.55`, path_mae `0.033978`, as_primary `0`, as_primary_hit `None`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, direction_hit `0.6`, path_mae `0.059791`, as_primary `0`, as_primary_hit `None`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, direction_hit `0.8`, path_mae `0.064742`, as_primary `0`, as_primary_hit `None`, avg `0.052484`, median `0.06367`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.022698, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.040953, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.059336, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.118384, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.093365, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.01454, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.022698, 'direction_hit_rate': 0.65}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.022698, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.021795, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.040953, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.040953, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.033978, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.059336, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.059336, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.059791, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.118384, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.2, 'primary_mean_absolute_error': 0.118384, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 20, 'sample_gate': 'early_evidence', 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.8, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 20, 'path_mean_absolute_error': 0.064742, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 20, 'path_mean_absolute_error': 0.093365, 'direction_hit_rate': 0.8}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.093365, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `2`
- 3d: sample `2`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.009659`, avg `0.018182`, median `0.018182`
- 5d: sample `2`, primary_hit `0.5`, primary_closer `0.0`, primary_mae `0.044173`, avg `-0.00541`, median `-0.00541`
- 10d: sample `2`, primary_hit `0.5`, primary_closer `0.0`, primary_mae `0.060027`, avg `0.00239`, median `0.00239`
- 20d: sample `2`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.146474`, avg `-0.018135`, median `-0.018135`
- 60d: sample `2`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.185313`, avg `-0.053633`, median `-0.053633`

### top_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.010171`, avg `0.019857`, median `0.018182`
- 5d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.038603`, avg `0.00016`, median `-0.00541`
- 10d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.070135`, avg `-0.007719`, median `0.00239`
- 20d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.140204`, avg `-0.011865`, median `-0.018135`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.134631`, avg `0.008293`, median `-0.028969`

### bottom_20
- sample_size: `4`
- 3d: sample `4`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.010171`, avg `0.019857`, median `0.018182`
- 5d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.038603`, avg `0.00016`, median `-0.00541`
- 10d: sample `4`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.070135`, avg `-0.007719`, median `0.00239`
- 20d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.140204`, avg `-0.011865`, median `-0.018135`
- 60d: sample `4`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.134631`, avg `0.008293`, median `-0.028969`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

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
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### options_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

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
