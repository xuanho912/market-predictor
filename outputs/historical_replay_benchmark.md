# Historical Replay Benchmark

Generated at: `2026-08-12T13:50:13.528056+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `60`
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
- sample_size: `60`
- primary_hit_rate: `0.6667`
- secondary_hit_rate: `0.6667`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4833`
- primary_mean_absolute_error: `0.016146`
- secondary_mean_absolute_error: `0.014085`
- primary_error_advantage: `-0.002061`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 5d
- sample_size: `60`
- primary_hit_rate: `0.6333`
- secondary_hit_rate: `0.6333`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4667`
- primary_mean_absolute_error: `0.022124`
- secondary_mean_absolute_error: `0.022243`
- primary_error_advantage: `0.000119`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4667`

### 10d
- sample_size: `60`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4833`
- primary_mean_absolute_error: `0.035391`
- secondary_mean_absolute_error: `0.035812`
- primary_error_advantage: `0.000421`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 20d
- sample_size: `60`
- primary_hit_rate: `0.6833`
- secondary_hit_rate: `0.6833`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.062049`
- secondary_mean_absolute_error: `0.061985`
- primary_error_advantage: `-6.4e-05`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 60d
- sample_size: `60`
- primary_hit_rate: `0.65`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.093592`
- secondary_mean_absolute_error: `0.086741`
- primary_error_advantage: `-0.006851`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6667`, path_mae `0.013853`, as_primary `0`, as_primary_hit `None`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, direction_hit `0.6333`, path_mae `0.020329`, as_primary `0`, as_primary_hit `None`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, direction_hit `0.6`, path_mae `0.030095`, as_primary `0`, as_primary_hit `None`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, direction_hit `0.6833`, path_mae `0.047825`, as_primary `0`, as_primary_hit `None`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, direction_hit `0.65`, path_mae `0.076538`, as_primary `0`, as_primary_hit `None`, avg `0.030404`, median `0.046405`

### bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6667`, path_mae `0.016933`, as_primary `40`, as_primary_hit `0.625`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, direction_hit `0.6333`, path_mae `0.027664`, as_primary `40`, as_primary_hit `0.625`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, direction_hit `0.6`, path_mae `0.044642`, as_primary `40`, as_primary_hit `0.6`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, direction_hit `0.6833`, path_mae `0.079603`, as_primary `40`, as_primary_hit `0.7`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, direction_hit `0.65`, path_mae `0.106727`, as_primary `40`, as_primary_hit `0.65`, avg `0.030404`, median `0.046405`

### failed_bounce_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.3333`, path_mae `0.014287`, as_primary `0`, as_primary_hit `None`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, direction_hit `0.3667`, path_mae `0.019317`, as_primary `0`, as_primary_hit `None`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, direction_hit `0.4`, path_mae `0.037484`, as_primary `0`, as_primary_hit `None`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, direction_hit `0.3167`, path_mae `0.08753`, as_primary `0`, as_primary_hit `None`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, direction_hit `0.35`, path_mae `0.106757`, as_primary `0`, as_primary_hit `None`, avg `0.030404`, median `0.046405`

