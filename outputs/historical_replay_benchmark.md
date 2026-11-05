# Historical Replay Benchmark

Generated at: `2026-11-05T00:58:49.862129+00:00`
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
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.4125`
- primary_vs_secondary_accuracy_spread: `0.175`
- primary_closer_than_secondary_rate: `0.5125`
- primary_mean_absolute_error: `0.018179`
- secondary_mean_absolute_error: `0.018297`
- primary_error_advantage: `0.000118`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.5`
- primary_mean_absolute_error: `0.024984`
- secondary_mean_absolute_error: `0.022244`
- primary_error_advantage: `-0.00274`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.5167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.525`
- primary_mean_absolute_error: `0.033208`
- secondary_mean_absolute_error: `0.038967`
- primary_error_advantage: `0.005759`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.575`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.55`
- primary_mean_absolute_error: `0.044968`
- secondary_mean_absolute_error: `0.050961`
- primary_error_advantage: `0.005993`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.425`
- primary_vs_secondary_accuracy_spread: `0.1375`
- primary_closer_than_secondary_rate: `0.5625`
- primary_mean_absolute_error: `0.049042`
- secondary_mean_absolute_error: `0.061118`
- primary_error_advantage: `0.012076`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6167`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.017537`, as_primary `0`, as_primary_hit `None`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.02296`, as_primary `0`, as_primary_hit `None`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.026704`, as_primary `0`, as_primary_hit `None`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.029529`, as_primary `0`, as_primary_hit `None`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.044599`, as_primary `0`, as_primary_hit `None`, avg `0.045025`, median `0.057306`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.020284`, as_primary `60`, as_primary_hit `0.6167`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.028441`, as_primary `60`, as_primary_hit `0.6167`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.035685`, as_primary `60`, as_primary_hit `0.7`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.041693`, as_primary `60`, as_primary_hit `0.75`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.050639`, as_primary `60`, as_primary_hit `0.7167`, avg `0.045025`, median `0.057306`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4125`, path_mae `0.018403`, as_primary `20`, as_primary_hit `0.5`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, direction_hit `0.4`, path_mae `0.022654`, as_primary `20`, as_primary_hit `0.55`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, direction_hit `0.275`, path_mae `0.040501`, as_primary `20`, as_primary_hit `0.8`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, direction_hit `0.2`, path_mae `0.058694`, as_primary `20`, as_primary_hit `0.95`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, direction_hit `0.2375`, path_mae `0.062509`, as_primary `20`, as_primary_hit `0.85`, avg `0.045025`, median `0.057306`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5875`, path_mae `0.016545`, as_primary `0`, as_primary_hit `None`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, direction_hit `0.6`, path_mae `0.020735`, as_primary `0`, as_primary_hit `None`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, direction_hit `0.725`, path_mae `0.025418`, as_primary `0`, as_primary_hit `None`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.028962`, as_primary `0`, as_primary_hit `None`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, direction_hit `0.75`, path_mae `0.043964`, as_primary `0`, as_primary_hit `None`, avg `0.045025`, median `0.057306`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.5167`, primary_mae `0.016816`, avg `0.003135`, median `0.0063`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.5167`, primary_mae `0.023769`, avg `0.008235`, median `0.010083`
- 10d: sample `60`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.034349`, avg `0.015829`, median `0.019858`
- 20d: sample `60`, primary_hit `0.75`, primary_closer `0.6833`, primary_mae `0.041313`, avg `0.024612`, median `0.029549`
- 60d: sample `60`, primary_hit `0.7167`, primary_closer `0.6167`, primary_mae `0.053396`, avg `0.038485`, median `0.053803`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022268`, avg `0.004511`, median `-0.002931`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02863`, avg `0.008093`, median `0.002887`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.029786`, avg `0.033389`, median `0.032704`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.15`, primary_mae `0.055932`, avg `0.05737`, median `0.057013`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.4`, primary_mae `0.035983`, avg `0.064645`, median `0.067284`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.625`, primary_closer `0.475`, primary_mae `0.017004`, avg `0.003712`, median `0.005463`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.425`, primary_mae `0.025752`, avg `0.005113`, median `0.004691`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.575`, primary_mae `0.036973`, avg `0.011803`, median `0.016156`
- 20d: sample `40`, primary_hit `0.775`, primary_closer `0.675`, primary_mae `0.040102`, avg `0.025511`, median `0.028724`
- 60d: sample `40`, primary_hit `0.725`, primary_closer `0.6`, primary_mae `0.053483`, avg `0.03287`, median `0.049227`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.6`, primary_mae `0.01644`, avg `0.001982`, median `0.008138`
- 5d: sample `20`, primary_hit `0.75`, primary_closer `0.7`, primary_mae `0.019802`, avg `0.014477`, median `0.018061`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.65`, primary_mae `0.0291`, avg `0.023881`, median `0.023768`
- 20d: sample `20`, primary_hit `0.7`, primary_closer `0.7`, primary_mae `0.043734`, avg `0.022815`, median `0.042729`
- 60d: sample `20`, primary_hit `0.7`, primary_closer `0.65`, primary_mae `0.053222`, avg `0.049714`, median `0.060099`

### risk_expansion_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022268`, avg `0.004511`, median `-0.002931`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02863`, avg `0.008093`, median `0.002887`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.029786`, avg `0.033389`, median `0.032704`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.15`, primary_mae `0.055932`, avg `0.05737`, median `0.057013`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.4`, primary_mae `0.035983`, avg `0.064645`, median `0.067284`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01644, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.019802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.0291, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.040102, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.035983, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_vs_secondary_accuracy_spread': 0.175, 'primary_closer_than_secondary_rate': 0.5125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016545, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020284, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.01644, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.5, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020735, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028441, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.7, 'primary_mean_absolute_error': 0.019802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.525, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025418, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040501, 'direction_hit_rate': 0.275}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.65, 'primary_mean_absolute_error': 0.0291, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.55, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028962, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058694, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.775, 'primary_closer_than_secondary_rate': 0.675, 'primary_mean_absolute_error': 0.040102, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.425, 'primary_vs_secondary_accuracy_spread': 0.1375, 'primary_closer_than_secondary_rate': 0.5625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.043964, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.062509, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'risk_expansion_predictor', 'sample_size': 20, 'primary_hit_rate': 0.1, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.035983, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.011237`, avg `0.005346`, median `0.009938`
- 5d: sample `8`, primary_hit `0.625`, primary_closer `0.375`, primary_mae `0.01831`, avg `0.006265`, median `0.006642`
- 10d: sample `8`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.033682`, avg `0.011401`, median `0.024934`
- 20d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.046279`, avg `0.016085`, median `0.024463`
- 60d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.054176`, avg `0.032459`, median `0.046255`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5625`, primary_closer `0.5`, primary_mae `0.012467`, avg `0.003131`, median `0.004897`
- 5d: sample `16`, primary_hit `0.5625`, primary_closer `0.375`, primary_mae `0.019869`, avg `0.003706`, median `0.006642`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.041856`, avg `0.000853`, median `0.002861`
- 20d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.044551`, avg `0.01513`, median `0.022803`
- 60d: sample `16`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.053813`, avg `0.028357`, median `0.041934`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.024049`, avg `0.00476`, median `0.002018`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.030074`, avg `0.009005`, median `0.006005`
- 10d: sample `16`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.031433`, avg `0.03293`, median `0.034572`
- 20d: sample `16`, primary_hit `0.0625`, primary_closer `0.1875`, primary_mae `0.0561`, avg `0.055377`, median `0.058445`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.4375`, primary_mae `0.03636`, avg `0.067536`, median `0.067284`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5125`, primary_mae `0.018179`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.024984`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.033208`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.044968`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.049042`, avg `0.045025`, median `0.057306`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5125`, primary_mae `0.018179`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.024984`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.033208`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.044968`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.049042`, avg `0.045025`, median `0.057306`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6167`, primary_closer `0.5167`, primary_mae `0.016816`, avg `0.003135`, median `0.0063`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.5167`, primary_mae `0.023769`, avg `0.008235`, median `0.010083`
- 10d: sample `60`, primary_hit `0.7`, primary_closer `0.6`, primary_mae `0.034349`, avg `0.015829`, median `0.019858`
- 20d: sample `60`, primary_hit `0.75`, primary_closer `0.6833`, primary_mae `0.041313`, avg `0.024612`, median `0.029549`
- 60d: sample `60`, primary_hit `0.7167`, primary_closer `0.6167`, primary_mae `0.053396`, avg `0.038485`, median `0.053803`

### breadth_conflicted
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.022268`, avg `0.004511`, median `-0.002931`
- 5d: sample `20`, primary_hit `0.45`, primary_closer `0.45`, primary_mae `0.02863`, avg `0.008093`, median `0.002887`
- 10d: sample `20`, primary_hit `0.2`, primary_closer `0.3`, primary_mae `0.029786`, avg `0.033389`, median `0.032704`
- 20d: sample `20`, primary_hit `0.05`, primary_closer `0.15`, primary_mae `0.055932`, avg `0.05737`, median `0.057013`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.4`, primary_mae `0.035983`, avg `0.064645`, median `0.067284`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5125`, primary_mae `0.018179`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.024984`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.033208`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.044968`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.049042`, avg `0.045025`, median `0.057306`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5125`, primary_mae `0.018179`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.024984`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.033208`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.044968`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.049042`, avg `0.045025`, median `0.057306`

### flow_conflicted
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.5875`, primary_closer `0.5125`, primary_mae `0.018179`, avg `0.003479`, median `0.005557`
- 5d: sample `80`, primary_hit `0.575`, primary_closer `0.5`, primary_mae `0.024984`, avg `0.008199`, median `0.007368`
- 10d: sample `80`, primary_hit `0.575`, primary_closer `0.525`, primary_mae `0.033208`, avg `0.020219`, median `0.02383`
- 20d: sample `80`, primary_hit `0.575`, primary_closer `0.55`, primary_mae `0.044968`, avg `0.032802`, median `0.041393`
- 60d: sample `80`, primary_hit `0.5625`, primary_closer `0.5625`, primary_mae `0.049042`, avg `0.045025`, median `0.057306`

- data_enhancement_question: `historical_replay_available_compare_bucket_metrics_but_forward_validation_required`
## Guardrails

- Historical replay is research evaluation only and cannot replace daily forward validation.
- Historical replay results must not be described as confirmed alpha.
- Forecast Accuracy Ledger remains immutable; this benchmark does not rewrite forecast_records.csv.
- No buy/sell, entry/exit, PnL, paper trading, or execution recommendation is produced.
- Alpha v1 threshold remains frozen at 0.32534311.
