# Historical Replay Benchmark

Generated at: `2026-08-14T03:32:20.098211+00:00`
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
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.01781`
- secondary_mean_absolute_error: `0.013333`
- primary_error_advantage: `-0.004477`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.028324`
- secondary_mean_absolute_error: `0.017298`
- primary_error_advantage: `-0.011026`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.03736`
- secondary_mean_absolute_error: `0.024568`
- primary_error_advantage: `-0.012792`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.068257`
- secondary_mean_absolute_error: `0.04046`
- primary_error_advantage: `-0.027797`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.25`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.086939`
- secondary_mean_absolute_error: `0.069854`
- primary_error_advantage: `-0.017085`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.275`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.014359`, as_primary `0`, as_primary_hit `None`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.020733`, as_primary `0`, as_primary_hit `None`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.026198`, as_primary `0`, as_primary_hit `None`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.043106`, as_primary `0`, as_primary_hit `None`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.067993`, as_primary `0`, as_primary_hit `None`, avg `0.023903`, median `0.045588`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.01781`, as_primary `80`, as_primary_hit `0.625`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.028324`, as_primary `80`, as_primary_hit `0.625`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.03736`, as_primary `80`, as_primary_hit `0.5875`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.068257`, as_primary `80`, as_primary_hit `0.7`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.086939`, as_primary `80`, as_primary_hit `0.6375`, avg `0.023903`, median `0.045588`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.014072`, as_primary `0`, as_primary_hit `None`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.019806`, as_primary `0`, as_primary_hit `None`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.035926`, as_primary `0`, as_primary_hit `None`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, direction_hit `0.3`, path_mae `0.079826`, as_primary `0`, as_primary_hit `None`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.095799`, as_primary `0`, as_primary_hit `None`, avg `0.023903`, median `0.045588`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.013333`, as_primary `0`, as_primary_hit `None`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.017298`, as_primary `0`, as_primary_hit `None`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.024568`, as_primary `0`, as_primary_hit `None`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, direction_hit `0.7`, path_mae `0.04046`, as_primary `0`, as_primary_hit `None`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.069854`, as_primary `0`, as_primary_hit `None`, avg `0.023903`, median `0.045588`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.01618`, avg `0.003011`, median `0.004555`
- 5d: sample `60`, primary_hit `0.65`, primary_closer `0.3167`, primary_mae `0.024114`, avg `0.006347`, median `0.005889`
- 10d: sample `60`, primary_hit `0.6`, primary_closer `0.3833`, primary_mae `0.030035`, avg `0.00606`, median `0.009079`
- 20d: sample `60`, primary_hit `0.7333`, primary_closer `0.3`, primary_mae `0.051547`, avg `0.011081`, median `0.019709`
- 60d: sample `60`, primary_hit `0.5833`, primary_closer `0.3833`, primary_mae `0.084796`, avg `0.014376`, median `0.044393`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.017817`, avg `0.003332`, median `0.004555`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.2833`, primary_mae `0.02691`, avg `0.004478`, median `0.005202`
- 10d: sample `60`, primary_hit `0.6167`, primary_closer `0.3833`, primary_mae `0.034298`, avg `0.007238`, median `0.01093`
- 20d: sample `60`, primary_hit `0.7167`, primary_closer `0.2667`, primary_mae `0.064643`, avg `0.015898`, median `0.015644`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.3667`, primary_mae `0.079274`, avg `0.02595`, median `0.028346`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.01779`, avg `0.007331`, median `0.013006`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.032566`, avg `0.007694`, median `0.00796`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.3`, primary_mae `0.046545`, avg `0.003808`, median `-0.001573`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.3`, primary_mae `0.079098`, avg `0.002815`, median `0.015768`
- 60d: sample `20`, primary_hit `0.75`, primary_closer `0.3`, primary_mae `0.109933`, avg `0.017761`, median `0.059654`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01779, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.02691, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.034298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.064643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.079274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013333, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01781, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.01779, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017298, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028324, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6333, 'primary_closer_than_secondary_rate': 0.2833, 'primary_mean_absolute_error': 0.02691, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024568, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03736, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6167, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.034298, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04046, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079826, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7167, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.064643, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067993, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.095799, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.079274, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.023807`, avg `-0.000728`, median `-0.000883`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.125`, primary_mae `0.028453`, avg `0.000875`, median `0.004667`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.027328`, avg `0.007606`, median `0.011059`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.125`, primary_mae `0.05439`, avg `0.01684`, median `0.015956`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.090144`, avg `0.006335`, median `-0.025539`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024354`, avg `-0.000393`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.026563`, avg `0.005531`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.02696`, avg `0.01176`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050723`, avg `0.023687`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.07842`, avg `0.018535`, median `0.012785`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.024354`, avg `-0.000393`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.026563`, avg `0.005531`, median `0.004667`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.02696`, avg `0.01176`, median `0.011059`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.050723`, avg `0.023687`, median `0.026122`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.07842`, avg `0.018535`, median `0.012785`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.01781`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.2875`, primary_mae `0.028324`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.03736`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.275`, primary_mae `0.068257`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.086939`, avg `0.023903`, median `0.045588`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.01781`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.2875`, primary_mae `0.028324`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.03736`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.275`, primary_mae `0.068257`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.086939`, avg `0.023903`, median `0.045588`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.425`, primary_mae `0.015376`, avg `0.000851`, median `0.001025`
- 5d: sample `40`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.019888`, avg `0.005673`, median `0.005885`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.02178`, avg `0.007186`, median `0.011059`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.3`, primary_mae `0.037772`, avg `0.015213`, median `0.020543`
- 60d: sample `40`, primary_hit `0.5`, primary_closer `0.425`, primary_mae `0.072228`, avg `0.012684`, median `0.007512`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.25`, primary_mae `0.022698`, avg `0.008292`, median `0.010408`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.2`, primary_mae `0.040953`, avg `0.002088`, median `0.001259`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.059336`, avg `0.007342`, median `0.009041`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.2`, primary_mae `0.118384`, avg `0.017266`, median `0.01074`
- 60d: sample `20`, primary_hit `0.8`, primary_closer `0.25`, primary_mae `0.093365`, avg `0.052484`, median `0.06367`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.01781`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.2875`, primary_mae `0.028324`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.03736`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.275`, primary_mae `0.068257`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.086939`, avg `0.023903`, median `0.045588`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.3875`, primary_mae `0.01781`, avg `0.004332`, median `0.005611`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.2875`, primary_mae `0.028324`, avg `0.005282`, median `0.005323`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.3625`, primary_mae `0.03736`, avg `0.00638`, median `0.009079`
- 20d: sample `80`, primary_hit `0.7`, primary_closer `0.275`, primary_mae `0.068257`, avg `0.012627`, median `0.015644`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.35`, primary_mae `0.086939`, avg `0.023903`, median `0.045588`

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
