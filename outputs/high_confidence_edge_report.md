# High Confidence Edge Report

Generated at: `2026-11-13T02:17:54.059358+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.010088`, median `0.012502`, mae `0.019388`
- 5d: sample `60`, hit `0.7`, avg `0.013178`, median `0.017467`, mae `0.025586`
- 10d: sample `60`, hit `0.7167`, avg `0.019125`, median `0.02569`, mae `0.039508`
- 20d: sample `60`, hit `0.8667`, avg `0.039677`, median `0.039296`, mae `0.054198`
- 60d: sample `60`, hit `0.95`, avg `0.091923`, median `0.096597`, mae `0.094707`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.015645`, median `0.018644`, mae `0.022959`
- 5d: sample `20`, hit `0.85`, avg `0.022195`, median `0.024027`, mae `0.03212`
- 10d: sample `20`, hit `0.7`, avg `0.024965`, median `0.030744`, mae `0.05688`
- 20d: sample `20`, hit `0.9`, avg `0.050125`, median `0.03791`, mae `0.067935`
- 60d: sample `20`, hit `0.85`, avg `0.118317`, median `0.109805`, mae `0.121702`

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
- 3d: sample `8`, hit `0.625`, avg `0.011259`, median `0.022579`, mae `0.022463`
- 5d: sample `8`, hit `0.75`, avg `0.015354`, median `0.026456`, mae `0.027491`
- 10d: sample `8`, hit `0.625`, avg `0.022958`, median `0.032575`, mae `0.032184`
- 20d: sample `8`, hit `1.0`, avg `0.056495`, median `0.062955`, mae `0.056495`
- 60d: sample `8`, hit `1.0`, avg `0.110147`, median `0.121826`, mae `0.110147`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `1.0`, avg `0.013512`, median `0.011414`, mae `0.013512`
- 5d: sample `8`, hit `1.0`, avg `0.021434`, median `0.025304`, mae `0.021434`
- 10d: sample `8`, hit `1.0`, avg `0.027829`, median `0.027042`, mae `0.027829`
- 20d: sample `8`, hit `1.0`, avg `0.032709`, median `0.033597`, mae `0.032709`
- 60d: sample `8`, hit `1.0`, avg `0.084908`, median `0.090809`, mae `0.084908`

### confidence validation
- `{'strong_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.010088, 'median_return': 0.012502, 'mean_absolute_return': 0.019388, 'max_adverse_excursion': -0.034906, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.013178, 'median_return': 0.017467, 'mean_absolute_return': 0.025586, 'max_adverse_excursion': -0.039432, 'max_favorable_excursion': 0.062512}, '10d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.019125, 'median_return': 0.02569, 'mean_absolute_return': 0.039508, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.039677, 'median_return': 0.039296, 'mean_absolute_return': 0.054198, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.117235}, '60d': {'sample_size': 60, 'hit_rate': 0.95, 'avg_return': 0.091923, 'median_return': 0.096597, 'mean_absolute_return': 0.094707, 'max_adverse_excursion': -0.052574, 'max_favorable_excursion': 0.195631}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.013512, 'median_return': 0.011414, 'mean_absolute_return': 0.013512, 'max_adverse_excursion': 0.004542, 'max_favorable_excursion': 0.030754}, '5d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.021434, 'median_return': 0.025304, 'mean_absolute_return': 0.021434, 'max_adverse_excursion': 0.00774, 'max_favorable_excursion': 0.038957}, '10d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.027829, 'median_return': 0.027042, 'mean_absolute_return': 0.027829, 'max_adverse_excursion': 0.012215, 'max_favorable_excursion': 0.048125}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.032709, 'median_return': 0.033597, 'mean_absolute_return': 0.032709, 'max_adverse_excursion': 0.025541, 'max_favorable_excursion': 0.04151}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.084908, 'median_return': 0.090809, 'mean_absolute_return': 0.084908, 'max_adverse_excursion': 0.043741, 'max_favorable_excursion': 0.10629}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.011251, 'median_return': 0.013598, 'mean_absolute_return': 0.021033, 'max_adverse_excursion': -0.04969, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.014766, 'median_return': 0.018242, 'mean_absolute_return': 0.027862, 'max_adverse_excursion': -0.04207, 'max_favorable_excursion': 0.067976}, '10d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.01978, 'median_return': 0.030654, 'mean_absolute_return': 0.045631, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 72, 'hit_rate': 0.8611, 'avg_return': 0.043354, 'median_return': 0.043749, 'mean_absolute_return': 0.060402, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.158039}, '60d': {'sample_size': 72, 'hit_rate': 0.9167, 'avg_return': 0.100034, 'median_return': 0.099838, 'mean_absolute_return': 0.103295, 'max_adverse_excursion': -0.052574, 'max_favorable_excursion': 0.258847}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.75}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.175, 'both_hit': 43, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.175, 'both_hit': 42, 'both_miss': 18}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.1, 'both_hit': 43, 'both_miss': 17}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.875, 'primary_minus_secondary': -0.2, 'both_hit': 52, 'both_miss': 8}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.925, 'primary_minus_secondary': -0.175, 'both_hit': 57, 'both_miss': 3}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.015645, 'median_return': 0.018644, 'mean_absolute_return': 0.022959, 'max_adverse_excursion': -0.04969, 'max_favorable_excursion': 0.040067}, '5d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.022195, 'median_return': 0.024027, 'mean_absolute_return': 0.03212, 'max_adverse_excursion': -0.04207, 'max_favorable_excursion': 0.067976}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.024965, 'median_return': 0.030744, 'mean_absolute_return': 0.05688, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.050125, 'median_return': 0.03791, 'mean_absolute_return': 0.067935, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.158039}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.118317, 'median_return': 0.109805, 'mean_absolute_return': 0.121702, 'max_adverse_excursion': -0.016165, 'max_favorable_excursion': 0.258847}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.010088, 'median_return': 0.012502, 'mean_absolute_return': 0.019388, 'max_adverse_excursion': -0.034906, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.013178, 'median_return': 0.017467, 'mean_absolute_return': 0.025586, 'max_adverse_excursion': -0.039432, 'max_favorable_excursion': 0.062512}, '10d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.019125, 'median_return': 0.02569, 'mean_absolute_return': 0.039508, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 60, 'hit_rate': 0.8667, 'avg_return': 0.039677, 'median_return': 0.039296, 'mean_absolute_return': 0.054198, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.117235}, '60d': {'sample_size': 60, 'hit_rate': 0.95, 'avg_return': 0.091923, 'median_return': 0.096597, 'mean_absolute_return': 0.094707, 'max_adverse_excursion': -0.052574, 'max_favorable_excursion': 0.195631}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.010088`, median `0.012502`, mae `0.019388`
- 5d: sample `60`, hit `0.7`, avg `0.013178`, median `0.017467`, mae `0.025586`
- 10d: sample `60`, hit `0.7167`, avg `0.019125`, median `0.02569`, mae `0.039508`
- 20d: sample `60`, hit `0.8667`, avg `0.039677`, median `0.039296`, mae `0.054198`
- 60d: sample `60`, hit `0.95`, avg `0.091923`, median `0.096597`, mae `0.094707`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.015645`, median `0.018644`, mae `0.022959`
- 5d: sample `20`, hit `0.85`, avg `0.022195`, median `0.024027`, mae `0.03212`
- 10d: sample `20`, hit `0.7`, avg `0.024965`, median `0.030744`, mae `0.05688`
- 20d: sample `20`, hit `0.9`, avg `0.050125`, median `0.03791`, mae `0.067935`
- 60d: sample `20`, hit `0.85`, avg `0.118317`, median `0.109805`, mae `0.121702`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.010088`, median `0.012502`, mae `0.019388`
- 5d: sample `60`, hit `0.7`, avg `0.013178`, median `0.017467`, mae `0.025586`
- 10d: sample `60`, hit `0.7167`, avg `0.019125`, median `0.02569`, mae `0.039508`
- 20d: sample `60`, hit `0.8667`, avg `0.039677`, median `0.039296`, mae `0.054198`
- 60d: sample `60`, hit `0.95`, avg `0.091923`, median `0.096597`, mae `0.094707`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.015108`, median `0.025242`, mae `0.02505`
- 5d: sample `20`, hit `0.8`, avg `0.021034`, median `0.026653`, mae `0.031431`
- 10d: sample `20`, hit `0.95`, avg `0.039061`, median `0.042458`, mae `0.054892`
- 20d: sample `20`, hit `0.9`, avg `0.056159`, median `0.076433`, mae `0.066483`
- 60d: sample `20`, hit `0.95`, avg `0.112362`, median `0.123154`, mae `0.117619`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.010088`, median `0.012502`, mae `0.019388`
- 5d: sample `60`, hit `0.7`, avg `0.013178`, median `0.017467`, mae `0.025586`
- 10d: sample `60`, hit `0.7167`, avg `0.019125`, median `0.02569`, mae `0.039508`
- 20d: sample `60`, hit `0.8667`, avg `0.039677`, median `0.039296`, mae `0.054198`
- 60d: sample `60`, hit `0.95`, avg `0.091923`, median `0.096597`, mae `0.094707`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.015108`, median `0.025242`, mae `0.02505`
- 5d: sample `20`, hit `0.8`, avg `0.021034`, median `0.026653`, mae `0.031431`
- 10d: sample `20`, hit `0.95`, avg `0.039061`, median `0.042458`, mae `0.054892`
- 20d: sample `20`, hit `0.9`, avg `0.056159`, median `0.076433`, mae `0.066483`
- 60d: sample `20`, hit `0.95`, avg `0.112362`, median `0.123154`, mae `0.117619`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.015645`, median `0.018644`, mae `0.022959`
- 5d: sample `20`, hit `0.85`, avg `0.022195`, median `0.024027`, mae `0.03212`
- 10d: sample `20`, hit `0.7`, avg `0.024965`, median `0.030744`, mae `0.05688`
- 20d: sample `20`, hit `0.9`, avg `0.050125`, median `0.03791`, mae `0.067935`
- 60d: sample `20`, hit `0.85`, avg `0.118317`, median `0.109805`, mae `0.121702`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.007578`, median `0.011957`, mae `0.016557`
- 5d: sample `40`, hit `0.65`, avg `0.009251`, median `0.012091`, mae `0.022663`
- 10d: sample `40`, hit `0.6`, avg `0.009156`, median `0.015974`, mae `0.031816`
- 20d: sample `40`, hit `0.85`, avg `0.031436`, median `0.035222`, mae `0.048056`
- 60d: sample `40`, hit `0.95`, avg `0.081703`, median `0.087238`, mae `0.083251`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.015108`, median `0.025242`, mae `0.02505`
- 5d: sample `20`, hit `0.8`, avg `0.021034`, median `0.026653`, mae `0.031431`
- 10d: sample `20`, hit `0.95`, avg `0.039061`, median `0.042458`, mae `0.054892`
- 20d: sample `20`, hit `0.9`, avg `0.056159`, median `0.076433`, mae `0.066483`
- 60d: sample `20`, hit `0.95`, avg `0.112362`, median `0.123154`, mae `0.117619`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.015645`, median `0.018644`, mae `0.022959`
- 5d: sample `20`, hit `0.85`, avg `0.022195`, median `0.024027`, mae `0.03212`
- 10d: sample `20`, hit `0.7`, avg `0.024965`, median `0.030744`, mae `0.05688`
- 20d: sample `20`, hit `0.9`, avg `0.050125`, median `0.03791`, mae `0.067935`
- 60d: sample `20`, hit `0.85`, avg `0.118317`, median `0.109805`, mae `0.121702`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.007578`, median `0.011957`, mae `0.016557`
- 5d: sample `40`, hit `0.65`, avg `0.009251`, median `0.012091`, mae `0.022663`
- 10d: sample `40`, hit `0.6`, avg `0.009156`, median `0.015974`, mae `0.031816`
- 20d: sample `40`, hit `0.85`, avg `0.031436`, median `0.035222`, mae `0.048056`
- 60d: sample `40`, hit `0.95`, avg `0.081703`, median `0.087238`, mae `0.083251`

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
- 3d: sample `80`, hit `0.75`, avg `0.011477`, median `0.01272`, mae `0.020281`
- 5d: sample `80`, hit `0.7375`, avg `0.015433`, median `0.018242`, mae `0.027219`
- 10d: sample `80`, hit `0.7125`, avg `0.020585`, median `0.027042`, mae `0.043851`
- 20d: sample `80`, hit `0.875`, avg `0.042289`, median `0.03801`, mae `0.057632`
- 60d: sample `80`, hit `0.925`, avg `0.098521`, median `0.098961`, mae `0.101456`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.75`, avg `0.011477`, median `0.01272`, mae `0.020281`
- 5d: sample `80`, hit `0.7375`, avg `0.015433`, median `0.018242`, mae `0.027219`
- 10d: sample `80`, hit `0.7125`, avg `0.020585`, median `0.027042`, mae `0.043851`
- 20d: sample `80`, hit `0.875`, avg `0.042289`, median `0.03801`, mae `0.057632`
- 60d: sample `80`, hit `0.925`, avg `0.098521`, median `0.098961`, mae `0.101456`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.010088`, median `0.012502`, mae `0.019388`
- 5d: sample `60`, hit `0.7`, avg `0.013178`, median `0.017467`, mae `0.025586`
- 10d: sample `60`, hit `0.7167`, avg `0.019125`, median `0.02569`, mae `0.039508`
- 20d: sample `60`, hit `0.8667`, avg `0.039677`, median `0.039296`, mae `0.054198`
- 60d: sample `60`, hit `0.95`, avg `0.091923`, median `0.096597`, mae `0.094707`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.7167`, avg `0.010088`, median `0.012502`, mae `0.019388`
- 5d: sample `60`, hit `0.7`, avg `0.013178`, median `0.017467`, mae `0.025586`
- 10d: sample `60`, hit `0.7167`, avg `0.019125`, median `0.02569`, mae `0.039508`
- 20d: sample `60`, hit `0.8667`, avg `0.039677`, median `0.039296`, mae `0.054198`
- 60d: sample `60`, hit `0.95`, avg `0.091923`, median `0.096597`, mae `0.094707`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.85`, avg `0.015645`, median `0.018644`, mae `0.022959`
- 5d: sample `20`, hit `0.85`, avg `0.022195`, median `0.024027`, mae `0.03212`
- 10d: sample `20`, hit `0.7`, avg `0.024965`, median `0.030744`, mae `0.05688`
- 20d: sample `20`, hit `0.9`, avg `0.050125`, median `0.03791`, mae `0.067935`
- 60d: sample `20`, hit `0.85`, avg `0.118317`, median `0.109805`, mae `0.121702`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
