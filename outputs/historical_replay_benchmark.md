# Historical Replay Benchmark

Generated at: `2026-10-23T01:16:56.463949+00:00`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.023947`
- secondary_mean_absolute_error: `0.019916`
- primary_error_advantage: `-0.004031`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.030489`
- secondary_mean_absolute_error: `0.029538`
- primary_error_advantage: `-0.000951`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.049027`
- secondary_mean_absolute_error: `0.04447`
- primary_error_advantage: `-0.004557`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.065846`
- secondary_mean_absolute_error: `0.047793`
- primary_error_advantage: `-0.018053`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.175`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `-0.65`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.055374`
- secondary_mean_absolute_error: `0.05433`
- primary_error_advantage: `-0.001044`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.019728`, as_primary `0`, as_primary_hit `None`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025578`, as_primary `0`, as_primary_hit `None`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.03909`, as_primary `0`, as_primary_hit `None`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.042432`, as_primary `0`, as_primary_hit `None`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.049427`, as_primary `0`, as_primary_hit `None`, avg `0.065094`, median `0.06755`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.021681`, as_primary `0`, as_primary_hit `None`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.032422`, as_primary `0`, as_primary_hit `None`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.050974`, as_primary `0`, as_primary_hit `None`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.059262`, as_primary `0`, as_primary_hit `None`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.058526`, as_primary `0`, as_primary_hit `None`, avg `0.065094`, median `0.06755`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.023947`, as_primary `80`, as_primary_hit `0.575`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.030489`, as_primary `80`, as_primary_hit `0.55`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.049027`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, direction_hit `0.5125`, path_mae `0.065846`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.175`, path_mae `0.055374`, as_primary `80`, as_primary_hit `0.825`, avg `0.065094`, median `0.06755`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.019703`, as_primary `0`, as_primary_hit `None`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025719`, as_primary `0`, as_primary_hit `None`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.038027`, as_primary `0`, as_primary_hit `None`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, direction_hit `0.4875`, path_mae `0.040832`, as_primary `0`, as_primary_hit `None`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, direction_hit `0.825`, path_mae `0.048969`, as_primary `0`, as_primary_hit `None`, avg `0.065094`, median `0.06755`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.023947`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.030489`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.049027`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4`, primary_mae `0.065846`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.5`, primary_mae `0.055374`, avg `0.065094`, median `0.06755`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.02629`, avg `0.000537`, median `0.00282`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.4`, primary_mae `0.034526`, avg `-0.001025`, median `0.004858`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.053238`, avg `-0.001382`, median `0.004799`
- 20d: sample `40`, primary_hit `0.475`, primary_closer `0.275`, primary_mae `0.063736`, avg `-0.003785`, median `0.001969`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.072897`, avg `0.084275`, median `0.098198`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.021605`, avg `0.003996`, median `0.007812`
- 5d: sample `40`, primary_hit `0.425`, primary_closer `0.525`, primary_mae `0.026453`, avg `0.002259`, median `0.004099`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.525`, primary_mae `0.044816`, avg `-0.001868`, median `-0.008604`
- 20d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.067956`, avg `-0.009059`, median `-0.021284`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.6`, primary_mae `0.03785`, avg `0.045913`, median `0.056969`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021605, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026453, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.044816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.063736, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.03785, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019703, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023947, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.021605, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025578, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032422, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.026453, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038027, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050974, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.044816, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040832, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.065846, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.063736, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': -0.65, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048969, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058526, 'direction_hit_rate': 0.825}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 40, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.03785, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021526`, avg `0.004536`, median `0.008001`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.030994`, avg `0.003249`, median `0.00149`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.04866`, avg `0.002268`, median `0.004277`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.079038`, avg `-0.004281`, median `-0.002353`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.625`, primary_mae `0.034748`, avg `0.052016`, median `0.067424`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.024082`, avg `0.002366`, median `0.014943`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.030039`, avg `0.001756`, median `0.002693`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.050554`, avg `0.008064`, median `0.006413`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.076397`, avg `-0.011839`, median `-0.017639`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.6875`, primary_mae `0.030888`, avg `0.055818`, median `0.057796`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.032031`, avg `-0.002769`, median `-0.002328`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.041575`, avg `-0.006169`, median `0.004357`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.046277`, avg `0.006932`, median `0.008601`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.047476`, avg `0.001475`, median `-0.000982`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.061317`, avg `0.108476`, median `0.108183`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.023947`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.030489`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.049027`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4`, primary_mae `0.065846`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.5`, primary_mae `0.055374`, avg `0.065094`, median `0.06755`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.023947`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.030489`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.049027`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4`, primary_mae `0.065846`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.5`, primary_mae `0.055374`, avg `0.065094`, median `0.06755`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4167`, primary_closer `0.4167`, primary_mae `0.021443`, avg `0.003524`, median `0.007355`
- 5d: sample `60`, primary_hit `0.4667`, primary_closer `0.5`, primary_mae `0.026403`, avg `0.001442`, median `0.002693`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.4833`, primary_mae `0.048526`, avg `-0.006299`, median `-0.013087`
- 20d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.070364`, avg `-0.010876`, median `-0.014269`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.5333`, primary_mae `0.053336`, avg `0.049566`, median `0.05872`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.03146`, avg `-0.001506`, median `0.004933`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.042747`, avg `-0.001858`, median `0.00779`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.050529`, avg `0.012395`, median `0.010405`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.052293`, avg `0.00694`, median `0.001969`
- 60d: sample `20`, primary_hit `0.0`, primary_closer `0.4`, primary_mae `0.061486`, avg `0.111679`, median `0.108729`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.023947`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.030489`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.049027`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4`, primary_mae `0.065846`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.5`, primary_mae `0.055374`, avg `0.065094`, median `0.06755`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.023947`, avg `0.002267`, median `0.007275`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.030489`, avg `0.000617`, median `0.004543`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.4375`, primary_mae `0.049027`, avg `-0.001625`, median `0.000938`
- 20d: sample `80`, primary_hit `0.5125`, primary_closer `0.4`, primary_mae `0.065846`, avg `-0.006422`, median `-0.002679`
- 60d: sample `80`, primary_hit `0.175`, primary_closer `0.5`, primary_mae `0.055374`, avg `0.065094`, median `0.06755`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
