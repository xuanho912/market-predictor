# Historical Replay Benchmark

Generated at: `2026-10-07T18:59:46.382220+00:00`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.017789`
- secondary_mean_absolute_error: `0.015143`
- primary_error_advantage: `-0.002646`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.55`
- secondary_hit_rate: `0.45`
- primary_vs_secondary_accuracy_spread: `0.1`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.022839`
- secondary_mean_absolute_error: `0.01973`
- primary_error_advantage: `-0.003109`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5375`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.040435`
- secondary_mean_absolute_error: `0.029774`
- primary_error_advantage: `-0.010661`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.25`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.4375`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `-0.125`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.071695`
- secondary_mean_absolute_error: `0.05645`
- primary_error_advantage: `-0.015245`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2125`
- secondary_hit_rate: `0.7875`
- primary_vs_secondary_accuracy_spread: `-0.575`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.072433`
- secondary_mean_absolute_error: `0.057753`
- primary_error_advantage: `-0.01468`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015523`, as_primary `0`, as_primary_hit `None`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018996`, as_primary `0`, as_primary_hit `None`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.029046`, as_primary `0`, as_primary_hit `None`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.040585`, as_primary `0`, as_primary_hit `None`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.050674`, as_primary `0`, as_primary_hit `None`, avg `0.037608`, median `0.050314`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.015192`, as_primary `0`, as_primary_hit `None`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.019621`, as_primary `0`, as_primary_hit `None`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.032475`, as_primary `0`, as_primary_hit `None`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.059204`, as_primary `0`, as_primary_hit `None`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.057471`, as_primary `0`, as_primary_hit `None`, avg `0.037608`, median `0.050314`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.017789`, as_primary `80`, as_primary_hit `0.4`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.55`, path_mae `0.022839`, as_primary `80`, as_primary_hit `0.45`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.5375`, path_mae `0.040435`, as_primary `80`, as_primary_hit `0.4625`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, direction_hit `0.4375`, path_mae `0.071695`, as_primary `80`, as_primary_hit `0.5625`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.072433`, as_primary `80`, as_primary_hit `0.7875`, avg `0.037608`, median `0.050314`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.014828`, as_primary `0`, as_primary_hit `None`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, direction_hit `0.45`, path_mae `0.018956`, as_primary `0`, as_primary_hit `None`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, direction_hit `0.4625`, path_mae `0.027895`, as_primary `0`, as_primary_hit `None`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, direction_hit `0.5625`, path_mae `0.040393`, as_primary `0`, as_primary_hit `None`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.052884`, as_primary `0`, as_primary_hit `None`, avg `0.037608`, median `0.050314`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017789`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3625`, primary_mae `0.022839`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.040435`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.071695`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3`, primary_mae `0.072433`, avg `0.037608`, median `0.050314`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017789`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3625`, primary_mae `0.022839`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.040435`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.071695`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3`, primary_mae `0.072433`, avg `0.037608`, median `0.050314`

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

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.017789, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.022839, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.040435, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.071695, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2125, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.072433, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.014828, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017789, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.4375, 'primary_mean_absolute_error': 0.017789, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_vs_secondary_accuracy_spread': 0.1, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018956, 'direction_hit_rate': 0.45}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.022839, 'direction_hit_rate': 0.55}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.55, 'primary_closer_than_secondary_rate': 0.3625, 'primary_mean_absolute_error': 0.022839, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.027895, 'direction_hit_rate': 0.4625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040435, 'direction_hit_rate': 0.5375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.5375, 'primary_closer_than_secondary_rate': 0.3875, 'primary_mean_absolute_error': 0.040435, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': -0.125, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040393, 'direction_hit_rate': 0.5625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.071695, 'direction_hit_rate': 0.4375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.4375, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.071695, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_vs_secondary_accuracy_spread': -0.575, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050674, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072433, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 80, 'primary_hit_rate': 0.2125, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.072433, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.012309`, avg `-0.003344`, median `-0.000114`
- 5d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.012326`, avg `-0.003361`, median `0.000528`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.020671`, avg `0.000654`, median `0.001749`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.058065`, avg `0.009033`, median `0.032633`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.0`, primary_mae `0.04374`, avg `0.047583`, median `0.044525`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.009593`, avg `8.4e-05`, median `0.001336`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.3125`, primary_mae `0.011565`, avg `-0.002329`, median `0.001171`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.024085`, avg `0.007733`, median `0.010165`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.125`, primary_mae `0.063011`, avg `0.0197`, median `0.029416`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.1875`, primary_mae `0.040011`, avg `0.030562`, median `0.041986`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.021107`, avg `-0.012295`, median `-0.010671`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.020399`, avg `-0.010149`, median `-0.011444`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.051734`, avg `-0.004786`, median `-0.006323`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.095181`, avg `0.01986`, median `0.036789`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.097503`, avg `0.096701`, median `0.115176`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017789`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3625`, primary_mae `0.022839`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.040435`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.071695`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3`, primary_mae `0.072433`, avg `0.037608`, median `0.050314`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017789`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3625`, primary_mae `0.022839`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.040435`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.071695`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3`, primary_mae `0.072433`, avg `0.037608`, median `0.050314`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_conflicted
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.55`, primary_closer `0.45`, primary_mae `0.01687`, avg `-0.003674`, median `-0.003098`
- 5d: sample `60`, primary_hit `0.5333`, primary_closer `0.3833`, primary_mae `0.018743`, avg `-0.004644`, median `-0.002007`
- 10d: sample `60`, primary_hit `0.4667`, primary_closer `0.4333`, primary_mae `0.039582`, avg `-0.003599`, median `0.004006`
- 20d: sample `60`, primary_hit `0.4`, primary_closer `0.3667`, primary_mae `0.068001`, avg `0.009799`, median `0.015722`
- 60d: sample `60`, primary_hit `0.15`, primary_closer `0.2667`, primary_mae `0.060407`, avg `0.053776`, median `0.05712`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017789`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3625`, primary_mae `0.022839`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.040435`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.071695`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3`, primary_mae `0.072433`, avg `0.037608`, median `0.050314`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.4375`, primary_mae `0.017789`, avg `-0.00607`, median `-0.003662`
- 5d: sample `80`, primary_hit `0.55`, primary_closer `0.3625`, primary_mae `0.022839`, avg `-0.007331`, median `-0.005714`
- 10d: sample `80`, primary_hit `0.5375`, primary_closer `0.3875`, primary_mae `0.040435`, avg `-0.008747`, median `-0.006704`
- 20d: sample `80`, primary_hit `0.4375`, primary_closer `0.35`, primary_mae `0.071695`, avg `0.003459`, median `0.011992`
- 60d: sample `80`, primary_hit `0.2125`, primary_closer `0.3`, primary_mae `0.072433`, avg `0.037608`, median `0.050314`

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
