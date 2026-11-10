# Historical Replay Benchmark

Generated at: `2026-11-10T19:47:15.719982+00:00`
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
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.022284`
- secondary_mean_absolute_error: `0.020537`
- primary_error_advantage: `-0.001747`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.425`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.021619`
- secondary_mean_absolute_error: `0.025057`
- primary_error_advantage: `0.003438`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.55`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.2625`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.04463`
- secondary_mean_absolute_error: `0.036694`
- primary_error_advantage: `-0.007936`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.064739`
- secondary_mean_absolute_error: `0.043151`
- primary_error_advantage: `-0.021588`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.15`
- secondary_hit_rate: `0.85`
- primary_vs_secondary_accuracy_spread: `-0.7`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.053385`
- secondary_mean_absolute_error: `0.039811`
- primary_error_advantage: `-0.013574`
- close_call_sample_size: `40`
- close_call_primary_closer_rate: `0.3`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.018238`, as_primary `0`, as_primary_hit `None`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.021168`, as_primary `0`, as_primary_hit `None`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.029405`, as_primary `0`, as_primary_hit `None`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.032123`, as_primary `0`, as_primary_hit `None`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.034016`, as_primary `0`, as_primary_hit `None`, avg `0.053862`, median `0.067412`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.020701`, as_primary `0`, as_primary_hit `None`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.024907`, as_primary `0`, as_primary_hit `None`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.035462`, as_primary `0`, as_primary_hit `None`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.046246`, as_primary `0`, as_primary_hit `None`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.041544`, as_primary `0`, as_primary_hit `None`, avg `0.053862`, median `0.067412`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.45`, path_mae `0.022284`, as_primary `80`, as_primary_hit `0.55`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, direction_hit `0.425`, path_mae `0.021619`, as_primary `80`, as_primary_hit `0.575`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.04463`, as_primary `80`, as_primary_hit `0.625`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.064739`, as_primary `80`, as_primary_hit `0.725`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, direction_hit `0.15`, path_mae `0.053385`, as_primary `80`, as_primary_hit `0.85`, avg `0.053862`, median `0.067412`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.55`, path_mae `0.017962`, as_primary `0`, as_primary_hit `None`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, direction_hit `0.575`, path_mae `0.019681`, as_primary `0`, as_primary_hit `None`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, direction_hit `0.625`, path_mae `0.028436`, as_primary `0`, as_primary_hit `None`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.032577`, as_primary `0`, as_primary_hit `None`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.034719`, as_primary `0`, as_primary_hit `None`, avg `0.053862`, median `0.067412`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.022284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.021619, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.04463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.064739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.053385, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017962, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022284, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4625, 'primary_mean_absolute_error': 0.022284, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019681, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024907, 'direction_hit_rate': 0.575}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.425, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.021619, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.2625, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028436, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04463, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.3625, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.04463, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032123, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.064739, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3125, 'primary_mean_absolute_error': 0.064739, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.15, 'secondary_hit_rate': 0.85, 'primary_vs_secondary_accuracy_spread': -0.7, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034016, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.053385, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.053385, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.022988`, avg `0.008091`, median `0.016333`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.028625`, avg `0.021151`, median `0.026904`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.125`, primary_mae `0.065331`, avg `0.04168`, median `0.04932`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.091868`, avg `0.056508`, median `0.054962`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.096755`, avg `0.071794`, median `0.065415`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020496`, avg `-0.001`, median `-0.001364`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.025886`, avg `0.005898`, median `0.006717`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.048761`, avg `0.018755`, median `0.021014`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.065595`, avg `0.027064`, median `0.033185`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.077118`, avg `0.04082`, median `0.055914`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.4375`, primary_mae `0.021475`, avg `0.00737`, median `0.008431`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.023881`, avg `0.017401`, median `0.006005`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.059423`, avg `0.010116`, median `0.034572`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.077504`, avg `0.002813`, median `0.01352`
- 60d: sample `16`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.015372`, avg `0.077719`, median `0.079167`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4667`, primary_closer `0.4667`, primary_mae `0.022438`, avg `0.001629`, median `0.002529`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.5833`, primary_mae `0.021065`, avg `0.002917`, median `0.00151`
- 10d: sample `60`, primary_hit `0.3833`, primary_closer `0.4667`, primary_mae `0.04022`, avg `0.009102`, median `0.010917`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.35`, primary_mae `0.057221`, avg `0.018177`, median `0.025425`
- 60d: sample `60`, primary_hit `0.1833`, primary_closer `0.3667`, primary_mae `0.063753`, avg `0.045861`, median `0.056753`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.021823`, avg `0.006699`, median `0.008431`
- 5d: sample `20`, primary_hit `0.25`, primary_closer `0.45`, primary_mae `0.02328`, avg `0.016677`, median `0.006467`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.057862`, avg `0.013447`, median `0.030746`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.2`, primary_mae `0.087295`, avg `0.014611`, median `0.037655`
- 60d: sample `20`, primary_hit `0.05`, primary_closer `0.4`, primary_mae `0.02228`, avg `0.077865`, median `0.079167`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.45`, primary_closer `0.4625`, primary_mae `0.022284`, avg `0.002897`, median `0.003409`
- 5d: sample `80`, primary_hit `0.425`, primary_closer `0.55`, primary_mae `0.021619`, avg `0.006357`, median `0.004111`
- 10d: sample `80`, primary_hit `0.3625`, primary_closer `0.425`, primary_mae `0.04463`, avg `0.010188`, median `0.014924`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3125`, primary_mae `0.064739`, avg `0.017285`, median `0.026691`
- 60d: sample `80`, primary_hit `0.15`, primary_closer `0.375`, primary_mae `0.053385`, avg `0.053862`, median `0.067412`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
