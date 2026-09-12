# Historical Replay Benchmark

Generated at: `2026-09-12T00:46:55.713721+00:00`
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
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.019216`
- secondary_mean_absolute_error: `0.016048`
- primary_error_advantage: `-0.003168`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.022184`
- secondary_mean_absolute_error: `0.019353`
- primary_error_advantage: `-0.002831`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.032688`
- secondary_mean_absolute_error: `0.024552`
- primary_error_advantage: `-0.008136`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.15`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `-0.7`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.048443`
- secondary_mean_absolute_error: `0.028541`
- primary_error_advantage: `-0.019902`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.2667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.2875`
- primary_mean_absolute_error: `0.07927`
- secondary_mean_absolute_error: `0.061962`
- primary_error_advantage: `-0.017308`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.2667`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.015723`, as_primary `0`, as_primary_hit `None`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.019849`, as_primary `0`, as_primary_hit `None`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.025434`, as_primary `0`, as_primary_hit `None`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.031459`, as_primary `0`, as_primary_hit `None`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.060212`, as_primary `0`, as_primary_hit `None`, avg `0.058903`, median `0.083602`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.01669`, as_primary `0`, as_primary_hit `None`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.0229`, as_primary `0`, as_primary_hit `None`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.032372`, as_primary `0`, as_primary_hit `None`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.045485`, as_primary `0`, as_primary_hit `None`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.065871`, as_primary `0`, as_primary_hit `None`, avg `0.058903`, median `0.083602`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.019216`, as_primary `80`, as_primary_hit `0.6625`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.022184`, as_primary `80`, as_primary_hit `0.6125`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, direction_hit `0.2875`, path_mae `0.032688`, as_primary `80`, as_primary_hit `0.7125`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, direction_hit `0.15`, path_mae `0.048443`, as_primary `80`, as_primary_hit `0.85`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.07927`, as_primary `80`, as_primary_hit `0.75`, avg `0.058903`, median `0.083602`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.016048`, as_primary `0`, as_primary_hit `None`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.019353`, as_primary `0`, as_primary_hit `None`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, direction_hit `0.7125`, path_mae `0.024552`, as_primary `0`, as_primary_hit `None`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, direction_hit `0.85`, path_mae `0.028541`, as_primary `0`, as_primary_hit `None`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.061962`, as_primary `0`, as_primary_hit `None`, avg `0.058903`, median `0.083602`

## Edge Status Performance

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.019216`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.022184`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.35`, primary_mae `0.032688`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.048443`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.07927`, avg `0.058903`, median `0.083602`

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
- 3d: sample `20`, primary_hit `0.55`, primary_closer `0.3`, primary_mae `0.028415`, avg `-0.003278`, median `-0.000629`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.033864`, avg `-0.005236`, median `-0.008994`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.055764`, avg `0.011384`, median `0.023894`
- 20d: sample `20`, primary_hit `0.2`, primary_closer `0.2`, primary_mae `0.060548`, avg `0.020351`, median `0.02288`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.094586`, avg `0.01529`, median `0.047391`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.2667`, primary_closer `0.3833`, primary_mae `0.01615`, avg `0.008556`, median `0.01276`
- 5d: sample `60`, primary_hit `0.3167`, primary_closer `0.4833`, primary_mae `0.018291`, avg `0.011939`, median `0.012488`
- 10d: sample `60`, primary_hit `0.25`, primary_closer `0.3667`, primary_mae `0.024995`, avg `0.018541`, median `0.017793`
- 20d: sample `60`, primary_hit `0.1333`, primary_closer `0.2667`, primary_mae `0.044408`, avg `0.042139`, median `0.035118`
- 60d: sample `60`, primary_hit `0.1833`, primary_closer `0.2667`, primary_mae `0.074164`, avg `0.07344`, median `0.091366`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.01615, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.018291, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.024995, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1333, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.044408, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1833, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.074164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015723, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019216, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.01615, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019353, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0229, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.018291, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024552, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032688, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.024995, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': -0.7, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028541, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.048443, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1333, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.044408, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.2875, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060212, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07927, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.1833, 'primary_closer_than_secondary_rate': 0.2667, 'primary_mean_absolute_error': 0.074164, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.017259`, avg `0.00112`, median `0.005307`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.014185`, avg `0.005184`, median `0.008828`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.015261`, avg `0.008551`, median `0.01205`
- 20d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.053295`, avg `0.047984`, median `0.058396`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.038631`, avg `0.106475`, median `0.120549`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.014042`, avg `0.007265`, median `0.014733`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.015575`, avg `0.009924`, median `0.011781`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.015509`, avg `0.015699`, median `0.018985`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.043915`, avg `0.036774`, median `0.03746`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.25`, primary_mae `0.039871`, avg `0.087103`, median `0.099778`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.0625`, primary_closer `0.125`, primary_mae `0.020477`, avg `0.019397`, median `0.019768`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.025374`, avg `0.023261`, median `0.023997`
- 10d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.044974`, avg `0.039487`, median `0.033823`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.062439`, avg `0.066213`, median `0.061983`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.12101`, avg `0.07242`, median `0.097264`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.019216`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.022184`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.35`, primary_mae `0.032688`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.048443`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.07927`, avg `0.058903`, median `0.083602`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.019216`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.022184`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.35`, primary_mae `0.032688`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.048443`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.07927`, avg `0.058903`, median `0.083602`

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
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.3625`, primary_mae `0.019216`, avg `0.005598`, median `0.011216`
- 5d: sample `80`, primary_hit `0.3875`, primary_closer `0.4375`, primary_mae `0.022184`, avg `0.007645`, median `0.00893`
- 10d: sample `80`, primary_hit `0.2875`, primary_closer `0.35`, primary_mae `0.032688`, avg `0.016752`, median `0.018151`
- 20d: sample `80`, primary_hit `0.15`, primary_closer `0.25`, primary_mae `0.048443`, avg `0.036692`, median `0.034563`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.2875`, primary_mae `0.07927`, avg `0.058903`, median `0.083602`

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
