# Historical Replay Benchmark

Generated at: `2026-06-15T13:55:30.492694+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
Overfit warning: `{'level': 'high', 'reasons': ['primary path is not closer than secondary path on most horizons', 'high signal confirmation is mixed or not better in historical replay', 'forward validation completed samples are below the minimum gate'], 'rule': 'If historical replay is mixed and forward samples are insufficient, keep confidence capped and avoid adding new data blindly.'}`

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
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.013896`
- secondary_mean_absolute_error: `0.012847`
- primary_error_advantage: `-0.001049`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.4625`
- primary_vs_secondary_accuracy_spread: `0.15`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.019249`
- secondary_mean_absolute_error: `0.016148`
- primary_error_advantage: `-0.003101`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.029696`
- secondary_mean_absolute_error: `0.026575`
- primary_error_advantage: `-0.003121`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.6875`
- secondary_hit_rate: `0.6625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.050816`
- secondary_mean_absolute_error: `0.044253`
- primary_error_advantage: `-0.006563`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.5875`
- secondary_hit_rate: `0.5625`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.3875`
- primary_mean_absolute_error: `0.07311`
- secondary_mean_absolute_error: `0.059002`
- primary_error_advantage: `-0.014108`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013047`, as_primary `0`, as_primary_hit `None`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.016361`, as_primary `0`, as_primary_hit `None`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.023024`, as_primary `0`, as_primary_hit `None`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.034587`, as_primary `0`, as_primary_hit `None`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.055732`, as_primary `0`, as_primary_hit `None`, avg `0.025805`, median `0.031374`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.013896`, as_primary `80`, as_primary_hit `0.6125`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.019249`, as_primary `80`, as_primary_hit `0.6125`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.029696`, as_primary `80`, as_primary_hit `0.5875`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.050816`, as_primary `80`, as_primary_hit `0.6875`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.07311`, as_primary `80`, as_primary_hit `0.5875`, avg `0.025805`, median `0.031374`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3875`, path_mae `0.013069`, as_primary `0`, as_primary_hit `None`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.016449`, as_primary `0`, as_primary_hit `None`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, direction_hit `0.4125`, path_mae `0.028136`, as_primary `0`, as_primary_hit `None`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, direction_hit `0.3125`, path_mae `0.060856`, as_primary `0`, as_primary_hit `None`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, direction_hit `0.4125`, path_mae `0.06861`, as_primary `0`, as_primary_hit `None`, avg `0.025805`, median `0.031374`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6125`, path_mae `0.012365`, as_primary `0`, as_primary_hit `None`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.01511`, as_primary `0`, as_primary_hit `None`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, direction_hit `0.5875`, path_mae `0.021932`, as_primary `0`, as_primary_hit `None`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, direction_hit `0.6875`, path_mae `0.031609`, as_primary `0`, as_primary_hit `None`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, direction_hit `0.5875`, path_mae `0.052836`, as_primary `0`, as_primary_hit `None`, avg `0.025805`, median `0.031374`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013896`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.019249`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.029696`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.35`, primary_mae `0.050816`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07311`, avg `0.025805`, median `0.031374`

## Predictor Performance

### bounce_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.65`, primary_closer `0.425`, primary_mae `0.01402`, avg `0.005617`, median `0.004633`
- 5d: sample `40`, primary_hit `0.75`, primary_closer `0.4`, primary_mae `0.018517`, avg `0.008371`, median `0.007361`
- 10d: sample `40`, primary_hit `0.65`, primary_closer `0.55`, primary_mae `0.028278`, avg `0.006349`, median `0.008571`
- 20d: sample `40`, primary_hit `0.675`, primary_closer `0.45`, primary_mae `0.052867`, avg `0.00163`, median `0.01201`
- 60d: sample `40`, primary_hit `0.475`, primary_closer `0.425`, primary_mae `0.072522`, avg `0.008307`, median `-0.00433`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.575`, primary_closer `0.4`, primary_mae `0.013772`, avg `0.001621`, median `0.003745`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.325`, primary_mae `0.019981`, avg `0.000407`, median `-0.001663`
- 10d: sample `40`, primary_hit `0.525`, primary_closer `0.35`, primary_mae `0.031113`, avg `0.006965`, median `0.005512`
- 20d: sample `40`, primary_hit `0.7`, primary_closer `0.25`, primary_mae `0.048765`, avg `0.017004`, median `0.020209`
- 60d: sample `40`, primary_hit `0.7`, primary_closer `0.35`, primary_mae `0.073699`, avg `0.043304`, median `0.051612`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.013772, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018517, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.028278, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.048765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.072522, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.012365, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013896, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.575, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.013772, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_vs_secondary_accuracy_spread': 0.15, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01511, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019249, 'direction_hit_rate': 0.6125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.018517, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021932, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029696, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.55, 'primary_mean_absolute_error': 0.028278, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031609, 'direction_hit_rate': 0.6875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.060856, 'direction_hit_rate': 0.3125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 40, 'primary_hit_rate': 0.7, 'primary_closer_than_secondary_rate': 0.25, 'primary_mean_absolute_error': 0.048765, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.3875, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.052836, 'direction_hit_rate': 0.5875}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07311, 'direction_hit_rate': 0.5875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 40, 'primary_hit_rate': 0.475, 'primary_closer_than_secondary_rate': 0.425, 'primary_mean_absolute_error': 0.072522, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.013881`, avg `-0.007791`, median `-0.007158`
- 5d: sample `8`, primary_hit `0.125`, primary_closer `0.125`, primary_mae `0.015631`, avg `-0.011833`, median `-0.012995`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.012386`, avg `0.008706`, median `0.006918`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.125`, primary_mae `0.015756`, avg `0.028852`, median `0.030181`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.032369`, avg `0.054535`, median `0.055714`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.014561`, avg `-0.005398`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015039`, avg `-0.005107`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.015222`, avg `0.008574`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.024104`, avg `0.022746`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.053134`, avg `0.027526`, median `0.033759`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.014561`, avg `-0.005398`, median `-0.006238`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.015039`, avg `-0.005107`, median `-0.007506`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.625`, primary_mae `0.015222`, avg `0.008574`, median `0.010282`
- 20d: sample `16`, primary_hit `0.8125`, primary_closer `0.25`, primary_mae `0.024104`, avg `0.022746`, median `0.028979`
- 60d: sample `16`, primary_hit `0.6875`, primary_closer `0.375`, primary_mae `0.053134`, avg `0.027526`, median `0.033759`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013896`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.019249`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.029696`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.35`, primary_mae `0.050816`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07311`, avg `0.025805`, median `0.031374`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013896`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.019249`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.029696`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.35`, primary_mae `0.050816`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07311`, avg `0.025805`, median `0.031374`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013896`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.019249`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.029696`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.35`, primary_mae `0.050816`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07311`, avg `0.025805`, median `0.031374`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013896`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.019249`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.029696`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.35`, primary_mae `0.050816`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07311`, avg `0.025805`, median `0.031374`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6125`, primary_closer `0.4125`, primary_mae `0.013896`, avg `0.003619`, median `0.004555`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.3625`, primary_mae `0.019249`, avg `0.004389`, median `0.004573`
- 10d: sample `80`, primary_hit `0.5875`, primary_closer `0.45`, primary_mae `0.029696`, avg `0.006657`, median `0.00719`
- 20d: sample `80`, primary_hit `0.6875`, primary_closer `0.35`, primary_mae `0.050816`, avg `0.009317`, median `0.017134`
- 60d: sample `80`, primary_hit `0.5875`, primary_closer `0.3875`, primary_mae `0.07311`, avg `0.025805`, median `0.031374`

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
