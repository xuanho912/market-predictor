# Historical Replay Benchmark

Generated at: `2026-09-28T19:43:26.692991+00:00`
Validation type: `historical_replay`
Status: `research_evaluation_only_not_forward_validation`
Sample size: `80`
Historical replay grade: `WEAK`
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
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.020277`
- secondary_mean_absolute_error: `0.016856`
- primary_error_advantage: `-0.003421`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.5625`
- secondary_hit_rate: `0.4375`
- primary_vs_secondary_accuracy_spread: `0.125`
- primary_closer_than_secondary_rate: `0.3625`
- primary_mean_absolute_error: `0.025749`
- secondary_mean_absolute_error: `0.020532`
- primary_error_advantage: `-0.005217`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.4`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.5125`
- secondary_hit_rate: `0.4875`
- primary_vs_secondary_accuracy_spread: `0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.03619`
- secondary_mean_absolute_error: `0.027831`
- primary_error_advantage: `-0.008359`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.3`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.375`
- secondary_hit_rate: `0.625`
- primary_vs_secondary_accuracy_spread: `-0.25`
- primary_closer_than_secondary_rate: `0.35`
- primary_mean_absolute_error: `0.069133`
- secondary_mean_absolute_error: `0.049094`
- primary_error_advantage: `-0.020039`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.5`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.1875`
- secondary_hit_rate: `0.8125`
- primary_vs_secondary_accuracy_spread: `-0.625`
- primary_closer_than_secondary_rate: `0.3`
- primary_mean_absolute_error: `0.090862`
- secondary_mean_absolute_error: `0.065746`
- primary_error_advantage: `-0.025116`
- close_call_sample_size: `20`
- close_call_primary_closer_rate: `0.45`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016679`, as_primary `0`, as_primary_hit `None`, avg `-0.006906`, median `-0.004451`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.019555`, as_primary `0`, as_primary_hit `None`, avg `-0.010059`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.026411`, as_primary `0`, as_primary_hit `None`, avg `-0.005419`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.041189`, as_primary `0`, as_primary_hit `None`, avg `0.010537`, median `0.018008`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.059111`, as_primary `0`, as_primary_hit `None`, avg `0.049908`, median `0.060391`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016829`, as_primary `0`, as_primary_hit `None`, avg `-0.006906`, median `-0.004451`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.022119`, as_primary `0`, as_primary_hit `None`, avg `-0.010059`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.03229`, as_primary `0`, as_primary_hit `None`, avg `-0.005419`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.060692`, as_primary `0`, as_primary_hit `None`, avg `0.010537`, median `0.018008`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.069344`, as_primary `0`, as_primary_hit `None`, avg `0.049908`, median `0.060391`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.6`, path_mae `0.020277`, as_primary `80`, as_primary_hit `0.4`, avg `-0.006906`, median `-0.004451`
- 5d: sample `80`, direction_hit `0.5625`, path_mae `0.025749`, as_primary `80`, as_primary_hit `0.4375`, avg `-0.010059`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.5125`, path_mae `0.03619`, as_primary `80`, as_primary_hit `0.4875`, avg `-0.005419`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.375`, path_mae `0.069133`, as_primary `80`, as_primary_hit `0.625`, avg `0.010537`, median `0.018008`
- 60d: sample `80`, direction_hit `0.1875`, path_mae `0.090862`, as_primary `80`, as_primary_hit `0.8125`, avg `0.049908`, median `0.060391`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4`, path_mae `0.016379`, as_primary `0`, as_primary_hit `None`, avg `-0.006906`, median `-0.004451`
- 5d: sample `80`, direction_hit `0.4375`, path_mae `0.018988`, as_primary `0`, as_primary_hit `None`, avg `-0.010059`, median `-0.006281`
- 10d: sample `80`, direction_hit `0.4875`, path_mae `0.0261`, as_primary `0`, as_primary_hit `None`, avg `-0.005419`, median `-0.000315`
- 20d: sample `80`, direction_hit `0.625`, path_mae `0.040817`, as_primary `0`, as_primary_hit `None`, avg `0.010537`, median `0.018008`
- 60d: sample `80`, direction_hit `0.8125`, path_mae `0.061342`, as_primary `0`, as_primary_hit `None`, avg `0.049908`, median `0.060391`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020277`, avg `-0.006906`, median `-0.004451`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.025749`, avg `-0.010059`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.03619`, avg `-0.005419`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.069133`, avg `0.010537`, median `0.018008`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.090862`, avg `0.049908`, median `0.060391`

## Predictor Performance

### bounce_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### downside_continuation_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.6667`, primary_closer `0.4333`, primary_mae `0.0211`, avg `-0.010151`, median `-0.010028`
- 5d: sample `60`, primary_hit `0.6167`, primary_closer `0.35`, primary_mae `0.025772`, avg `-0.012954`, median `-0.009034`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.03625`, avg `-0.005649`, median `-0.005392`
- 20d: sample `60`, primary_hit `0.3833`, primary_closer `0.3`, primary_mae `0.076244`, avg `0.010769`, median `0.023936`
- 60d: sample `60`, primary_hit `0.2`, primary_closer `0.25`, primary_mae `0.10326`, avg `0.049146`, median `0.066699`

### trend_reversal_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.01781`, avg `0.00283`, median `0.005108`
- 5d: sample `20`, primary_hit `0.4`, primary_closer `0.4`, primary_mae `0.025678`, avg `-0.001374`, median `0.005583`
- 10d: sample `20`, primary_hit `0.4`, primary_closer `0.3`, primary_mae `0.03601`, avg `-0.00473`, median `0.004006`
- 20d: sample `20`, primary_hit `0.35`, primary_closer `0.5`, primary_mae `0.0478`, avg `0.009844`, median `0.010261`
- 60d: sample `20`, primary_hit `0.15`, primary_closer `0.45`, primary_mae `0.053668`, avg `0.052197`, median `0.056479`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01781, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025678, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.0478, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.053668, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016379, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.020277, 'direction_hit_rate': 0.6}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.01781, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_vs_secondary_accuracy_spread': 0.125, 'primary_closer_than_secondary_rate': 0.3625, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018988, 'direction_hit_rate': 0.4375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.025749, 'direction_hit_rate': 0.5625}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.025678, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_vs_secondary_accuracy_spread': 0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.0261, 'direction_hit_rate': 0.4875}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.03619, 'direction_hit_rate': 0.5125}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.4, 'primary_closer_than_secondary_rate': 0.3, 'primary_mean_absolute_error': 0.03601, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_vs_secondary_accuracy_spread': -0.25, 'primary_closer_than_secondary_rate': 0.35, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.040817, 'direction_hit_rate': 0.625}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.069133, 'direction_hit_rate': 0.375}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.35, 'primary_closer_than_secondary_rate': 0.5, 'primary_mean_absolute_error': 0.0478, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_vs_secondary_accuracy_spread': -0.625, 'primary_closer_than_secondary_rate': 0.3, 'best_scenario_type': {'scenario': 'base_path', 'sample_size': 80, 'path_mean_absolute_error': 0.059111, 'direction_hit_rate': 0.8125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.090862, 'direction_hit_rate': 0.1875}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 20, 'primary_hit_rate': 0.15, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.053668, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.019829`, avg `0.006361`, median `0.008516`
- 5d: sample `8`, primary_hit `0.25`, primary_closer `0.25`, primary_mae `0.026194`, avg `0.002239`, median `0.006826`
- 10d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.032179`, avg `-0.000775`, median `0.004074`
- 20d: sample `8`, primary_hit `0.25`, primary_closer `0.375`, primary_mae `0.058726`, avg `0.024693`, median `0.032362`
- 60d: sample `8`, primary_hit `0.0`, primary_closer `0.375`, primary_mae `0.036516`, avg `0.054033`, median `0.056479`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.018605`, avg `0.004283`, median `0.008809`
- 5d: sample `16`, primary_hit `0.3125`, primary_closer `0.3125`, primary_mae `0.027704`, avg `0.004298`, median `0.007597`
- 10d: sample `16`, primary_hit `0.3125`, primary_closer `0.25`, primary_mae `0.038293`, avg `0.000961`, median `0.005974`
- 20d: sample `16`, primary_hit `0.25`, primary_closer `0.4375`, primary_mae `0.05263`, avg `0.016421`, median `0.017343`
- 60d: sample `16`, primary_hit `0.0625`, primary_closer `0.375`, primary_mae `0.051922`, avg `0.064264`, median `0.06255`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.875`, primary_closer `0.25`, primary_mae `0.023321`, avg `-0.016732`, median `-0.014095`
- 5d: sample `16`, primary_hit `0.75`, primary_closer `0.375`, primary_mae `0.027724`, avg `-0.016736`, median `-0.012686`
- 10d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.049712`, avg `0.002404`, median `0.012828`
- 20d: sample `16`, primary_hit `0.4375`, primary_closer `0.375`, primary_mae `0.090019`, avg `0.017423`, median `0.039587`
- 60d: sample `16`, primary_hit `0.1875`, primary_closer `0.25`, primary_mae `0.090566`, avg `0.065669`, median `0.114142`

- effectiveness_question: `historical_replay_supportive_but_not_forward_validated`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020277`, avg `-0.006906`, median `-0.004451`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.025749`, avg `-0.010059`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.03619`, avg `-0.005419`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.069133`, avg `0.010537`, median `0.018008`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.090862`, avg `0.049908`, median `0.060391`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.6`, primary_closer `0.425`, primary_mae `0.020277`, avg `-0.006906`, median `-0.004451`
- 5d: sample `80`, primary_hit `0.5625`, primary_closer `0.3625`, primary_mae `0.025749`, avg `-0.010059`, median `-0.006281`
- 10d: sample `80`, primary_hit `0.5125`, primary_closer `0.375`, primary_mae `0.03619`, avg `-0.005419`, median `-0.000315`
- 20d: sample `80`, primary_hit `0.375`, primary_closer `0.35`, primary_mae `0.069133`, avg `0.010537`, median `0.018008`
- 60d: sample `80`, primary_hit `0.1875`, primary_closer `0.3`, primary_mae `0.090862`, avg `0.049908`, median `0.060391`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.5`, primary_closer `0.45`, primary_mae `0.022685`, avg `-0.003689`, median `-0.00023`
- 5d: sample `40`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.030176`, avg `-0.009478`, median `-0.009034`
- 10d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.036468`, avg `-0.010821`, median `-0.006475`
- 20d: sample `40`, primary_hit `0.4`, primary_closer `0.425`, primary_mae `0.064841`, avg `0.004847`, median `0.015082`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.375`, primary_mae `0.097792`, avg `0.042938`, median `0.056479`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.7`, primary_closer `0.4`, primary_mae `0.01787`, avg `-0.010123`, median `-0.009933`
- 5d: sample `40`, primary_hit `0.575`, primary_closer `0.325`, primary_mae `0.021321`, avg `-0.01064`, median `-0.004042`
- 10d: sample `40`, primary_hit `0.45`, primary_closer `0.425`, primary_mae `0.035912`, avg `-1.7e-05`, median `0.006069`
- 20d: sample `40`, primary_hit `0.35`, primary_closer `0.275`, primary_mae `0.073425`, avg `0.016227`, median `0.030977`
- 60d: sample `40`, primary_hit `0.15`, primary_closer `0.225`, primary_mae `0.083932`, avg `0.056878`, median `0.075175`

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
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.0121`, avg `-0.000934`, median `-0.000774`
- 5d: sample `20`, primary_hit `0.35`, primary_closer `0.3`, primary_mae `0.014792`, avg `-0.002844`, median `0.001566`
- 10d: sample `20`, primary_hit `0.35`, primary_closer `0.35`, primary_mae `0.027452`, avg `0.0072`, median `0.01092`
- 20d: sample `20`, primary_hit `0.15`, primary_closer `0.15`, primary_mae `0.067739`, avg `0.025518`, median `0.032633`
- 60d: sample `20`, primary_hit `0.1`, primary_closer `0.15`, primary_mae `0.083988`, avg `0.047248`, median `0.053848`

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
