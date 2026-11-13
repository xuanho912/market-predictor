# High Confidence Edge Report

Generated at: `2026-11-13T03:24:03.360728+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `188`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `historical_proxy_supports_higher_confidence_but_forward_validation_required`

## Forward Sample Gates

- 3d: completed `188`, gate `stronger_evidence`
- 5d: completed `188`, gate `stronger_evidence`
- 10d: completed `188`, gate `stronger_evidence`
- 20d: completed `188`, gate `stronger_evidence`
- 60d: completed `188`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002816`, median `0.003538`, mae `0.019338`
- 5d: sample `20`, hit `0.55`, avg `0.005814`, median `0.008121`, mae `0.02116`
- 10d: sample `20`, hit `0.55`, avg `0.008511`, median `0.005616`, mae `0.030944`
- 20d: sample `20`, hit `0.75`, avg `0.008345`, median `0.013823`, mae `0.038229`
- 60d: sample `20`, hit `0.45`, avg `-0.004`, median `-0.018976`, mae `0.079613`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.003471`, median `-0.006734`, mae `0.014196`
- 5d: sample `40`, hit `0.525`, avg `-0.001687`, median `0.000762`, mae `0.014867`
- 10d: sample `40`, hit `0.375`, avg `-0.001212`, median `-0.006017`, mae `0.016835`
- 20d: sample `40`, hit `0.55`, avg `0.007418`, median `0.012291`, mae `0.029843`
- 60d: sample `40`, hit `0.3`, avg `-0.013752`, median `-0.02013`, mae `0.051601`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003671`, median `0.01312`, mae `0.024957`
- 5d: sample `8`, hit `0.375`, avg `-0.007346`, median `-0.007378`, mae `0.021954`
- 10d: sample `8`, hit `0.25`, avg `-0.011852`, median `-0.011194`, mae `0.025995`
- 20d: sample `8`, hit `0.75`, avg `-0.000917`, median `0.013823`, mae `0.030682`
- 60d: sample `8`, hit `0.25`, avg `-0.011402`, median `-0.029513`, mae `0.036401`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.003671`, median `0.01312`, mae `0.024957`
- 5d: sample `8`, hit `0.375`, avg `-0.007346`, median `-0.007378`, mae `0.021954`
- 10d: sample `8`, hit `0.25`, avg `-0.011852`, median `-0.011194`, mae `0.025995`
- 20d: sample `8`, hit `0.75`, avg `-0.000917`, median `0.013823`, mae `0.030682`
- 60d: sample `8`, hit `0.25`, avg `-0.011402`, median `-0.029513`, mae `0.036401`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002816, 'median_return': 0.003538, 'mean_absolute_return': 0.019338, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.005814, 'median_return': 0.008121, 'mean_absolute_return': 0.02116, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.008511, 'median_return': 0.005616, 'mean_absolute_return': 0.030944, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008345, 'median_return': 0.013823, 'mean_absolute_return': 0.038229, 'max_adverse_excursion': -0.120224, 'max_favorable_excursion': 0.101125}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.004, 'median_return': -0.018976, 'mean_absolute_return': 0.079613, 'max_adverse_excursion': -0.294669, 'max_favorable_excursion': 0.186083}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.003471, 'median_return': -0.006734, 'mean_absolute_return': 0.014196, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.038451}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001687, 'median_return': 0.000762, 'mean_absolute_return': 0.014867, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.001212, 'median_return': -0.006017, 'mean_absolute_return': 0.016835, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.007418, 'median_return': 0.012291, 'mean_absolute_return': 0.029843, 'max_adverse_excursion': -0.051042, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.3, 'avg_return': -0.013752, 'median_return': -0.02013, 'mean_absolute_return': 0.051601, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003671, 'median_return': 0.01312, 'mean_absolute_return': 0.024957, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.029672}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007346, 'median_return': -0.007378, 'mean_absolute_return': 0.021954, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.035985}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.011852, 'median_return': -0.011194, 'mean_absolute_return': 0.025995, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.050956}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': -0.000917, 'median_return': 0.013823, 'mean_absolute_return': 0.030682, 'max_adverse_excursion': -0.085064, 'max_favorable_excursion': 0.050144}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.011402, 'median_return': -0.029513, 'mean_absolute_return': 0.036401, 'max_adverse_excursion': -0.041166, 'max_favorable_excursion': 0.055266}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.002003, 'median_return': 0.001558, 'mean_absolute_return': 0.016085, 'max_adverse_excursion': -0.04969, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.005014, 'median_return': 0.004408, 'mean_absolute_return': 0.017556, 'max_adverse_excursion': -0.04207, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.005015, 'median_return': 0.000197, 'mean_absolute_return': 0.026654, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.015403, 'median_return': 0.015661, 'mean_absolute_return': 0.036628, 'max_adverse_excursion': -0.120224, 'max_favorable_excursion': 0.152433}, '60d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.000723, 'median_return': -0.005523, 'mean_absolute_return': 0.072436, 'max_adverse_excursion': -0.316659, 'max_favorable_excursion': 0.258847}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3875}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.425}, '20d': {'sample_size': 80, 'hit_rate': 0.525}, '60d': {'sample_size': 80, 'hit_rate': 0.35}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.009868, 'median_return': 0.012584, 'mean_absolute_return': 0.020157, 'max_adverse_excursion': -0.04969, 'max_favorable_excursion': 0.036856}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.012674, 'median_return': 0.012634, 'mean_absolute_return': 0.021089, 'max_adverse_excursion': -0.04207, 'max_favorable_excursion': 0.049091}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.007226, 'median_return': 0.018412, 'mean_absolute_return': 0.041737, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.031904, 'median_return': 0.036446, 'mean_absolute_return': 0.046219, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.152433}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.024342, 'median_return': 0.045321, 'mean_absolute_return': 0.092516, 'max_adverse_excursion': -0.316659, 'max_favorable_excursion': 0.258847}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': -0.001375, 'median_return': -0.002654, 'mean_absolute_return': 0.01591, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.000813, 'median_return': 0.000762, 'mean_absolute_return': 0.016964, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 60, 'hit_rate': 0.4333, 'avg_return': 0.002029, 'median_return': -0.005891, 'mean_absolute_return': 0.021538, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.007727, 'median_return': 0.012291, 'mean_absolute_return': 0.032639, 'max_adverse_excursion': -0.120224, 'max_favorable_excursion': 0.101125}, '60d': {'sample_size': 60, 'hit_rate': 0.35, 'avg_return': -0.010501, 'median_return': -0.02013, 'mean_absolute_return': 0.060938, 'max_adverse_excursion': -0.294669, 'max_favorable_excursion': 0.186083}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001375`, median `-0.002654`, mae `0.01591`
- 5d: sample `60`, hit `0.5333`, avg `0.000813`, median `0.000762`, mae `0.016964`
- 10d: sample `60`, hit `0.4333`, avg `0.002029`, median `-0.005891`, mae `0.021538`
- 20d: sample `60`, hit `0.6167`, avg `0.007727`, median `0.012291`, mae `0.032639`
- 60d: sample `60`, hit `0.35`, avg `-0.010501`, median `-0.02013`, mae `0.060938`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001375`, median `-0.002654`, mae `0.01591`
- 5d: sample `60`, hit `0.5333`, avg `0.000813`, median `0.000762`, mae `0.016964`
- 10d: sample `60`, hit `0.4333`, avg `0.002029`, median `-0.005891`, mae `0.021538`
- 20d: sample `60`, hit `0.6167`, avg `0.007727`, median `0.012291`, mae `0.032639`
- 60d: sample `60`, hit `0.35`, avg `-0.010501`, median `-0.02013`, mae `0.060938`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001375`, median `-0.002654`, mae `0.01591`
- 5d: sample `60`, hit `0.5333`, avg `0.000813`, median `0.000762`, mae `0.016964`
- 10d: sample `60`, hit `0.4333`, avg `0.002029`, median `-0.005891`, mae `0.021538`
- 20d: sample `60`, hit `0.6167`, avg `0.007727`, median `0.012291`, mae `0.032639`
- 60d: sample `60`, hit `0.35`, avg `-0.010501`, median `-0.02013`, mae `0.060938`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.003471`, median `-0.006734`, mae `0.014196`
- 5d: sample `40`, hit `0.525`, avg `-0.001687`, median `0.000762`, mae `0.014867`
- 10d: sample `40`, hit `0.375`, avg `-0.001212`, median `-0.006017`, mae `0.016835`
- 20d: sample `40`, hit `0.55`, avg `0.007418`, median `0.012291`, mae `0.029843`
- 60d: sample `40`, hit `0.3`, avg `-0.013752`, median `-0.02013`, mae `0.051601`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002816`, median `0.003538`, mae `0.019338`
- 5d: sample `20`, hit `0.55`, avg `0.005814`, median `0.008121`, mae `0.02116`
- 10d: sample `20`, hit `0.55`, avg `0.008511`, median `0.005616`, mae `0.030944`
- 20d: sample `20`, hit `0.75`, avg `0.008345`, median `0.013823`, mae `0.038229`
- 60d: sample `20`, hit `0.45`, avg `-0.004`, median `-0.018976`, mae `0.079613`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.003471`, median `-0.006734`, mae `0.014196`
- 5d: sample `40`, hit `0.525`, avg `-0.001687`, median `0.000762`, mae `0.014867`
- 10d: sample `40`, hit `0.375`, avg `-0.001212`, median `-0.006017`, mae `0.016835`
- 20d: sample `40`, hit `0.55`, avg `0.007418`, median `0.012291`, mae `0.029843`
- 60d: sample `40`, hit `0.3`, avg `-0.013752`, median `-0.02013`, mae `0.051601`

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
- 3d: sample `80`, hit `0.5125`, avg `0.001435`, median `0.001558`, mae `0.016972`
- 5d: sample `80`, hit `0.6`, avg `0.003778`, median `0.003714`, mae `0.017996`
- 10d: sample `80`, hit `0.475`, avg `0.003328`, median `-0.003071`, mae `0.026588`
- 20d: sample `80`, hit `0.65`, avg `0.013771`, median `0.014567`, mae `0.036034`
- 60d: sample `80`, hit `0.425`, avg `-0.001791`, median `-0.007569`, mae `0.068833`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `0.001435`, median `0.001558`, mae `0.016972`
- 5d: sample `80`, hit `0.6`, avg `0.003778`, median `0.003714`, mae `0.017996`
- 10d: sample `80`, hit `0.475`, avg `0.003328`, median `-0.003071`, mae `0.026588`
- 20d: sample `80`, hit `0.65`, avg `0.013771`, median `0.014567`, mae `0.036034`
- 60d: sample `80`, hit `0.425`, avg `-0.001791`, median `-0.007569`, mae `0.068833`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001375`, median `-0.002654`, mae `0.01591`
- 5d: sample `60`, hit `0.5333`, avg `0.000813`, median `0.000762`, mae `0.016964`
- 10d: sample `60`, hit `0.4333`, avg `0.002029`, median `-0.005891`, mae `0.021538`
- 20d: sample `60`, hit `0.6167`, avg `0.007727`, median `0.012291`, mae `0.032639`
- 60d: sample `60`, hit `0.35`, avg `-0.010501`, median `-0.02013`, mae `0.060938`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.001375`, median `-0.002654`, mae `0.01591`
- 5d: sample `60`, hit `0.5333`, avg `0.000813`, median `0.000762`, mae `0.016964`
- 10d: sample `60`, hit `0.4333`, avg `0.002029`, median `-0.005891`, mae `0.021538`
- 20d: sample `60`, hit `0.6167`, avg `0.007727`, median `0.012291`, mae `0.032639`
- 60d: sample `60`, hit `0.35`, avg `-0.010501`, median `-0.02013`, mae `0.060938`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
