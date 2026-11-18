# Historical Replay Benchmark

Generated at: `2026-11-18T03:57:33.931498+00:00`
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
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.025064`
- secondary_mean_absolute_error: `0.020922`
- primary_error_advantage: `-0.004142`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.026354`
- secondary_mean_absolute_error: `0.022069`
- primary_error_advantage: `-0.004285`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.033405`
- secondary_mean_absolute_error: `0.028837`
- primary_error_advantage: `-0.004568`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.054478`
- secondary_mean_absolute_error: `0.037288`
- primary_error_advantage: `-0.01719`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.072353`
- secondary_mean_absolute_error: `0.070016`
- primary_error_advantage: `-0.002337`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.021652`, as_primary `0`, as_primary_hit `None`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022846`, as_primary `0`, as_primary_hit `None`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.029701`, as_primary `0`, as_primary_hit `None`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.041364`, as_primary `0`, as_primary_hit `None`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.072714`, as_primary `0`, as_primary_hit `None`, avg `0.047937`, median `0.053364`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.021199`, as_primary `0`, as_primary_hit `None`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022684`, as_primary `0`, as_primary_hit `None`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.033354`, as_primary `0`, as_primary_hit `None`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.061304`, as_primary `0`, as_primary_hit `None`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.084477`, as_primary `0`, as_primary_hit `None`, avg `0.047937`, median `0.053364`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.025064`, as_primary `80`, as_primary_hit `0.5875`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, direction_hit `0.35`, path_mae `0.026354`, as_primary `80`, as_primary_hit `0.65`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.033405`, as_primary `80`, as_primary_hit `0.65`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.054478`, as_primary `80`, as_primary_hit `0.725`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, direction_hit `0.3875`, path_mae `0.072353`, as_primary `80`, as_primary_hit `0.6125`, avg `0.047937`, median `0.053364`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.020922`, as_primary `0`, as_primary_hit `None`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, direction_hit `0.65`, path_mae `0.022069`, as_primary `0`, as_primary_hit `None`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.028837`, as_primary `0`, as_primary_hit `None`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.037288`, as_primary `0`, as_primary_hit `None`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, direction_hit `0.6125`, path_mae `0.070016`, as_primary `0`, as_primary_hit `None`, avg `0.047937`, median `0.053364`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3625`, primary_mae `0.025064`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.026354`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.033405`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.054478`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.072353`, avg `0.047937`, median `0.053364`

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
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.031481`, avg `-0.003279`, median `0.001708`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.035357`, avg `0.008372`, median `0.016116`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.036777`, avg `0.022443`, median `0.019434`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.081012`, avg `0.012449`, median `-0.007388`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.091817`, avg `0.012581`, median `-0.014177`

### trend_reversal_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### risk_expansion_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.35`, primary_mae `0.022925`, avg `0.00828`, median `0.008928`
- 5d: sample `60`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.023353`, avg `0.00904`, median `0.006404`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.45`, primary_mae `0.032281`, avg `0.017042`, median `0.009948`
- 20d: sample `60`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.045634`, avg `0.037703`, median `0.03694`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4`, primary_mae `0.065864`, avg `0.059722`, median `0.067587`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022925, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.023353, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.032281, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.045634, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.065864, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': -0.175, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020922, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025064, 'direction_hit_rate': 0.4125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3833, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.022925, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022069, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026354, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.023353, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028837, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033405, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.032281, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037288, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061304, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.045634, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070016, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.084477, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3167, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.065864, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.030363`, avg `0.024709`, median `0.02697`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.024381`, avg `0.014645`, median `0.023063`
- 10d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.033621`, avg `0.022843`, median `0.010784`
- 20d: sample `8`, primary_hit `0.0`, primary_closer `0.5`, primary_mae `0.03117`, avg `0.045188`, median `0.044059`
- 60d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.053786`, avg `0.088635`, median `0.118517`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.028574`, avg `0.018963`, median `0.024622`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.030924`, avg `0.02061`, median `0.023063`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.4375`, primary_mae `0.045314`, avg `0.036825`, median `0.034527`
- 20d: sample `16`, primary_hit `0.0`, primary_closer `0.4375`, primary_mae `0.044159`, avg `0.059537`, median `0.045914`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.061453`, avg `0.100331`, median `0.126585`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.030624`, avg `-0.002366`, median `-0.005955`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.036955`, avg `0.009517`, median `0.016116`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.034954`, avg `0.025013`, median `0.019434`
- 20d: sample `16`, primary_hit `0.5625`, primary_closer `0.4375`, primary_mae `0.06805`, avg `-0.001291`, median `-0.023373`
- 60d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.078304`, avg `0.005849`, median `-0.014177`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3625`, primary_mae `0.025064`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.026354`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.033405`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.054478`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.072353`, avg `0.047937`, median `0.053364`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3625`, primary_mae `0.025064`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.026354`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.033405`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.054478`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.072353`, avg `0.047937`, median `0.053364`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3833`, primary_closer `0.35`, primary_mae `0.022925`, avg `0.00828`, median `0.008928`
- 5d: sample `60`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.023353`, avg `0.00904`, median `0.006404`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.45`, primary_mae `0.032281`, avg `0.017042`, median `0.009948`
- 20d: sample `60`, primary_hit `0.2`, primary_closer `0.35`, primary_mae `0.045634`, avg `0.037703`, median `0.03694`
- 60d: sample `60`, primary_hit `0.3167`, primary_closer `0.4`, primary_mae `0.065864`, avg `0.059722`, median `0.067587`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.031481`, avg `-0.003279`, median `0.001708`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.035357`, avg `0.008372`, median `0.016116`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.036777`, avg `0.022443`, median `0.019434`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.35`, primary_mae `0.081012`, avg `0.012449`, median `-0.007388`
- 60d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.091817`, avg `0.012581`, median `-0.014177`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3625`, primary_mae `0.025064`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.026354`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.033405`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.054478`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.072353`, avg `0.047937`, median `0.053364`

### flow_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.025838`, avg `0.010279`, median `0.010315`
- 5d: sample `40`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.027309`, avg `0.010318`, median `0.006404`
- 10d: sample `40`, primary_hit `0.4`, primary_closer `0.475`, primary_mae `0.035607`, avg `0.020779`, median `0.012783`
- 20d: sample `40`, primary_hit `0.2`, primary_closer `0.375`, primary_mae `0.048457`, avg `0.043298`, median `0.038807`
- 60d: sample `40`, primary_hit `0.3`, primary_closer `0.35`, primary_mae `0.071348`, avg `0.073998`, median `0.111523`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4125`, primary_closer `0.3625`, primary_mae `0.025064`, avg `0.005391`, median `0.008272`
- 5d: sample `80`, primary_hit `0.35`, primary_closer `0.3875`, primary_mae `0.026354`, avg `0.008873`, median `0.00906`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.4375`, primary_mae `0.033405`, avg `0.018392`, median `0.012538`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.35`, primary_mae `0.054478`, avg `0.03139`, median `0.036272`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.45`, primary_mae `0.072353`, avg `0.047937`, median `0.053364`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
