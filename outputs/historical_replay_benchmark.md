# Historical Replay Benchmark

Generated at: `2026-06-16T11:20:03.330947+00:00`
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
- primary_hit_rate: `0.6375`
- secondary_hit_rate: `0.6375`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.019466`
- secondary_mean_absolute_error: `0.017471`
- primary_error_advantage: `-0.001995`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.6125`
- secondary_hit_rate: `0.6125`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4375`
- primary_mean_absolute_error: `0.024064`
- secondary_mean_absolute_error: `0.0208`
- primary_error_advantage: `-0.003264`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.6`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.031194`
- secondary_mean_absolute_error: `0.026203`
- primary_error_advantage: `-0.004991`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.75`
- secondary_hit_rate: `0.75`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.3125`
- primary_mean_absolute_error: `0.041352`
- secondary_mean_absolute_error: `0.026637`
- primary_error_advantage: `-0.014715`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.725`
- secondary_hit_rate: `0.725`
- primary_vs_secondary_accuracy_spread: `0.0`
- primary_closer_than_secondary_rate: `0.4`
- primary_mean_absolute_error: `0.061402`
- secondary_mean_absolute_error: `0.047066`
- primary_error_advantage: `-0.014336`
- close_call_sample_size: `0`
- close_call_primary_closer_rate: `None`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.017399`, as_primary `0`, as_primary_hit `None`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.020742`, as_primary `0`, as_primary_hit `None`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.027849`, as_primary `0`, as_primary_hit `None`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.028514`, as_primary `0`, as_primary_hit `None`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.049874`, as_primary `0`, as_primary_hit `None`, avg `0.037145`, median `0.044727`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.019466`, as_primary `80`, as_primary_hit `0.6375`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.024064`, as_primary `80`, as_primary_hit `0.6125`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.031194`, as_primary `80`, as_primary_hit `0.6`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.041352`, as_primary `80`, as_primary_hit `0.75`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.061402`, as_primary `80`, as_primary_hit `0.725`, avg `0.037145`, median `0.044727`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.3625`, path_mae `0.023542`, as_primary `0`, as_primary_hit `None`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, direction_hit `0.3875`, path_mae `0.026857`, as_primary `0`, as_primary_hit `None`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.039458`, as_primary `0`, as_primary_hit `None`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, direction_hit `0.25`, path_mae `0.050166`, as_primary `0`, as_primary_hit `None`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, direction_hit `0.275`, path_mae `0.057826`, as_primary `0`, as_primary_hit `None`, avg `0.037145`, median `0.044727`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6375`, path_mae `0.017471`, as_primary `0`, as_primary_hit `None`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, direction_hit `0.6125`, path_mae `0.0208`, as_primary `0`, as_primary_hit `None`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.026203`, as_primary `0`, as_primary_hit `None`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, direction_hit `0.75`, path_mae `0.026637`, as_primary `0`, as_primary_hit `None`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, direction_hit `0.725`, path_mae `0.047066`, as_primary `0`, as_primary_hit `None`, avg `0.037145`, median `0.044727`

