# Historical Replay Benchmark

Generated at: `2026-08-29T10:27:52.333956+00:00`
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
- primary_hit_rate: `0.7625`
- secondary_hit_rate: `0.6875`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.016486`
- secondary_mean_absolute_error: `0.01538`
- primary_error_advantage: `-0.001106`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.75`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.023728`
- secondary_mean_absolute_error: `0.020646`
- primary_error_advantage: `-0.003082`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.4125`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.7`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.45`
- primary_mean_absolute_error: `0.034891`
- secondary_mean_absolute_error: `0.031606`
- primary_error_advantage: `-0.003285`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.45`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.8`
- secondary_hit_rate: `0.775`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.055055`
- secondary_mean_absolute_error: `0.041692`
- primary_error_advantage: `-0.013363`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.35`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.7875`
- secondary_hit_rate: `0.7125`
- primary_vs_secondary_accuracy_spread: `0.075`
- primary_closer_than_secondary_rate: `0.475`
- primary_mean_absolute_error: `0.059818`
- secondary_mean_absolute_error: `0.054674`
- primary_error_advantage: `-0.005144`
- close_call_sample_size: `80`
- close_call_primary_closer_rate: `0.475`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7625`, path_mae `0.01425`, as_primary `0`, as_primary_hit `None`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, direction_hit `0.75`, path_mae `0.019314`, as_primary `0`, as_primary_hit `None`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, direction_hit `0.7`, path_mae `0.029436`, as_primary `0`, as_primary_hit `None`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.039696`, as_primary `0`, as_primary_hit `None`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.050394`, as_primary `0`, as_primary_hit `None`, avg `0.063143`, median `0.081846`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7625`, path_mae `0.016486`, as_primary `80`, as_primary_hit `0.7625`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, direction_hit `0.75`, path_mae `0.023728`, as_primary `80`, as_primary_hit `0.75`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, direction_hit `0.7`, path_mae `0.034891`, as_primary `80`, as_primary_hit `0.7`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.055055`, as_primary `80`, as_primary_hit `0.8`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.059818`, as_primary `80`, as_primary_hit `0.7875`, avg `0.063143`, median `0.081846`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.2375`, path_mae `0.021693`, as_primary `0`, as_primary_hit `None`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, direction_hit `0.25`, path_mae `0.028698`, as_primary `0`, as_primary_hit `None`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, direction_hit `0.3`, path_mae `0.04274`, as_primary `0`, as_primary_hit `None`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, direction_hit `0.2`, path_mae `0.057658`, as_primary `0`, as_primary_hit `None`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, direction_hit `0.2125`, path_mae `0.07694`, as_primary `0`, as_primary_hit `None`, avg `0.063143`, median `0.081846`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.7625`, path_mae `0.014524`, as_primary `0`, as_primary_hit `None`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, direction_hit `0.75`, path_mae `0.018958`, as_primary `0`, as_primary_hit `None`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, direction_hit `0.7`, path_mae `0.029389`, as_primary `0`, as_primary_hit `None`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, direction_hit `0.8`, path_mae `0.035491`, as_primary `0`, as_primary_hit `None`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, direction_hit `0.7875`, path_mae `0.053101`, as_primary `0`, as_primary_hit `None`, avg `0.063143`, median `0.081846`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7625`, primary_closer `0.475`, primary_mae `0.016486`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, primary_hit `0.75`, primary_closer `0.4125`, primary_mae `0.023728`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.034891`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.055055`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, primary_hit `0.7875`, primary_closer `0.475`, primary_mae `0.059818`, avg `0.063143`, median `0.081846`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.012447`, avg `0.01261`, median `0.017216`
- 5d: sample `20`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.019264`, avg `0.017795`, median `0.018877`
- 10d: sample `20`, primary_hit `0.8`, primary_closer `0.45`, primary_mae `0.026141`, avg `0.021127`, median `0.024318`
- 20d: sample `20`, primary_hit `0.95`, primary_closer `0.3`, primary_mae `0.037484`, avg `0.041649`, median `0.032962`
- 60d: sample `20`, primary_hit `0.9`, primary_closer `0.5`, primary_mae `0.031659`, avg `0.075671`, median `0.086443`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.75`, primary_closer `0.4833`, primary_mae `0.017832`, avg `0.008638`, median `0.010603`
- 5d: sample `60`, primary_hit `0.7333`, primary_closer `0.4`, primary_mae `0.025216`, avg `0.01282`, median `0.016329`
- 10d: sample `60`, primary_hit `0.6667`, primary_closer `0.45`, primary_mae `0.037807`, avg `0.017583`, median `0.021377`
- 20d: sample `60`, primary_hit `0.75`, primary_closer `0.3667`, primary_mae `0.060912`, avg `0.030229`, median `0.032012`
- 60d: sample `60`, primary_hit `0.75`, primary_closer `0.4667`, primary_mae `0.069204`, avg `0.058967`, median `0.07206`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.012447, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019264, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.037484, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.031659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7625, 'secondary_hit_rate': 0.6875, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.01425, 'direction_hit_rate': 0.7625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.021693, 'direction_hit_rate': 0.2375}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.012447, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018958, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.028698, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.019264, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.45, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.029389, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.04274, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.8, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.026141, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.775, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.035491, 'direction_hit_rate': 0.8}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.057658, 'direction_hit_rate': 0.2}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.95, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.037484, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.7875, 'secondary_hit_rate': 0.7125, 'primary_vs_secondary_accuracy_spread': 0.075, 'primary_closer_than_secondary_rate': 0.475, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050394, 'direction_hit_rate': 0.7875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.07694, 'direction_hit_rate': 0.2125}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.031659, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.005766`, avg `0.018743`, median `0.021989`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.012021`, avg `0.024356`, median `0.031363`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.016486`, avg `0.030415`, median `0.038994`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.625`, primary_mae `0.019008`, avg `0.06254`, median `0.069475`
- 60d: sample `8`, primary_hit `0.875`, primary_closer `0.875`, primary_mae `0.025626`, avg `0.082138`, median `0.096338`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.014331`, avg `0.010944`, median `0.01606`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.020661`, avg `0.015654`, median `0.017098`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.029042`, avg `0.016758`, median `0.020731`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.038189`, avg `0.041347`, median `0.032962`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.031897`, avg `0.071278`, median `0.086443`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.014331`, avg `0.010944`, median `0.01606`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.4375`, primary_mae `0.020661`, avg `0.015654`, median `0.017098`
- 10d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.029042`, avg `0.016758`, median `0.020731`
- 20d: sample `16`, primary_hit `0.9375`, primary_closer `0.3125`, primary_mae `0.038189`, avg `0.041347`, median `0.032962`
- 60d: sample `16`, primary_hit `0.875`, primary_closer `0.5`, primary_mae `0.031897`, avg `0.071278`, median `0.086443`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7625`, primary_closer `0.475`, primary_mae `0.016486`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, primary_hit `0.75`, primary_closer `0.4125`, primary_mae `0.023728`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.034891`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.055055`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, primary_hit `0.7875`, primary_closer `0.475`, primary_mae `0.059818`, avg `0.063143`, median `0.081846`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7625`, primary_closer `0.475`, primary_mae `0.016486`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, primary_hit `0.75`, primary_closer `0.4125`, primary_mae `0.023728`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.034891`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.055055`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, primary_hit `0.7875`, primary_closer `0.475`, primary_mae `0.059818`, avg `0.063143`, median `0.081846`

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
- 3d: sample `60`, primary_hit `0.7667`, primary_closer `0.4833`, primary_mae `0.013496`, avg `0.010661`, median `0.012522`
- 5d: sample `60`, primary_hit `0.75`, primary_closer `0.4333`, primary_mae `0.021509`, avg `0.014418`, median `0.015064`
- 10d: sample `60`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.03232`, avg `0.018283`, median `0.022309`
- 20d: sample `60`, primary_hit `0.8`, primary_closer `0.3833`, primary_mae `0.054124`, avg `0.034499`, median `0.032209`
- 60d: sample `60`, primary_hit `0.8`, primary_closer `0.5167`, primary_mae `0.052813`, avg `0.067902`, median `0.08262`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7625`, primary_closer `0.475`, primary_mae `0.016486`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, primary_hit `0.75`, primary_closer `0.4125`, primary_mae `0.023728`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.034891`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.055055`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, primary_hit `0.7875`, primary_closer `0.475`, primary_mae `0.059818`, avg `0.063143`, median `0.081846`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.7625`, primary_closer `0.475`, primary_mae `0.016486`, avg `0.009631`, median `0.012513`
- 5d: sample `80`, primary_hit `0.75`, primary_closer `0.4125`, primary_mae `0.023728`, avg `0.014063`, median `0.017439`
- 10d: sample `80`, primary_hit `0.7`, primary_closer `0.45`, primary_mae `0.034891`, avg `0.018469`, median `0.022309`
- 20d: sample `80`, primary_hit `0.8`, primary_closer `0.35`, primary_mae `0.055055`, avg `0.033084`, median `0.032209`
- 60d: sample `80`, primary_hit `0.7875`, primary_closer `0.475`, primary_mae `0.059818`, avg `0.063143`, median `0.081846`

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
