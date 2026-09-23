# Historical Replay Benchmark

Generated at: `2026-09-23T01:35:13.293085+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `PROMISING`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.019418`
- secondary_mean_absolute_error: `0.01958`
- primary_error_advantage: `0.000162`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.625`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.4625`
- primary_mean_absolute_error: `0.024576`
- secondary_mean_absolute_error: `0.022031`
- primary_error_advantage: `-0.002545`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4625`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.05`
- primary_closer_than_secondary_rate: `0.4875`
- primary_mean_absolute_error: `0.036514`
- secondary_mean_absolute_error: `0.038666`
- primary_error_advantage: `0.002152`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4875`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.8375`
- secondary_hit_rate: `0.5875`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.057816`
- secondary_mean_absolute_error: `0.043583`
- primary_error_advantage: `-0.014233`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.3625`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.85`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.25`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.062274`
- secondary_mean_absolute_error: `0.069549`
- primary_error_advantage: `0.007275`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.5125`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.016856`, as_primary `0`, as_primary_hit `None`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.021439`, as_primary `0`, as_primary_hit `None`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.03127`, as_primary `0`, as_primary_hit `None`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, direction_hit `0.8375`, path_mae `0.039446`, as_primary `0`, as_primary_hit `None`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.052933`, as_primary `0`, as_primary_hit `None`, avg `0.066426`, median `0.08262`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.019418`, as_primary `80`, as_primary_hit `0.6375`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.024576`, as_primary `80`, as_primary_hit `0.625`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.036514`, as_primary `80`, as_primary_hit `0.6375`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, direction_hit `0.8375`, path_mae `0.057816`, as_primary `80`, as_primary_hit `0.8375`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.062274`, as_primary `80`, as_primary_hit `0.85`, avg `0.066426`, median `0.08262`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.020356`, as_primary `0`, as_primary_hit `None`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, direction_hit `0.375`, path_mae `0.022757`, as_primary `0`, as_primary_hit `None`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, direction_hit `0.3625`, path_mae `0.039209`, as_primary `0`, as_primary_hit `None`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, direction_hit `0.1625`, path_mae `0.0515`, as_primary `0`, as_primary_hit `None`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, direction_hit `0.15`, path_mae `0.076428`, as_primary `0`, as_primary_hit `None`, avg `0.066426`, median `0.08262`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.016928`, as_primary `0`, as_primary_hit `None`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, direction_hit `0.625`, path_mae `0.019728`, as_primary `0`, as_primary_hit `None`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, direction_hit `0.6375`, path_mae `0.029702`, as_primary `0`, as_primary_hit `None`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, direction_hit `0.8375`, path_mae `0.033619`, as_primary `0`, as_primary_hit `None`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, direction_hit `0.85`, path_mae `0.052225`, as_primary `0`, as_primary_hit `None`, avg `0.066426`, median `0.08262`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.019418`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.024576`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.036514`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, primary_hit `0.8375`, primary_closer `0.3625`, primary_mae `0.057816`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, primary_hit `0.85`, primary_closer `0.5125`, primary_mae `0.062274`, avg `0.066426`, median `0.08262`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.55`, primary_mae `0.011013`, avg `0.00496`, median `0.009174`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.01328`, avg `0.004889`, median `0.010121`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.6`, primary_mae `0.015398`, avg `0.007392`, median `0.010263`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.3`, primary_mae `0.03191`, avg `0.026815`, median `0.030823`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.5`, primary_mae `0.028617`, avg `0.084077`, median `0.083602`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6`, primary_closer `0.55`, primary_mae `0.02222`, avg `0.003901`, median `0.010061`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.4167`, primary_mae `0.028342`, avg `0.004874`, median `0.009885`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.45`, primary_mae `0.043552`, avg `0.009672`, median `0.007609`
- 20d: sample `60`, primary_hit `0.8333`, primary_closer `0.3833`, primary_mae `0.066452`, avg `0.034757`, median `0.029212`
- 60d: sample `60`, primary_hit `0.8167`, primary_closer `0.5167`, primary_mae `0.073494`, avg `0.060542`, median `0.078249`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.011013, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01328, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015398, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03191, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.028617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016856, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020356, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.011013, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.4625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019728, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024576, 'direction_hit_rate': 0.625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01328, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.05, 'primary_closer_than_secondary_rate': 0.4875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029702, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039209, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.015398, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.8375, 'secondary_hit_rate': 0.5875, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.033619, 'direction_hit_rate': 0.8375}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057816, 'direction_hit_rate': 0.8375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.85, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03191, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.85, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.25, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052225, 'direction_hit_rate': 0.85}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.076428, 'direction_hit_rate': 0.15}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.028617, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.013113`, avg `0.011441`, median `0.019319`
- 5d: sample `8`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.019887`, avg `0.013802`, median `0.011781`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.025857`, avg `0.016973`, median `0.017921`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.019818`, avg `0.061725`, median `0.060676`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.75`, primary_mae `0.032184`, avg `0.085751`, median `0.098383`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.011792`, avg `0.009858`, median `0.01387`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.018509`, avg `0.01299`, median `0.012047`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.023138`, avg `0.018372`, median `0.018911`
- 20d: sample `16`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.028144`, avg `0.053391`, median `0.058396`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.030602`, avg `0.089577`, median `0.096338`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.011792`, avg `0.009858`, median `0.01387`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.018509`, avg `0.01299`, median `0.012047`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.023138`, avg `0.018372`, median `0.018911`
- 20d: sample `16`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.028144`, avg `0.053391`, median `0.058396`
- 60d: sample `16`, primary_hit `0.9375`, primary_closer `0.5625`, primary_mae `0.030602`, avg `0.089577`, median `0.096338`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.019418`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.024576`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.036514`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, primary_hit `0.8375`, primary_closer `0.3625`, primary_mae `0.057816`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, primary_hit `0.85`, primary_closer `0.5125`, primary_mae `0.062274`, avg `0.066426`, median `0.08262`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.019418`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.024576`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.036514`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, primary_hit `0.8375`, primary_closer `0.3625`, primary_mae `0.057816`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, primary_hit `0.85`, primary_closer `0.5125`, primary_mae `0.062274`, avg `0.066426`, median `0.08262`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.75`, primary_closer `0.55`, primary_mae `0.011013`, avg `0.00496`, median `0.009174`
- 5d: sample `20`, primary_hit `0.65`, primary_closer `0.6`, primary_mae `0.01328`, avg `0.004889`, median `0.010121`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.6`, primary_mae `0.015398`, avg `0.007392`, median `0.010263`
- 20d: sample `20`, primary_hit `0.85`, primary_closer `0.3`, primary_mae `0.03191`, avg `0.026815`, median `0.030823`
- 60d: sample `20`, primary_hit `0.95`, primary_closer `0.5`, primary_mae `0.028617`, avg `0.084077`, median `0.083602`

### breadth_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.019418`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.024576`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.036514`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, primary_hit `0.8375`, primary_closer `0.3625`, primary_mae `0.057816`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, primary_hit `0.85`, primary_closer `0.5125`, primary_mae `0.062274`, avg `0.066426`, median `0.08262`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.019418`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.024576`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.036514`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, primary_hit `0.8375`, primary_closer `0.3625`, primary_mae `0.057816`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, primary_hit `0.85`, primary_closer `0.5125`, primary_mae `0.062274`, avg `0.066426`, median `0.08262`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.55`, primary_mae `0.019418`, avg `0.004166`, median `0.010061`
- 5d: sample `80`, primary_hit `0.625`, primary_closer `0.4625`, primary_mae `0.024576`, avg `0.004877`, median `0.009885`
- 10d: sample `80`, primary_hit `0.6375`, primary_closer `0.4875`, primary_mae `0.036514`, avg `0.009102`, median `0.009969`
- 20d: sample `80`, primary_hit `0.8375`, primary_closer `0.3625`, primary_mae `0.057816`, avg `0.032772`, median `0.030135`
- 60d: sample `80`, primary_hit `0.85`, primary_closer `0.5125`, primary_mae `0.062274`, avg `0.066426`, median `0.08262`

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
