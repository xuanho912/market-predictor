# Historical Replay Benchmark

Generated at: `2026-06-16T13:42:06.834954+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.01407`
- secondary_mean_absolute_error: `0.013443`
- primary_error_advantage: `-0.000627`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.019804`
- secondary_mean_absolute_error: `0.01682`
- primary_error_advantage: `-0.002984`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.029607`
- secondary_mean_absolute_error: `0.027733`
- primary_error_advantage: `-0.001874`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.051032`
- secondary_mean_absolute_error: `0.051316`
- primary_error_advantage: `0.000284`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.07011`
- secondary_mean_absolute_error: `0.059481`
- primary_error_advantage: `-0.010629`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.01324`, as_primary `0`, as_primary_hit `None`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.016822`, as_primary `0`, as_primary_hit `None`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.022704`, as_primary `0`, as_primary_hit `None`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.033392`, as_primary `0`, as_primary_hit `None`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.056213`, as_primary `0`, as_primary_hit `None`, avg `0.024862`, median `0.031374`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.01407`, as_primary `80`, as_primary_hit `0.625`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.019804`, as_primary `80`, as_primary_hit `0.6375`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.029607`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.051032`, as_primary `80`, as_primary_hit `0.675`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.07011`, as_primary `80`, as_primary_hit `0.5875`, avg `0.024862`, median `0.031374`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.375`, path_mae `0.013642`, as_primary `0`, as_primary_hit `None`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.017145`, as_primary `0`, as_primary_hit `None`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.028443`, as_primary `0`, as_primary_hit `None`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.060346`, as_primary `0`, as_primary_hit `None`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.06887`, as_primary `0`, as_primary_hit `None`, avg `0.024862`, median `0.031374`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.625`, path_mae `0.012302`, as_primary `0`, as_primary_hit `None`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.015215`, as_primary `0`, as_primary_hit `None`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.021404`, as_primary `0`, as_primary_hit `None`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031828`, as_primary `0`, as_primary_hit `None`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.053635`, as_primary `0`, as_primary_hit `None`, avg `0.024862`, median `0.031374`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.01407`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.019804`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.029607`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.051032`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07011`, avg `0.024862`, median `0.031374`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.013601`, avg `0.006604`, median `0.005077`
- 5d: sample `40`, primary_hit `0.775`, primary_closer `0.425`, primary_mae `0.017279`, avg `0.010282`, median `0.010041`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.625`, primary_mae `0.026957`, avg `0.00767`, median `0.008571`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.675`, primary_mae `0.053235`, avg `0.001262`, median `0.01042`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.074362`, avg `0.006467`, median `-0.00576`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.014539`, avg `0.00189`, median `0.003745`
- 5d: sample `40`, primary_hit `0.5`, primary_closer `0.325`, primary_mae `0.022328`, avg `0.001257`, median `-0.000454`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.032257`, avg `0.005982`, median `0.005512`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.225`, primary_mae `0.048829`, avg `0.014404`, median `0.019428`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.065858`, avg `0.043257`, median `0.051612`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.026957, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.048829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.065858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012302, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01407, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.013601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015215, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019804, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017279, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021404, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029607, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.026957, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031828, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060346, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.675, 'primary_closer_than_secondary_rate': 0.225, 'primary_mean_absolute_error': 0.048829, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053635, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07011, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.065858, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.014963`, avg `-0.006356`, median `-0.005255`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019403`, avg `-0.007284`, median `-0.010372`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.01491`, avg `0.005714`, median `0.006918`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.0`, primary_mae `0.02524`, avg `0.022118`, median `0.027661`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.052983`, avg `0.029911`, median `0.037982`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015663`, avg `-0.003068`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.018223`, avg `-0.003972`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.015353`, avg `0.007518`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.026474`, avg `0.0228`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.056387`, avg `0.036473`, median `0.055714`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.015663`, avg `-0.003068`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.018223`, avg `-0.003972`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.015353`, avg `0.007518`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.026474`, avg `0.0228`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.056387`, avg `0.036473`, median `0.055714`

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
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.01407`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.019804`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.029607`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.051032`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07011`, avg `0.024862`, median `0.031374`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.01407`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.019804`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.029607`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.051032`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07011`, avg `0.024862`, median `0.031374`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.01407`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.019804`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.029607`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.051032`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07011`, avg `0.024862`, median `0.031374`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.01407`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.019804`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.029607`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.051032`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07011`, avg `0.024862`, median `0.031374`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.625`, primary_closer `0.425`, primary_mae `0.01407`, avg `0.004247`, median `0.004633`
- 5d: sample `80`, primary_hit `0.6375`, primary_closer `0.375`, primary_mae `0.019804`, avg `0.00577`, median `0.005601`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.4875`, primary_mae `0.029607`, avg `0.006826`, median `0.00719`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.051032`, avg `0.007833`, median `0.016418`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.4125`, primary_mae `0.07011`, avg `0.024862`, median `0.031374`

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
