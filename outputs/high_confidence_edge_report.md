# High Confidence Edge Report

Generated at: `2026-10-21T17:21:15.096240+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `124`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `124`, gate `stronger_evidence`
- 5d: completed `124`, gate `stronger_evidence`
- 10d: completed `124`, gate `stronger_evidence`
- 20d: completed `124`, gate `stronger_evidence`
- 60d: completed `124`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001027`, median `0.001558`, mae `0.009999`
- 5d: sample `40`, hit `0.525`, avg `-0.000808`, median `0.003005`, mae `0.012982`
- 10d: sample `40`, hit `0.575`, avg `0.003259`, median `0.007467`, mae `0.017226`
- 20d: sample `40`, hit `0.775`, avg `0.018673`, median `0.023636`, mae `0.026461`
- 60d: sample `40`, hit `0.625`, avg `0.021943`, median `0.036513`, mae `0.064767`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000808`, median `0.007374`, mae `0.015454`
- 5d: sample `40`, hit `0.5`, avg `0.000281`, median `0.000519`, mae `0.020579`
- 10d: sample `40`, hit `0.525`, avg `0.000212`, median `0.004924`, mae `0.029343`
- 20d: sample `40`, hit `0.7`, avg `0.016215`, median `0.019265`, mae `0.031969`
- 60d: sample `40`, hit `0.725`, avg `0.042894`, median `0.042006`, mae `0.063519`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.008856`, median `-0.009383`, mae `0.017435`
- 5d: sample `8`, hit `0.375`, avg `-0.007496`, median `-0.004438`, mae `0.017059`
- 10d: sample `8`, hit `0.375`, avg `-0.004284`, median `-0.010456`, mae `0.020099`
- 20d: sample `8`, hit `0.625`, avg `0.010284`, median `0.026531`, mae `0.033483`
- 60d: sample `8`, hit `0.5`, avg `0.004041`, median `0.029831`, mae `0.061685`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.008856`, median `-0.009383`, mae `0.017435`
- 5d: sample `8`, hit `0.375`, avg `-0.007496`, median `-0.004438`, mae `0.017059`
- 10d: sample `8`, hit `0.375`, avg `-0.004284`, median `-0.010456`, mae `0.020099`
- 20d: sample `8`, hit `0.625`, avg `0.010284`, median `0.026531`, mae `0.033483`
- 60d: sample `8`, hit `0.5`, avg `0.004041`, median `0.029831`, mae `0.061685`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001027, 'median_return': 0.001558, 'mean_absolute_return': 0.009999, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.000808, 'median_return': 0.003005, 'mean_absolute_return': 0.012982, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003259, 'median_return': 0.007467, 'mean_absolute_return': 0.017226, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.032557}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.018673, 'median_return': 0.023636, 'mean_absolute_return': 0.026461, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.021943, 'median_return': 0.036513, 'mean_absolute_return': 0.064767, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008856, 'median_return': -0.009383, 'mean_absolute_return': 0.017435, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007496, 'median_return': -0.004438, 'mean_absolute_return': 0.017059, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.004284, 'median_return': -0.010456, 'mean_absolute_return': 0.020099, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.010284, 'median_return': 0.026531, 'mean_absolute_return': 0.033483, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004041, 'median_return': 0.029831, 'mean_absolute_return': 0.061685, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.000862, 'median_return': 0.003412, 'mean_absolute_return': 0.012203, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.00054, 'median_return': 0.003026, 'mean_absolute_return': 0.016749, 'max_adverse_excursion': -0.040291, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002404, 'median_return': 0.006356, 'mean_absolute_return': 0.023639, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.01824, 'median_return': 0.022652, 'mean_absolute_return': 0.028741, 'max_adverse_excursion': -0.061156, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.035572, 'median_return': 0.042006, 'mean_absolute_return': 0.064416, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.167676}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.5}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.5375}, '60d': {'sample_size': 80, 'hit_rate': 0.45}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.0625, 'both_hit': 13, 'both_miss': 8}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.05, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.15, 'both_hit': 12, 'both_miss': 8}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.0, 'median_return': 0.00234, 'mean_absolute_return': 0.010808, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.000178, 'median_return': 0.003005, 'mean_absolute_return': 0.014296, 'max_adverse_excursion': -0.040291, 'max_favorable_excursion': 0.032128}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.003568, 'median_return': 0.007467, 'mean_absolute_return': 0.019907, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.037669}, '20d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.018988, 'median_return': 0.022652, 'mean_absolute_return': 0.030217, 'max_adverse_excursion': -0.048112, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.030219, 'median_return': 0.036513, 'mean_absolute_return': 0.069884, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.167676}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.00044, 'median_return': 0.003412, 'mean_absolute_return': 0.018481, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001588, 'median_return': -0.003888, 'mean_absolute_return': 0.024234, 'max_adverse_excursion': -0.036122, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.003762, 'median_return': -0.01314, 'mean_absolute_return': 0.033417, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.053454}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.012812, 'median_return': 0.023289, 'mean_absolute_return': 0.026211, 'max_adverse_excursion': -0.061156, 'max_favorable_excursion': 0.060178}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.039017, 'median_return': 0.042006, 'mean_absolute_return': 0.046921, 'max_adverse_excursion': -0.035018, 'max_favorable_excursion': 0.108246}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001027`, median `0.001558`, mae `0.009999`
- 5d: sample `40`, hit `0.525`, avg `-0.000808`, median `0.003005`, mae `0.012982`
- 10d: sample `40`, hit `0.575`, avg `0.003259`, median `0.007467`, mae `0.017226`
- 20d: sample `40`, hit `0.775`, avg `0.018673`, median `0.023636`, mae `0.026461`
- 60d: sample `40`, hit `0.625`, avg `0.021943`, median `0.036513`, mae `0.064767`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000808`, median `0.007374`, mae `0.015454`
- 5d: sample `40`, hit `0.5`, avg `0.000281`, median `0.000519`, mae `0.020579`
- 10d: sample `40`, hit `0.525`, avg `0.000212`, median `0.004924`, mae `0.029343`
- 20d: sample `40`, hit `0.7`, avg `0.016215`, median `0.019265`, mae `0.031969`
- 60d: sample `40`, hit `0.725`, avg `0.042894`, median `0.042006`, mae `0.063519`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001027`, median `0.001558`, mae `0.009999`
- 5d: sample `40`, hit `0.525`, avg `-0.000808`, median `0.003005`, mae `0.012982`
- 10d: sample `40`, hit `0.575`, avg `0.003259`, median `0.007467`, mae `0.017226`
- 20d: sample `40`, hit `0.775`, avg `0.018673`, median `0.023636`, mae `0.026461`
- 60d: sample `40`, hit `0.625`, avg `0.021943`, median `0.036513`, mae `0.064767`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.005259`, median `-0.001811`, mae `0.01199`
- 5d: sample `20`, hit `0.4`, avg `-0.005004`, median `-0.004438`, mae `0.013175`
- 10d: sample `20`, hit `0.4`, avg `0.001083`, median `-0.003071`, mae `0.016902`
- 20d: sample `20`, hit `0.8`, avg `0.023202`, median `0.031196`, mae `0.03324`
- 60d: sample `20`, hit `0.65`, avg `0.037776`, median `0.059495`, mae `0.068243`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002055`, median `0.007492`, mae `0.012426`
- 5d: sample `20`, hit `0.55`, avg `0.00215`, median `0.007116`, mae `0.016923`
- 10d: sample `20`, hit `0.65`, avg `0.004186`, median `0.017632`, mae `0.025269`
- 20d: sample `20`, hit `0.7`, avg `0.019619`, median `0.019265`, mae `0.037727`
- 60d: sample `20`, hit `0.65`, avg `0.046771`, median `0.058598`, mae `0.080117`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001027`, median `0.001558`, mae `0.009999`
- 5d: sample `40`, hit `0.525`, avg `-0.000808`, median `0.003005`, mae `0.012982`
- 10d: sample `40`, hit `0.575`, avg `0.003259`, median `0.007467`, mae `0.017226`
- 20d: sample `40`, hit `0.775`, avg `0.018673`, median `0.023636`, mae `0.026461`
- 60d: sample `40`, hit `0.625`, avg `0.021943`, median `0.036513`, mae `0.064767`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.005259`, median `-0.001811`, mae `0.01199`
- 5d: sample `20`, hit `0.4`, avg `-0.005004`, median `-0.004438`, mae `0.013175`
- 10d: sample `20`, hit `0.4`, avg `0.001083`, median `-0.003071`, mae `0.016902`
- 20d: sample `20`, hit `0.8`, avg `0.023202`, median `0.031196`, mae `0.03324`
- 60d: sample `20`, hit `0.65`, avg `0.037776`, median `0.059495`, mae `0.068243`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000808`, median `0.007374`, mae `0.015454`
- 5d: sample `40`, hit `0.5`, avg `0.000281`, median `0.000519`, mae `0.020579`
- 10d: sample `40`, hit `0.525`, avg `0.000212`, median `0.004924`, mae `0.029343`
- 20d: sample `40`, hit `0.7`, avg `0.016215`, median `0.019265`, mae `0.031969`
- 60d: sample `40`, hit `0.725`, avg `0.042894`, median `0.042006`, mae `0.063519`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `-0.00011`, median `0.00234`, mae `0.012726`
- 5d: sample `80`, hit `0.5125`, avg `-0.000264`, median `0.000519`, mae `0.01678`
- 10d: sample `80`, hit `0.55`, avg `0.001735`, median `0.004924`, mae `0.023285`
- 20d: sample `80`, hit `0.7375`, avg `0.017444`, median `0.022652`, mae `0.029215`
- 60d: sample `80`, hit `0.675`, avg `0.032419`, median `0.036513`, mae `0.064143`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001027`, median `0.001558`, mae `0.009999`
- 5d: sample `40`, hit `0.525`, avg `-0.000808`, median `0.003005`, mae `0.012982`
- 10d: sample `40`, hit `0.575`, avg `0.003259`, median `0.007467`, mae `0.017226`
- 20d: sample `40`, hit `0.775`, avg `0.018673`, median `0.023636`, mae `0.026461`
- 60d: sample `40`, hit `0.625`, avg `0.021943`, median `0.036513`, mae `0.064767`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5375`, avg `-0.00011`, median `0.00234`, mae `0.012726`
- 5d: sample `80`, hit `0.5125`, avg `-0.000264`, median `0.000519`, mae `0.01678`
- 10d: sample `80`, hit `0.55`, avg `0.001735`, median `0.004924`, mae `0.023285`
- 20d: sample `80`, hit `0.7375`, avg `0.017444`, median `0.022652`, mae `0.029215`
- 60d: sample `80`, hit `0.675`, avg `0.032419`, median `0.036513`, mae `0.064143`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001027`, median `0.001558`, mae `0.009999`
- 5d: sample `40`, hit `0.525`, avg `-0.000808`, median `0.003005`, mae `0.012982`
- 10d: sample `40`, hit `0.575`, avg `0.003259`, median `0.007467`, mae `0.017226`
- 20d: sample `40`, hit `0.775`, avg `0.018673`, median `0.023636`, mae `0.026461`
- 60d: sample `40`, hit `0.625`, avg `0.021943`, median `0.036513`, mae `0.064767`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.000808`, median `0.007374`, mae `0.015454`
- 5d: sample `40`, hit `0.5`, avg `0.000281`, median `0.000519`, mae `0.020579`
- 10d: sample `40`, hit `0.525`, avg `0.000212`, median `0.004924`, mae `0.029343`
- 20d: sample `40`, hit `0.7`, avg `0.016215`, median `0.019265`, mae `0.031969`
- 60d: sample `40`, hit `0.725`, avg `0.042894`, median `0.042006`, mae `0.063519`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
