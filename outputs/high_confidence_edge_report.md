# High Confidence Edge Report

Generated at: `2026-10-22T00:27:10.498263+00:00`

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
- 3d: sample `40`, hit `0.75`, avg `0.009866`, median `0.014926`, mae `0.016367`
- 5d: sample `40`, hit `0.725`, avg `0.011206`, median `0.012953`, mae `0.021401`
- 10d: sample `40`, hit `0.625`, avg `0.010313`, median `0.020119`, mae `0.031053`
- 20d: sample `40`, hit `0.75`, avg `0.021968`, median `0.03107`, mae `0.043525`
- 60d: sample `40`, hit `0.85`, avg `0.064851`, median `0.077143`, mae `0.072981`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001116`, median `0.008574`, mae `0.019475`
- 5d: sample `40`, hit `0.575`, avg `-0.002634`, median `0.007168`, mae `0.024524`
- 10d: sample `40`, hit `0.525`, avg `-0.003938`, median `0.001785`, mae `0.036822`
- 20d: sample `40`, hit `0.625`, avg `0.006276`, median `0.007366`, mae `0.035376`
- 60d: sample `40`, hit `0.725`, avg `0.056178`, median `0.064286`, mae `0.082474`

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
- 3d: sample `8`, hit `0.75`, avg `0.015298`, median `0.022579`, mae `0.019212`
- 5d: sample `8`, hit `0.875`, avg `0.020091`, median `0.030736`, mae `0.025364`
- 10d: sample `8`, hit `0.75`, avg `0.021892`, median `0.037104`, mae `0.036363`
- 20d: sample `8`, hit `0.875`, avg `0.047512`, median `0.062955`, mae `0.055191`
- 60d: sample `8`, hit `0.875`, avg `0.079695`, median `0.095628`, mae `0.082233`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.015298`, median `0.022579`, mae `0.019212`
- 5d: sample `8`, hit `0.875`, avg `0.020091`, median `0.030736`, mae `0.025364`
- 10d: sample `8`, hit `0.75`, avg `0.021892`, median `0.037104`, mae `0.036363`
- 20d: sample `8`, hit `0.875`, avg `0.047512`, median `0.062955`, mae `0.055191`
- 60d: sample `8`, hit `0.875`, avg `0.079695`, median `0.095628`, mae `0.082233`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.009866, 'median_return': 0.014926, 'mean_absolute_return': 0.016367, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.011206, 'median_return': 0.012953, 'mean_absolute_return': 0.021401, 'max_adverse_excursion': -0.029469, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.010313, 'median_return': 0.020119, 'mean_absolute_return': 0.031053, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.021968, 'median_return': 0.03107, 'mean_absolute_return': 0.043525, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.064851, 'median_return': 0.077143, 'mean_absolute_return': 0.072981, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.015298, 'median_return': 0.022579, 'mean_absolute_return': 0.019212, 'max_adverse_excursion': -0.013999, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.020091, 'median_return': 0.030736, 'mean_absolute_return': 0.025364, 'max_adverse_excursion': -0.021092, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.021892, 'median_return': 0.037104, 'mean_absolute_return': 0.036363, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.047512, 'median_return': 0.062955, 'mean_absolute_return': 0.055191, 'max_adverse_excursion': -0.030715, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.079695, 'median_return': 0.095628, 'mean_absolute_return': 0.082233, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.004401, 'median_return': 0.009349, 'mean_absolute_return': 0.017778, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.00253, 'median_return': 0.009561, 'mean_absolute_return': 0.022695, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001109, 'median_return': 0.009015, 'mean_absolute_return': 0.033668, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.010412, 'median_return': 0.020326, 'mean_absolute_return': 0.037702, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.058383, 'median_return': 0.065766, 'mean_absolute_return': 0.077227, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.55}, '20d': {'sample_size': 80, 'hit_rate': 0.5625}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.1, 'both_hit': 30, 'both_miss': 10}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.075, 'both_hit': 29, 'both_miss': 11}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.025, 'both_hit': 25, 'both_miss': 15}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.125, 'both_hit': 30, 'both_miss': 10}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.225, 'both_hit': 34, 'both_miss': 6}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.009499, 'median_return': 0.014926, 'mean_absolute_return': 0.019053, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.009265, 'median_return': 0.013852, 'mean_absolute_return': 0.022756, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.012475, 'median_return': 0.011071, 'mean_absolute_return': 0.027293, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.061936}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.02603, 'median_return': 0.025179, 'mean_absolute_return': 0.037063, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.070734, 'median_return': 0.083723, 'mean_absolute_return': 0.082579, 'max_adverse_excursion': -0.061391, 'max_favorable_excursion': 0.188184}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.001483, 'median_return': 0.005136, 'mean_absolute_return': 0.016789, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.000693, 'median_return': 0.007168, 'mean_absolute_return': 0.023169, 'max_adverse_excursion': -0.04784, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.0061, 'median_return': 0.004542, 'mean_absolute_return': 0.040582, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.067422}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002215, 'median_return': 0.019193, 'mean_absolute_return': 0.041838, 'max_adverse_excursion': -0.103293, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.050295, 'median_return': 0.058598, 'mean_absolute_return': 0.072876, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.164619}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.009866`, median `0.014926`, mae `0.016367`
- 5d: sample `40`, hit `0.725`, avg `0.011206`, median `0.012953`, mae `0.021401`
- 10d: sample `40`, hit `0.625`, avg `0.010313`, median `0.020119`, mae `0.031053`
- 20d: sample `40`, hit `0.75`, avg `0.021968`, median `0.03107`, mae `0.043525`
- 60d: sample `40`, hit `0.85`, avg `0.064851`, median `0.077143`, mae `0.072981`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001116`, median `0.008574`, mae `0.019475`
- 5d: sample `40`, hit `0.575`, avg `-0.002634`, median `0.007168`, mae `0.024524`
- 10d: sample `40`, hit `0.525`, avg `-0.003938`, median `0.001785`, mae `0.036822`
- 20d: sample `40`, hit `0.625`, avg `0.006276`, median `0.007366`, mae `0.035376`
- 60d: sample `40`, hit `0.725`, avg `0.056178`, median `0.064286`, mae `0.082474`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.009866`, median `0.014926`, mae `0.016367`
- 5d: sample `40`, hit `0.725`, avg `0.011206`, median `0.012953`, mae `0.021401`
- 10d: sample `40`, hit `0.625`, avg `0.010313`, median `0.020119`, mae `0.031053`
- 20d: sample `40`, hit `0.75`, avg `0.021968`, median `0.03107`, mae `0.043525`
- 60d: sample `40`, hit `0.85`, avg `0.064851`, median `0.077143`, mae `0.072981`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.014633`, median `0.0207`, mae `0.020515`
- 5d: sample `20`, hit `0.8`, avg `0.016494`, median `0.017411`, mae `0.023954`
- 10d: sample `20`, hit `0.7`, avg `0.018513`, median `0.032575`, mae `0.033469`
- 20d: sample `20`, hit `0.85`, avg `0.04085`, median `0.058396`, mae `0.051606`
- 60d: sample `20`, hit `0.85`, avg `0.07801`, median `0.095628`, mae `0.087138`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.004365`, median `0.009859`, mae `0.017592`
- 5d: sample `20`, hit `0.75`, avg `0.002036`, median `0.01152`, mae `0.021557`
- 10d: sample `20`, hit `0.55`, avg `0.006438`, median `0.008188`, mae `0.021118`
- 20d: sample `20`, hit `0.7`, avg `0.011209`, median `0.007366`, mae `0.022521`
- 60d: sample `20`, hit `0.7`, avg `0.063459`, median `0.06911`, mae `0.078021`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.009866`, median `0.014926`, mae `0.016367`
- 5d: sample `40`, hit `0.725`, avg `0.011206`, median `0.012953`, mae `0.021401`
- 10d: sample `40`, hit `0.625`, avg `0.010313`, median `0.020119`, mae `0.031053`
- 20d: sample `40`, hit `0.75`, avg `0.021968`, median `0.03107`, mae `0.043525`
- 60d: sample `40`, hit `0.85`, avg `0.064851`, median `0.077143`, mae `0.072981`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.014633`, median `0.0207`, mae `0.020515`
- 5d: sample `20`, hit `0.8`, avg `0.016494`, median `0.017411`, mae `0.023954`
- 10d: sample `20`, hit `0.7`, avg `0.018513`, median `0.032575`, mae `0.033469`
- 20d: sample `20`, hit `0.85`, avg `0.04085`, median `0.058396`, mae `0.051606`
- 60d: sample `20`, hit `0.85`, avg `0.07801`, median `0.095628`, mae `0.087138`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001116`, median `0.008574`, mae `0.019475`
- 5d: sample `40`, hit `0.575`, avg `-0.002634`, median `0.007168`, mae `0.024524`
- 10d: sample `40`, hit `0.525`, avg `-0.003938`, median `0.001785`, mae `0.036822`
- 20d: sample `40`, hit `0.625`, avg `0.006276`, median `0.007366`, mae `0.035376`
- 60d: sample `40`, hit `0.725`, avg `0.056178`, median `0.064286`, mae `0.082474`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005098`, median `0.007259`, mae `0.012219`
- 5d: sample `20`, hit `0.65`, avg `0.005918`, median `0.011604`, mae `0.018847`
- 10d: sample `20`, hit `0.55`, avg `0.002113`, median `0.012215`, mae `0.028638`
- 20d: sample `20`, hit `0.65`, avg `0.003087`, median `0.025541`, mae `0.035445`
- 60d: sample `20`, hit `0.85`, avg `0.051692`, median `0.048421`, mae `0.058825`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.675`, avg `0.005491`, median `0.010773`, mae `0.017921`
- 5d: sample `80`, hit `0.65`, avg `0.004286`, median `0.010061`, mae `0.022962`
- 10d: sample `80`, hit `0.575`, avg `0.003188`, median `0.011031`, mae `0.033938`
- 20d: sample `80`, hit `0.6875`, avg `0.014122`, median `0.023565`, mae `0.039451`
- 60d: sample `80`, hit `0.7875`, avg `0.060515`, median `0.069082`, mae `0.077728`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.009866`, median `0.014926`, mae `0.016367`
- 5d: sample `40`, hit `0.725`, avg `0.011206`, median `0.012953`, mae `0.021401`
- 10d: sample `40`, hit `0.625`, avg `0.010313`, median `0.020119`, mae `0.031053`
- 20d: sample `40`, hit `0.75`, avg `0.021968`, median `0.03107`, mae `0.043525`
- 60d: sample `40`, hit `0.85`, avg `0.064851`, median `0.077143`, mae `0.072981`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005098`, median `0.007259`, mae `0.012219`
- 5d: sample `20`, hit `0.65`, avg `0.005918`, median `0.011604`, mae `0.018847`
- 10d: sample `20`, hit `0.55`, avg `0.002113`, median `0.012215`, mae `0.028638`
- 20d: sample `20`, hit `0.65`, avg `0.003087`, median `0.025541`, mae `0.035445`
- 60d: sample `20`, hit `0.85`, avg `0.051692`, median `0.048421`, mae `0.058825`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.675`, avg `0.005491`, median `0.010773`, mae `0.017921`
- 5d: sample `80`, hit `0.65`, avg `0.004286`, median `0.010061`, mae `0.022962`
- 10d: sample `80`, hit `0.575`, avg `0.003188`, median `0.011031`, mae `0.033938`
- 20d: sample `80`, hit `0.6875`, avg `0.014122`, median `0.023565`, mae `0.039451`
- 60d: sample `80`, hit `0.7875`, avg `0.060515`, median `0.069082`, mae `0.077728`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.005098`, median `0.007259`, mae `0.012219`
- 5d: sample `20`, hit `0.65`, avg `0.005918`, median `0.011604`, mae `0.018847`
- 10d: sample `20`, hit `0.55`, avg `0.002113`, median `0.012215`, mae `0.028638`
- 20d: sample `20`, hit `0.65`, avg `0.003087`, median `0.025541`, mae `0.035445`
- 60d: sample `20`, hit `0.85`, avg `0.051692`, median `0.048421`, mae `0.058825`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.009866`, median `0.014926`, mae `0.016367`
- 5d: sample `40`, hit `0.725`, avg `0.011206`, median `0.012953`, mae `0.021401`
- 10d: sample `40`, hit `0.625`, avg `0.010313`, median `0.020119`, mae `0.031053`
- 20d: sample `40`, hit `0.75`, avg `0.021968`, median `0.03107`, mae `0.043525`
- 60d: sample `40`, hit `0.85`, avg `0.064851`, median `0.077143`, mae `0.072981`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001116`, median `0.008574`, mae `0.019475`
- 5d: sample `40`, hit `0.575`, avg `-0.002634`, median `0.007168`, mae `0.024524`
- 10d: sample `40`, hit `0.525`, avg `-0.003938`, median `0.001785`, mae `0.036822`
- 20d: sample `40`, hit `0.625`, avg `0.006276`, median `0.007366`, mae `0.035376`
- 60d: sample `40`, hit `0.725`, avg `0.056178`, median `0.064286`, mae `0.082474`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
