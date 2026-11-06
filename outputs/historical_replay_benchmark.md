# Historical Replay Benchmark

Generated at: `2026-11-06T02:06:22.887296+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'medium', 'reasons': ['high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.020495`
- secondary_mean_absolute_error: `0.019839`
- primary_error_advantage: `-0.000656`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.023456`
- secondary_mean_absolute_error: `0.025202`
- primary_error_advantage: `0.001746`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.039767`
- secondary_mean_absolute_error: `0.042824`
- primary_error_advantage: `0.003057`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.35`
- primary_vs_secondary_accuracy_spread: `0.3`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.068371`
- secondary_mean_absolute_error: `0.054948`
- primary_error_advantage: `-0.013423`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.04328`
- secondary_mean_absolute_error: `0.045626`
- primary_error_advantage: `0.002346`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.019658`, as_primary `0`, as_primary_hit `None`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.024121`, as_primary `0`, as_primary_hit `None`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.039659`, as_primary `0`, as_primary_hit `None`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.045006`, as_primary `0`, as_primary_hit `None`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.04342`, as_primary `0`, as_primary_hit `None`, avg `0.056883`, median `0.061274`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.019847`, as_primary `0`, as_primary_hit `None`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.028015`, as_primary `0`, as_primary_hit `None`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.053068`, as_primary `0`, as_primary_hit `None`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.071054`, as_primary `0`, as_primary_hit `None`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.05436`, as_primary `0`, as_primary_hit `None`, avg `0.056883`, median `0.061274`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.020495`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.023456`, as_primary `80`, as_primary_hit `0.45`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.039767`, as_primary `80`, as_primary_hit `0.3625`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.068371`, as_primary `80`, as_primary_hit `0.35`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.04328`, as_primary `80`, as_primary_hit `0.7625`, avg `0.056883`, median `0.061274`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.019785`, as_primary `0`, as_primary_hit `None`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.022951`, as_primary `0`, as_primary_hit `None`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.036383`, as_primary `0`, as_primary_hit `None`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.044127`, as_primary `0`, as_primary_hit `None`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.04223`, as_primary `0`, as_primary_hit `None`, avg `0.056883`, median `0.061274`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.020495`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023456`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5375`, primary_mae `0.039767`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.375`, primary_mae `0.068371`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.5125`, primary_mae `0.04328`, avg `0.056883`, median `0.061274`

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
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.025966`, avg `0.001647`, median `0.012752`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.030634`, avg `0.008353`, median `0.006746`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.046768`, avg `0.016203`, median `0.005882`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.07411`, avg `-0.019737`, median `-0.041695`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.03345`, avg `0.104323`, median `0.112837`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.018672`, avg `-0.00607`, median `-0.005099`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.6`, primary_mae `0.021063`, avg `-0.007503`, median `-0.014608`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.55`, primary_mae `0.037433`, avg `-0.009177`, median `-0.019126`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.066458`, avg `-0.019191`, median `-0.028064`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.5667`, primary_mae `0.046556`, avg `0.04107`, median `0.045791`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.018672, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.021063, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.037433, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.066458, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03345, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019658, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020495, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.018672, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022951, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028015, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.021063, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036383, 'direction_hit_rate': 0.3625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053068, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.037433, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.35, 'primary_vs_secondary_accuracy_spread': 0.3, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044127, 'direction_hit_rate': 0.35}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071054, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.066458, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04223, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05436, 'direction_hit_rate': 0.7625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.03345, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.019308`, avg `-0.008911`, median `-0.016472`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.75`, primary_mae `0.029441`, avg `-0.008802`, median `-0.021928`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.043348`, avg `0.005541`, median `-0.016669`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.084639`, avg `-0.014121`, median `-0.02913`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.03976`, avg `0.04832`, median `0.034972`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020223`, avg `-0.002176`, median `0.002736`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.025406`, avg `-0.00243`, median `-0.004615`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.043388`, avg `-0.002732`, median `-0.016669`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.072808`, avg `-0.023151`, median `-0.031256`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.6875`, primary_mae `0.03238`, avg `0.0584`, median `0.061274`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.022088`, avg `0.00323`, median `0.012752`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.026616`, avg `0.010097`, median `0.006746`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.043395`, avg `0.012737`, median `0.005882`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.3125`, primary_mae `0.069082`, avg `-0.025822`, median `-0.041695`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.3125`, primary_mae `0.029846`, avg `0.105215`, median `0.112837`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.020495`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023456`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5375`, primary_mae `0.039767`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.375`, primary_mae `0.068371`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.5125`, primary_mae `0.04328`, avg `0.056883`, median `0.061274`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.020495`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023456`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5375`, primary_mae `0.039767`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.375`, primary_mae `0.068371`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.5125`, primary_mae `0.04328`, avg `0.056883`, median `0.061274`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.018672`, avg `-0.00607`, median `-0.005099`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.6`, primary_mae `0.021063`, avg `-0.007503`, median `-0.014608`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.55`, primary_mae `0.037433`, avg `-0.009177`, median `-0.019126`
- 20d: sample `60`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.066458`, avg `-0.019191`, median `-0.028064`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.5667`, primary_mae `0.046556`, avg `0.04107`, median `0.045791`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.025966`, avg `0.001647`, median `0.012752`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.030634`, avg `0.008353`, median `0.006746`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.046768`, avg `0.016203`, median `0.005882`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.07411`, avg `-0.019737`, median `-0.041695`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.35`, primary_mae `0.03345`, avg `0.104323`, median `0.112837`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.020495`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023456`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5375`, primary_mae `0.039767`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.375`, primary_mae `0.068371`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.5125`, primary_mae `0.04328`, avg `0.056883`, median `0.061274`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.020495`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023456`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5375`, primary_mae `0.039767`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.375`, primary_mae `0.068371`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.5125`, primary_mae `0.04328`, avg `0.056883`, median `0.061274`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5125`, primary_mae `0.020495`, avg `-0.004141`, median `-0.003994`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023456`, avg `-0.003539`, median `-0.009154`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.5375`, primary_mae `0.039767`, avg `-0.002832`, median `-0.016332`
- 20d: sample `80`, primary_hit `0.65`, primary_closer `0.375`, primary_mae `0.068371`, avg `-0.019327`, median `-0.030747`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.5125`, primary_mae `0.04328`, avg `0.056883`, median `0.061274`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
