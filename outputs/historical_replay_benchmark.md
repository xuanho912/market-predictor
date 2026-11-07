# Historical Replay Benchmark

Generated at: `2026-11-07T01:26:44.743229+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.019844`
- secondary_mean_absolute_error: `0.019289`
- primary_error_advantage: `-0.000555`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.024363`
- secondary_mean_absolute_error: `0.025446`
- primary_error_advantage: `0.001083`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `0.325`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.040566`
- secondary_mean_absolute_error: `0.044173`
- primary_error_advantage: `0.003607`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.3125`
- primary_vs_secondary_accuracy_spread: `0.375`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.067061`
- secondary_mean_absolute_error: `0.054675`
- primary_error_advantage: `-0.012386`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.039394`
- secondary_mean_absolute_error: `0.043195`
- primary_error_advantage: `0.003801`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.018677`, as_primary `0`, as_primary_hit `None`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.024957`, as_primary `0`, as_primary_hit `None`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.03951`, as_primary `0`, as_primary_hit `None`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.043732`, as_primary `0`, as_primary_hit `None`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.042457`, as_primary `0`, as_primary_hit `None`, avg `0.054809`, median `0.05838`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.019675`, as_primary `0`, as_primary_hit `None`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.028812`, as_primary `0`, as_primary_hit `None`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.055186`, as_primary `0`, as_primary_hit `None`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.073322`, as_primary `0`, as_primary_hit `None`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.053992`, as_primary `0`, as_primary_hit `None`, avg `0.054809`, median `0.05838`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.019844`, as_primary `80`, as_primary_hit `0.5`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.024363`, as_primary `80`, as_primary_hit `0.45`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.040566`, as_primary `80`, as_primary_hit `0.3375`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.067061`, as_primary `80`, as_primary_hit `0.3125`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.039394`, as_primary `80`, as_primary_hit `0.775`, avg `0.054809`, median `0.05838`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.019056`, as_primary `0`, as_primary_hit `None`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.022884`, as_primary `0`, as_primary_hit `None`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.037139`, as_primary `0`, as_primary_hit `None`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.042773`, as_primary `0`, as_primary_hit `None`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.039381`, as_primary `0`, as_primary_hit `None`, avg `0.054809`, median `0.05838`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019844`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.024363`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.5375`, primary_mae `0.040566`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3875`, primary_mae `0.067061`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5625`, primary_mae `0.039394`, avg `0.054809`, median `0.05838`

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
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.022442`, avg `0.003624`, median `0.012752`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.029509`, avg `0.010044`, median `0.006746`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.053459`, avg `0.009083`, median `0.005882`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.074501`, avg `-0.023442`, median `-0.041695`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.55`, primary_mae `0.030206`, avg `0.102265`, median `0.111958`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4833`, primary_mae `0.018978`, avg `-0.006017`, median `-0.004738`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.5167`, primary_mae `0.022647`, avg `-0.007133`, median `-0.014349`
- 10d: sample `60`, primary_hit `0.7167`, primary_closer `0.5667`, primary_mae `0.036269`, avg `-0.014152`, median `-0.020987`
- 20d: sample `60`, primary_hit `0.7`, primary_closer `0.4333`, primary_mae `0.064581`, avg `-0.026671`, median `-0.03079`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.5667`, primary_mae `0.042457`, avg `0.03899`, median `0.040264`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.018978, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.022647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.036269, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.064581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.030206, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018677, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019844, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.018978, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022884, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028812, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.022647, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3375, 'primary_vs_secondary_accuracy_spread': 0.325, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037139, 'direction_hit_rate': 0.3375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055186, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.5667, 'primary_mean_absolute_error': 0.036269, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.3125, 'primary_vs_secondary_accuracy_spread': 0.375, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042773, 'direction_hit_rate': 0.3125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.073322, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.064581, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039381, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053992, 'direction_hit_rate': 0.775}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.0, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.030206, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.019252`, avg `-0.003007`, median `-0.007814`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.027967`, avg `-0.005605`, median `-0.010462`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.044491`, avg `0.001768`, median `-0.020033`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.083367`, avg `-0.007427`, median `-0.02913`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.038558`, avg `0.052162`, median `0.050344`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.022181`, avg `0.002137`, median `0.010214`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.625`, primary_mae `0.029605`, avg `0.002433`, median `0.001372`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.049297`, avg `0.003207`, median `-0.008604`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.079881`, avg `-0.014896`, median `-0.02913`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.625`, primary_mae `0.032313`, avg `0.058334`, median `0.062627`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.024394`, avg `0.0005`, median `0.0103`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.031683`, avg `0.006606`, median `0.004312`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.050566`, avg `0.000407`, median `-0.012207`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.1875`, primary_mae `0.075332`, avg `-0.019408`, median `-0.041695`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.03419`, avg `0.09715`, median `0.10214`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019844`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.024363`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.5375`, primary_mae `0.040566`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3875`, primary_mae `0.067061`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5625`, primary_mae `0.039394`, avg `0.054809`, median `0.05838`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019844`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.024363`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.5375`, primary_mae `0.040566`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3875`, primary_mae `0.067061`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5625`, primary_mae `0.039394`, avg `0.054809`, median `0.05838`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.4833`, primary_mae `0.018978`, avg `-0.006017`, median `-0.004738`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.5167`, primary_mae `0.022647`, avg `-0.007133`, median `-0.014349`
- 10d: sample `60`, primary_hit `0.7167`, primary_closer `0.5667`, primary_mae `0.036269`, avg `-0.014152`, median `-0.020987`
- 20d: sample `60`, primary_hit `0.7`, primary_closer `0.4333`, primary_mae `0.064581`, avg `-0.026671`, median `-0.03079`
- 60d: sample `60`, primary_hit `0.3`, primary_closer `0.5667`, primary_mae `0.042457`, avg `0.03899`, median `0.040264`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.022442`, avg `0.003624`, median `0.012752`
- 5d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.029509`, avg `0.010044`, median `0.006746`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.053459`, avg `0.009083`, median `0.005882`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.074501`, avg `-0.023442`, median `-0.041695`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.55`, primary_mae `0.030206`, avg `0.102265`, median `0.111958`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019844`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.024363`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.5375`, primary_mae `0.040566`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3875`, primary_mae `0.067061`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5625`, primary_mae `0.039394`, avg `0.054809`, median `0.05838`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019844`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.024363`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.5375`, primary_mae `0.040566`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3875`, primary_mae `0.067061`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5625`, primary_mae `0.039394`, avg `0.054809`, median `0.05838`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.019844`, avg `-0.003607`, median `-0.000596`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.5125`, primary_mae `0.024363`, avg `-0.002839`, median `-0.007263`
- 10d: sample `80`, primary_hit `0.6625`, primary_closer `0.5375`, primary_mae `0.040566`, avg `-0.008343`, median `-0.018142`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.3875`, primary_mae `0.067061`, avg `-0.025864`, median `-0.032633`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.5625`, primary_mae `0.039394`, avg `0.054809`, median `0.05838`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
