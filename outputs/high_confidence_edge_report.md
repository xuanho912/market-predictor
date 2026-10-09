# High Confidence Edge Report

Generated at: `2026-10-09T01:25:47.379067+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `88`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `88`, gate `moderate_evidence`
- 5d: completed `88`, gate `moderate_evidence`
- 10d: completed `88`, gate `moderate_evidence`
- 20d: completed `88`, gate `moderate_evidence`
- 60d: completed `88`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.002886`, median `-0.001797`, mae `0.017958`
- 5d: sample `80`, hit `0.425`, avg `-0.00483`, median `-0.010073`, mae `0.022904`
- 10d: sample `80`, hit `0.525`, avg `-0.000456`, median `0.001517`, mae `0.0288`
- 20d: sample `80`, hit `0.725`, avg `0.029362`, median `0.029348`, mae `0.046397`
- 60d: sample `80`, hit `0.8375`, avg `0.069369`, median `0.084301`, mae `0.079526`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `8`, hit `0.75`, avg `0.010606`, median `0.0207`, mae `0.019302`
- 5d: sample `8`, hit `0.875`, avg `0.014887`, median `0.013852`, mae `0.02145`
- 10d: sample `8`, hit `0.75`, avg `0.016471`, median `0.024811`, mae `0.024193`
- 20d: sample `8`, hit `1.0`, avg `0.059849`, median `0.062955`, mae `0.059849`
- 60d: sample `8`, hit `1.0`, avg `0.105861`, median `0.099838`, mae `0.105861`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.010606`, median `0.0207`, mae `0.019302`
- 5d: sample `8`, hit `0.875`, avg `0.014887`, median `0.013852`, mae `0.02145`
- 10d: sample `8`, hit `0.75`, avg `0.016471`, median `0.024811`, mae `0.024193`
- 20d: sample `8`, hit `1.0`, avg `0.059849`, median `0.062955`, mae `0.059849`
- 60d: sample `8`, hit `1.0`, avg `0.105861`, median `0.099838`, mae `0.105861`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.002886, 'median_return': -0.001797, 'mean_absolute_return': 0.017958, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.00483, 'median_return': -0.010073, 'mean_absolute_return': 0.022904, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.000456, 'median_return': 0.001517, 'mean_absolute_return': 0.0288, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.029362, 'median_return': 0.029348, 'mean_absolute_return': 0.046397, 'max_adverse_excursion': -0.090946, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.8375, 'avg_return': 0.069369, 'median_return': 0.084301, 'mean_absolute_return': 0.079526, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010606, 'median_return': 0.0207, 'mean_absolute_return': 0.019302, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.014887, 'median_return': 0.013852, 'mean_absolute_return': 0.02145, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016471, 'median_return': 0.024811, 'mean_absolute_return': 0.024193, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.059849, 'median_return': 0.062955, 'mean_absolute_return': 0.059849, 'max_adverse_excursion': 0.024743, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.105861, 'median_return': 0.099838, 'mean_absolute_return': 0.105861, 'max_adverse_excursion': 0.085781, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.004386, 'median_return': -0.003676, 'mean_absolute_return': 0.017808, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.007021, 'median_return': -0.013237, 'mean_absolute_return': 0.023066, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.002337, 'median_return': 0.000197, 'mean_absolute_return': 0.029312, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.025975, 'median_return': 0.027502, 'mean_absolute_return': 0.044902, 'max_adverse_excursion': -0.090946, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.065315, 'median_return': 0.079528, 'mean_absolute_return': 0.0766, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.725}, '60d': {'sample_size': 80, 'hit_rate': 0.6625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.15, 'both_hit': 15, 'both_miss': 5}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.125, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.075, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.275, 'both_hit': 17, 'both_miss': 3}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.1, 'both_hit': 19, 'both_miss': 1}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.002886, 'median_return': -0.001797, 'mean_absolute_return': 0.017958, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.00483, 'median_return': -0.010073, 'mean_absolute_return': 0.022904, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.000456, 'median_return': 0.001517, 'mean_absolute_return': 0.0288, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.029362, 'median_return': 0.029348, 'mean_absolute_return': 0.046397, 'max_adverse_excursion': -0.090946, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.8375, 'avg_return': 0.069369, 'median_return': 0.084301, 'mean_absolute_return': 0.079526, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008481`, median `0.012813`, mae `0.016317`
- 5d: sample `20`, hit `0.65`, avg `0.00962`, median `0.010241`, mae `0.019149`
- 10d: sample `20`, hit `0.75`, avg `0.01323`, median `0.013997`, mae `0.022886`
- 20d: sample `20`, hit `0.85`, avg `0.042711`, median `0.043456`, mae `0.045706`
- 60d: sample `20`, hit `0.95`, avg `0.093442`, median `0.099719`, mae `0.098038`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.3`, avg `-0.007327`, median `-0.009843`, mae `0.019932`
- 5d: sample `40`, hit `0.3`, avg `-0.01019`, median `-0.017697`, mae `0.026506`
- 10d: sample `40`, hit `0.425`, avg `-0.001478`, median `-0.009092`, mae `0.034891`
- 20d: sample `40`, hit `0.725`, avg `0.032865`, median `0.027885`, mae `0.053381`
- 60d: sample `40`, hit `0.8`, avg `0.074789`, median `0.092008`, mae `0.082501`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008481`, median `0.012813`, mae `0.016317`
- 5d: sample `20`, hit `0.65`, avg `0.00962`, median `0.010241`, mae `0.019149`
- 10d: sample `20`, hit `0.75`, avg `0.01323`, median `0.013997`, mae `0.022886`
- 20d: sample `20`, hit `0.85`, avg `0.042711`, median `0.043456`, mae `0.045706`
- 60d: sample `20`, hit `0.95`, avg `0.093442`, median `0.099719`, mae `0.098038`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000819`, median `0.006632`, mae `0.019063`
- 5d: sample `20`, hit `0.45`, avg `0.000564`, median `-0.009444`, mae `0.026405`
- 10d: sample `20`, hit `0.5`, avg `0.01076`, median `0.00326`, mae `0.025779`
- 20d: sample `20`, hit `0.95`, avg `0.045287`, median `0.027885`, mae `0.045608`
- 60d: sample `20`, hit `0.75`, avg `0.072833`, median `0.04207`, mae `0.07961`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000819`, median `0.006632`, mae `0.019063`
- 5d: sample `20`, hit `0.45`, avg `0.000564`, median `-0.009444`, mae `0.026405`
- 10d: sample `20`, hit `0.5`, avg `0.01076`, median `0.00326`, mae `0.025779`
- 20d: sample `20`, hit `0.95`, avg `0.045287`, median `0.027885`, mae `0.045608`
- 60d: sample `20`, hit `0.75`, avg `0.072833`, median `0.04207`, mae `0.07961`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008481`, median `0.012813`, mae `0.016317`
- 5d: sample `20`, hit `0.65`, avg `0.00962`, median `0.010241`, mae `0.019149`
- 10d: sample `20`, hit `0.75`, avg `0.01323`, median `0.013997`, mae `0.022886`
- 20d: sample `20`, hit `0.85`, avg `0.042711`, median `0.043456`, mae `0.045706`
- 60d: sample `20`, hit `0.95`, avg `0.093442`, median `0.099719`, mae `0.098038`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.002277`, median `-0.002755`, mae `0.017356`
- 5d: sample `40`, hit `0.45`, avg `-0.003998`, median `-0.013237`, mae `0.02293`
- 10d: sample `40`, hit `0.5`, avg `-0.000668`, median `0.000197`, mae `0.024156`
- 20d: sample `40`, hit `0.775`, avg `0.027147`, median `0.025198`, mae `0.039364`
- 60d: sample `40`, hit `0.775`, avg `0.053645`, median `0.046407`, mae `0.067338`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.1`, avg `-0.015472`, median `-0.011068`, mae `0.020802`
- 5d: sample `20`, hit `0.15`, avg `-0.020944`, median `-0.022868`, mae `0.026608`
- 10d: sample `20`, hit `0.35`, avg `-0.013717`, median `-0.032571`, mae `0.044004`
- 20d: sample `20`, hit `0.5`, avg `0.020444`, median `0.039427`, mae `0.061154`
- 60d: sample `20`, hit `0.85`, avg `0.076745`, median `0.092689`, mae `0.085391`

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
- 3d: sample `80`, hit `0.4375`, avg `-0.002886`, median `-0.001797`, mae `0.017958`
- 5d: sample `80`, hit `0.425`, avg `-0.00483`, median `-0.010073`, mae `0.022904`
- 10d: sample `80`, hit `0.525`, avg `-0.000456`, median `0.001517`, mae `0.0288`
- 20d: sample `80`, hit `0.725`, avg `0.029362`, median `0.029348`, mae `0.046397`
- 60d: sample `80`, hit `0.8375`, avg `0.069369`, median `0.084301`, mae `0.079526`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.001309`, median `0.004815`, mae `0.017009`
- 5d: sample `60`, hit `0.5167`, avg `0.000541`, median `0.004557`, mae `0.02167`
- 10d: sample `60`, hit `0.5833`, avg `0.003964`, median `0.003815`, mae `0.023732`
- 20d: sample `60`, hit `0.8`, avg `0.032335`, median `0.029348`, mae `0.041478`
- 60d: sample `60`, hit `0.8333`, avg `0.066911`, median `0.084216`, mae `0.077571`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4375`, avg `-0.002886`, median `-0.001797`, mae `0.017958`
- 5d: sample `80`, hit `0.425`, avg `-0.00483`, median `-0.010073`, mae `0.022904`
- 10d: sample `80`, hit `0.525`, avg `-0.000456`, median `0.001517`, mae `0.0288`
- 20d: sample `80`, hit `0.725`, avg `0.029362`, median `0.029348`, mae `0.046397`
- 60d: sample `80`, hit `0.8375`, avg `0.069369`, median `0.084301`, mae `0.079526`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.001309`, median `0.004815`, mae `0.017009`
- 5d: sample `60`, hit `0.5167`, avg `0.000541`, median `0.004557`, mae `0.02167`
- 10d: sample `60`, hit `0.5833`, avg `0.003964`, median `0.003815`, mae `0.023732`
- 20d: sample `60`, hit `0.8`, avg `0.032335`, median `0.029348`, mae `0.041478`
- 60d: sample `60`, hit `0.8333`, avg `0.066911`, median `0.084216`, mae `0.077571`

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
