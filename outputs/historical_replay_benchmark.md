# Historical Replay Benchmark

Generated at: `2026-08-10T13:48:28.221806+00:00`
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
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.019084`
- secondary_mean_absolute_error: `0.017106`
- primary_error_advantage: `-0.001978`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.02196`
- secondary_mean_absolute_error: `0.020891`
- primary_error_advantage: `-0.001069`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.45`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.03693`
- secondary_mean_absolute_error: `0.030791`
- primary_error_advantage: `-0.006139`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3667`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `-0.2`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.076512`
- secondary_mean_absolute_error: `0.055693`
- primary_error_advantage: `-0.020819`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.2667`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3875`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `-0.225`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.083557`
- secondary_mean_absolute_error: `0.069251`
- primary_error_advantage: `-0.014306`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013894`, as_primary `0`, as_primary_hit `None`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.018999`, as_primary `0`, as_primary_hit `None`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.026626`, as_primary `0`, as_primary_hit `None`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.042468`, as_primary `0`, as_primary_hit `None`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.067955`, as_primary `0`, as_primary_hit `None`, avg `0.018203`, median `0.019108`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.016065`, as_primary `20`, as_primary_hit `0.5`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.024222`, as_primary `20`, as_primary_hit `0.75`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.034913`, as_primary `20`, as_primary_hit `0.5`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.062773`, as_primary `20`, as_primary_hit `0.6`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.08232`, as_primary `20`, as_primary_hit `0.35`, avg `0.018203`, median `0.019108`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.020706`, as_primary `60`, as_primary_hit `0.65`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, direction_hit `0.3375`, path_mae `0.022442`, as_primary `60`, as_primary_hit `0.6333`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.039289`, as_primary `60`, as_primary_hit `0.55`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, direction_hit `0.35`, path_mae `0.082615`, as_primary `60`, as_primary_hit `0.6667`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, direction_hit `0.4625`, path_mae `0.081602`, as_primary `60`, as_primary_hit `0.6`, avg `0.018203`, median `0.019108`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013868`, as_primary `0`, as_primary_hit `None`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.017684`, as_primary `0`, as_primary_hit `None`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.025474`, as_primary `0`, as_primary_hit `None`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, direction_hit `0.65`, path_mae `0.040686`, as_primary `0`, as_primary_hit `None`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, direction_hit `0.5375`, path_mae `0.062673`, as_primary `0`, as_primary_hit `None`, avg `0.018203`, median `0.019108`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.5`, primary_mae `0.019084`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.02196`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.03693`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.076512`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.083557`, avg `0.018203`, median `0.019108`

## Predictor Performance

### bounce_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.5167`, primary_mae `0.015421`, avg `0.003781`, median `0.004555`
- 5d: sample `60`, primary_hit `0.4833`, primary_closer `0.4667`, primary_mae `0.021205`, avg `0.004401`, median `0.005644`
- 10d: sample `60`, primary_hit `0.4833`, primary_closer `0.4167`, primary_mae `0.040047`, avg `0.002792`, median `0.001089`
- 20d: sample `60`, primary_hit `0.4333`, primary_closer `0.35`, primary_mae `0.0786`, avg `0.001672`, median `0.012734`
- 60d: sample `60`, primary_hit `0.35`, primary_closer `0.3667`, primary_mae `0.087902`, avg `0.018383`, median `0.021115`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.030073`, avg `-0.001655`, median `0.002617`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.6`, primary_mae `0.024225`, avg `0.003606`, median `0.003509`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.45`, primary_mae `0.027579`, avg `0.007335`, median `0.011059`
- 20d: sample `20`, primary_hit `0.3`, primary_closer `0.4`, primary_mae `0.070247`, avg `0.015715`, median `0.023697`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.55`, primary_mae `0.070522`, avg `0.017662`, median `0.003555`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.015421, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.021205, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027579, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070247, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.070522, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013868, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020706, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.3667, 'primary_closer_than_secondary_rate': 0.5167, 'primary_mean_absolute_error': 0.015421, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017684, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024222, 'direction_hit_rate': 0.6625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 60, 'primary_hit_rate': 0.4833, 'primary_closer_than_secondary_rate': 0.4667, 'primary_mean_absolute_error': 0.021205, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025474, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039289, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.027579, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': -0.2, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040686, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.082615, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.3, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.070247, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': -0.225, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062673, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.08232, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.070522, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.028904`, avg `0.000217`, median `0.004081`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.02256`, avg `0.003846`, median `0.004667`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.025678`, avg `0.009059`, median `0.01669`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.067799`, avg `0.018489`, median `0.02136`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.75`, primary_mae `0.042449`, avg `-0.002859`, median `-0.02547`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.027875`, avg `-0.004765`, median `-0.000883`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.023514`, avg `0.00155`, median `0.003509`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.5`, primary_mae `0.026198`, avg `0.004817`, median `0.006104`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.4375`, primary_mae `0.066706`, avg `0.010868`, median `0.02136`
- 60d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.060198`, avg `0.00672`, median `-0.012556`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.014038`, avg `0.008376`, median `0.011155`
- 5d: sample `16`, primary_hit `0.25`, primary_closer `0.3125`, primary_mae `0.022825`, avg `0.009263`, median `0.014435`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.046357`, avg `-0.000975`, median `-0.001807`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.093829`, avg `-0.007949`, median `0.013942`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.1875`, primary_mae `0.109896`, avg `0.029685`, median `0.055366`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.5`, primary_mae `0.019084`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.02196`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.03693`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.076512`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.083557`, avg `0.018203`, median `0.019108`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.5`, primary_mae `0.019084`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.02196`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.03693`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.076512`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.083557`, avg `0.018203`, median `0.019108`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.475`, primary_closer `0.65`, primary_mae `0.019645`, avg `-0.002085`, median `0.000173`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.625`, primary_mae `0.017566`, avg `0.003035`, median `0.00431`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.022284`, avg `0.003946`, median `0.009079`
- 20d: sample `40`, primary_hit `0.45`, primary_closer `0.525`, primary_mae `0.051986`, avg `0.006119`, median `0.016623`
- 60d: sample `40`, primary_hit `0.425`, primary_closer `0.475`, primary_mae `0.070075`, avg `0.004189`, median `-0.017782`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.024705`, avg `0.007758`, median `0.010408`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.031807`, avg `0.004451`, median `0.005967`
- 10d: sample `20`, primary_hit `0.45`, primary_closer `0.25`, primary_mae `0.059746`, avg `0.009234`, median `0.006552`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.15`, primary_mae `0.111151`, avg `0.01616`, median `0.013042`
- 60d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.093277`, avg `0.042095`, median `0.022458`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.5`, primary_mae `0.019084`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.02196`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.03693`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.076512`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.083557`, avg `0.018203`, median `0.019108`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3875`, primary_closer `0.5`, primary_mae `0.019084`, avg `0.002422`, median `0.004273`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.5`, primary_mae `0.02196`, avg `0.004202`, median `0.005202`
- 10d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.03693`, avg `0.003927`, median `0.003776`
- 20d: sample `80`, primary_hit `0.4`, primary_closer `0.3625`, primary_mae `0.076512`, avg `0.005182`, median `0.013942`
- 60d: sample `80`, primary_hit `0.3875`, primary_closer `0.4125`, primary_mae `0.083557`, avg `0.018203`, median `0.019108`

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
