# High Confidence Edge Report

Generated at: `2026-10-09T00:42:55.307343+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004426`, median `0.009349`, mae `0.015713`
- 5d: sample `60`, hit `0.5667`, avg `0.004446`, median `0.008152`, mae `0.02048`
- 10d: sample `60`, hit `0.65`, avg `0.009609`, median `0.005356`, mae `0.021752`
- 20d: sample `60`, hit `0.9`, avg `0.03985`, median `0.033597`, mae `0.041916`
- 60d: sample `60`, hit `0.8833`, avg `0.084089`, median `0.095628`, mae `0.088574`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003641`, median `-0.0002`, mae `0.016354`
- 5d: sample `20`, hit `0.35`, avg `-0.005618`, median `-0.005796`, mae `0.019238`
- 10d: sample `20`, hit `0.4`, avg `-0.010428`, median `-0.019497`, mae `0.034812`
- 20d: sample `20`, hit `0.45`, avg `-0.001691`, median `-0.006813`, mae `0.045345`
- 60d: sample `20`, hit `0.85`, avg `0.089323`, median `0.11278`, mae `0.099772`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.004426, 'median_return': 0.009349, 'mean_absolute_return': 0.015713, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.004446, 'median_return': 0.008152, 'mean_absolute_return': 0.02048, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.009609, 'median_return': 0.005356, 'mean_absolute_return': 0.021752, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.9, 'avg_return': 0.03985, 'median_return': 0.033597, 'mean_absolute_return': 0.041916, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.8833, 'avg_return': 0.084089, 'median_return': 0.095628, 'mean_absolute_return': 0.088574, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010606, 'median_return': 0.0207, 'mean_absolute_return': 0.019302, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.014887, 'median_return': 0.013852, 'mean_absolute_return': 0.02145, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016471, 'median_return': 0.024811, 'mean_absolute_return': 0.024193, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.059849, 'median_return': 0.062955, 'mean_absolute_return': 0.059849, 'max_adverse_excursion': 0.024743, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.105861, 'median_return': 0.099838, 'mean_absolute_return': 0.105861, 'max_adverse_excursion': 0.085781, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001499, 'median_return': 0.004542, 'mean_absolute_return': 0.015492, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.000491, 'median_return': -0.003262, 'mean_absolute_return': 0.020028, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.003281, 'median_return': 0.004187, 'mean_absolute_return': 0.025108, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.026089, 'median_return': 0.027885, 'mean_absolute_return': 0.040876, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.8611, 'avg_return': 0.083123, 'median_return': 0.098199, 'mean_absolute_return': 0.089764, 'max_adverse_excursion': -0.053658, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.6375}, '20d': {'sample_size': 80, 'hit_rate': 0.8125}, '60d': {'sample_size': 80, 'hit_rate': 0.7}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.025, 'both_hit': 28, 'both_miss': 12}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.05, 'both_hit': 25, 'both_miss': 15}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.05, 'both_hit': 29, 'both_miss': 11}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.8125, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.25, 'both_hit': 35, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.05, 'both_hit': 38, 'both_miss': 2}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.004426, 'median_return': 0.009349, 'mean_absolute_return': 0.015713, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.004446, 'median_return': 0.008152, 'mean_absolute_return': 0.02048, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.009609, 'median_return': 0.005356, 'mean_absolute_return': 0.021752, 'max_adverse_excursion': -0.055394, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 60, 'hit_rate': 0.9, 'avg_return': 0.03985, 'median_return': 0.033597, 'mean_absolute_return': 0.041916, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 60, 'hit_rate': 0.8833, 'avg_return': 0.084089, 'median_return': 0.095628, 'mean_absolute_return': 0.088574, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.003641, 'median_return': -0.0002, 'mean_absolute_return': 0.016354, 'max_adverse_excursion': -0.036265, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.005618, 'median_return': -0.005796, 'mean_absolute_return': 0.019238, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010428, 'median_return': -0.019497, 'mean_absolute_return': 0.034812, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001691, 'median_return': -0.006813, 'mean_absolute_return': 0.045345, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.085181}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.089323, 'median_return': 0.11278, 'mean_absolute_return': 0.099772, 'max_adverse_excursion': -0.053658, 'max_favorable_excursion': 0.14571}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `40`, hit `0.475`, avg `-0.001411`, median `-0.0002`, mae `0.017709`
- 5d: sample `40`, hit `0.4`, avg `-0.002527`, median `-0.00693`, mae `0.022821`
- 10d: sample `40`, hit `0.45`, avg `0.000166`, median `-0.007019`, mae `0.030295`
- 20d: sample `40`, hit `0.7`, avg `0.021798`, median `0.024506`, mae `0.045476`
- 60d: sample `40`, hit `0.8`, avg `0.081078`, median `0.104804`, mae `0.089691`

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
- 3d: sample `40`, hit `0.575`, avg `0.002399`, median `0.004815`, mae `0.015411`
- 5d: sample `40`, hit `0.525`, avg `0.001859`, median `0.006609`, mae `0.021146`
- 10d: sample `40`, hit `0.6`, avg `0.007798`, median `0.003921`, mae `0.021185`
- 20d: sample `40`, hit `0.925`, avg `0.03842`, median `0.032299`, mae `0.040022`
- 60d: sample `40`, hit `0.85`, avg `0.079412`, median `0.084216`, mae `0.083842`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003641`, median `-0.0002`, mae `0.016354`
- 5d: sample `20`, hit `0.35`, avg `-0.005618`, median `-0.005796`, mae `0.019238`
- 10d: sample `20`, hit `0.4`, avg `-0.010428`, median `-0.019497`, mae `0.034812`
- 20d: sample `20`, hit `0.45`, avg `-0.001691`, median `-0.006813`, mae `0.045345`
- 60d: sample `20`, hit `0.85`, avg `0.089323`, median `0.11278`, mae `0.099772`

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
- 3d: sample `80`, hit `0.5875`, avg `0.002409`, median `0.006042`, mae `0.015873`
- 5d: sample `80`, hit `0.5125`, avg `0.00193`, median `0.00288`, mae `0.02017`
- 10d: sample `80`, hit `0.5875`, avg `0.0046`, median `0.004196`, mae `0.025017`
- 20d: sample `80`, hit `0.7875`, avg `0.029465`, median `0.032102`, mae `0.042774`
- 60d: sample `80`, hit `0.875`, avg `0.085397`, median `0.099512`, mae `0.091373`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004426`, median `0.009349`, mae `0.015713`
- 5d: sample `60`, hit `0.5667`, avg `0.004446`, median `0.008152`, mae `0.02048`
- 10d: sample `60`, hit `0.65`, avg `0.009609`, median `0.005356`, mae `0.021752`
- 20d: sample `60`, hit `0.9`, avg `0.03985`, median `0.033597`, mae `0.041916`
- 60d: sample `60`, hit `0.8833`, avg `0.084089`, median `0.095628`, mae `0.088574`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.002409`, median `0.006042`, mae `0.015873`
- 5d: sample `80`, hit `0.5125`, avg `0.00193`, median `0.00288`, mae `0.02017`
- 10d: sample `80`, hit `0.5875`, avg `0.0046`, median `0.004196`, mae `0.025017`
- 20d: sample `80`, hit `0.7875`, avg `0.029465`, median `0.032102`, mae `0.042774`
- 60d: sample `80`, hit `0.875`, avg `0.085397`, median `0.099512`, mae `0.091373`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004426`, median `0.009349`, mae `0.015713`
- 5d: sample `60`, hit `0.5667`, avg `0.004446`, median `0.008152`, mae `0.02048`
- 10d: sample `60`, hit `0.65`, avg `0.009609`, median `0.005356`, mae `0.021752`
- 20d: sample `60`, hit `0.9`, avg `0.03985`, median `0.033597`, mae `0.041916`
- 60d: sample `60`, hit `0.8833`, avg `0.084089`, median `0.095628`, mae `0.088574`

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
