# Historical Replay Benchmark

Generated at: `2026-09-08T16:41:37.307548+00:00`
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
- primary_hit_rate: `0.4875`
- secondary_hit_rate: `0.5125`
- primary_vs_secondary_accuracy_spread: `-0.025`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.018501`
- secondary_mean_absolute_error: `0.013866`
- primary_error_advantage: `-0.004635`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 5d
- sample_size: `80`
- primary_hit_rate: `0.4625`
- secondary_hit_rate: `0.5375`
- primary_vs_secondary_accuracy_spread: `-0.075`
- primary_closer_than_secondary_rate: `0.425`
- primary_mean_absolute_error: `0.019925`
- secondary_mean_absolute_error: `0.017186`
- primary_error_advantage: `-0.002739`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4167`

### 10d
- sample_size: `80`
- primary_hit_rate: `0.6`
- secondary_hit_rate: `0.4`
- primary_vs_secondary_accuracy_spread: `0.2`
- primary_closer_than_secondary_rate: `0.575`
- primary_mean_absolute_error: `0.028375`
- secondary_mean_absolute_error: `0.031152`
- primary_error_advantage: `0.002777`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.6167`

### 20d
- sample_size: `80`
- primary_hit_rate: `0.325`
- secondary_hit_rate: `0.675`
- primary_vs_secondary_accuracy_spread: `-0.35`
- primary_closer_than_secondary_rate: `0.375`
- primary_mean_absolute_error: `0.054044`
- secondary_mean_absolute_error: `0.041673`
- primary_error_advantage: `-0.012371`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.3833`

### 60d
- sample_size: `80`
- primary_hit_rate: `0.3`
- secondary_hit_rate: `0.7`
- primary_vs_secondary_accuracy_spread: `-0.4`
- primary_closer_than_secondary_rate: `0.4125`
- primary_mean_absolute_error: `0.085258`
- secondary_mean_absolute_error: `0.064792`
- primary_error_advantage: `-0.020466`
- close_call_sample_size: `60`
- close_call_primary_closer_rate: `0.4333`

## Scenario Type Performance

### base_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014051`, as_primary `0`, as_primary_hit `None`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.016891`, as_primary `0`, as_primary_hit `None`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.026481`, as_primary `0`, as_primary_hit `None`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.034105`, as_primary `0`, as_primary_hit `None`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.061439`, as_primary `0`, as_primary_hit `None`, avg `0.035945`, median `0.051777`

### bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.014257`, as_primary `0`, as_primary_hit `None`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.018442`, as_primary `0`, as_primary_hit `None`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.036347`, as_primary `0`, as_primary_hit `None`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.04891`, as_primary `0`, as_primary_hit `None`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.074265`, as_primary `0`, as_primary_hit `None`, avg `0.035945`, median `0.051777`

### failed_bounce_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.4875`, path_mae `0.018501`, as_primary `80`, as_primary_hit `0.5125`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, direction_hit `0.4625`, path_mae `0.019925`, as_primary `80`, as_primary_hit `0.5375`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, direction_hit `0.6`, path_mae `0.028375`, as_primary `80`, as_primary_hit `0.4`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.325`, path_mae `0.054044`, as_primary `80`, as_primary_hit `0.675`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, direction_hit `0.3`, path_mae `0.085258`, as_primary `80`, as_primary_hit `0.7`, avg `0.035945`, median `0.051777`

### analog_average_path
- sample_size: `80`
- 3d: sample `80`, direction_hit `0.5125`, path_mae `0.013973`, as_primary `0`, as_primary_hit `None`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, direction_hit `0.5375`, path_mae `0.016816`, as_primary `0`, as_primary_hit `None`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, direction_hit `0.4`, path_mae `0.023347`, as_primary `0`, as_primary_hit `None`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, direction_hit `0.675`, path_mae `0.031905`, as_primary `0`, as_primary_hit `None`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, direction_hit `0.7`, path_mae `0.058202`, as_primary `0`, as_primary_hit `None`, avg `0.035945`, median `0.051777`

## Edge Status Performance

### RISK_WARNING
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.018501`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.019925`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.028375`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054044`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.085258`, avg `0.035945`, median `0.051777`

## Predictor Performance

### bounce_predictor
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.008821`, avg `-0.002498`, median `-0.002618`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.011098`, avg `-0.004111`, median `-0.000876`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.020618`, avg `-0.009002`, median `-0.013311`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.06377`, avg `-0.013876`, median `-0.005516`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.088`, avg `0.011253`, median `0.013899`

