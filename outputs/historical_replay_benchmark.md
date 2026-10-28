# Historical Replay Benchmark

Generated at: `2026-10-28T18:24:01.949998+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `FAIL`
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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.014609`
- secondary_mean_absolute_error: `0.013283`
- primary_error_advantage: `-0.001326`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.020509`
- secondary_mean_absolute_error: `0.018296`
- primary_error_advantage: `-0.002213`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.029792`
- secondary_mean_absolute_error: `0.024363`
- primary_error_advantage: `-0.005429`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.35`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.675`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.05`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.039271`
- secondary_mean_absolute_error: `0.027686`
- primary_error_advantage: `-0.011585`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3167`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.062546`
- secondary_mean_absolute_error: `0.051562`
- primary_error_advantage: `-0.010984`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.014576`, as_primary `0`, as_primary_hit `None`, avg `0.003892`, median `0.004638`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.019826`, as_primary `0`, as_primary_hit `None`, avg `0.00634`, median `0.008466`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.027074`, as_primary `0`, as_primary_hit `None`, avg `0.012976`, median `0.011971`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.029983`, as_primary `0`, as_primary_hit `None`, avg `0.022809`, median `0.027397`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.0517`, as_primary `0`, as_primary_hit `None`, avg `0.035618`, median `0.050858`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.016197`, as_primary `60`, as_primary_hit `0.65`, avg `0.003892`, median `0.004638`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.022724`, as_primary `60`, as_primary_hit `0.6333`, avg `0.00634`, median `0.008466`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.034876`, as_primary `60`, as_primary_hit `0.7667`, avg `0.012976`, median `0.011971`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.041699`, as_primary `60`, as_primary_hit `0.7667`, avg `0.022809`, median `0.027397`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.05684`, as_primary `60`, as_primary_hit `0.7333`, avg `0.035618`, median `0.050858`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.014399`, as_primary `20`, as_primary_hit `0.5`, avg `0.003892`, median `0.004638`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019727`, as_primary `20`, as_primary_hit `0.5`, avg `0.00634`, median `0.008466`
- 10d: sample `80`, direction_hit `0.275`, path_mae `0.033166`, as_primary `20`, as_primary_hit `0.6`, avg `0.012976`, median `0.011971`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.042841`, as_primary `20`, as_primary_hit `0.6`, avg `0.022809`, median `0.027397`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.078028`, as_primary `20`, as_primary_hit `0.7`, avg `0.035618`, median `0.050858`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013283`, as_primary `0`, as_primary_hit `None`, avg `0.003892`, median `0.004638`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.018296`, as_primary `0`, as_primary_hit `None`, avg `0.00634`, median `0.008466`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.024363`, as_primary `0`, as_primary_hit `None`, avg `0.012976`, median `0.011971`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.027686`, as_primary `0`, as_primary_hit `None`, avg `0.022809`, median `0.027397`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.051562`, as_primary `0`, as_primary_hit `None`, avg `0.035618`, median `0.050858`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.013185`, avg `0.005243`, median `0.005755`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.45`, primary_mae `0.020606`, avg `0.008275`, median `0.009948`
- 10d: sample `60`, primary_hit `0.7667`, primary_closer `0.35`, primary_mae `0.029218`, avg `0.015405`, median `0.018478`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.3167`, primary_mae `0.035371`, avg `0.025869`, median `0.028709`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.4833`, primary_mae `0.051926`, avg `0.036147`, median `0.050858`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.01888`, avg `-0.000162`, median `-0.001791`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02022`, avg `0.000536`, median `8.1e-05`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.031513`, avg `0.005691`, median `0.006526`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.050971`, avg `0.01363`, median `0.002175`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.094405`, avg `0.034032`, median `0.042266`

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
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.01888`, avg `-0.000162`, median `-0.001791`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02022`, avg `0.000536`, median `8.1e-05`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.031513`, avg `0.005691`, median `0.006526`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.050971`, avg `0.01363`, median `0.002175`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.094405`, avg `0.034032`, median `0.042266`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.013185`, avg `0.005243`, median `0.005755`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.45`, primary_mae `0.020606`, avg `0.008275`, median `0.009948`
- 10d: sample `60`, primary_hit `0.7667`, primary_closer `0.35`, primary_mae `0.029218`, avg `0.015405`, median `0.018478`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.3167`, primary_mae `0.035371`, avg `0.025869`, median `0.028709`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.4833`, primary_mae `0.051926`, avg `0.036147`, median `0.050858`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.013185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.029218, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.035371, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.051926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013283, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016197, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4333, 'primary_mean_absolute_error': 0.013185, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018296, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022724, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.02022, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024363, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034876, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.029218, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.05, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027686, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042841, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7667, 'primary_closer_than_secondary_rate': 0.3167, 'primary_mean_absolute_error': 0.035371, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.051562, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.078028, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.7333, 'primary_closer_than_secondary_rate': 0.4833, 'primary_mean_absolute_error': 0.051926, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.021698`, avg `0.005635`, median `0.002901`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.031684`, avg `0.006385`, median `0.001226`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.037944`, avg `0.015161`, median `0.014259`
- 20d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.038836`, avg `0.033414`, median `0.029911`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.024843`, avg `0.067525`, median `0.070816`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.02042`, avg `0.006565`, median `0.002901`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.029636`, avg `0.007852`, median `0.010356`
- 10d: sample `16`, primary_hit `0.625`, primary_closer `0.25`, primary_mae `0.038055`, avg `0.016721`, median `0.022448`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.040675`, avg `0.031534`, median `0.028445`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.038155`, avg `0.054584`, median `0.070816`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.4375`, primary_mae `0.019117`, avg `0.00173`, median `-0.001683`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.5625`, primary_mae `0.018468`, avg `0.004259`, median `0.006972`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.030736`, avg `0.009642`, median `0.008601`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.04904`, avg `0.013851`, median `0.002175`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.101392`, avg `0.044526`, median `0.055033`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.014609`, avg `0.003892`, median `0.004638`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.020509`, avg `0.00634`, median `0.008466`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.029792`, avg `0.012976`, median `0.011971`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.039271`, avg `0.022809`, median `0.027397`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.062546`, avg `0.035618`, median `0.050858`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.014609`, avg `0.003892`, median `0.004638`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.020509`, avg `0.00634`, median `0.008466`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.029792`, avg `0.012976`, median `0.011971`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.039271`, avg `0.022809`, median `0.027397`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.062546`, avg `0.035618`, median `0.050858`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4333`, primary_mae `0.013185`, avg `0.005243`, median `0.005755`
- 5d: sample `60`, primary_hit `0.6333`, primary_closer `0.45`, primary_mae `0.020606`, avg `0.008275`, median `0.009948`
- 10d: sample `60`, primary_hit `0.7667`, primary_closer `0.35`, primary_mae `0.029218`, avg `0.015405`, median `0.018478`
- 20d: sample `60`, primary_hit `0.7667`, primary_closer `0.3167`, primary_mae `0.035371`, avg `0.025869`, median `0.028709`
- 60d: sample `60`, primary_hit `0.7333`, primary_closer `0.4833`, primary_mae `0.051926`, avg `0.036147`, median `0.050858`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.01888`, avg `-0.000162`, median `-0.001791`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.02022`, avg `0.000536`, median `8.1e-05`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.031513`, avg `0.005691`, median `0.006526`
- 20d: sample `20`, primary_hit `0.4`, primary_closer `0.35`, primary_mae `0.050971`, avg `0.01363`, median `0.002175`
- 60d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.094405`, avg `0.034032`, median `0.042266`

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
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.425`, primary_mae `0.014609`, avg `0.003892`, median `0.004638`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4625`, primary_mae `0.020509`, avg `0.00634`, median `0.008466`
- 10d: sample `80`, primary_hit `0.675`, primary_closer `0.3625`, primary_mae `0.029792`, avg `0.012976`, median `0.011971`
- 20d: sample `80`, primary_hit `0.675`, primary_closer `0.325`, primary_mae `0.039271`, avg `0.022809`, median `0.027397`
- 60d: sample `80`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.062546`, avg `0.035618`, median `0.050858`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
