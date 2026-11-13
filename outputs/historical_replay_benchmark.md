# Historical Replay Benchmark

Generated at: `2026-11-13T19:46:09.889561+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'medium', 'reasons': ['primary path is not closer than secondary path on most horizons'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.019536`
- secondary_mean_absolute_error: `0.017935`
- primary_error_advantage: `-0.001601`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.024904`
- secondary_mean_absolute_error: `0.021398`
- primary_error_advantage: `-0.003506`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.041943`
- secondary_mean_absolute_error: `0.035042`
- primary_error_advantage: `-0.006901`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.072954`
- secondary_mean_absolute_error: `0.074959`
- primary_error_advantage: `0.002005`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.114412`
- secondary_mean_absolute_error: `0.098152`
- primary_error_advantage: `-0.01626`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.017197`, as_primary `0`, as_primary_hit `None`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.021111`, as_primary `0`, as_primary_hit `None`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.031001`, as_primary `0`, as_primary_hit `None`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.046636`, as_primary `0`, as_primary_hit `None`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.081656`, as_primary `0`, as_primary_hit `None`, avg `0.01542`, median `0.003892`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.019477`, as_primary `60`, as_primary_hit `0.35`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.025501`, as_primary `60`, as_primary_hit `0.4833`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.044621`, as_primary `60`, as_primary_hit `0.35`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.071359`, as_primary `60`, as_primary_hit `0.5667`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.11459`, as_primary `60`, as_primary_hit `0.4333`, avg `0.01542`, median `0.003892`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017995`, as_primary `20`, as_primary_hit `0.75`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.020801`, as_primary `20`, as_primary_hit `0.75`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.032363`, as_primary `20`, as_primary_hit `0.6`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.4`, path_mae `0.076554`, as_primary `20`, as_primary_hit `0.7`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, direction_hit `0.4875`, path_mae `0.097974`, as_primary `20`, as_primary_hit `0.75`, avg `0.01542`, median `0.003892`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.016926`, as_primary `0`, as_primary_hit `None`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.019528`, as_primary `0`, as_primary_hit `None`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.026651`, as_primary `0`, as_primary_hit `None`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, direction_hit `0.6`, path_mae `0.044483`, as_primary `0`, as_primary_hit `None`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, direction_hit `0.5125`, path_mae `0.074255`, as_primary `0`, as_primary_hit `None`, avg `0.01542`, median `0.003892`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.019536`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.024904`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.041943`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.072954`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.114412`, avg `0.01542`, median `0.003892`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.4667`, primary_mae `0.019698`, avg `-0.003992`, median `-0.008299`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.02465`, avg `-0.001853`, median `-0.001154`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.037545`, avg `-0.000154`, median `-0.010434`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.061345`, avg `0.005416`, median `0.012625`
- 60d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.106852`, avg `-0.001121`, median `-0.021064`

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
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.019051`, avg `0.017121`, median `0.022255`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.025664`, avg `0.018977`, median `0.018988`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.055135`, avg `0.020096`, median `0.023013`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.107781`, avg `0.036616`, median `0.030573`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.137095`, avg `0.065044`, median `0.05308`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02465, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.037545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.061345, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.106852, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016926, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019477, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019051, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019528, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025501, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.02465, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026651, 'direction_hit_rate': 0.4125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044621, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.037545, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.044483, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076554, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5667, 'primary_closer_than_secondary_rate': 0.5333, 'primary_mean_absolute_error': 0.061345, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074255, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.11459, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4333, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.106852, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.5`, primary_mae `0.011764`, avg `-0.014139`, median `-0.01401`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.01694`, avg `-0.017817`, median `-0.02258`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.02649`, avg `-0.015109`, median `-0.013277`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.056624`, avg `0.004121`, median `-0.006947`
- 60d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.096561`, avg `0.010735`, median `0.003168`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.015649`, avg `-0.010207`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.016621`, avg `-0.011084`, median `-0.009462`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.027292`, avg `-0.007888`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.05436`, avg `0.008055`, median `0.005646`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.096448`, avg `0.00842`, median `0.003555`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.5625`, primary_mae `0.019732`, avg `0.01914`, median `0.033435`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.027776`, avg `0.020048`, median `0.02246`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.056291`, avg `0.019606`, median `0.018187`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.110106`, avg `0.040622`, median `0.026931`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.5625`, primary_mae `0.147497`, avg `0.070578`, median `0.05308`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.019536`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.024904`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.041943`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.072954`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.114412`, avg `0.01542`, median `0.003892`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.019536`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.024904`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.041943`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.072954`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.114412`, avg `0.01542`, median `0.003892`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.35`, primary_closer `0.4667`, primary_mae `0.019698`, avg `-0.003992`, median `-0.008299`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.35`, primary_mae `0.02465`, avg `-0.001853`, median `-0.001154`
- 10d: sample `60`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.037545`, avg `-0.000154`, median `-0.010434`
- 20d: sample `60`, primary_hit `0.5667`, primary_closer `0.5333`, primary_mae `0.061345`, avg `0.005416`, median `0.012625`
- 60d: sample `60`, primary_hit `0.4333`, primary_closer `0.4333`, primary_mae `0.106852`, avg `-0.001121`, median `-0.021064`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.019051`, avg `0.017121`, median `0.022255`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.025664`, avg `0.018977`, median `0.018988`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.55`, primary_mae `0.055135`, avg `0.020096`, median `0.023013`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.5`, primary_mae `0.107781`, avg `0.036616`, median `0.030573`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.137095`, avg `0.065044`, median `0.05308`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.019536`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.024904`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.041943`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.072954`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.114412`, avg `0.01542`, median `0.003892`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.019536`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.024904`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.041943`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.072954`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.114412`, avg `0.01542`, median `0.003892`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.019536`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.024904`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.041943`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.072954`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.114412`, avg `0.01542`, median `0.003892`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.325`, primary_closer `0.4625`, primary_mae `0.019536`, avg `0.001287`, median `-0.003238`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.024904`, avg `0.003354`, median `0.003016`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.4`, primary_mae `0.041943`, avg `0.004909`, median `-0.00812`
- 20d: sample `80`, primary_hit `0.5`, primary_closer `0.525`, primary_mae `0.072954`, avg `0.013216`, median `0.015284`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4625`, primary_mae `0.114412`, avg `0.01542`, median `0.003892`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
