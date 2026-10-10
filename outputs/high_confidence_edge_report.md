# High Confidence Edge Report

Generated at: `2026-10-10T00:24:42.398691+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `92`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `92`, gate `moderate_evidence`
- 5d: completed `92`, gate `moderate_evidence`
- 10d: completed `92`, gate `moderate_evidence`
- 20d: completed `92`, gate `moderate_evidence`
- 60d: completed `92`, gate `moderate_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.001786`, median `0.004542`, mae `0.015565`
- 5d: sample `60`, hit `0.5`, avg `0.001277`, median `0.002462`, mae `0.01825`
- 10d: sample `60`, hit `0.6`, avg `0.004346`, median `0.004196`, mae `0.018402`
- 20d: sample `60`, hit `0.8667`, avg `0.030662`, median `0.032102`, mae `0.033858`
- 60d: sample `60`, hit `0.85`, avg `0.069489`, median `0.084301`, mae `0.078116`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.005797`, median `-0.001058`, mae `0.017876`
- 5d: sample `20`, hit `0.35`, avg `-0.00614`, median `-0.005796`, mae `0.01976`
- 10d: sample `20`, hit `0.4`, avg `-0.009378`, median `-0.019497`, mae `0.033762`
- 20d: sample `20`, hit `0.45`, avg `-0.00305`, median `-0.009713`, mae `0.046704`
- 60d: sample `20`, hit `0.8`, avg `0.077065`, median `0.104804`, mae `0.097459`

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
- 3d: sample `8`, hit `0.5`, avg `0.000559`, median `0.012272`, mae `0.017638`
- 5d: sample `8`, hit `0.625`, avg `0.001369`, median `0.007948`, mae `0.014272`
- 10d: sample `8`, hit `0.5`, avg `0.000212`, median `0.011031`, mae `0.022848`
- 20d: sample `8`, hit `1.0`, avg `0.04772`, median `0.058396`, mae `0.04772`
- 60d: sample `8`, hit `0.875`, avg `0.078355`, median `0.099838`, mae `0.089845`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.000559`, median `0.012272`, mae `0.017638`
- 5d: sample `8`, hit `0.625`, avg `0.001369`, median `0.007948`, mae `0.014272`
- 10d: sample `8`, hit `0.5`, avg `0.000212`, median `0.011031`, mae `0.022848`
- 20d: sample `8`, hit `1.0`, avg `0.04772`, median `0.058396`, mae `0.04772`
- 60d: sample `8`, hit `0.875`, avg `0.078355`, median `0.099838`, mae `0.089845`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.001786, 'median_return': 0.004542, 'mean_absolute_return': 0.015565, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.001277, 'median_return': 0.002462, 'mean_absolute_return': 0.01825, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.004346, 'median_return': 0.004196, 'mean_absolute_return': 0.018402, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.030662, 'median_return': 0.032102, 'mean_absolute_return': 0.033858, 'max_adverse_excursion': -0.024707, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 60, 'hit_rate': 0.85, 'avg_return': 0.069489, 'median_return': 0.084301, 'mean_absolute_return': 0.078116, 'max_adverse_excursion': -0.064821, 'max_favorable_excursion': 0.188643}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000559, 'median_return': 0.012272, 'mean_absolute_return': 0.017638, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001369, 'median_return': 0.007948, 'mean_absolute_return': 0.014272, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000212, 'median_return': 0.011031, 'mean_absolute_return': 0.022848, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.04772, 'median_return': 0.058396, 'mean_absolute_return': 0.04772, 'max_adverse_excursion': 0.01983, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.078355, 'median_return': 0.099838, 'mean_absolute_return': 0.089845, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': -0.000184, 'median_return': 0.001405, 'mean_absolute_return': 0.015976, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.000793, 'median_return': -0.003796, 'mean_absolute_return': 0.019112, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.000994, 'median_return': 0.003921, 'mean_absolute_return': 0.022175, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.019403, 'median_return': 0.025198, 'mean_absolute_return': 0.035886, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.070608, 'median_return': 0.092008, 'mean_absolute_return': 0.082185, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.188643}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6125}, '10d': {'sample_size': 80, 'hit_rate': 0.675}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.125, 'both_hit': 15, 'both_miss': 5}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.15, 'both_hit': 13, 'both_miss': 7}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.225, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 17, 'both_miss': 3}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.025, 'both_hit': 18, 'both_miss': 2}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.001786, 'median_return': 0.004542, 'mean_absolute_return': 0.015565, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.001277, 'median_return': 0.002462, 'mean_absolute_return': 0.01825, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.004346, 'median_return': 0.004196, 'mean_absolute_return': 0.018402, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.030662, 'median_return': 0.032102, 'mean_absolute_return': 0.033858, 'max_adverse_excursion': -0.024707, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 60, 'hit_rate': 0.85, 'avg_return': 0.069489, 'median_return': 0.084301, 'mean_absolute_return': 0.078116, 'max_adverse_excursion': -0.064821, 'max_favorable_excursion': 0.188643}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.005797, 'median_return': -0.001058, 'mean_absolute_return': 0.017876, 'max_adverse_excursion': -0.036767, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.00614, 'median_return': -0.005796, 'mean_absolute_return': 0.01976, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.009378, 'median_return': -0.019497, 'mean_absolute_return': 0.033762, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.00305, 'median_return': -0.009713, 'mean_absolute_return': 0.046704, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.085181}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.077065, 'median_return': 0.104804, 'mean_absolute_return': 0.097459, 'max_adverse_excursion': -0.099444, 'max_favorable_excursion': 0.135527}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009137`, median `0.014926`, mae `0.016973`
- 5d: sample `20`, hit `0.65`, avg `0.009363`, median `0.010241`, mae `0.018892`
- 10d: sample `20`, hit `0.75`, avg `0.01332`, median `0.015799`, mae `0.022976`
- 20d: sample `20`, hit `0.85`, avg `0.042723`, median `0.043456`, mae `0.045718`
- 60d: sample `20`, hit `0.9`, avg `0.087459`, median `0.099719`, mae `0.095571`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005014`, median `-0.003676`, mae `0.018375`
- 5d: sample `40`, hit `0.35`, avg `-0.006107`, median `-0.011157`, mae `0.020853`
- 10d: sample `40`, hit `0.375`, avg `-0.00586`, median `-0.009694`, mae `0.025944`
- 20d: sample `40`, hit `0.675`, avg `0.008399`, median `0.015661`, mae `0.033895`
- 60d: sample `40`, hit `0.75`, avg `0.057918`, median `0.076106`, mae `0.075958`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009137`, median `0.014926`, mae `0.016973`
- 5d: sample `20`, hit `0.65`, avg `0.009363`, median `0.010241`, mae `0.018892`
- 10d: sample `20`, hit `0.75`, avg `0.01332`, median `0.015799`, mae `0.022976`
- 20d: sample `20`, hit `0.85`, avg `0.042723`, median `0.043456`, mae `0.045718`
- 60d: sample `20`, hit `0.9`, avg `0.087459`, median `0.099719`, mae `0.095571`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009137`, median `0.014926`, mae `0.016973`
- 5d: sample `20`, hit `0.65`, avg `0.009363`, median `0.010241`, mae `0.018892`
- 10d: sample `20`, hit `0.75`, avg `0.01332`, median `0.015799`, mae `0.022976`
- 20d: sample `20`, hit `0.85`, avg `0.042723`, median `0.043456`, mae `0.045718`
- 60d: sample `20`, hit `0.9`, avg `0.087459`, median `0.099719`, mae `0.095571`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000453`, median `0.001405`, mae `0.010848`
- 5d: sample `20`, hit `0.5`, avg `0.000542`, median `0.002462`, mae `0.013913`
- 10d: sample `20`, hit `0.7`, avg `0.002063`, median `0.006423`, mae `0.014103`
- 20d: sample `20`, hit `0.85`, avg `0.029415`, median `0.033704`, mae `0.034769`
- 60d: sample `20`, hit `0.95`, avg `0.082236`, median `0.084597`, mae `0.084318`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.005014`, median `-0.003676`, mae `0.018375`
- 5d: sample `40`, hit `0.35`, avg `-0.006107`, median `-0.011157`, mae `0.020853`
- 10d: sample `40`, hit `0.375`, avg `-0.00586`, median `-0.009694`, mae `0.025944`
- 20d: sample `40`, hit `0.675`, avg `0.008399`, median `0.015661`, mae `0.033895`
- 60d: sample `40`, hit `0.75`, avg `0.057918`, median `0.076106`, mae `0.075958`

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
- 3d: sample `80`, hit `0.525`, avg `-0.000109`, median `0.001405`, mae `0.016143`
- 5d: sample `80`, hit `0.4625`, avg `-0.000577`, median `-0.003262`, mae `0.018628`
- 10d: sample `80`, hit `0.55`, avg `0.000915`, median `0.003921`, mae `0.022242`
- 20d: sample `80`, hit `0.7625`, avg `0.022234`, median `0.027885`, mae `0.037069`
- 60d: sample `80`, hit `0.8375`, avg `0.071383`, median `0.092008`, mae `0.082951`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004795`, median `0.010897`, mae `0.01391`
- 5d: sample `40`, hit `0.575`, avg `0.004953`, median `0.007948`, mae `0.016402`
- 10d: sample `40`, hit `0.725`, avg `0.007691`, median `0.008676`, mae `0.018539`
- 20d: sample `40`, hit `0.85`, avg `0.036069`, median `0.03801`, mae `0.040243`
- 60d: sample `40`, hit `0.925`, avg `0.084848`, median `0.097048`, mae `0.089945`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.003192`, median `-0.001227`, mae `0.015866`
- 5d: sample `60`, hit `0.4`, avg `-0.00389`, median `-0.006464`, mae `0.018539`
- 10d: sample `60`, hit `0.4833`, avg `-0.003219`, median `-0.000648`, mae `0.021997`
- 20d: sample `60`, hit `0.7333`, avg `0.015404`, median `0.024601`, mae `0.034186`
- 60d: sample `60`, hit `0.8167`, avg `0.066024`, median `0.081673`, mae `0.078745`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000453`, median `0.001405`, mae `0.010848`
- 5d: sample `20`, hit `0.5`, avg `0.000542`, median `0.002462`, mae `0.013913`
- 10d: sample `20`, hit `0.7`, avg `0.002063`, median `0.006423`, mae `0.014103`
- 20d: sample `20`, hit `0.85`, avg `0.029415`, median `0.033704`, mae `0.034769`
- 60d: sample `20`, hit `0.95`, avg `0.082236`, median `0.084597`, mae `0.084318`

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
