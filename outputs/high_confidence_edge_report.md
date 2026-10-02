# High Confidence Edge Report

Generated at: `2026-10-02T17:54:46.221583+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `72`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `72`, gate `moderate_evidence`
- 5d: completed `72`, gate `moderate_evidence`
- 10d: completed `72`, gate `moderate_evidence`
- 20d: completed `72`, gate `moderate_evidence`
- 60d: completed `72`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003596`, median `-0.001658`, mae `0.015343`
- 5d: sample `40`, hit `0.475`, avg `-0.00682`, median `-0.000423`, mae `0.016237`
- 10d: sample `40`, hit `0.45`, avg `-0.00613`, median `-0.004767`, mae `0.023858`
- 20d: sample `40`, hit `0.575`, avg `0.00246`, median `0.014747`, mae `0.036902`
- 60d: sample `40`, hit `0.825`, avg `0.032175`, median `0.044367`, mae `0.062417`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.004079`, median `-0.002952`, mae `0.016332`
- 5d: sample `40`, hit `0.45`, avg `-0.00324`, median `-0.002452`, mae `0.018593`
- 10d: sample `40`, hit `0.525`, avg `-0.009427`, median `0.003815`, mae `0.034958`
- 20d: sample `40`, hit `0.575`, avg `0.004458`, median `0.015416`, mae `0.045497`
- 60d: sample `40`, hit `0.825`, avg `0.064892`, median `0.084597`, mae `0.087178`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.000163`, median `0.004068`, mae `0.010102`
- 5d: sample `8`, hit `0.625`, avg `0.001297`, median `0.009569`, mae `0.010053`
- 10d: sample `8`, hit `0.625`, avg `0.003735`, median `0.012066`, mae `0.018711`
- 20d: sample `8`, hit `0.75`, avg `0.012634`, median `0.033164`, mae `0.042335`
- 60d: sample `8`, hit `1.0`, avg `0.050604`, median `0.05019`, mae `0.050604`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.000163`, median `0.004068`, mae `0.010102`
- 5d: sample `8`, hit `0.625`, avg `0.001297`, median `0.009569`, mae `0.010053`
- 10d: sample `8`, hit `0.625`, avg `0.003735`, median `0.012066`, mae `0.018711`
- 20d: sample `8`, hit `0.75`, avg `0.012634`, median `0.033164`, mae `0.042335`
- 60d: sample `8`, hit `1.0`, avg `0.050604`, median `0.05019`, mae `0.050604`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000163, 'median_return': 0.004068, 'mean_absolute_return': 0.010102, 'max_adverse_excursion': -0.031857, 'max_favorable_excursion': 0.016338}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001297, 'median_return': 0.009569, 'mean_absolute_return': 0.010053, 'max_adverse_excursion': -0.018424, 'max_favorable_excursion': 0.013193}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003735, 'median_return': 0.012066, 'mean_absolute_return': 0.018711, 'max_adverse_excursion': -0.04812, 'max_favorable_excursion': 0.035913}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.012634, 'median_return': 0.033164, 'mean_absolute_return': 0.042335, 'max_adverse_excursion': -0.083351, 'max_favorable_excursion': 0.059335}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.050604, 'median_return': 0.05019, 'mean_absolute_return': 0.050604, 'max_adverse_excursion': 0.029401, 'max_favorable_excursion': 0.075909}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.004246, 'median_return': -0.003244, 'mean_absolute_return': 0.016475, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.005733, 'median_return': -0.003262, 'mean_absolute_return': 0.018233, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.009058, 'median_return': -0.006389, 'mean_absolute_return': 0.030597, 'max_adverse_excursion': -0.078971, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.00244, 'median_return': 0.012117, 'mean_absolute_return': 0.041074, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.048303, 'median_return': 0.059104, 'mean_absolute_return': 0.077485, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.175}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_minus_secondary': -0.65, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.003838, 'median_return': -0.002952, 'mean_absolute_return': 0.015838, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.00503, 'median_return': -0.002166, 'mean_absolute_return': 0.017415, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.007779, 'median_return': -0.0004, 'mean_absolute_return': 0.029408, 'max_adverse_excursion': -0.078971, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.003459, 'median_return': 0.014747, 'mean_absolute_return': 0.0412, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.825, 'avg_return': 0.048533, 'median_return': 0.056732, 'mean_absolute_return': 0.074797, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.154804}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.003838`, median `-0.002952`, mae `0.015838`
- 5d: sample `80`, hit `0.4625`, avg `-0.00503`, median `-0.002166`, mae `0.017415`
- 10d: sample `80`, hit `0.4875`, avg `-0.007779`, median `-0.0004`, mae `0.029408`
- 20d: sample `80`, hit `0.575`, avg `0.003459`, median `0.014747`, mae `0.0412`
- 60d: sample `80`, hit `0.825`, avg `0.048533`, median `0.056732`, mae `0.074797`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.003838`, median `-0.002952`, mae `0.015838`
- 5d: sample `80`, hit `0.4625`, avg `-0.00503`, median `-0.002166`, mae `0.017415`
- 10d: sample `80`, hit `0.4875`, avg `-0.007779`, median `-0.0004`, mae `0.029408`
- 20d: sample `80`, hit `0.575`, avg `0.003459`, median `0.014747`, mae `0.0412`
- 60d: sample `80`, hit `0.825`, avg `0.048533`, median `0.056732`, mae `0.074797`

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
- 3d: sample `80`, hit `0.45`, avg `-0.003838`, median `-0.002952`, mae `0.015838`
- 5d: sample `80`, hit `0.4625`, avg `-0.00503`, median `-0.002166`, mae `0.017415`
- 10d: sample `80`, hit `0.4875`, avg `-0.007779`, median `-0.0004`, mae `0.029408`
- 20d: sample `80`, hit `0.575`, avg `0.003459`, median `0.014747`, mae `0.0412`
- 60d: sample `80`, hit `0.825`, avg `0.048533`, median `0.056732`, mae `0.074797`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.003838`, median `-0.002952`, mae `0.015838`
- 5d: sample `80`, hit `0.4625`, avg `-0.00503`, median `-0.002166`, mae `0.017415`
- 10d: sample `80`, hit `0.4875`, avg `-0.007779`, median `-0.0004`, mae `0.029408`
- 20d: sample `80`, hit `0.575`, avg `0.003459`, median `0.014747`, mae `0.0412`
- 60d: sample `80`, hit `0.825`, avg `0.048533`, median `0.056732`, mae `0.074797`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### risk_path_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
