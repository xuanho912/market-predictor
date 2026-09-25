# High Confidence Edge Report

Generated at: `2026-09-25T09:07:26.582523+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `47`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `47`, gate `early_evidence`
- 5d: completed `47`, gate `early_evidence`
- 10d: completed `47`, gate `early_evidence`
- 20d: completed `47`, gate `early_evidence`
- 60d: completed `47`, gate `early_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.004905`, median `-0.003649`, mae `0.016026`
- 5d: sample `60`, hit `0.4833`, avg `-0.006697`, median `-0.001562`, mae `0.018731`
- 10d: sample `60`, hit `0.55`, avg `-0.004399`, median `0.005535`, mae `0.029969`
- 20d: sample `60`, hit `0.6333`, avg `0.008522`, median `0.015725`, mae `0.043229`
- 60d: sample `60`, hit `0.8333`, avg `0.049552`, median `0.057507`, mae `0.074497`

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
- 3d: sample `8`, hit `0.25`, avg `-0.016717`, median `-0.030499`, mae `0.027882`
- 5d: sample `8`, hit `0.375`, avg `-0.022926`, median `-0.024165`, mae `0.029269`
- 10d: sample `8`, hit `0.0`, avg `-0.023846`, median `-0.017071`, mae `0.023846`
- 20d: sample `8`, hit `0.625`, avg `-0.004187`, median `0.021759`, mae `0.046567`
- 60d: sample `8`, hit `0.75`, avg `0.019077`, median `0.050438`, mae `0.088012`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.016717`, median `-0.030499`, mae `0.027882`
- 5d: sample `8`, hit `0.375`, avg `-0.022926`, median `-0.024165`, mae `0.029269`
- 10d: sample `8`, hit `0.0`, avg `-0.023846`, median `-0.017071`, mae `0.023846`
- 20d: sample `8`, hit `0.625`, avg `-0.004187`, median `0.021759`, mae `0.046567`
- 60d: sample `8`, hit `0.75`, avg `0.019077`, median `0.050438`, mae `0.088012`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.010292, 'median_return': -0.010094, 'mean_absolute_return': 0.022162, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.017705, 'median_return': -0.018175, 'mean_absolute_return': 0.023983, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.15, 'avg_return': -0.021642, 'median_return': -0.013832, 'mean_absolute_return': 0.026163, 'max_adverse_excursion': -0.065338, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.00108, 'median_return': 0.020068, 'mean_absolute_return': 0.047614, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.027605, 'median_return': 0.046132, 'mean_absolute_return': 0.077497, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.016717, 'median_return': -0.030499, 'mean_absolute_return': 0.027882, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.022926, 'median_return': -0.024165, 'mean_absolute_return': 0.029269, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.010589}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.023846, 'median_return': -0.017071, 'mean_absolute_return': 0.023846, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.004187, 'median_return': 0.021759, 'mean_absolute_return': 0.046567, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.019077, 'median_return': 0.050438, 'mean_absolute_return': 0.088012, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.005089, 'median_return': -0.003676, 'mean_absolute_return': 0.016414, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.007951, 'median_return': -0.005796, 'mean_absolute_return': 0.019019, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.007028, 'median_return': 0.000397, 'mean_absolute_return': 0.029592, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.007867, 'median_return': 0.016021, 'mean_absolute_return': 0.044076, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.046842, 'median_return': 0.053855, 'mean_absolute_return': 0.073828, 'max_adverse_excursion': -0.177096, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.375}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.3125}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': -0.006252, 'median_return': -0.003995, 'mean_absolute_return': 0.01756, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.009449, 'median_return': -0.00693, 'mean_absolute_return': 0.020044, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 80, 'hit_rate': 0.45, 'avg_return': -0.00871, 'median_return': -0.006017, 'mean_absolute_return': 0.029017, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.006662, 'median_return': 0.016027, 'mean_absolute_return': 0.044325, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.8125, 'avg_return': 0.044065, 'median_return': 0.050438, 'mean_absolute_return': 0.075247, 'max_adverse_excursion': -0.177096, 'max_favorable_excursion': 0.154804}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.006252`, median `-0.003995`, mae `0.01756`
- 5d: sample `80`, hit `0.4375`, avg `-0.009449`, median `-0.00693`, mae `0.020044`
- 10d: sample `80`, hit `0.45`, avg `-0.00871`, median `-0.006017`, mae `0.029017`
- 20d: sample `80`, hit `0.625`, avg `0.006662`, median `0.016027`, mae `0.044325`
- 60d: sample `80`, hit `0.8125`, avg `0.044065`, median `0.050438`, mae `0.075247`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.004905`, median `-0.003649`, mae `0.016026`
- 5d: sample `60`, hit `0.4833`, avg `-0.006697`, median `-0.001562`, mae `0.018731`
- 10d: sample `60`, hit `0.55`, avg `-0.004399`, median `0.005535`, mae `0.029969`
- 20d: sample `60`, hit `0.6333`, avg `0.008522`, median `0.015725`, mae `0.043229`
- 60d: sample `60`, hit `0.8333`, avg `0.049552`, median `0.057507`, mae `0.074497`

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
- 3d: sample `80`, hit `0.4125`, avg `-0.006252`, median `-0.003995`, mae `0.01756`
- 5d: sample `80`, hit `0.4375`, avg `-0.009449`, median `-0.00693`, mae `0.020044`
- 10d: sample `80`, hit `0.45`, avg `-0.00871`, median `-0.006017`, mae `0.029017`
- 20d: sample `80`, hit `0.625`, avg `0.006662`, median `0.016027`, mae `0.044325`
- 60d: sample `80`, hit `0.8125`, avg `0.044065`, median `0.050438`, mae `0.075247`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4125`, avg `-0.006252`, median `-0.003995`, mae `0.01756`
- 5d: sample `80`, hit `0.4375`, avg `-0.009449`, median `-0.00693`, mae `0.020044`
- 10d: sample `80`, hit `0.45`, avg `-0.00871`, median `-0.006017`, mae `0.029017`
- 20d: sample `80`, hit `0.625`, avg `0.006662`, median `0.016027`, mae `0.044325`
- 60d: sample `80`, hit `0.8125`, avg `0.044065`, median `0.050438`, mae `0.075247`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.010292`, median `-0.010094`, mae `0.022162`
- 5d: sample `20`, hit `0.3`, avg `-0.017705`, median `-0.018175`, mae `0.023983`
- 10d: sample `20`, hit `0.15`, avg `-0.021642`, median `-0.013832`, mae `0.026163`
- 20d: sample `20`, hit `0.6`, avg `0.00108`, median `0.020068`, mae `0.047614`
- 60d: sample `20`, hit `0.75`, avg `0.027605`, median `0.046132`, mae `0.077497`

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
