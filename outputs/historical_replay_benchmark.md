# Historical Replay Benchmark

Generated at: `2026-11-20T12:12:52.713269+00:00`
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
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.023087`
- secondary_mean_absolute_error: `0.020511`
- primary_error_advantage: `-0.002576`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3625`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `-0.275`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.024069`
- secondary_mean_absolute_error: `0.022133`
- primary_error_advantage: `-0.001936`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.039715`
- secondary_mean_absolute_error: `0.031466`
- primary_error_advantage: `-0.008249`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.2375`
- primary_mean_absolute_error: `0.075197`
- secondary_mean_absolute_error: `0.04238`
- primary_error_advantage: `-0.032817`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4125`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `-0.175`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.085857`
- secondary_mean_absolute_error: `0.077366`
- primary_error_advantage: `-0.008491`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.020923`, as_primary `0`, as_primary_hit `None`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.022201`, as_primary `0`, as_primary_hit `None`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.033386`, as_primary `0`, as_primary_hit `None`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.045189`, as_primary `0`, as_primary_hit `None`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.079253`, as_primary `0`, as_primary_hit `None`, avg `0.042632`, median `0.053364`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.020825`, as_primary `0`, as_primary_hit `None`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.022444`, as_primary `0`, as_primary_hit `None`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.0407`, as_primary `0`, as_primary_hit `None`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.069364`, as_primary `0`, as_primary_hit `None`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.098229`, as_primary `0`, as_primary_hit `None`, avg `0.042632`, median `0.053364`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.023087`, as_primary `80`, as_primary_hit `0.5875`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, direction_hit `0.3625`, path_mae `0.024069`, as_primary `80`, as_primary_hit `0.6375`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.039715`, as_primary `80`, as_primary_hit `0.675`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, direction_hit `0.2875`, path_mae `0.075197`, as_primary `80`, as_primary_hit `0.7125`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.085857`, as_primary `80`, as_primary_hit `0.5875`, avg `0.042632`, median `0.053364`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.020511`, as_primary `0`, as_primary_hit `None`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, direction_hit `0.6375`, path_mae `0.022133`, as_primary `0`, as_primary_hit `None`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.031466`, as_primary `0`, as_primary_hit `None`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, direction_hit `0.7125`, path_mae `0.04238`, as_primary `0`, as_primary_hit `None`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.077366`, as_primary `0`, as_primary_hit `None`, avg `0.042632`, median `0.053364`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.023087`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.4125`, primary_mae `0.024069`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.039715`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.075197`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.085857`, avg `0.042632`, median `0.053364`

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
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.032668`, avg `-0.005981`, median `-0.002747`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.027525`, avg `0.005705`, median `0.010878`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.052875`, avg `0.017999`, median `0.019434`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.2`, primary_mae `0.127392`, avg `0.02237`, median `0.040222`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.45`, primary_mae `0.108879`, avg `-0.000207`, median `-0.021408`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.4167`, primary_mae `0.019894`, avg `0.009652`, median `0.00859`
- 5d: sample `60`, primary_hit `0.35`, primary_closer `0.4167`, primary_mae `0.022917`, avg `0.009579`, median `0.006404`
- 10d: sample `60`, primary_hit `0.3333`, primary_closer `0.35`, primary_mae `0.035328`, avg `0.018323`, median `0.013914`
- 20d: sample `60`, primary_hit `0.2667`, primary_closer `0.25`, primary_mae `0.057799`, avg `0.035161`, median `0.038323`
- 60d: sample `60`, primary_hit `0.3333`, primary_closer `0.4167`, primary_mae `0.078183`, avg `0.056912`, median `0.066693`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.019894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.022917, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035328, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.057799, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.078183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020511, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023087, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.019894, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': -0.275, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022133, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024069, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.022917, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031466, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0407, 'direction_hit_rate': 0.675}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.035328, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.2375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04238, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.075197, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2667, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.057799, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077366, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.098229, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3333, 'primary_closer_than_secondary_rate': 0.4167, 'primary_mean_absolute_error': 0.078183, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.019371`, avg `0.013871`, median `0.010315`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.024925`, avg `0.009745`, median `0.002986`
- 10d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.043859`, avg `0.035268`, median `0.03504`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.25`, primary_mae `0.068236`, avg `0.064782`, median `0.058385`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.117335`, avg `0.114108`, median `0.155419`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.625`, primary_mae `0.018703`, avg `0.012605`, median `0.009541`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.5`, primary_mae `0.027881`, avg `0.016152`, median `0.016938`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.04837`, avg `0.035066`, median `0.042409`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.25`, primary_mae `0.068697`, avg `0.05698`, median `0.057783`
- 60d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.113371`, avg `0.095172`, median `0.128786`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.3125`, primary_mae `0.034455`, avg `-0.003303`, median `-0.001755`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.027506`, avg `0.006989`, median `0.010878`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.04816`, avg `0.029764`, median `0.019434`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.1875`, primary_mae `0.119134`, avg `0.029897`, median `0.040222`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.5`, primary_mae `0.079847`, avg `-0.009305`, median `-0.034156`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.023087`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.4125`, primary_mae `0.024069`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.039715`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.075197`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.085857`, avg `0.042632`, median `0.053364`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.023087`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.4125`, primary_mae `0.024069`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.039715`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.075197`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.085857`, avg `0.042632`, median `0.053364`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.023735`, avg `0.003945`, median `0.007093`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.021303`, avg `0.000676`, median `0.001655`
- 10d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.029755`, avg `0.000896`, median `-0.000779`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.3`, primary_mae `0.055729`, avg `0.012537`, median `0.008148`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.069652`, avg `0.023077`, median `0.020882`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.023406`, avg `0.001945`, median `0.006403`
- 5d: sample `60`, primary_hit `0.3833`, primary_closer `0.4`, primary_mae `0.021585`, avg `0.003722`, median `0.005446`
- 10d: sample `60`, primary_hit `0.3833`, primary_closer `0.3667`, primary_mae `0.035237`, avg `0.01015`, median `0.007697`
- 20d: sample `60`, primary_hit `0.35`, primary_closer `0.25`, primary_mae `0.076442`, avg `0.022152`, median `0.030451`
- 60d: sample `60`, primary_hit `0.4667`, primary_closer `0.45`, primary_mae `0.078701`, avg `0.024534`, median `0.003033`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.023087`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.4125`, primary_mae `0.024069`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.039715`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.075197`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.085857`, avg `0.042632`, median `0.053364`

### flow_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.4`, primary_mae `0.023087`, avg `0.005744`, median `0.007564`
- 5d: sample `80`, primary_hit `0.3625`, primary_closer `0.4125`, primary_mae `0.024069`, avg `0.008611`, median `0.006786`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.3375`, primary_mae `0.039715`, avg `0.018242`, median `0.017483`
- 20d: sample `80`, primary_hit `0.2875`, primary_closer `0.2375`, primary_mae `0.075197`, avg `0.031963`, median `0.038323`
- 60d: sample `80`, primary_hit `0.4125`, primary_closer `0.425`, primary_mae `0.085857`, avg `0.042632`, median `0.053364`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
