# Historical Replay Benchmark

Generated at: `2026-08-28T15:41:56.542113+00:00`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.017726`
- secondary_mean_absolute_error: `0.015877`
- primary_error_advantage: `-0.001849`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.02123`
- secondary_mean_absolute_error: `0.019091`
- primary_error_advantage: `-0.002139`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.032341`
- secondary_mean_absolute_error: `0.025649`
- primary_error_advantage: `-0.006692`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.054184`
- secondary_mean_absolute_error: `0.038951`
- primary_error_advantage: `-0.015233`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.070312`
- secondary_mean_absolute_error: `0.060482`
- primary_error_advantage: `-0.00983`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.425`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015379`, as_primary `0`, as_primary_hit `None`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.01928`, as_primary `0`, as_primary_hit `None`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.024354`, as_primary `0`, as_primary_hit `None`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.032203`, as_primary `0`, as_primary_hit `None`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.053641`, as_primary `0`, as_primary_hit `None`, avg `0.033174`, median `0.03883`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.017772`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.021261`, as_primary `60`, as_primary_hit `0.5333`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.032927`, as_primary `60`, as_primary_hit `0.5833`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.046968`, as_primary `60`, as_primary_hit `0.7`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.064384`, as_primary `60`, as_primary_hit `0.6833`, avg `0.033174`, median `0.03883`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.020712`, as_primary `20`, as_primary_hit `0.4`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, direction_hit `0.4875`, path_mae `0.024075`, as_primary `20`, as_primary_hit `0.45`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.032072`, as_primary `20`, as_primary_hit `0.3`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.057108`, as_primary `20`, as_primary_hit `0.6`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.079973`, as_primary `20`, as_primary_hit `0.65`, avg `0.033174`, median `0.03883`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.015362`, as_primary `0`, as_primary_hit `None`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, direction_hit `0.5125`, path_mae `0.019002`, as_primary `0`, as_primary_hit `None`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.023336`, as_primary `0`, as_primary_hit `None`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031487`, as_primary `0`, as_primary_hit `None`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.052939`, as_primary `0`, as_primary_hit `None`, avg `0.033174`, median `0.03883`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.017726`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.02123`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.032341`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.054184`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.070312`, avg `0.033174`, median `0.03883`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.007196`, avg `-0.001995`, median `-0.001535`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.55`, primary_mae `0.010158`, avg `-0.006662`, median `-0.007934`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.018855`, avg `-0.00812`, median `-0.00951`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.25`, primary_mae `0.066748`, avg `-0.006683`, median `0.006712`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.0764`, avg `0.018905`, median `0.032753`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4667`, primary_mae `0.021237`, avg `-0.002035`, median `0.001691`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.4333`, primary_mae `0.02492`, avg `-0.000496`, median `0.002189`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.3667`, primary_mae `0.036837`, avg `0.007136`, median `0.011033`
- 20d: sample `60`, primary_hit `0.7`, primary_closer `0.3667`, primary_mae `0.049996`, avg `0.015239`, median `0.017028`
- 60d: sample `60`, primary_hit `0.6833`, primary_closer `0.4333`, primary_mae `0.068282`, avg `0.03793`, median `0.047922`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.007196, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.010158, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.018855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.049996, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.068282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015362, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020712, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.007196, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019002, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024075, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.010158, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023336, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032927, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.018855, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031487, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057108, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.049996, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052939, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.079973, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6833, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.068282, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018377`, avg `-0.004471`, median `-0.000127`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.022873`, avg `-0.006804`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.021742`, avg `0.011181`, median `0.020076`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.030847`, avg `0.022572`, median `0.027848`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.068733`, avg `0.034462`, median `0.037982`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.018283`, avg `-0.001001`, median `-0.000127`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.019217`, avg `-0.001681`, median `-0.004713`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.02737`, avg `0.008208`, median `0.013417`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.75`, primary_mae `0.036236`, avg `0.020432`, median `0.027848`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.064692`, avg `0.0388`, median `0.062395`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.00742`, avg `-0.000434`, median `-0.000413`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.010476`, avg `-0.006894`, median `-0.007934`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.019218`, avg `-0.008567`, median `-0.011375`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.070777`, avg `-0.003924`, median `0.009266`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.086316`, avg `0.033005`, median `0.045303`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.017726`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.02123`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.032341`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.054184`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.070312`, avg `0.033174`, median `0.03883`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.017726`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.02123`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.032341`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.054184`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.070312`, avg `0.033174`, median `0.03883`

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
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.016917`, avg `-0.00045`, median `0.000684`
- 5d: sample `60`, primary_hit `0.55`, primary_closer `0.4667`, primary_mae `0.020564`, avg `-0.001867`, median `0.000552`
- 10d: sample `60`, primary_hit `0.6833`, primary_closer `0.4833`, primary_mae `0.029297`, avg `0.006068`, median `0.008315`
- 20d: sample `60`, primary_hit `0.6333`, primary_closer `0.35`, primary_mae `0.05574`, avg `0.012329`, median `0.017157`
- 60d: sample `60`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.073917`, avg `0.042263`, median `0.05856`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.017726`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.02123`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.032341`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.054184`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.070312`, avg `0.033174`, median `0.03883`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4875`, primary_mae `0.017726`, avg `-0.002025`, median `-5.7e-05`
- 5d: sample `80`, primary_hit `0.5375`, primary_closer `0.4625`, primary_mae `0.02123`, avg `-0.002038`, median `0.000482`
- 10d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.032341`, avg `0.003322`, median `0.001017`
- 20d: sample `80`, primary_hit `0.625`, primary_closer `0.3375`, primary_mae `0.054184`, avg `0.009759`, median `0.015083`
- 60d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.070312`, avg `0.033174`, median `0.03883`

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