### downside_continuation_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### trend_reversal_predictor
- sample_size: `60`
- 3d: sample `60`, primary_hit `0.45`, primary_closer `0.35`, primary_mae `0.021728`, avg `-0.000393`, median `0.001691`
- 5d: sample `60`, primary_hit `0.45`, primary_closer `0.4333`, primary_mae `0.022868`, avg `0.000446`, median `0.002122`
- 10d: sample `60`, primary_hit `0.55`, primary_closer `0.5167`, primary_mae `0.03096`, avg `0.002631`, median `-0.004843`
- 20d: sample `60`, primary_hit `0.25`, primary_closer `0.3667`, primary_mae `0.050802`, avg `0.017722`, median `0.021678`
- 60d: sample `60`, primary_hit `0.2333`, primary_closer `0.3833`, primary_mae `0.084344`, avg `0.044176`, median `0.056221`

### risk_expansion_predictor
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

## Best Predictor By Horizon

- 3d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.008821, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 5d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.011098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 10d: `{'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.020618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 20d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.050802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`
- 60d: `{'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.084344, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}`

## Horizon Performance

- 3d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_vs_secondary_accuracy_spread': -0.025, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.013973, 'direction_hit_rate': 0.5125}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.018501, 'direction_hit_rate': 0.4875}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.6, 'primary_closer_than_secondary_rate': 0.45, 'primary_mean_absolute_error': 0.008821, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 5d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_vs_secondary_accuracy_spread': -0.075, 'primary_closer_than_secondary_rate': 0.425, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.016816, 'direction_hit_rate': 0.5375}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.019925, 'direction_hit_rate': 0.4625}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.5, 'primary_closer_than_secondary_rate': 0.4, 'primary_mean_absolute_error': 0.011098, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 10d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_vs_secondary_accuracy_spread': 0.2, 'primary_closer_than_secondary_rate': 0.575, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.023347, 'direction_hit_rate': 0.4}, 'worst_scenario_type': {'scenario': 'bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.036347, 'direction_hit_rate': 0.4}, 'best_predictor': {'predictor': 'bounce_predictor', 'sample_size': 20, 'primary_hit_rate': 0.75, 'primary_closer_than_secondary_rate': 0.75, 'primary_mean_absolute_error': 0.020618, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 20d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_vs_secondary_accuracy_spread': -0.35, 'primary_closer_than_secondary_rate': 0.375, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.031905, 'direction_hit_rate': 0.675}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.054044, 'direction_hit_rate': 0.325}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.25, 'primary_closer_than_secondary_rate': 0.3667, 'primary_mean_absolute_error': 0.050802, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`
- 60d: `{'sample_size': 80, 'sample_gate': 'moderate_evidence', 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_vs_secondary_accuracy_spread': -0.4, 'primary_closer_than_secondary_rate': 0.4125, 'best_scenario_type': {'scenario': 'analog_average_path', 'sample_size': 80, 'path_mean_absolute_error': 0.058202, 'direction_hit_rate': 0.7}, 'worst_scenario_type': {'scenario': 'failed_bounce_path', 'sample_size': 80, 'path_mean_absolute_error': 0.085258, 'direction_hit_rate': 0.3}, 'best_predictor': {'predictor': 'trend_reversal_predictor', 'sample_size': 60, 'primary_hit_rate': 0.2333, 'primary_closer_than_secondary_rate': 0.3833, 'primary_mean_absolute_error': 0.084344, 'selection_method': 'lowest primary path error, tie-broken by hit rate and primary-vs-secondary closeness'}}`

## Signal Confirmation Effectiveness

### top_10
- sample_size: `8`
- 3d: sample `8`, primary_hit `0.375`, primary_closer `0.25`, primary_mae `0.027922`, avg `0.002979`, median `0.011157`
- 5d: sample `8`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.029434`, avg `0.008595`, median `0.004639`
- 10d: sample `8`, primary_hit `0.5`, primary_closer `0.625`, primary_mae `0.029166`, avg `-0.005178`, median `-0.005711`
- 20d: sample `8`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.058523`, avg `-0.002322`, median `0.004283`
- 60d: sample `8`, primary_hit `0.25`, primary_closer `0.625`, primary_mae `0.085037`, avg `0.004335`, median `0.007994`

### top_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.4375`, primary_closer `0.25`, primary_mae `0.026782`, avg `-0.001767`, median `0.00122`
- 5d: sample `16`, primary_hit `0.375`, primary_closer `0.375`, primary_mae `0.030415`, avg `0.00512`, median `0.009264`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5625`, primary_mae `0.036198`, avg `-0.000874`, median `-0.005711`
- 20d: sample `16`, primary_hit `0.375`, primary_closer `0.5`, primary_mae `0.06035`, avg `0.004491`, median `0.004833`
- 60d: sample `16`, primary_hit `0.25`, primary_closer `0.5`, primary_mae `0.098208`, avg `0.022822`, median `0.026306`

### bottom_20
- sample_size: `16`
- 3d: sample `16`, primary_hit `0.375`, primary_closer `0.3125`, primary_mae `0.024986`, avg `0.005292`, median `0.009495`
- 5d: sample `16`, primary_hit `0.4375`, primary_closer `0.4375`, primary_mae `0.029504`, avg `0.005514`, median `0.009408`
- 10d: sample `16`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.037138`, avg `0.010816`, median `-0.004137`
- 20d: sample `16`, primary_hit `0.1875`, primary_closer `0.3125`, primary_mae `0.040662`, avg `0.033003`, median `0.024365`
- 60d: sample `16`, primary_hit `0.125`, primary_closer `0.3125`, primary_mae `0.061697`, avg `0.073094`, median `0.071616`

- effectiveness_question: `historical_replay_mixed_or_not_better_keep_confidence_capped`

## Data Completeness / Evidence Buckets

### high_data_completeness
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.018501`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.019925`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.028375`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054044`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.085258`, avg `0.035945`, median `0.051777`

### low_data_completeness
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### fred_available
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.018501`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.019925`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.028375`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054044`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.085258`, avg `0.035945`, median `0.051777`

### fred_missing
- sample_size: `0`
- 3d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 5d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 10d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 20d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`
- 60d: sample `0`, primary_hit `None`, primary_closer `None`, primary_mae `None`, avg `None`, median `None`

### breadth_confirmed
- sample_size: `20`
- 3d: sample `20`, primary_hit `0.6`, primary_closer `0.45`, primary_mae `0.008821`, avg `-0.002498`, median `-0.002618`
- 5d: sample `20`, primary_hit `0.5`, primary_closer `0.4`, primary_mae `0.011098`, avg `-0.004111`, median `-0.000876`
- 10d: sample `20`, primary_hit `0.75`, primary_closer `0.75`, primary_mae `0.020618`, avg `-0.009002`, median `-0.013311`
- 20d: sample `20`, primary_hit `0.55`, primary_closer `0.4`, primary_mae `0.06377`, avg `-0.013876`, median `-0.005516`
- 60d: sample `20`, primary_hit `0.5`, primary_closer `0.5`, primary_mae `0.088`, avg `0.011253`, median `0.013899`

### breadth_conflicted
- sample_size: `40`
- 3d: sample `40`, primary_hit `0.45`, primary_closer `0.375`, primary_mae `0.02035`, avg `0.001126`, median `0.002335`
- 5d: sample `40`, primary_hit `0.475`, primary_closer `0.45`, primary_mae `0.020484`, avg `-0.000793`, median `0.000311`
- 10d: sample `40`, primary_hit `0.55`, primary_closer `0.475`, primary_mae `0.029609`, avg `0.005261`, median `-0.002801`
- 20d: sample `40`, primary_hit `0.175`, primary_closer `0.3`, primary_mae `0.046483`, avg `0.024294`, median `0.02778`
- 60d: sample `40`, primary_hit `0.225`, primary_closer `0.325`, primary_mae `0.079064`, avg `0.053993`, median `0.064699`

### options_confirmed
- sample_size: `80`
- 3d: sample `80`, primary_hit `0.4875`, primary_closer `0.375`, primary_mae `0.018501`, avg `-0.00092`, median `0.000609`
- 5d: sample `80`, primary_hit `0.4625`, primary_closer `0.425`, primary_mae `0.019925`, avg `-0.000693`, median `0.000781`
- 10d: sample `80`, primary_hit `0.6`, primary_closer `0.575`, primary_mae `0.028375`, avg `-0.000277`, median `-0.008001`
- 20d: sample `80`, primary_hit `0.325`, primary_closer `0.375`, primary_mae `0.054044`, avg `0.009822`, median `0.015718`
- 60d: sample `80`, primary_hit `0.3`, primary_closer `0.4125`, primary_mae `0.085258`, avg `0.035945`, median `0.051777`

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
