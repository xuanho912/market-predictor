# Historical Replay Benchmark

Generated at: `2026-07-23T06:20:08.811662+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.019579`
- secondary_mean_absolute_error: `0.017557`
- primary_error_advantage: `-0.002022`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.5`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.024639`
- secondary_mean_absolute_error: `0.020185`
- primary_error_advantage: `-0.004454`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.525`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.5375`
- primary_mean_absolute_error: `0.029662`
- secondary_mean_absolute_error: `0.028364`
- primary_error_advantage: `-0.001298`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.65`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.071155`
- secondary_mean_absolute_error: `0.05286`
- primary_error_advantage: `-0.018295`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.325`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.111019`
- secondary_mean_absolute_error: `0.087311`
- primary_error_advantage: `-0.023708`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015632`, as_primary `0`, as_primary_hit `None`, avg `-0.005425`, median `-0.003082`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.018613`, as_primary `0`, as_primary_hit `None`, avg `-0.007055`, median `-0.006211`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.024289`, as_primary `0`, as_primary_hit `None`, avg `-0.003266`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.039278`, as_primary `0`, as_primary_hit `None`, avg `0.004295`, median `0.016991`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.074141`, as_primary `0`, as_primary_hit `None`, avg `0.004667`, median `0.021984`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.017691`, as_primary `0`, as_primary_hit `None`, avg `-0.005425`, median `-0.003082`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.02138`, as_primary `0`, as_primary_hit `None`, avg `-0.007055`, median `-0.006211`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.031872`, as_primary `0`, as_primary_hit `None`, avg `-0.003266`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.054783`, as_primary `0`, as_primary_hit `None`, avg `0.004295`, median `0.016991`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.090227`, as_primary `0`, as_primary_hit `None`, avg `0.004667`, median `0.021984`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.019579`, as_primary `80`, as_primary_hit `0.45`, avg `-0.005425`, median `-0.003082`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.024639`, as_primary `80`, as_primary_hit `0.425`, avg `-0.007055`, median `-0.006211`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.029662`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.003266`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.3625`, path_mae `0.071155`, as_primary `80`, as_primary_hit `0.6375`, avg `0.004295`, median `0.016991`
- 60d: sample `80`, direction_hit `0.4375`, path_mae `0.111019`, as_primary `80`, as_primary_hit `0.5625`, avg `0.004667`, median `0.021984`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.015348`, as_primary `0`, as_primary_hit `None`, avg `-0.005425`, median `-0.003082`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.017766`, as_primary `0`, as_primary_hit `None`, avg `-0.007055`, median `-0.006211`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.022534`, as_primary `0`, as_primary_hit `None`, avg `-0.003266`, median `-0.007064`
- 20d: sample `80`, direction_hit `0.6375`, path_mae `0.03901`, as_primary `0`, as_primary_hit `None`, avg `0.004295`, median `0.016991`
- 60d: sample `80`, direction_hit `0.5625`, path_mae `0.074559`, as_primary `0`, as_primary_hit `None`, avg `0.004667`, median `0.021984`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.024197`, avg `-0.009316`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.034316`, avg `-0.011233`, median `-0.01025`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.7`, primary_mae `0.019219`, avg `-0.00227`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.071803`, avg `0.01574`, median `0.020913`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.112705`, avg `0.042203`, median `0.054785`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4167`, primary_mae `0.01804`, avg `-0.004128`, median `-0.001935`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.35`, primary_mae `0.021413`, avg `-0.005663`, median `-0.006211`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.033143`, avg `-0.003598`, median `-0.007037`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.3167`, primary_mae `0.070939`, avg `0.00048`, median `0.011582`
- 60d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.110456`, avg `-0.007845`, median `0.000898`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5333`, primary_closer `0.4167`, primary_mae `0.01804`, avg `-0.004128`, median `-0.001935`
- 5d: sample `60`, primary_hit `0.5833`, primary_closer `0.35`, primary_mae `0.021413`, avg `-0.005663`, median `-0.006211`
- 10d: sample `60`, primary_hit `0.5333`, primary_closer `0.4833`, primary_mae `0.033143`, avg `-0.003598`, median `-0.007037`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.3167`, primary_mae `0.070939`, avg `0.00048`, median `0.011582`
- 60d: sample `60`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.110456`, avg `-0.007845`, median `0.000898`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.5`, primary_mae `0.024197`, avg `-0.009316`, median `-0.009708`
- 5d: sample `20`, primary_hit `0.55`, primary_closer `0.5`, primary_mae `0.034316`, avg `-0.011233`, median `-0.01025`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.7`, primary_mae `0.019219`, avg `-0.00227`, median `-0.007383`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.071803`, avg `0.01574`, median `0.020913`
- 60d: sample `20`, primary_hit `0.25`, primary_closer `0.35`, primary_mae `0.112705`, avg `0.042203`, median `0.054785`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.01804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021413, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.019219, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.070939, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.110456, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015348, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019579, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.01804, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017766, 'direction_hit_rate': 0.425}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024639, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.021413, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.5375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022534, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031872, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.019219, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03901, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071155, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.070939, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.074141, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.111019, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.110456, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016444`, avg `-0.020804`, median `-0.031812`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.022475`, avg `-0.028823`, median `-0.028941`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.013655`, avg `-0.016415`, median `-0.019121`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.058941`, avg `-0.00875`, median `0.01014`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.093769`, avg `0.011496`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.021662`, avg `-0.012659`, median `-0.018199`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.030141`, avg `-0.016367`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.75`, primary_mae `0.018431`, avg `-0.004553`, median `-0.007383`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.07314`, avg `0.015139`, median `0.023936`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.116226`, avg `0.043762`, median `0.059313`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.013491`, avg `-0.003212`, median `-0.002878`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.1875`, primary_mae `0.024524`, avg `-0.005031`, median `-0.002769`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.046515`, avg `-0.013879`, median `-0.006421`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.090128`, avg `-0.02271`, median `0.012493`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.144942`, avg `-0.066952`, median `-0.075187`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019579`, avg `-0.005425`, median `-0.003082`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.3875`, primary_mae `0.024639`, avg `-0.007055`, median `-0.006211`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.029662`, avg `-0.003266`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.071155`, avg `0.004295`, median `0.016991`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.111019`, avg `0.004667`, median `0.021984`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019579`, avg `-0.005425`, median `-0.003082`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.3875`, primary_mae `0.024639`, avg `-0.007055`, median `-0.006211`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.029662`, avg `-0.003266`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.071155`, avg `0.004295`, median `0.016991`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.111019`, avg `0.004667`, median `0.021984`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.018845`, avg `-0.008526`, median `-0.008696`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.024737`, avg `-0.010221`, median `-0.005451`
- 10d: sample `40`, primary_hit `0.675`, primary_closer `0.65`, primary_mae `0.020959`, avg `-0.006788`, median `-0.010657`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.325`, primary_mae `0.071269`, avg `0.004351`, median `0.016081`
- 60d: sample `40`, primary_hit `0.375`, primary_closer `0.4`, primary_mae `0.094086`, avg `0.025584`, median `0.035204`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.026842`, avg `-0.002054`, median `0.002036`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.3`, primary_mae `0.025412`, avg `-0.002018`, median `-0.007626`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.029119`, avg `0.012609`, median `0.01787`
- 20d: sample `20`, primary_hit `0.1`, primary_closer `0.25`, primary_mae `0.047445`, avg `0.025881`, median `0.033856`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.09107`, avg `0.013798`, median `0.031665`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.55`, primary_closer `0.4375`, primary_mae `0.019579`, avg `-0.005425`, median `-0.003082`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.3875`, primary_mae `0.024639`, avg `-0.007055`, median `-0.006211`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.5375`, primary_mae `0.029662`, avg `-0.003266`, median `-0.007064`
- 20d: sample `80`, primary_hit `0.3625`, primary_closer `0.325`, primary_mae `0.071155`, avg `0.004295`, median `0.016991`
- 60d: sample `80`, primary_hit `0.4375`, primary_closer `0.425`, primary_mae `0.111019`, avg `0.004667`, median `0.021984`

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
