# High Confidence Edge Report

Generated at: `2026-10-06T01:53:22.051531+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `76`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `76`, gate `moderate_evidence`
- 5d: completed `76`, gate `moderate_evidence`
- 10d: completed `76`, gate `moderate_evidence`
- 20d: completed `76`, gate `moderate_evidence`
- 60d: completed `76`, gate `moderate_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.4`, avg `-0.007025`, median `-0.003995`, mae `0.017695`
- 5d: sample `80`, hit `0.425`, avg `-0.011012`, median `-0.007113`, mae `0.022099`
- 10d: sample `80`, hit `0.4125`, avg `-0.013625`, median `-0.009882`, mae `0.032047`
- 20d: sample `80`, hit `0.55`, avg `-0.003616`, median `0.010829`, mae `0.042836`
- 60d: sample `80`, hit `0.75`, avg `0.030122`, median `0.046132`, mae `0.076425`

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
- 3d: sample `8`, hit `0.5`, avg `-0.002548`, median `0.004068`, mae `0.011513`
- 5d: sample `8`, hit `0.625`, avg `0.001216`, median `0.009569`, mae `0.009687`
- 10d: sample `8`, hit `0.625`, avg `0.006939`, median `0.014793`, mae `0.021915`
- 20d: sample `8`, hit `0.75`, avg `0.014696`, median `0.034024`, mae `0.044396`
- 60d: sample `8`, hit `1.0`, avg `0.044563`, median `0.044683`, mae `0.044563`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.009683`, median `0.006895`, mae `0.026003`
- 5d: sample `8`, hit `0.5`, avg `-0.014553`, median `0.005072`, mae `0.0316`
- 10d: sample `8`, hit `0.25`, avg `-0.017771`, median `-0.013832`, mae `0.025554`
- 20d: sample `8`, hit `0.5`, avg `-0.01538`, median `0.001463`, mae `0.038088`
- 60d: sample `8`, hit `0.5`, avg `-0.046636`, median `0.037425`, mae `0.105094`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.009683, 'median_return': 0.006895, 'mean_absolute_return': 0.026003, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.014553, 'median_return': 0.005072, 'mean_absolute_return': 0.0316, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026602}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.017771, 'median_return': -0.013832, 'mean_absolute_return': 0.025554, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.01538, 'median_return': 0.001463, 'mean_absolute_return': 0.038088, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.046636, 'median_return': 0.037425, 'mean_absolute_return': 0.105094, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.00673, 'median_return': -0.003995, 'mean_absolute_return': 0.016772, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.010619, 'median_return': -0.007113, 'mean_absolute_return': 0.021044, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.013164, 'median_return': -0.007019, 'mean_absolute_return': 0.032768, 'max_adverse_excursion': -0.105849, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.002309, 'median_return': 0.013156, 'mean_absolute_return': 0.043364, 'max_adverse_excursion': -0.130909, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.03865, 'median_return': 0.05019, 'mean_absolute_return': 0.07324, 'max_adverse_excursion': -0.219397, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.25}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.5, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.005382, 'median_return': -0.003649, 'mean_absolute_return': 0.015665, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.008607, 'median_return': -0.000423, 'mean_absolute_return': 0.01861, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026602}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.010819, 'median_return': -0.007019, 'mean_absolute_return': 0.025748, 'max_adverse_excursion': -0.095057, 'max_favorable_excursion': 0.051845}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.003057, 'median_return': 0.014806, 'mean_absolute_return': 0.039228, 'max_adverse_excursion': -0.130909, 'max_favorable_excursion': 0.059335}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.009723, 'median_return': 0.03743, 'mean_absolute_return': 0.065316, 'max_adverse_excursion': -0.219397, 'max_favorable_excursion': 0.130806}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.008668, 'median_return': -0.009843, 'mean_absolute_return': 0.019725, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.013418, 'median_return': -0.013237, 'mean_absolute_return': 0.025589, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.01643, 'median_return': -0.013412, 'mean_absolute_return': 0.038346, 'max_adverse_excursion': -0.105849, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.004176, 'median_return': 0.001515, 'mean_absolute_return': 0.046444, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.050521, 'median_return': 0.084216, 'mean_absolute_return': 0.087533, 'max_adverse_excursion': -0.146938, 'max_favorable_excursion': 0.154804}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.005761`, median `-0.003649`, mae `0.016259`
- 5d: sample `60`, hit `0.45`, avg `-0.009331`, median `-0.005632`, mae `0.020595`
- 10d: sample `60`, hit `0.4833`, avg `-0.009851`, median `-0.004767`, mae `0.032955`
- 20d: sample `60`, hit `0.5667`, avg `-0.000851`, median `0.013156`, mae `0.0436`
- 60d: sample `60`, hit `0.7667`, avg `0.038192`, median `0.05019`, mae `0.07557`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4167`, avg `-0.005761`, median `-0.003649`, mae `0.016259`
- 5d: sample `60`, hit `0.45`, avg `-0.009331`, median `-0.005632`, mae `0.020595`
- 10d: sample `60`, hit `0.4833`, avg `-0.009851`, median `-0.004767`, mae `0.032955`
- 20d: sample `60`, hit `0.5667`, avg `-0.000851`, median `0.013156`, mae `0.0436`
- 60d: sample `60`, hit `0.7667`, avg `0.038192`, median `0.05019`, mae `0.07557`

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
- 3d: sample `80`, hit `0.4`, avg `-0.007025`, median `-0.003995`, mae `0.017695`
- 5d: sample `80`, hit `0.425`, avg `-0.011012`, median `-0.007113`, mae `0.022099`
- 10d: sample `80`, hit `0.4125`, avg `-0.013625`, median `-0.009882`, mae `0.032047`
- 20d: sample `80`, hit `0.55`, avg `-0.003616`, median `0.010829`, mae `0.042836`
- 60d: sample `80`, hit `0.75`, avg `0.030122`, median `0.046132`, mae `0.076425`

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
- 3d: sample `80`, hit `0.4`, avg `-0.007025`, median `-0.003995`, mae `0.017695`
- 5d: sample `80`, hit `0.425`, avg `-0.011012`, median `-0.007113`, mae `0.022099`
- 10d: sample `80`, hit `0.4125`, avg `-0.013625`, median `-0.009882`, mae `0.032047`
- 20d: sample `80`, hit `0.55`, avg `-0.003616`, median `0.010829`, mae `0.042836`
- 60d: sample `80`, hit `0.75`, avg `0.030122`, median `0.046132`, mae `0.076425`

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
