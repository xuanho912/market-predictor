# Historical Replay Benchmark

Generated at: `2026-09-05T00:55:41.497128+00:00`
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
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.25`
- primary_mean_absolute_error: `0.026282`
- secondary_mean_absolute_error: `0.016524`
- primary_error_advantage: `-0.009758`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.3375`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `-0.325`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.02804`
- secondary_mean_absolute_error: `0.019716`
- primary_error_advantage: `-0.008324`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.325`
- primary_mean_absolute_error: `0.041576`
- secondary_mean_absolute_error: `0.028504`
- primary_error_advantage: `-0.013072`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.175`
- secondary_hit_rate: `0.825`
- primary_vs_secondary_accuracy_spread: `-0.65`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.052142`
- secondary_mean_absolute_error: `0.030308`
- primary_error_advantage: `-0.021834`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.2875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `-0.425`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.072649`
- secondary_mean_absolute_error: `0.056405`
- primary_error_advantage: `-0.016244`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.016711`, as_primary `0`, as_primary_hit `None`, avg `0.005507`, median `0.010123`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.019868`, as_primary `0`, as_primary_hit `None`, avg `0.007676`, median `0.012347`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.030028`, as_primary `0`, as_primary_hit `None`, avg `0.013144`, median `0.018382`
- 20d: sample `80`, direction_hit `0.825`, path_mae `0.032358`, as_primary `0`, as_primary_hit `None`, avg `0.027525`, median `0.032209`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.062549`, as_primary `0`, as_primary_hit `None`, avg `0.046956`, median `0.064205`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.01725`, as_primary `0`, as_primary_hit `None`, avg `0.005507`, median `0.010123`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.021309`, as_primary `0`, as_primary_hit `None`, avg `0.007676`, median `0.012347`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.035742`, as_primary `0`, as_primary_hit `None`, avg `0.013144`, median `0.018382`
- 20d: sample `80`, direction_hit `0.825`, path_mae `0.045042`, as_primary `0`, as_primary_hit `None`, avg `0.027525`, median `0.032209`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.067258`, as_primary `0`, as_primary_hit `None`, avg `0.046956`, median `0.064205`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3375`, path_mae `0.026282`, as_primary `80`, as_primary_hit `0.6625`, avg `0.005507`, median `0.010123`
- 5d: sample `80`, direction_hit `0.3375`, path_mae `0.02804`, as_primary `80`, as_primary_hit `0.6625`, avg `0.007676`, median `0.012347`
- 10d: sample `80`, direction_hit `0.325`, path_mae `0.041576`, as_primary `80`, as_primary_hit `0.675`, avg `0.013144`, median `0.018382`
- 20d: sample `80`, direction_hit `0.175`, path_mae `0.052142`, as_primary `80`, as_primary_hit `0.825`, avg `0.027525`, median `0.032209`
- 60d: sample `80`, direction_hit `0.2875`, path_mae `0.072649`, as_primary `80`, as_primary_hit `0.7125`, avg `0.046956`, median `0.064205`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6625`, path_mae `0.016524`, as_primary `0`, as_primary_hit `None`, avg `0.005507`, median `0.010123`
- 5d: sample `80`, direction_hit `0.6625`, path_mae `0.019716`, as_primary `0`, as_primary_hit `None`, avg `0.007676`, median `0.012347`
- 10d: sample `80`, direction_hit `0.675`, path_mae `0.028504`, as_primary `0`, as_primary_hit `None`, avg `0.013144`, median `0.018382`
- 20d: sample `80`, direction_hit `0.825`, path_mae `0.030308`, as_primary `0`, as_primary_hit `None`, avg `0.027525`, median `0.032209`
- 60d: sample `80`, direction_hit `0.7125`, path_mae `0.056405`, as_primary `0`, as_primary_hit `None`, avg `0.046956`, median `0.064205`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.25`, primary_mae `0.026282`, avg `0.005507`, median `0.010123`
- 5d: sample `80`, primary_hit `0.3375`, primary_closer `0.3125`, primary_mae `0.02804`, avg `0.007676`, median `0.012347`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.041576`, avg `0.013144`, median `0.018382`
- 20d: sample `80`, primary_hit `0.175`, primary_closer `0.3`, primary_mae `0.052142`, avg `0.027525`, median `0.032209`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.35`, primary_mae `0.072649`, avg `0.046956`, median `0.064205`

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
- 3d: sample `20`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.022688`, avg `0.01063`, median `0.013091`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.027167`, avg `0.011203`, median `0.016178`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.4`, primary_mae `0.034748`, avg `0.018985`, median `0.018181`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.45`, primary_mae `0.033002`, avg `0.035053`, median `0.029246`
- 60d: sample `20`, primary_hit `0.55`, primary_closer `0.65`, primary_mae `0.073883`, avg `0.026792`, median `-0.005815`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.3667`, primary_closer `0.25`, primary_mae `0.02748`, avg `0.003799`, median `0.007355`
- 5d: sample `60`, primary_hit `0.3333`, primary_closer `0.3`, primary_mae `0.02833`, avg `0.0065`, median `0.011847`
- 10d: sample `60`, primary_hit `0.3167`, primary_closer `0.3`, primary_mae `0.043852`, avg `0.011197`, median `0.018762`
- 20d: sample `60`, primary_hit `0.2167`, primary_closer `0.25`, primary_mae `0.058522`, avg `0.025015`, median `0.032209`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.072238`, avg `0.053677`, median `0.069194`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.022688, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.027167, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.034748, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.033002, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.072238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.25, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016524, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026282, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.022688, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': -0.325, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019716, 'direction_hit_rate': 0.6625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.02804, 'direction_hit_rate': 0.3375}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.35, 'primary_mean_absolute_error': 0.027167, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.325, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028504, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.041576, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.034748, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_vs_secondary_accuracy_spread': -0.65, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.030308, 'direction_hit_rate': 0.825}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052142, 'direction_hit_rate': 0.175}, 'best_predictor': {'predictor': 'downside_continuation_predictor', 'sample_size': 20, 'primary_hit_rate': 0.05, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.033002, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': -0.425, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.056405, 'direction_hit_rate': 0.7125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.072649, 'direction_hit_rate': 0.2875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.072238, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.5`, primary_closer `0.375`, primary_mae `0.036009`, avg `-0.010646`, median `0.001503`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.031975`, avg `-0.011518`, median `-0.011716`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.5`, primary_mae `0.040808`, avg `-0.011322`, median `-0.015492`
- 20d: sample `8`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.043869`, avg `-0.006973`, median `-0.011642`
- 60d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.072913`, avg `-0.03393`, median `-0.028397`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.25`, primary_mae `0.036684`, avg `-0.002821`, median `0.00075`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.040746`, avg `0.000734`, median `0.006576`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.058163`, avg `0.006497`, median `0.012002`
- 20d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.061775`, avg `0.013296`, median `0.021333`
- 60d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.086406`, avg `0.019197`, median `0.061361`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.020103`, avg `0.007436`, median `0.010967`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.027027`, avg `0.0107`, median `0.016178`
- 10d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.036196`, avg `0.018618`, median `0.01979`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.5`, primary_mae `0.027361`, avg `0.029265`, median `0.020181`
- 60d: sample `16`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.066508`, avg `0.038494`, median `0.001124`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.25`, primary_mae `0.026282`, avg `0.005507`, median `0.010123`
- 5d: sample `80`, primary_hit `0.3375`, primary_closer `0.3125`, primary_mae `0.02804`, avg `0.007676`, median `0.012347`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.041576`, avg `0.013144`, median `0.018382`
- 20d: sample `80`, primary_hit `0.175`, primary_closer `0.3`, primary_mae `0.052142`, avg `0.027525`, median `0.032209`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.35`, primary_mae `0.072649`, avg `0.046956`, median `0.064205`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.3375`, primary_closer `0.25`, primary_mae `0.026282`, avg `0.005507`, median `0.010123`
- 5d: sample `80`, primary_hit `0.3375`, primary_closer `0.3125`, primary_mae `0.02804`, avg `0.007676`, median `0.012347`
- 10d: sample `80`, primary_hit `0.325`, primary_closer `0.325`, primary_mae `0.041576`, avg `0.013144`, median `0.018382`
- 20d: sample `80`, primary_hit `0.175`, primary_closer `0.3`, primary_mae `0.052142`, avg `0.027525`, median `0.032209`
- 60d: sample `80`, primary_hit `0.2875`, primary_closer `0.35`, primary_mae `0.072649`, avg `0.046956`, median `0.064205`

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
- 3d: sample `60`, primary_hit `0.2833`, primary_closer `0.2667`, primary_mae `0.022804`, avg `0.007795`, median `0.012244`
- 5d: sample `60`, primary_hit `0.3`, primary_closer `0.3167`, primary_mae `0.024299`, avg `0.010169`, median `0.013632`
- 10d: sample `60`, primary_hit `0.3`, primary_closer `0.3167`, primary_mae `0.035165`, avg `0.014295`, median `0.018151`
- 20d: sample `60`, primary_hit `0.1333`, primary_closer `0.3`, primary_mae `0.04879`, avg `0.032009`, median `0.033589`
- 60d: sample `60`, primary_hit `0.2833`, primary_closer `0.3667`, primary_mae `0.064944`, avg `0.050446`, median `0.060854`

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
