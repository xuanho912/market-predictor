# Historical Replay Benchmark

Generated at: `2026-10-08T18:54:26.769273+00:00`
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
- primary_hit_rate: `0.6625`
- secondary_hit_rate: `0.3375`
- primary_vs_secondary_accuracy_spread: `0.325`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.020871`
- secondary_mean_absolute_error: `0.016725`
- primary_error_advantage: `-0.004146`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3875`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.024394`
- secondary_mean_absolute_error: `0.019457`
- primary_error_advantage: `-0.004937`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.035125`
- secondary_mean_absolute_error: `0.032759`
- primary_error_advantage: `-0.002366`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.425`
- secondary_hit_rate: `0.575`
- primary_vs_secondary_accuracy_spread: `-0.15`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.07721`
- secondary_mean_absolute_error: `0.061276`
- primary_error_advantage: `-0.015934`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.25`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `-0.5`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.077432`
- secondary_mean_absolute_error: `0.069219`
- primary_error_advantage: `-0.008213`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.375`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.016368`, as_primary `0`, as_primary_hit `None`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.017985`, as_primary `0`, as_primary_hit `None`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.026262`, as_primary `0`, as_primary_hit `None`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.042404`, as_primary `0`, as_primary_hit `None`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.055695`, as_primary `0`, as_primary_hit `None`, avg `0.030744`, median `0.046392`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.016725`, as_primary `0`, as_primary_hit `None`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019457`, as_primary `0`, as_primary_hit `None`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.032759`, as_primary `0`, as_primary_hit `None`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.061276`, as_primary `0`, as_primary_hit `None`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.069219`, as_primary `0`, as_primary_hit `None`, avg `0.030744`, median `0.046392`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.020871`, as_primary `80`, as_primary_hit `0.3375`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.024394`, as_primary `80`, as_primary_hit `0.4`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.5625`, path_mae `0.035125`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.425`, path_mae `0.07721`, as_primary `80`, as_primary_hit `0.575`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, direction_hit `0.25`, path_mae `0.077432`, as_primary `80`, as_primary_hit `0.75`, avg `0.030744`, median `0.046392`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.015369`, as_primary `0`, as_primary_hit `None`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.017715`, as_primary `0`, as_primary_hit `None`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, direction_hit `0.4375`, path_mae `0.025607`, as_primary `0`, as_primary_hit `None`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, direction_hit `0.575`, path_mae `0.042728`, as_primary `0`, as_primary_hit `None`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.059117`, as_primary `0`, as_primary_hit `None`, avg `0.030744`, median `0.046392`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.3875`, primary_mae `0.020871`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.024394`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.035125`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.07721`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.077432`, avg `0.030744`, median `0.046392`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.022823`, avg `-0.009733`, median `-0.010538`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.034394`, avg `-0.012103`, median `-0.018412`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.3`, primary_mae `0.0375`, avg `-0.015491`, median `-0.012632`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.083699`, avg `0.001066`, median `0.009104`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.122591`, avg `-0.000463`, median `0.045479`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.020221`, avg `-0.006213`, median `-0.004007`
- 5d: sample `60`, primary_hit `0.6`, primary_closer `0.4`, primary_mae `0.02106`, avg `-0.01045`, median `-0.012577`
- 10d: sample `60`, primary_hit `0.5167`, primary_closer `0.5`, primary_mae `0.034334`, avg `-0.008435`, median `-0.005578`
- 20d: sample `60`, primary_hit `0.4167`, primary_closer `0.4`, primary_mae `0.075048`, avg `0.011566`, median `0.015722`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.3667`, primary_mae `0.062379`, avg `0.041147`, median `0.048222`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.020221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.02106, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034334, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.075048, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.062379, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.3375, 'primary_vs_secondary_accuracy_spread': 0.325, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015369, 'direction_hit_rate': 0.3375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020871, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.020221, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017715, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024394, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.02106, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025607, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035125, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.5167, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034334, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_vs_secondary_accuracy_spread': -0.15, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.042404, 'direction_hit_rate': 0.575}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07721, 'direction_hit_rate': 0.425}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.075048, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': -0.5, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.055695, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077432, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.062379, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.023847`, avg `-0.009664`, median `-0.016078`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.035175`, avg `-0.011557`, median `-0.009546`
- 10d: sample `8`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.036096`, avg `-0.012306`, median `-0.015452`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.125`, primary_mae `0.092759`, avg `0.00631`, median `0.019252`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.132998`, avg `0.017567`, median `0.048285`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.4375`, primary_mae `0.023625`, avg `-0.009708`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.034929`, avg `-0.012757`, median `-0.019358`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.25`, primary_mae `0.03994`, avg `-0.011952`, median `-0.010944`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.088917`, avg `0.00701`, median `0.019252`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.129158`, avg `0.007361`, median `0.048285`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.0625`, primary_mae `0.031731`, avg `-0.009057`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.125`, primary_mae `0.027229`, avg `-0.01486`, median `-0.019296`
- 10d: sample `16`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.0484`, avg `-0.003598`, median `-0.02209`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.102433`, avg `0.033281`, median `0.042225`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.3125`, primary_mae `0.076804`, avg `0.086182`, median `0.092349`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.3875`, primary_mae `0.020871`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.024394`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.035125`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.07721`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.077432`, avg `0.030744`, median `0.046392`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.3875`, primary_mae `0.020871`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.024394`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.035125`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.07721`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.077432`, avg `0.030744`, median `0.046392`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.022823`, avg `-0.009733`, median `-0.010538`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.034394`, avg `-0.012103`, median `-0.018412`
- 10d: sample `20`, primary_hit `0.7`, primary_closer `0.3`, primary_mae `0.0375`, avg `-0.015491`, median `-0.012632`
- 20d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.083699`, avg `0.001066`, median `0.009104`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.122591`, avg `-0.000463`, median `0.045479`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.675`, primary_closer `0.375`, primary_mae `0.02095`, avg `-0.006633`, median `-0.004464`
- 5d: sample `40`, primary_hit `0.625`, primary_closer `0.325`, primary_mae `0.019353`, avg `-0.011394`, median `-0.011804`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.03285`, avg `-0.006604`, median `-0.005578`
- 20d: sample `40`, primary_hit `0.425`, primary_closer `0.375`, primary_mae `0.083313`, avg `0.012846`, median `0.014591`
- 60d: sample `40`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.070806`, avg `0.044491`, median `0.048206`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.3875`, primary_mae `0.020871`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.024394`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.035125`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.07721`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.077432`, avg `0.030744`, median `0.046392`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6625`, primary_closer `0.3875`, primary_mae `0.020871`, avg `-0.007093`, median `-0.004922`
- 5d: sample `80`, primary_hit `0.6`, primary_closer `0.4125`, primary_mae `0.024394`, avg `-0.010863`, median `-0.013233`
- 10d: sample `80`, primary_hit `0.5625`, primary_closer `0.45`, primary_mae `0.035125`, avg `-0.010199`, median `-0.006976`
- 20d: sample `80`, primary_hit `0.425`, primary_closer `0.4`, primary_mae `0.07721`, avg `0.008941`, median `0.015722`
- 60d: sample `80`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.077432`, avg `0.030744`, median `0.046392`

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
