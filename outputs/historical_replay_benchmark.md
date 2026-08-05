# Historical Replay Benchmark

Generated at: `2026-08-05T21:41:46.827911+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
Overfit warning: `{'level': 'medium', 'reasons': ['high signal confirmation is mixed or not better in historical replay'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

> Historical replay is only a research benchmark. It is not forward validation and does not confirm alpha.

## Core Questions

- primary_scenario_beats_secondary: `yes_historical_replay`
- moderate_or_strong_edge_beats_no_edge: `insufficient_comparison_samples`
- signal_confirmation_high_samples_more_accurate: `historical_replay_mixed_or_not_better_keep_confidence_capped`
- data_enhancement_improves_prediction_quality: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
- forward_validation_required: `yes_daily_forward_validation_remains_decisive`

## Primary vs Secondary Scenario

### 3d
- sample_size: `80`
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.015452`
- secondary_mean_absolute_error: `0.017249`
- primary_error_advantage: `0.001797`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.3875`
- primary_vs_secondary_accuracy_spread: `0.225`
- primary_closer_than_secondary_rate: `0.6`
- primary_mean_absolute_error: `0.018992`
- secondary_mean_absolute_error: `0.02328`
- primary_error_advantage: `0.004288`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.6`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.525`
- secondary_hit_rate: `0.475`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.029818`
- secondary_mean_absolute_error: `0.037317`
- primary_error_advantage: `0.007499`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.575`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.6375`
- primary_mean_absolute_error: `0.056988`
- secondary_mean_absolute_error: `0.07221`
- primary_error_advantage: `0.015222`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.6375`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.073745`
- secondary_mean_absolute_error: `0.074997`
- primary_error_advantage: `0.001252`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.013778`, as_primary `0`, as_primary_hit `None`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.017113`, as_primary `0`, as_primary_hit `None`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.026199`, as_primary `0`, as_primary_hit `None`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.037706`, as_primary `0`, as_primary_hit `None`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.06125`, as_primary `0`, as_primary_hit `None`, avg `0.021114`, median `0.019108`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.016067`, as_primary `60`, as_primary_hit `0.5667`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.022325`, as_primary `60`, as_primary_hit `0.6833`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.034376`, as_primary `60`, as_primary_hit `0.55`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.058605`, as_primary `60`, as_primary_hit `0.6667`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.077118`, as_primary `60`, as_primary_hit `0.5`, avg `0.021114`, median `0.019108`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016634`, as_primary `20`, as_primary_hit `0.7`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, direction_hit `0.3375`, path_mae `0.019947`, as_primary `20`, as_primary_hit `0.6`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, direction_hit `0.45`, path_mae `0.032759`, as_primary `20`, as_primary_hit `0.55`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.070592`, as_primary `20`, as_primary_hit `0.75`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.071623`, as_primary `20`, as_primary_hit `0.65`, avg `0.021114`, median `0.019108`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.013717`, as_primary `0`, as_primary_hit `None`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.0157`, as_primary `0`, as_primary_hit `None`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, direction_hit `0.55`, path_mae `0.023728`, as_primary `0`, as_primary_hit `None`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.035665`, as_primary `0`, as_primary_hit `None`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.056797`, as_primary `0`, as_primary_hit `None`, avg `0.021114`, median `0.019108`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.015452`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.018992`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.029818`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.6375`, primary_mae `0.056988`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.073745`, avg `0.021114`, median `0.019108`

## Predictor Performance

### bounce_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.015452`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.018992`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.029818`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.6375`, primary_mae `0.056988`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.073745`, avg `0.021114`, median `0.019108`

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
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.015452, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6125, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.018992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.029818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.6375, 'primary_mean_absolute_error': 0.056988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.073745, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013717, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016634, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.5125, 'primary_mean_absolute_error': 0.015452, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_vs_secondary_accuracy_spread': 0.225, 'primary_closer_than_secondary_rate': 0.6, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0157, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022325, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6125, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.018992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023728, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.034376, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.525, 'primary_closer_than_secondary_rate': 0.575, 'primary_mean_absolute_error': 0.029818, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.6375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035665, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.070592, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5625, 'primary_closer_than_secondary_rate': 0.6375, 'primary_mean_absolute_error': 0.056988, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056797, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.077118, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4625, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.073745, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.015793`, avg `-0.00181`, median `0.004081`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.01461`, avg `0.003233`, median `0.003509`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021093`, avg `0.004693`, median `0.007471`
- 20d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.047483`, avg `0.011417`, median `0.02136`
- 60d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.08847`, avg `-0.011059`, median `-0.02547`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.013346`, avg `0.000139`, median `0.004136`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.014898`, avg `0.002517`, median `0.003509`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021178`, avg `0.001936`, median `0.002264`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.045756`, avg `0.012468`, median `0.016513`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.080114`, avg `0.00406`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.013346`, avg `0.000139`, median `0.004136`
- 5d: sample `16`, primary_hit `0.625`, primary_closer `0.5625`, primary_mae `0.014898`, avg `0.002517`, median `0.003509`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.021178`, avg `0.001936`, median `0.002264`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.6875`, primary_mae `0.045756`, avg `0.012468`, median `0.016513`
- 60d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.080114`, avg `0.00406`, median `-0.012556`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.015452`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.018992`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.029818`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.6375`, primary_mae `0.056988`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.073745`, avg `0.021114`, median `0.019108`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.015452`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.018992`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.029818`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.6375`, primary_mae `0.056988`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.073745`, avg `0.021114`, median `0.019108`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5667`, primary_closer `0.5`, primary_mae `0.01427`, avg `0.000163`, median `0.001778`
- 5d: sample `60`, primary_hit `0.6833`, primary_closer `0.5667`, primary_mae `0.015866`, avg `0.00361`, median `0.005202`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.024823`, avg `0.00215`, median `0.005212`
- 20d: sample `60`, primary_hit `0.6667`, primary_closer `0.6667`, primary_mae `0.044831`, avg `0.004187`, median `0.012625`
- 60d: sample `60`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.064804`, avg `0.010028`, median `0.004522`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.3`, primary_closer `0.55`, primary_mae `0.018998`, avg `0.005177`, median `0.009658`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.7`, primary_mae `0.028369`, avg `0.003033`, median `0.005857`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.75`, primary_mae `0.044806`, avg `0.010512`, median `0.006552`
- 20d: sample `20`, primary_hit `0.25`, primary_closer `0.55`, primary_mae `0.093458`, avg `0.025319`, median `0.015461`
- 60d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.100566`, avg `0.054371`, median `0.070486`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.015452`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.018992`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.029818`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.6375`, primary_mae `0.056988`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.073745`, avg `0.021114`, median `0.019108`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.5125`, primary_mae `0.015452`, avg `0.001416`, median `0.003771`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.6`, primary_mae `0.018992`, avg `0.003466`, median `0.005202`
- 10d: sample `80`, primary_hit `0.525`, primary_closer `0.575`, primary_mae `0.029818`, avg `0.004241`, median `0.005212`
- 20d: sample `80`, primary_hit `0.5625`, primary_closer `0.6375`, primary_mae `0.056988`, avg `0.00947`, median `0.013068`
- 60d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.073745`, avg `0.021114`, median `0.019108`

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
