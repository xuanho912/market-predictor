# High Confidence Edge Report

Generated at: `2026-09-26T00:21:34.003384+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `52`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `52`, gate `moderate_evidence`
- 5d: completed `52`, gate `moderate_evidence`
- 10d: completed `52`, gate `moderate_evidence`
- 20d: completed `52`, gate `moderate_evidence`
- 60d: completed `52`, gate `moderate_evidence`

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
- 3d: sample `40`, hit `0.575`, avg `0.002031`, median `0.006632`, mae `0.017503`
- 5d: sample `40`, hit `0.55`, avg `0.004511`, median `0.005772`, mae `0.020265`
- 10d: sample `40`, hit `0.65`, avg `0.010534`, median `0.013648`, mae `0.023484`
- 20d: sample `40`, hit `0.8`, avg `0.032976`, median `0.031464`, mae `0.03684`
- 60d: sample `40`, hit `0.85`, avg `0.069993`, median `0.085781`, mae `0.083519`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.003099`, median `-0.002952`, mae `0.014128`
- 5d: sample `40`, hit `0.475`, avg `-0.000446`, median `-0.000184`, mae `0.015327`
- 10d: sample `40`, hit `0.6`, avg `0.002376`, median `0.006423`, mae `0.021807`
- 20d: sample `40`, hit `0.625`, avg `0.009479`, median `0.026005`, mae `0.039921`
- 60d: sample `40`, hit `0.925`, avg `0.093103`, median `0.10344`, mae `0.096686`

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
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.005815`, median `0.012272`, mae `0.014511`
- 5d: sample `8`, hit `0.625`, avg `0.006695`, median `0.009709`, mae `0.016592`
- 10d: sample `8`, hit `0.75`, avg `0.009347`, median `0.013069`, mae `0.017068`
- 20d: sample `8`, hit `0.625`, avg `0.026788`, median `0.043456`, mae `0.034274`
- 60d: sample `8`, hit `1.0`, avg `0.114868`, median `0.119272`, mae `0.114868`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002031, 'median_return': 0.006632, 'mean_absolute_return': 0.017503, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.004511, 'median_return': 0.005772, 'mean_absolute_return': 0.020265, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.010534, 'median_return': 0.013648, 'mean_absolute_return': 0.023484, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.032976, 'median_return': 0.031464, 'mean_absolute_return': 0.03684, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.069993, 'median_return': 0.085781, 'mean_absolute_return': 0.083519, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005815, 'median_return': 0.012272, 'mean_absolute_return': 0.014511, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.023651}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006695, 'median_return': 0.009709, 'mean_absolute_return': 0.016592, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.027457}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.009347, 'median_return': 0.013069, 'mean_absolute_return': 0.017068, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026788, 'median_return': 0.043456, 'mean_absolute_return': 0.034274, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.114868, 'median_return': 0.119272, 'mean_absolute_return': 0.114868, 'max_adverse_excursion': 0.099512, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.00124, 'median_return': -0.001058, 'mean_absolute_return': 0.015961, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.001514, 'median_return': 0.00288, 'mean_absolute_return': 0.01793, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.006134, 'median_return': 0.007751, 'mean_absolute_return': 0.023266, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.02061, 'median_return': 0.027885, 'mean_absolute_return': 0.038837, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.875, 'avg_return': 0.077846, 'median_return': 0.087104, 'mean_absolute_return': 0.08735, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.1, 'both_hit': 14, 'both_miss': 6}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.075, 'both_hit': 14, 'both_miss': 6}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.125, 'both_hit': 15, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.275, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.8875, 'primary_minus_secondary': -0.575, 'both_hit': 18, 'both_miss': 2}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.00154, 'median_return': 0.003757, 'mean_absolute_return': 0.01567, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.003618, 'median_return': 0.005772, 'mean_absolute_return': 0.01791, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.054798}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.008792, 'median_return': 0.011031, 'mean_absolute_return': 0.019862, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.030101, 'median_return': 0.031464, 'mean_absolute_return': 0.035336, 'max_adverse_excursion': -0.026142, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.8833, 'avg_return': 0.073777, 'median_return': 0.084301, 'mean_absolute_return': 0.083488, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.006757, 'median_return': -0.009843, 'mean_absolute_return': 0.016252, 'max_adverse_excursion': -0.036265, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.002723, 'median_return': -0.002452, 'mean_absolute_return': 0.017453, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.000555, 'median_return': -0.001818, 'mean_absolute_return': 0.030998, 'max_adverse_excursion': -0.053986, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.005393, 'median_return': 0.017648, 'mean_absolute_return': 0.047513, 'max_adverse_excursion': -0.082211, 'max_favorable_excursion': 0.067793}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.104861, 'median_return': 0.114377, 'mean_absolute_return': 0.109944, 'max_adverse_excursion': -0.046434, 'max_favorable_excursion': 0.176653}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.5`, avg `-0.000534`, median `0.000239`, mae `0.015816`
- 5d: sample `80`, hit `0.5125`, avg `0.002032`, median `0.00374`, mae `0.017796`
- 10d: sample `80`, hit `0.625`, avg `0.006455`, median `0.008676`, mae `0.022646`
- 20d: sample `80`, hit `0.7125`, avg `0.021227`, median `0.027885`, mae `0.03838`
- 60d: sample `80`, hit `0.8875`, avg `0.081548`, median `0.098256`, mae `0.090102`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006509`, median `0.012272`, mae `0.014504`
- 5d: sample `20`, hit `0.7`, avg `0.009249`, median `0.013852`, mae `0.017973`
- 10d: sample `20`, hit `0.75`, avg `0.013199`, median `0.020334`, mae `0.022855`
- 20d: sample `20`, hit `0.8`, avg `0.033927`, median `0.034704`, mae `0.037726`
- 60d: sample `20`, hit `0.9`, avg `0.084068`, median `0.105939`, mae `0.092181`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.00154`, median `0.003757`, mae `0.01567`
- 5d: sample `60`, hit `0.55`, avg `0.003618`, median `0.005772`, mae `0.01791`
- 10d: sample `60`, hit `0.6833`, avg `0.008792`, median `0.011031`, mae `0.019862`
- 20d: sample `60`, hit `0.7833`, avg `0.030101`, median `0.031464`, mae `0.035336`
- 60d: sample `60`, hit `0.8833`, avg `0.073777`, median `0.084301`, mae `0.083488`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006509`, median `0.012272`, mae `0.014504`
- 5d: sample `20`, hit `0.7`, avg `0.009249`, median `0.013852`, mae `0.017973`
- 10d: sample `20`, hit `0.75`, avg `0.013199`, median `0.020334`, mae `0.022855`
- 20d: sample `20`, hit `0.8`, avg `0.033927`, median `0.034704`, mae `0.037726`
- 60d: sample `20`, hit `0.9`, avg `0.084068`, median `0.105939`, mae `0.092181`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002882`, median `-0.002952`, mae `0.016253`
- 5d: sample `60`, hit `0.45`, avg `-0.000373`, median `-0.001129`, mae `0.017737`
- 10d: sample `60`, hit `0.5833`, avg `0.004207`, median `0.004306`, mae `0.022576`
- 20d: sample `60`, hit `0.6833`, avg `0.016994`, median `0.026005`, mae `0.038598`
- 60d: sample `60`, hit `0.8833`, avg `0.080708`, median `0.092689`, mae `0.089409`

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
- 3d: sample `80`, hit `0.5`, avg `-0.000534`, median `0.000239`, mae `0.015816`
- 5d: sample `80`, hit `0.5125`, avg `0.002032`, median `0.00374`, mae `0.017796`
- 10d: sample `80`, hit `0.625`, avg `0.006455`, median `0.008676`, mae `0.022646`
- 20d: sample `80`, hit `0.7125`, avg `0.021227`, median `0.027885`, mae `0.03838`
- 60d: sample `80`, hit `0.8875`, avg `0.081548`, median `0.098256`, mae `0.090102`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006509`, median `0.012272`, mae `0.014504`
- 5d: sample `20`, hit `0.7`, avg `0.009249`, median `0.013852`, mae `0.017973`
- 10d: sample `20`, hit `0.75`, avg `0.013199`, median `0.020334`, mae `0.022855`
- 20d: sample `20`, hit `0.8`, avg `0.033927`, median `0.034704`, mae `0.037726`
- 60d: sample `20`, hit `0.9`, avg `0.084068`, median `0.105939`, mae `0.092181`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.000534`, median `0.000239`, mae `0.015816`
- 5d: sample `80`, hit `0.5125`, avg `0.002032`, median `0.00374`, mae `0.017796`
- 10d: sample `80`, hit `0.625`, avg `0.006455`, median `0.008676`, mae `0.022646`
- 20d: sample `80`, hit `0.7125`, avg `0.021227`, median `0.027885`, mae `0.03838`
- 60d: sample `80`, hit `0.8875`, avg `0.081548`, median `0.098256`, mae `0.090102`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006509`, median `0.012272`, mae `0.014504`
- 5d: sample `20`, hit `0.7`, avg `0.009249`, median `0.013852`, mae `0.017973`
- 10d: sample `20`, hit `0.75`, avg `0.013199`, median `0.020334`, mae `0.022855`
- 20d: sample `20`, hit `0.8`, avg `0.033927`, median `0.034704`, mae `0.037726`
- 60d: sample `20`, hit `0.9`, avg `0.084068`, median `0.105939`, mae `0.092181`

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