## Edge Status Performance

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.425`, primary_mae `0.019466`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.024064`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.031194`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.041352`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.4`, primary_mae `0.061402`, avg `0.037145`, median `0.044727`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.012424`, avg `0.002734`, median `0.004557`
- 5d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.017992`, avg `0.002483`, median `0.005051`
- 10d: sample `20`, primary_hit `0.65`, primary_closer `0.4`, primary_mae `0.027288`, avg `0.004564`, median `0.005594`
- 20d: sample `20`, primary_hit `0.65`, primary_closer `0.5`, primary_mae `0.034733`, avg `0.001428`, median `0.017361`
- 60d: sample `20`, primary_hit `0.9`, primary_closer `0.6`, primary_mae `0.021704`, avg `0.040703`, median `0.044043`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6333`, primary_closer `0.4333`, primary_mae `0.021814`, avg `0.004954`, median `0.009041`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.4333`, primary_mae `0.026089`, avg `0.001286`, median `0.008034`
- 10d: sample `60`, primary_hit `0.5833`, primary_closer `0.4333`, primary_mae `0.032496`, avg `0.007648`, median `0.01234`
- 20d: sample `60`, primary_hit `0.7833`, primary_closer `0.25`, primary_mae `0.043558`, avg `0.015958`, median `0.016362`
- 60d: sample `60`, primary_hit `0.6667`, primary_closer `0.3333`, primary_mae `0.074634`, avg `0.03596`, median `0.045619`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012424, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027288, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034733, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.021704, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.017399, 'direction_hit_rate': 0.6375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023542, 'direction_hit_rate': 0.3625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.012424, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4375, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020742, 'direction_hit_rate': 0.6125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026857, 'direction_hit_rate': 0.3875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.017992, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026203, 'direction_hit_rate': 0.6}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.039458, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.027288, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.3125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.026637, 'direction_hit_rate': 0.75}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.050166, 'direction_hit_rate': 0.25}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.65, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.034733, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.725, 'primary_vs_secondary_accuracy_spread': 0.0, 'primary_closer_than_secondary_rate': 0.4, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.047066, 'direction_hit_rate': 0.725}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.061402, 'direction_hit_rate': 0.725}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.9, 'primary_closer_than_secondary_rate': 0.6, 'primary_mean_absolute_error': 0.021704, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.014418`, avg `0.012094`, median `0.019397`
- 5d: sample `8`, primary_hit `0.875`, primary_closer `0.625`, primary_mae `0.017221`, avg `0.019425`, median `0.021934`
- 10d: sample `8`, primary_hit `0.75`, primary_closer `0.625`, primary_mae `0.022962`, avg `0.024014`, median `0.034294`
- 20d: sample `8`, primary_hit `1.0`, primary_closer `0.375`, primary_mae `0.021723`, avg `0.041763`, median `0.03628`
- 60d: sample `8`, primary_hit `1.0`, primary_closer `0.5`, primary_mae `0.027763`, avg `0.096768`, median `0.095118`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016514`, avg `0.007595`, median `0.017434`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.017471`, avg `0.013427`, median `0.012456`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.027045`, avg `0.015434`, median `0.028201`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.034053`, avg `0.028472`, median `0.030284`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.059234`, avg `0.063395`, median `0.075261`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.625`, primary_closer `0.625`, primary_mae `0.016514`, avg `0.007595`, median `0.017434`
- 5d: sample `16`, primary_hit `0.8125`, primary_closer `0.5`, primary_mae `0.017471`, avg `0.013427`, median `0.012456`
- 10d: sample `16`, primary_hit `0.6875`, primary_closer `0.5625`, primary_mae `0.027045`, avg `0.015434`, median `0.028201`
- 20d: sample `16`, primary_hit `0.875`, primary_closer `0.3125`, primary_mae `0.034053`, avg `0.028472`, median `0.030284`
- 60d: sample `16`, primary_hit `0.8125`, primary_closer `0.3125`, primary_mae `0.059234`, avg `0.063395`, median `0.075261`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.425`, primary_mae `0.019466`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.024064`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.031194`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.041352`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.4`, primary_mae `0.061402`, avg `0.037145`, median `0.044727`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.425`, primary_mae `0.019466`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.024064`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.031194`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.041352`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.4`, primary_mae `0.061402`, avg `0.037145`, median `0.044727`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.425`, primary_mae `0.019466`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.024064`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.031194`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.041352`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.4`, primary_mae `0.061402`, avg `0.037145`, median `0.044727`

### breadth_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.425`, primary_mae `0.019466`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.024064`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.031194`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.041352`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.4`, primary_mae `0.061402`, avg `0.037145`, median `0.044727`

### options_conflicted
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### flow_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6375`, primary_closer `0.425`, primary_mae `0.019466`, avg `0.004399`, median `0.006764`
- 5d: sample `80`, primary_hit `0.6125`, primary_closer `0.4375`, primary_mae `0.024064`, avg `0.001586`, median `0.00696`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.031194`, avg `0.006877`, median `0.0086`
- 20d: sample `80`, primary_hit `0.75`, primary_closer `0.3125`, primary_mae `0.041352`, avg `0.012326`, median `0.016362`
- 60d: sample `80`, primary_hit `0.725`, primary_closer `0.4`, primary_mae `0.061402`, avg `0.037145`, median `0.044727`

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
