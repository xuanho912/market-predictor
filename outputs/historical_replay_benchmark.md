# Historical Replay Benchmark

Generated at: `2026-09-25T01:13:18.235480+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.017868`
- secondary_mean_absolute_error: `0.016442`
- primary_error_advantage: `-0.001426`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.019658`
- secondary_mean_absolute_error: `0.020449`
- primary_error_advantage: `0.000791`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.022045`
- secondary_mean_absolute_error: `0.026161`
- primary_error_advantage: `0.004116`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.049158`
- secondary_mean_absolute_error: `0.048595`
- primary_error_advantage: `-0.000563`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.050602`
- secondary_mean_absolute_error: `0.043799`
- primary_error_advantage: `-0.006803`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015512`, as_primary `0`, as_primary_hit `None`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.019104`, as_primary `0`, as_primary_hit `None`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.022758`, as_primary `0`, as_primary_hit `None`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.034212`, as_primary `0`, as_primary_hit `None`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.040105`, as_primary `0`, as_primary_hit `None`, avg `0.088093`, median `0.103255`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.016459`, as_primary `20`, as_primary_hit `0.65`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.020378`, as_primary `20`, as_primary_hit `0.65`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.026241`, as_primary `20`, as_primary_hit `0.75`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.047835`, as_primary `20`, as_primary_hit `0.8`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.044239`, as_primary `20`, as_primary_hit `1.0`, avg `0.088093`, median `0.103255`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5375`, path_mae `0.017851`, as_primary `60`, as_primary_hit `0.4`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.525`, path_mae `0.019728`, as_primary `60`, as_primary_hit `0.4167`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.021965`, as_primary `60`, as_primary_hit `0.6`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.049917`, as_primary `60`, as_primary_hit `0.6833`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, direction_hit `0.0875`, path_mae `0.050161`, as_primary `60`, as_primary_hit `0.8833`, avg `0.088093`, median `0.103255`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4625`, path_mae `0.015278`, as_primary `0`, as_primary_hit `None`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, direction_hit `0.475`, path_mae `0.01741`, as_primary `0`, as_primary_hit `None`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.020971`, as_primary `0`, as_primary_hit `None`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.032076`, as_primary `0`, as_primary_hit `None`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, direction_hit `0.9125`, path_mae `0.040701`, as_primary `0`, as_primary_hit `None`, avg `0.088093`, median `0.103255`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.017868`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.019658`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.022045`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.049158`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.050602`, avg `0.088093`, median `0.103255`

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
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.020284`, avg `-0.006919`, median `-0.010089`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.02157`, avg `-0.004012`, median `-0.005714`
- 10d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.033659`, avg `0.001084`, median `-0.00067`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.069108`, avg `-0.004381`, median `0.003968`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.05599`, avg `0.094366`, median `0.114142`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5833`, primary_closer `0.4833`, primary_mae `0.017063`, avg `0.000334`, median `0.000822`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.5833`, primary_mae `0.01902`, avg `0.002394`, median `0.003101`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.55`, primary_mae `0.018174`, avg `0.007697`, median `0.008108`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.5167`, primary_mae `0.042507`, avg `0.031056`, median `0.030725`
- 60d: sample `60`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.048806`, avg `0.086003`, median `0.099675`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.017063, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5833, 'primary_mean_absolute_error': 0.01902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018174, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.042507, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.048806, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015278, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017851, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.017063, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01741, 'direction_hit_rate': 0.475}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020378, 'direction_hit_rate': 0.475}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.5833, 'primary_mean_absolute_error': 0.01902, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020971, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026241, 'direction_hit_rate': 0.6375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018174, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032076, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.049917, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.042507, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040105, 'direction_hit_rate': 0.9125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050161, 'direction_hit_rate': 0.0875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.048806, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.012832`, avg `0.005815`, median `0.008014`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.014792`, avg `0.006695`, median `0.008828`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.25`, primary_mae `0.01658`, avg `0.009347`, median `0.01205`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.045009`, avg `0.026788`, median `0.029102`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.009937`, avg `0.114868`, median `0.11635`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.3125`, primary_mae `0.01366`, avg `0.001739`, median `0.003357`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.016449`, avg `0.006766`, median `0.008828`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.4375`, primary_mae `0.019817`, avg `0.010293`, median `0.016702`
- 20d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.041111`, avg `0.031248`, median `0.029448`
- 60d: sample `16`, primary_hit `1.0`, primary_closer `0.4375`, primary_mae `0.027217`, avg `0.099981`, median `0.111461`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.020214`, avg `-0.006481`, median `-0.010089`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.25`, primary_mae `0.024926`, avg `0.001651`, median `-0.001427`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.038705`, avg `0.007091`, median `0.012828`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.07497`, avg `0.00114`, median `0.030078`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.375`, primary_mae `0.043752`, avg `0.107566`, median `0.114142`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.017868`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.019658`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.022045`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.049158`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.050602`, avg `0.088093`, median `0.103255`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.017868`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.019658`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.022045`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.049158`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.050602`, avg `0.088093`, median `0.103255`

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
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.017868`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.019658`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.022045`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.049158`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.050602`, avg `0.088093`, median `0.103255`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.017868`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.019658`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.022045`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.049158`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.050602`, avg `0.088093`, median `0.103255`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4625`, primary_mae `0.017868`, avg `-0.001479`, median `-0.001409`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.5375`, primary_mae `0.019658`, avg `0.000793`, median `-0.00179`
- 10d: sample `80`, primary_hit `0.4875`, primary_closer `0.55`, primary_mae `0.022045`, avg `0.006044`, median `0.005261`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.5125`, primary_mae `0.049158`, avg `0.022197`, median `0.028383`
- 60d: sample `80`, primary_hit `0.3375`, primary_closer `0.4375`, primary_mae `0.050602`, avg `0.088093`, median `0.103255`

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
