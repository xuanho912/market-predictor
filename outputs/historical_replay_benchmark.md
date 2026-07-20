# Historical Replay Benchmark

Generated at: `2026-07-20T22:35:34.808377+00:00`
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
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.01627`
- secondary_mean_absolute_error: `0.017018`
- primary_error_advantage: `0.000748`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.022759`
- secondary_mean_absolute_error: `0.02272`
- primary_error_advantage: `-3.9e-05`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4375`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.036173`
- secondary_mean_absolute_error: `0.029073`
- primary_error_advantage: `-0.0071`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.074079`
- secondary_mean_absolute_error: `0.056037`
- primary_error_advantage: `-0.018042`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.112235`
- secondary_mean_absolute_error: `0.080777`
- primary_error_advantage: `-0.031458`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014676`, as_primary `0`, as_primary_hit `None`, avg `-0.00049`, median `0.00113`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019424`, as_primary `0`, as_primary_hit `None`, avg `9.5e-05`, median `0.002614`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.026727`, as_primary `0`, as_primary_hit `None`, avg `0.001707`, median `-0.002035`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.03969`, as_primary `0`, as_primary_hit `None`, avg `0.015459`, median `0.023433`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.075133`, as_primary `0`, as_primary_hit `None`, avg `0.031672`, median `0.058364`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.016674`, as_primary `20`, as_primary_hit `0.4`, avg `-0.00049`, median `0.00113`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.022462`, as_primary `20`, as_primary_hit `0.4`, avg `9.5e-05`, median `0.002614`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.032074`, as_primary `20`, as_primary_hit `0.25`, avg `0.001707`, median `-0.002035`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.055935`, as_primary `20`, as_primary_hit `0.6`, avg `0.015459`, median `0.023433`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.082744`, as_primary `20`, as_primary_hit `0.65`, avg `0.031672`, median `0.058364`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.017052`, as_primary `60`, as_primary_hit `0.6667`, avg `-0.00049`, median `0.00113`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.024403`, as_primary `60`, as_primary_hit `0.6`, avg `9.5e-05`, median `0.002614`
- 10d: sample `80`, direction_hit `0.525`, path_mae `0.03468`, as_primary `60`, as_primary_hit `0.55`, avg `0.001707`, median `-0.002035`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.078104`, as_primary `60`, as_primary_hit `0.65`, avg `0.015459`, median `0.023433`
- 60d: sample `80`, direction_hit `0.3625`, path_mae `0.114658`, as_primary `60`, as_primary_hit `0.6333`, avg `0.031672`, median `0.058364`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.014669`, as_primary `0`, as_primary_hit `None`, avg `-0.00049`, median `0.00113`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019473`, as_primary `0`, as_primary_hit `None`, avg `9.5e-05`, median `0.002614`
- 10d: sample `80`, direction_hit `0.475`, path_mae `0.026408`, as_primary `0`, as_primary_hit `None`, avg `0.001707`, median `-0.002035`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.040406`, as_primary `0`, as_primary_hit `None`, avg `0.015459`, median `0.023433`
- 60d: sample `80`, direction_hit `0.6375`, path_mae `0.075252`, as_primary `0`, as_primary_hit `None`, avg `0.031672`, median `0.058364`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3167`, primary_closer `0.5833`, primary_mae `0.014053`, avg `-0.001269`, median `0.001065`
- 5d: sample `60`, primary_hit `0.4167`, primary_closer `0.4667`, primary_mae `0.020544`, avg `-0.002612`, median `0.000725`
- 10d: sample `60`, primary_hit `0.4333`, primary_closer `0.4667`, primary_mae `0.031195`, avg `-0.002394`, median `-0.007304`
- 20d: sample `60`, primary_hit `0.4667`, primary_closer `0.4167`, primary_mae `0.07326`, avg `0.011049`, median `0.020147`
- 60d: sample `60`, primary_hit `0.4833`, primary_closer `0.4667`, primary_mae `0.11152`, avg `0.026788`, median `0.050131`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022922`, avg `0.001845`, median `0.004566`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.029404`, avg `0.008217`, median `0.013056`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.051107`, avg `0.01401`, median `0.025214`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.076535`, avg `0.02869`, median `0.043649`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.114382`, avg `0.046322`, median `0.069075`

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
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.6`, primary_mae `0.010549`, avg `-0.00042`, median `0.001272`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.016641`, avg `-0.002979`, median `0.000725`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.023924`, avg `-0.006234`, median `-0.007304`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.067737`, avg `0.00076`, median `0.003123`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.059409`, avg `0.012163`, median `0.014967`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.5333`, primary_mae `0.018178`, avg `-0.000514`, median `0.001056`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.45`, primary_mae `0.024798`, avg `0.00112`, median `0.003601`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.3833`, primary_mae `0.040256`, avg `0.004354`, median `-0.000315`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.3833`, primary_mae `0.076193`, avg `0.020359`, median `0.032431`
- 60d: sample `60`, primary_hit `0.4167`, primary_closer `0.4`, primary_mae `0.129844`, avg `0.038174`, median `0.071421`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.010549, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016641, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.023924, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.067737, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.059409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014669, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017052, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.010549, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019424, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024403, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.016641, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026408, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03468, 'direction_hit_rate': 0.525}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.023924, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03969, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078104, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.067737, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075133, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.114658, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.059409, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.009527`, avg `0.002378`, median `0.001417`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.011951`, avg `-0.001896`, median `-0.000876`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.021459`, avg `-0.009546`, median `-0.01363`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.064968`, avg `0.002572`, median `0.008352`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.079082`, avg `0.038862`, median `0.058786`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.011377`, avg `-0.001247`, median `0.001086`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.01476`, avg `-0.00638`, median `-0.000876`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.022882`, avg `-0.006631`, median `-0.007304`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.067027`, avg `0.002068`, median `0.002755`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.058209`, avg `0.014269`, median `0.007843`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.021636`, avg `0.005659`, median `0.008855`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.030856`, avg `0.01032`, median `0.017979`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.054195`, avg `0.020027`, median `0.029659`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.086929`, avg `0.040362`, median `0.052213`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.11617`, avg `0.058974`, median `0.069075`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.01627`, avg `-0.00049`, median `0.00113`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.022759`, avg `9.5e-05`, median `0.002614`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.036173`, avg `0.001707`, median `-0.002035`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.074079`, avg `0.015459`, median `0.023433`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.112235`, avg `0.031672`, median `0.058364`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.01627`, avg `-0.00049`, median `0.00113`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.022759`, avg `9.5e-05`, median `0.002614`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.036173`, avg `0.001707`, median `-0.002035`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.074079`, avg `0.015459`, median `0.023433`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.112235`, avg `0.031672`, median `0.058364`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.625`, primary_mae `0.015744`, avg `-0.004837`, median `0.000684`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.020831`, avg `-0.008458`, median `-0.001935`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.024563`, avg `-0.005144`, median `-0.007304`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.060628`, avg `0.006351`, median `0.0123`
- 60d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.077476`, avg `0.02343`, median `0.03596`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.022922`, avg `0.001845`, median `0.004566`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.029404`, avg `0.008217`, median `0.013056`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.051107`, avg `0.01401`, median `0.025214`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.076535`, avg `0.02869`, median `0.043649`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.114382`, avg `0.046322`, median `0.069075`

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
- 3d: sample `80`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.01627`, avg `-0.00049`, median `0.00113`
- 5d: sample `80`, primary_hit `0.4`, primary_closer `0.4375`, primary_mae `0.022759`, avg `9.5e-05`, median `0.002614`
- 10d: sample `80`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.036173`, avg `0.001707`, median `-0.002035`
- 20d: sample `80`, primary_hit `0.4125`, primary_closer `0.375`, primary_mae `0.074079`, avg `0.015459`, median `0.023433`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.112235`, avg `0.031672`, median `0.058364`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
