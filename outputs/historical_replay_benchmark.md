# Historical Replay Benchmark

Generated at: `2026-09-01T16:43:31.549921+00:00`
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
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.018595`
- secondary_mean_absolute_error: `0.015412`
- primary_error_advantage: `-0.003183`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.022089`
- secondary_mean_absolute_error: `0.017115`
- primary_error_advantage: `-0.004974`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.028414`
- secondary_mean_absolute_error: `0.024543`
- primary_error_advantage: `-0.003871`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.275`
- primary_mean_absolute_error: `0.058698`
- secondary_mean_absolute_error: `0.034663`
- primary_error_advantage: `-0.024035`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2375`
- secondary_hit_rate: `0.7625`
- primary_vs_secondary_accuracy_spread: `-0.525`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.10026`
- secondary_mean_absolute_error: `0.059485`
- primary_error_advantage: `-0.040775`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.014333`, as_primary `0`, as_primary_hit `None`, avg `0.001637`, median `0.001274`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.01657`, as_primary `0`, as_primary_hit `None`, avg `0.000202`, median `0.001271`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.025323`, as_primary `0`, as_primary_hit `None`, avg `0.000605`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.032367`, as_primary `0`, as_primary_hit `None`, avg `0.012663`, median `0.022074`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.063509`, as_primary `0`, as_primary_hit `None`, avg `0.042067`, median `0.064505`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.015829`, as_primary `0`, as_primary_hit `None`, avg `0.001637`, median `0.001274`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.01942`, as_primary `0`, as_primary_hit `None`, avg `0.000202`, median `0.001271`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.032625`, as_primary `0`, as_primary_hit `None`, avg `0.000605`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.046509`, as_primary `0`, as_primary_hit `None`, avg `0.012663`, median `0.022074`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.069869`, as_primary `0`, as_primary_hit `None`, avg `0.042067`, median `0.064505`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.425`, path_mae `0.018595`, as_primary `80`, as_primary_hit `0.575`, avg `0.001637`, median `0.001274`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.022089`, as_primary `80`, as_primary_hit `0.55`, avg `0.000202`, median `0.001271`
- 10d: sample `80`, direction_hit `0.575`, path_mae `0.028414`, as_primary `80`, as_primary_hit `0.425`, avg `0.000605`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.3375`, path_mae `0.058698`, as_primary `80`, as_primary_hit `0.6625`, avg `0.012663`, median `0.022074`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.10026`, as_primary `80`, as_primary_hit `0.7625`, avg `0.042067`, median `0.064505`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.575`, path_mae `0.013793`, as_primary `0`, as_primary_hit `None`, avg `0.001637`, median `0.001274`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.016455`, as_primary `0`, as_primary_hit `None`, avg `0.000202`, median `0.001271`
- 10d: sample `80`, direction_hit `0.425`, path_mae `0.023721`, as_primary `0`, as_primary_hit `None`, avg `0.000605`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6625`, path_mae `0.032043`, as_primary `0`, as_primary_hit `None`, avg `0.012663`, median `0.022074`
- 60d: sample `80`, direction_hit `0.7625`, path_mae `0.060564`, as_primary `0`, as_primary_hit `None`, avg `0.042067`, median `0.064505`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.018595`, avg `0.001637`, median `0.001274`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022089`, avg `0.000202`, median `0.001271`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.028414`, avg `0.000605`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.275`, primary_mae `0.058698`, avg `0.012663`, median `0.022074`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.325`, primary_mae `0.10026`, avg `0.042067`, median `0.064505`

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
- 3d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.019234`, avg `0.006845`, median `0.009904`
- 5d: sample `40`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.024874`, avg `0.009003`, median `0.009356`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.035586`, avg `0.003437`, median `-0.010925`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.05889`, avg `0.011628`, median `0.023635`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.375`, primary_mae `0.109012`, avg `0.040347`, median `0.067172`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.017955`, avg `-0.00357`, median `-0.001735`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.019304`, avg `-0.0086`, median `-0.005451`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.021243`, avg `-0.002227`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.058506`, avg `0.013698`, median `0.020543`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.091508`, avg `0.043787`, median `0.060495`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.017955, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.019304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021243, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.058506, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.091508, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013793, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018595, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.017955, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016455, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022089, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.019304, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023721, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032625, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.475, 'primary_mean_absolute_error': 0.021243, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.275, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032043, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058698, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.325, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.058506, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_vs_secondary_accuracy_spread': -0.525, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060564, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.10026, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.275, 'primary_mean_absolute_error': 0.091508, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.023146`, avg `-0.007732`, median `-5e-05`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.024704`, avg `-0.012817`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.023126`, avg `0.001642`, median `0.0036`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.05434`, avg `0.020806`, median `0.030181`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.115716`, avg `0.064394`, median `0.076071`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.3125`, primary_mae `0.023237`, avg `-0.008081`, median `-0.005597`
- 5d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.022698`, avg `-0.014118`, median `-0.014548`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.020185`, avg `-0.000302`, median `-0.003556`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.053432`, avg `0.022655`, median `0.031427`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.109238`, avg `0.058086`, median `0.088952`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.016998`, avg `0.008793`, median `0.010782`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.021333`, avg `0.008888`, median `0.006922`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5`, primary_mae `0.030871`, avg `-0.008271`, median `-0.02037`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.085771`, avg `-0.001851`, median `0.004833`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.174964`, avg `0.003996`, median `0.046085`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.018595`, avg `0.001637`, median `0.001274`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022089`, avg `0.000202`, median `0.001271`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.028414`, avg `0.000605`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.275`, primary_mae `0.058698`, avg `0.012663`, median `0.022074`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.325`, primary_mae `0.10026`, avg `0.042067`, median `0.064505`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.018595`, avg `0.001637`, median `0.001274`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.022089`, avg `0.000202`, median `0.001271`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.4625`, primary_mae `0.028414`, avg `0.000605`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3375`, primary_closer `0.275`, primary_mae `0.058698`, avg `0.012663`, median `0.022074`
- 60d: sample `80`, primary_hit `0.2375`, primary_closer `0.325`, primary_mae `0.10026`, avg `0.042067`, median `0.064505`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.475`, primary_mae `0.017955`, avg `-0.00357`, median `-0.001735`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.019304`, avg `-0.0086`, median `-0.005451`
- 10d: sample `40`, primary_hit `0.6`, primary_closer `0.475`, primary_mae `0.021243`, avg `-0.002227`, median `-0.006514`
- 20d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.058506`, avg `0.013698`, median `0.020543`
- 60d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.091508`, avg `0.043787`, median `0.060495`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.2667`, primary_mae `0.021`, avg `0.002577`, median `0.003599`
- 5d: sample `60`, primary_hit `0.4333`, primary_closer `0.3667`, primary_mae `0.024696`, avg `0.002153`, median `0.002729`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.4333`, primary_mae `0.030188`, avg `0.002237`, median `-0.006514`
- 20d: sample `60`, primary_hit `0.3333`, primary_closer `0.25`, primary_mae `0.056104`, avg `0.014637`, median `0.024711`
- 60d: sample `60`, primary_hit `0.2167`, primary_closer `0.3333`, primary_mae `0.106969`, avg `0.044042`, median `0.067172`

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