### analog_average_path
- sample_size: `60`
- 3d: sample `60`, direction_hit `0.6667`, path_mae `0.013299`, as_primary `20`, as_primary_hit `0.75`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, direction_hit `0.6333`, path_mae `0.016703`, as_primary `20`, as_primary_hit `0.65`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, direction_hit `0.6`, path_mae `0.026561`, as_primary `20`, as_primary_hit `0.6`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, direction_hit `0.6833`, path_mae `0.04443`, as_primary `20`, as_primary_hit `0.65`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, direction_hit `0.65`, path_mae `0.073605`, as_primary `20`, as_primary_hit `0.65`, avg `0.030404`, median `0.046405`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.011622`, avg `0.008567`, median `0.010408`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.85`, primary_mae `0.020916`, avg `0.006005`, median `0.010001`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.8`, primary_mae `0.030611`, avg `0.011234`, median `0.011814`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.85`, primary_mae `0.051854`, avg `0.018705`, median `0.013042`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.75`, primary_mae `0.07441`, avg `0.036803`, median `0.021487`

### STRONG_EDGE
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.4`, primary_mae `0.018409`, avg `0.003858`, median `0.006103`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.275`, primary_mae `0.022728`, avg `0.005176`, median `0.004667`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.325`, primary_mae `0.037781`, avg `0.005529`, median `0.006608`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.067146`, avg `0.010064`, median `0.020956`
- 60d: sample `40`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.103182`, avg `0.027204`, median `0.049838`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.016146`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.022124`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4833`, primary_mae `0.035391`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.062049`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.093592`, avg `0.030404`, median `0.046405`

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

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.016146, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.022124, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.035391, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.062049, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.093592, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6667, 'secondary_hit_rate': 0.6667, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4833, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.013299, 'direction_hit_rate': 0.6667}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.016933, 'direction_hit_rate': 0.6667}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6667, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.016146, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6333, 'secondary_hit_rate': 0.6333, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4667, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.016703, 'direction_hit_rate': 0.6333}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.027664, 'direction_hit_rate': 0.6333}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.022124, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4833, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.026561, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.044642, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.035391, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6833, 'secondary_hit_rate': 0.6833, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.04443, 'direction_hit_rate': 0.6833}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.08753, 'direction_hit_rate': 0.3167}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.062049, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 60, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 60, 'path_mean_absolute_error': 0.073605, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 60, 'path_mean_absolute_error': 0.106757, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.093592, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `6`
- 3d: sample `6`, primary_hit `0.6667`, primary_closer `0.3333`, primary_mae `0.02254`, avg `0.000538`, median `0.005338`
- 5d: sample `6`, primary_hit `0.6667`, primary_closer `0.0`, primary_mae `0.027879`, avg `0.001449`, median `0.007128`
- 10d: sample `6`, primary_hit `0.6667`, primary_closer `0.5`, primary_mae `0.028479`, avg `0.006454`, median `0.011735`
- 20d: sample `6`, primary_hit `0.6667`, primary_closer `0.1667`, primary_mae `0.051763`, avg `0.019467`, median `0.023697`
- 60d: sample `6`, primary_hit `0.5`, primary_closer `0.3333`, primary_mae `0.079062`, avg `0.017417`, median `0.007661`

### top_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.028879`, avg `-0.005801`, median `-0.004351`
- 5d: sample `12`, primary_hit `0.5`, primary_closer `0.0`, primary_mae `0.030494`, avg `-0.001166`, median `0.000744`
- 10d: sample `12`, primary_hit `0.6667`, primary_closer `0.3333`, primary_mae `0.030739`, avg `0.004194`, median `0.007439`
- 20d: sample `12`, primary_hit `0.75`, primary_closer `0.0833`, primary_mae `0.060059`, avg `0.011171`, median `0.023697`
- 60d: sample `12`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.093795`, avg `0.002683`, median `-0.012625`

### bottom_20
- sample_size: `12`
- 3d: sample `12`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.028879`, avg `-0.005801`, median `-0.004351`
- 5d: sample `12`, primary_hit `0.5`, primary_closer `0.0`, primary_mae `0.030494`, avg `-0.001166`, median `0.000744`
- 10d: sample `12`, primary_hit `0.6667`, primary_closer `0.3333`, primary_mae `0.030739`, avg `0.004194`, median `0.007439`
- 20d: sample `12`, primary_hit `0.75`, primary_closer `0.0833`, primary_mae `0.060059`, avg `0.011171`, median `0.023697`
- 60d: sample `12`, primary_hit `0.4167`, primary_closer `0.25`, primary_mae `0.093795`, avg `0.002683`, median `-0.012625`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.016146`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.022124`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4833`, primary_mae `0.035391`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.062049`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.093592`, avg `0.030404`, median `0.046405`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.016146`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.022124`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4833`, primary_mae `0.035391`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.062049`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.093592`, avg `0.030404`, median `0.046405`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.35`, primary_mae `0.02342`, avg `0.000364`, median `0.004081`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.02622`, avg `0.005321`, median `0.003509`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.35`, primary_mae `0.030458`, avg `0.007504`, median `0.007439`
- 20d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.053272`, avg `0.020502`, median `0.023697`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.077061`, avg `0.02044`, median `0.021323`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.65`, primary_mae `0.011622`, avg `0.008567`, median `0.010408`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.85`, primary_mae `0.020916`, avg `0.006005`, median `0.010001`
- 10d: sample `20`, primary_hit `0.6`, primary_closer `0.8`, primary_mae `0.030611`, avg `0.011234`, median `0.011814`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.85`, primary_mae `0.051854`, avg `0.018705`, median `0.013042`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.75`, primary_mae `0.07441`, avg `0.036803`, median `0.021487`

### options_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.016146`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.022124`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4833`, primary_mae `0.035391`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.062049`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.093592`, avg `0.030404`, median `0.046405`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4833`, primary_mae `0.016146`, avg `0.005427`, median `0.009289`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.4667`, primary_mae `0.022124`, avg `0.005452`, median `0.005323`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.4833`, primary_mae `0.035391`, avg `0.007431`, median `0.00986`
- 20d: sample `60`, primary_hit `0.6833`, primary_closer `0.45`, primary_mae `0.062049`, avg `0.012944`, median `0.01616`
- 60d: sample `60`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.093592`, avg `0.030404`, median `0.046405`

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
