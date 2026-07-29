# Historical Replay Benchmark

Generated at: `2026-07-29T14:34:06.062087+00:00`
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
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.024282`
- secondary_mean_absolute_error: `0.016793`
- primary_error_advantage: `-0.007489`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.029296`
- secondary_mean_absolute_error: `0.020957`
- primary_error_advantage: `-0.008339`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.034064`
- secondary_mean_absolute_error: `0.032863`
- primary_error_advantage: `-0.001201`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.071204`
- secondary_mean_absolute_error: `0.048671`
- primary_error_advantage: `-0.022533`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.080903`
- secondary_mean_absolute_error: `0.0701`
- primary_error_advantage: `-0.010803`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016154`, as_primary `0`, as_primary_hit `None`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020546`, as_primary `0`, as_primary_hit `None`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.031234`, as_primary `0`, as_primary_hit `None`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.041032`, as_primary `0`, as_primary_hit `None`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.065625`, as_primary `0`, as_primary_hit `None`, avg `0.043363`, median `0.058049`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.018295`, as_primary `0`, as_primary_hit `None`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.024651`, as_primary `0`, as_primary_hit `None`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.038491`, as_primary `0`, as_primary_hit `None`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.058071`, as_primary `0`, as_primary_hit `None`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.079543`, as_primary `0`, as_primary_hit `None`, avg `0.043363`, median `0.058049`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.024282`, as_primary `80`, as_primary_hit `0.5875`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.029296`, as_primary `80`, as_primary_hit `0.6125`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.034064`, as_primary `80`, as_primary_hit `0.45`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.071204`, as_primary `80`, as_primary_hit `0.6375`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, direction_hit `0.325`, path_mae `0.080903`, as_primary `80`, as_primary_hit `0.675`, avg `0.043363`, median `0.058049`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016466`, as_primary `0`, as_primary_hit `None`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020318`, as_primary `0`, as_primary_hit `None`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.029566`, as_primary `0`, as_primary_hit `None`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.041068`, as_primary `0`, as_primary_hit `None`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, direction_hit `0.675`, path_mae `0.061587`, as_primary `0`, as_primary_hit `None`, avg `0.043363`, median `0.058049`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.024282`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.029296`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.034064`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.071204`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.080903`, avg `0.043363`, median `0.058049`

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
- 3d: sample `40`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.027489`, avg `0.004204`, median `0.005464`
- 5d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.034575`, avg `0.008894`, median `0.012138`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.047466`, avg `0.006634`, median `0.01026`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.084221`, avg `0.035549`, median `0.057309`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.225`, primary_mae `0.093683`, avg `0.066002`, median `0.092995`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.021074`, avg `-0.003731`, median `0.000952`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.024018`, avg `-0.006845`, median `0.000888`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.020663`, avg `-0.005985`, median `-0.006567`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.058188`, avg `0.007725`, median `0.007005`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.068122`, avg `0.020723`, median `0.033739`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.021074, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.024018, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.020663, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.058188, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.068122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016154, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024282, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.021074, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020318, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029296, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.024018, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029566, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.038491, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.625, 'primary_closer_than_secondary_rate': 0.625, 'primary_mean_absolute_error': 0.020663, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041032, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071204, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.058188, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061587, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080903, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.525, 'primary_mean_absolute_error': 0.068122, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.125`, primary_mae `0.040912`, avg `0.005922`, median `0.011798`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.038407`, avg `-0.001516`, median `0.001655`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.022799`, avg `-0.000459`, median `-0.000811`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.06712`, avg `0.035935`, median `0.047524`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.103058`, avg `0.055966`, median `0.103033`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.036471`, avg `0.000214`, median `0.004814`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.035907`, avg `-0.005072`, median `0.003026`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.017236`, avg `-0.001884`, median `-0.005954`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.052341`, avg `0.021156`, median `0.011854`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.084582`, avg `0.04184`, median `0.04846`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.033574`, avg `0.002053`, median `0.003377`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.045423`, avg `0.005489`, median `0.007767`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.048704`, avg `-0.001443`, median `-0.022754`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.091981`, avg `0.022178`, median `0.028021`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.107089`, avg `0.051103`, median `0.046249`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.024282`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.029296`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.034064`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.071204`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.080903`, avg `0.043363`, median `0.058049`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.024282`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.029296`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.034064`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.071204`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.080903`, avg `0.043363`, median `0.058049`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.021074`, avg `-0.003731`, median `0.000952`
- 5d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.024018`, avg `-0.006845`, median `0.000888`
- 10d: sample `40`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.020663`, avg `-0.005985`, median `-0.006567`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.058188`, avg `0.007725`, median `0.007005`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.525`, primary_mae `0.068122`, avg `0.020723`, median `0.033739`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.027489`, avg `0.004204`, median `0.005464`
- 5d: sample `40`, primary_hit `0.325`, primary_closer `0.3`, primary_mae `0.034575`, avg `0.008894`, median `0.012138`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.047466`, avg `0.006634`, median `0.01026`
- 20d: sample `40`, primary_hit `0.275`, primary_closer `0.275`, primary_mae `0.084221`, avg `0.035549`, median `0.057309`
- 60d: sample `40`, primary_hit `0.175`, primary_closer `0.225`, primary_mae `0.093683`, avg `0.066002`, median `0.092995`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.024282`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.029296`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.034064`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.071204`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.080903`, avg `0.043363`, median `0.058049`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3125`, primary_mae `0.024282`, avg `0.000236`, median `0.001272`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.3625`, primary_mae `0.029296`, avg `0.001025`, median `0.002747`
- 10d: sample `80`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.034064`, avg `0.000325`, median `-0.005954`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.3625`, primary_mae `0.071204`, avg `0.021637`, median `0.021599`
- 60d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.080903`, avg `0.043363`, median `0.058049`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
