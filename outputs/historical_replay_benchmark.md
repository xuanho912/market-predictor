# Historical Replay Benchmark

Generated at: `2026-11-03T03:56:15.309563+00:00`
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
- primary_hit_rate: `0.5`
- secondary_hit_rate: `0.5`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.028928`
- secondary_mean_absolute_error: `0.023534`
- primary_error_advantage: `-0.005394`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.55`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.45`
- secondary_hit_rate: `0.55`
- primary_vs_secondary_accuracy_spread: `-0.1`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.037626`
- secondary_mean_absolute_error: `0.030336`
- primary_error_advantage: `-0.00729`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.65`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.35`
- secondary_hit_rate: `0.65`
- primary_vs_secondary_accuracy_spread: `-0.3`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.052588`
- secondary_mean_absolute_error: `0.039095`
- primary_error_advantage: `-0.013493`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.275`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `-0.45`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.067846`
- secondary_mean_absolute_error: `0.044152`
- primary_error_advantage: `-0.023694`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.225`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `-0.55`
- primary_closer_than_secondary_rate: `0.3375`
- primary_mean_absolute_error: `0.058234`
- secondary_mean_absolute_error: `0.042155`
- primary_error_advantage: `-0.016079`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.02048`, as_primary `0`, as_primary_hit `None`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.026945`, as_primary `0`, as_primary_hit `None`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.032352`, as_primary `0`, as_primary_hit `None`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.038928`, as_primary `0`, as_primary_hit `None`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.040706`, as_primary `0`, as_primary_hit `None`, avg `0.043598`, median `0.058454`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.02469`, as_primary `0`, as_primary_hit `None`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.032258`, as_primary `0`, as_primary_hit `None`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.042572`, as_primary `0`, as_primary_hit `None`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.055223`, as_primary `0`, as_primary_hit `None`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.050479`, as_primary `0`, as_primary_hit `None`, avg `0.043598`, median `0.058454`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.028928`, as_primary `80`, as_primary_hit `0.5`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.037626`, as_primary `80`, as_primary_hit `0.55`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, direction_hit `0.35`, path_mae `0.052588`, as_primary `80`, as_primary_hit `0.65`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, direction_hit `0.275`, path_mae `0.067846`, as_primary `80`, as_primary_hit `0.725`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, direction_hit `0.225`, path_mae `0.058234`, as_primary `80`, as_primary_hit `0.775`, avg `0.043598`, median `0.058454`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5`, path_mae `0.020106`, as_primary `0`, as_primary_hit `None`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.024968`, as_primary `0`, as_primary_hit `None`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, direction_hit `0.65`, path_mae `0.032299`, as_primary `0`, as_primary_hit `None`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, direction_hit `0.725`, path_mae `0.03842`, as_primary `0`, as_primary_hit `None`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, direction_hit `0.775`, path_mae `0.040606`, as_primary `0`, as_primary_hit `None`, avg `0.043598`, median `0.058454`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.028928`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.037626`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.052588`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.067846`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.058234`, avg `0.043598`, median `0.058454`

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
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.028928`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.037626`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.052588`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.067846`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.058234`, avg `0.043598`, median `0.058454`

## Best Predictor By Horizon

- 3d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.028928, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.037626, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.052588, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.067846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.058234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020106, 'direction_hit_rate': 0.5}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028928, 'direction_hit_rate': 0.5}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.028928, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_vs_secondary_accuracy_spread': -0.1, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.024968, 'direction_hit_rate': 0.55}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.037626, 'direction_hit_rate': 0.45}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.45, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.037626, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_vs_secondary_accuracy_spread': -0.3, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.032299, 'direction_hit_rate': 0.65}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052588, 'direction_hit_rate': 0.35}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.375, 'primary_mean_absolute_error': 0.052588, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': -0.45, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03842, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.067846, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.275, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.067846, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': -0.55, 'primary_closer_than_secondary_rate': 0.3375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040606, 'direction_hit_rate': 0.775}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058234, 'direction_hit_rate': 0.225}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 80, 'primary_hit_rate': 0.225, 'primary_closer_than_secondary_rate': 0.3375, 'primary_mean_absolute_error': 0.058234, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.012649`, avg `0.003696`, median `0.003938`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.625`, primary_mae `0.019811`, avg `0.007888`, median `0.009272`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.044538`, avg `0.004186`, median `0.002861`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.058439`, avg `0.027756`, median `0.033551`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.070012`, avg `0.037654`, median `0.050745`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.625`, primary_mae `0.013491`, avg `-0.00096`, median `-0.004204`
- 5d: sample `16`, primary_hit `0.5`, primary_closer `0.75`, primary_mae `0.016273`, avg `0.002168`, median `0.000544`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.04071`, avg `0.004861`, median `0.002861`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.375`, primary_mae `0.05757`, avg `0.022166`, median `0.029414`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.073312`, avg `0.042971`, median `0.04831`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.039935`, avg `-0.002071`, median `-0.002931`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.035737`, avg `0.009197`, median `0.002887`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.058598`, avg `0.028332`, median `0.032704`
- 20d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.069765`, avg `0.049859`, median `0.053826`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.375`, primary_mae `0.043925`, avg `0.047953`, median `0.065439`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.028928`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.037626`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.052588`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.067846`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.058234`, avg `0.043598`, median `0.058454`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.028928`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.037626`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.052588`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.067846`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.058234`, avg `0.043598`, median `0.058454`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.5167`, primary_closer `0.45`, primary_mae `0.02488`, avg `0.001522`, median `-0.000692`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.038279`, avg `0.002414`, median `0.007096`
- 10d: sample `60`, primary_hit `0.3667`, primary_closer `0.4`, primary_mae `0.051176`, avg `0.010263`, median `0.011579`
- 20d: sample `60`, primary_hit `0.3167`, primary_closer `0.3833`, primary_mae `0.068949`, avg `0.02278`, median `0.029433`
- 60d: sample `60`, primary_hit `0.25`, primary_closer `0.3167`, primary_mae `0.063981`, avg `0.04225`, median `0.055443`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.45`, primary_closer `0.2`, primary_mae `0.04107`, avg `0.000522`, median `0.001007`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.4`, primary_mae `0.035666`, avg `0.009718`, median `0.002887`
- 10d: sample `20`, primary_hit `0.3`, primary_closer `0.3`, primary_mae `0.056824`, avg `0.020885`, median `0.029666`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.2`, primary_mae `0.064536`, avg `0.043442`, median `0.051724`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.4`, primary_mae `0.040991`, avg `0.047641`, median `0.065439`

### options_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.028928`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.037626`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.052588`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.067846`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.058234`, avg `0.043598`, median `0.058454`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.028928`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.037626`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.052588`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.067846`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.058234`, avg `0.043598`, median `0.058454`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5`, primary_closer `0.3875`, primary_mae `0.028928`, avg `0.001272`, median `-4.2e-05`
- 5d: sample `80`, primary_hit `0.45`, primary_closer `0.4375`, primary_mae `0.037626`, avg `0.00424`, median `0.006642`
- 10d: sample `80`, primary_hit `0.35`, primary_closer `0.375`, primary_mae `0.052588`, avg `0.012919`, median `0.019847`
- 20d: sample `80`, primary_hit `0.275`, primary_closer `0.3375`, primary_mae `0.067846`, avg `0.027945`, median `0.038522`
- 60d: sample `80`, primary_hit `0.225`, primary_closer `0.3375`, primary_mae `0.058234`, avg `0.043598`, median `0.058454`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
