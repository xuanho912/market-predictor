# Historical Replay Benchmark

Generated at: `2026-09-10T22:43:27.975402+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
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
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.021046`
- secondary_mean_absolute_error: `0.014985`
- primary_error_advantage: `-0.006061`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.02399`
- secondary_mean_absolute_error: `0.017277`
- primary_error_advantage: `-0.006713`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.032473`
- secondary_mean_absolute_error: `0.023337`
- primary_error_advantage: `-0.009136`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.064334`
- secondary_mean_absolute_error: `0.036187`
- primary_error_advantage: `-0.028147`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.101799`
- secondary_mean_absolute_error: `0.071843`
- primary_error_advantage: `-0.029956`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.015805`, as_primary `0`, as_primary_hit `None`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017782`, as_primary `0`, as_primary_hit `None`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.024497`, as_primary `0`, as_primary_hit `None`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.03689`, as_primary `0`, as_primary_hit `None`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.07795`, as_primary `0`, as_primary_hit `None`, avg `0.027297`, median `0.051506`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016318`, as_primary `0`, as_primary_hit `None`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.02053`, as_primary `0`, as_primary_hit `None`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.035341`, as_primary `0`, as_primary_hit `None`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.052587`, as_primary `0`, as_primary_hit `None`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.081747`, as_primary `0`, as_primary_hit `None`, avg `0.027297`, median `0.051506`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.021046`, as_primary `80`, as_primary_hit `0.5875`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.02399`, as_primary `80`, as_primary_hit `0.575`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.032473`, as_primary `80`, as_primary_hit `0.425`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.064334`, as_primary `80`, as_primary_hit `0.5625`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, direction_hit `0.375`, path_mae `0.101799`, as_primary `80`, as_primary_hit `0.625`, avg `0.027297`, median `0.051506`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.014985`, as_primary `0`, as_primary_hit `None`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.017277`, as_primary `0`, as_primary_hit `None`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.023337`, as_primary `0`, as_primary_hit `None`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.036187`, as_primary `0`, as_primary_hit `None`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, direction_hit `0.625`, path_mae `0.071843`, as_primary `0`, as_primary_hit `None`, avg `0.027297`, median `0.051506`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.021046`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.02399`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.032473`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.275`, primary_mae `0.064334`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.101799`, avg `0.027297`, median `0.051506`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.021046`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.02399`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.032473`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.275`, primary_mae `0.064334`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.101799`, avg `0.027297`, median `0.051506`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4125, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.021046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.02399, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.032473, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.064334, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.101799, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014985, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021046, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4125, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.021046, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017277, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02399, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.02399, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023337, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035341, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.032473, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036187, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064334, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.064334, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071843, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.101799, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.375, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.101799, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.027486`, avg `-0.001516`, median `0.004814`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.024237`, avg `-0.011121`, median `0.000647`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.017858`, avg `-0.014794`, median `-0.019121`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.056756`, avg `0.018164`, median `0.017863`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.091044`, avg `0.035099`, median `0.052814`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.026357`, avg `-0.002364`, median `0.003063`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.027113`, avg `-0.008712`, median `0.000647`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.018471`, avg `-0.006055`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.053955`, avg `0.018119`, median `0.024617`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.090294`, avg `0.037065`, median `0.052814`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.028097`, avg `0.003854`, median `0.007955`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.125`, primary_mae `0.040493`, avg `0.006702`, median `0.012415`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.1875`, primary_mae `0.058692`, avg `-0.004615`, median `-0.008235`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.1875`, primary_mae `0.103708`, avg `0.00495`, median `0.00706`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.204525`, avg `0.034023`, median `0.090548`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.021046`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.02399`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.032473`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.275`, primary_mae `0.064334`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.101799`, avg `0.027297`, median `0.051506`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.021046`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.02399`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.032473`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.275`, primary_mae `0.064334`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.101799`, avg `0.027297`, median `0.051506`

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
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.021046`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.02399`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.032473`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.275`, primary_mae `0.064334`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.101799`, avg `0.027297`, median `0.051506`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3`, primary_mae `0.021046`, avg `0.000354`, median `0.003063`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.3375`, primary_mae `0.02399`, avg `-0.002314`, median `0.001935`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.3625`, primary_mae `0.032473`, avg `-0.003483`, median `-0.006514`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.275`, primary_mae `0.064334`, avg `0.006527`, median `0.007005`
- 60d: sample `80`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.101799`, avg `0.027297`, median `0.051506`

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
