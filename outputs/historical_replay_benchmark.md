# Historical Replay Benchmark

Generated at: `2026-09-22T23:48:08.312892+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `STRONG_HISTORICAL_ONLY`
Overfit warning: `{'level': 'low', 'reasons': [], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_supportive_but_not_forward_validated`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.015708`
- secondary_mean_absolute_error: `0.016131`
- primary_error_advantage: `0.000423`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.018335`
- secondary_mean_absolute_error: `0.018993`
- primary_error_advantage: `0.000658`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.024342`
- secondary_mean_absolute_error: `0.025933`
- primary_error_advantage: `0.001591`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4833`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.6`
- primary_mean_absolute_error: `0.054148`
- secondary_mean_absolute_error: `0.066322`
- primary_error_advantage: `0.012174`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.3625`
- primary_vs_secondary_accuracy_spread: `0.275`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.071328`
- secondary_mean_absolute_error: `0.0856`
- primary_error_advantage: `0.014272`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.55`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.014467`, as_primary `0`, as_primary_hit `None`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.015822`, as_primary `0`, as_primary_hit `None`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.020009`, as_primary `0`, as_primary_hit `None`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.036924`, as_primary `0`, as_primary_hit `None`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.05753`, as_primary `0`, as_primary_hit `None`, avg `0.018593`, median `0.029695`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.016598`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.019073`, as_primary `60`, as_primary_hit `0.4833`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.026859`, as_primary `60`, as_primary_hit `0.4`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.058384`, as_primary `60`, as_primary_hit `0.6`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.075943`, as_primary `60`, as_primary_hit `0.7`, avg `0.018593`, median `0.029695`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5625`, path_mae `0.015241`, as_primary `20`, as_primary_hit `0.3`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.018255`, as_primary `20`, as_primary_hit `0.15`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, direction_hit `0.6625`, path_mae `0.023417`, as_primary `20`, as_primary_hit `0.15`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.45`, path_mae `0.062086`, as_primary `20`, as_primary_hit `0.4`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, direction_hit `0.3375`, path_mae `0.080985`, as_primary `20`, as_primary_hit `0.55`, avg `0.018593`, median `0.029695`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4375`, path_mae `0.0141`, as_primary `0`, as_primary_hit `None`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.015309`, as_primary `0`, as_primary_hit `None`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, direction_hit `0.3375`, path_mae `0.018636`, as_primary `0`, as_primary_hit `None`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, direction_hit `0.55`, path_mae `0.036509`, as_primary `0`, as_primary_hit `None`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, direction_hit `0.6625`, path_mae `0.05785`, as_primary `0`, as_primary_hit `None`, avg `0.018593`, median `0.029695`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.4833`, primary_closer `0.55`, primary_mae `0.016604`, avg `-0.003773`, median `-0.001442`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4833`, primary_mae `0.01786`, avg `-0.007418`, median `-0.000992`
- 10d: sample `60`, primary_hit `0.4`, primary_closer `0.4833`, primary_mae `0.026153`, avg `-0.005051`, median `-0.007166`
- 20d: sample `60`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.05173`, avg `0.010308`, median `0.017648`
- 60d: sample `60`, primary_hit `0.7`, primary_closer `0.55`, primary_mae `0.064653`, avg `0.023588`, median `0.034349`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.013021`, avg `-0.00475`, median `-0.003921`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.019761`, avg `-0.013547`, median `-0.013012`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.75`, primary_mae `0.01891`, avg `-0.024798`, median `-0.032156`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.061403`, avg `-0.011795`, median `-0.029855`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.091351`, avg `0.003609`, median `0.009913`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.55`, primary_closer `0.525`, primary_mae `0.015442`, avg `-0.000753`, median `0.002996`
- 5d: sample `40`, primary_hit `0.525`, primary_closer `0.425`, primary_mae `0.017627`, avg `-0.00411`, median `0.000776`
- 10d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.030006`, avg `-0.00164`, median `-0.005578`
- 20d: sample `40`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.04976`, avg `0.012374`, median `0.015722`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.55`, primary_mae `0.047126`, avg `0.024551`, median `0.030631`

### downside_continuation_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.013021`, avg `-0.00475`, median `-0.003921`
- 5d: sample `20`, primary_hit `0.85`, primary_closer `0.5`, primary_mae `0.019761`, avg `-0.013547`, median `-0.013012`
- 10d: sample `20`, primary_hit `0.85`, primary_closer `0.75`, primary_mae `0.01891`, avg `-0.024798`, median `-0.032156`
- 20d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.061403`, avg `-0.011795`, median `-0.029855`
- 60d: sample `20`, primary_hit `0.45`, primary_closer `0.55`, primary_mae `0.091351`, avg `0.003609`, median `0.009913`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.35`, primary_closer `0.6`, primary_mae `0.018928`, avg `-0.009815`, median `-0.010064`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.018327`, avg `-0.014033`, median `-0.010525`
- 10d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.018446`, avg `-0.011873`, median `-0.013277`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.7`, primary_mae `0.055671`, avg `0.006174`, median `0.020913`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.099708`, avg `0.021662`, median `0.041779`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.013021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017627, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.04976, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.047126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0141, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016598, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.013021, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.015309, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019073, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.017627, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018636, 'direction_hit_rate': 0.3375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026859, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.018446, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.6, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036509, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062086, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.04976, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_vs_secondary_accuracy_spread': 0.275, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.05753, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.080985, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.725, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.047126, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.125`, primary_closer `0.375`, primary_mae `0.020321`, avg `-0.020054`, median `-0.02628`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.019313`, avg `-0.016882`, median `-0.014301`
- 10d: sample `8`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.018131`, avg `-0.018343`, median `-0.017516`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.06322`, avg `-0.00332`, median `0.020913`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.110897`, avg `0.0071`, median `0.029112`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.5625`, primary_mae `0.017905`, avg `-0.011682`, median `-0.010064`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.5625`, primary_mae `0.018383`, avg `-0.01475`, median `-0.016241`
- 10d: sample `16`, primary_hit `0.1875`, primary_closer `0.5625`, primary_mae `0.018675`, avg `-0.013101`, median `-0.013277`
- 20d: sample `16`, primary_hit `0.625`, primary_closer `0.6875`, primary_mae `0.056311`, avg `0.006021`, median `0.020913`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.096843`, avg `0.023929`, median `0.052632`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.008993`, avg `-0.006484`, median `-0.003921`
- 5d: sample `16`, primary_hit `0.875`, primary_closer `0.5625`, primary_mae `0.018452`, avg `-0.016096`, median `-0.017739`
- 10d: sample `16`, primary_hit `0.9375`, primary_closer `0.8125`, primary_mae `0.013595`, avg `-0.031524`, median `-0.034582`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.057414`, avg `-0.016638`, median `-0.035529`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.089214`, avg `-0.004289`, median `0.003532`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5625`, primary_mae `0.015708`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.018335`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.024342`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.054148`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.071328`, avg `0.018593`, median `0.029695`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5625`, primary_mae `0.015708`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.018335`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.024342`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.054148`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.071328`, avg `0.018593`, median `0.029695`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.019994`, avg `-0.006821`, median `-0.008299`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.021701`, avg `-0.010271`, median `-0.012875`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.55`, primary_mae `0.026852`, avg `-0.01304`, median `-0.010196`
- 20d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.040657`, avg `0.008675`, median `0.007177`
- 60d: sample `20`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.04978`, avg `0.022801`, median `0.043394`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5625`, primary_mae `0.015708`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.018335`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.024342`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.054148`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.071328`, avg `0.018593`, median `0.029695`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5625`, primary_mae `0.015708`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.018335`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.024342`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.054148`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.071328`, avg `0.018593`, median `0.029695`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5375`, primary_closer `0.5625`, primary_mae `0.015708`, avg `-0.004018`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.4875`, primary_mae `0.018335`, avg `-0.00895`, median `-0.005726`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.55`, primary_mae `0.024342`, avg `-0.009988`, median `-0.012422`
- 20d: sample `80`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.054148`, avg `0.004782`, median `0.01126`
- 60d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.071328`, avg `0.018593`, median `0.029695`

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
