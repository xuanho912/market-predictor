# High Confidence Edge Report

Generated at: `2026-09-15T01:02:13.411358+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `16`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `16`, gate `insufficient`
- 5d: completed `16`, gate `insufficient`
- 10d: completed `16`, gate `insufficient`
- 20d: completed `16`, gate `insufficient`
- 60d: completed `16`, gate `insufficient`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004929`, median `0.012217`, mae `0.019512`
- 5d: sample `80`, hit `0.5875`, avg `0.006833`, median `0.01152`, mae `0.022007`
- 10d: sample `80`, hit `0.6875`, avg `0.012263`, median `0.01704`, mae `0.030038`
- 20d: sample `80`, hit `0.775`, avg `0.033075`, median `0.03551`, mae `0.044022`
- 60d: sample `80`, hit `0.8`, avg `0.067791`, median `0.08619`, mae `0.089592`

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
- 3d: sample `8`, hit `0.375`, avg `-0.001324`, median `-0.001591`, mae `0.015212`
- 5d: sample `8`, hit `0.75`, avg `0.004581`, median `0.009709`, mae `0.016718`
- 10d: sample `8`, hit `0.625`, avg `0.011426`, median `0.023826`, mae `0.020652`
- 20d: sample `8`, hit `1.0`, avg `0.050716`, median `0.058396`, mae `0.050716`
- 60d: sample `8`, hit `1.0`, avg `0.095878`, median `0.121826`, mae `0.095878`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.001324`, median `-0.001591`, mae `0.015212`
- 5d: sample `8`, hit `0.75`, avg `0.004581`, median `0.009709`, mae `0.016718`
- 10d: sample `8`, hit `0.625`, avg `0.011426`, median `0.023826`, mae `0.020652`
- 20d: sample `8`, hit `1.0`, avg `0.050716`, median `0.058396`, mae `0.050716`
- 60d: sample `8`, hit `1.0`, avg `0.095878`, median `0.121826`, mae `0.095878`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.001324, 'median_return': -0.001591, 'mean_absolute_return': 0.015212, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.004581, 'median_return': 0.009709, 'mean_absolute_return': 0.016718, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011426, 'median_return': 0.023826, 'mean_absolute_return': 0.020652, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.036071}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.050716, 'median_return': 0.058396, 'mean_absolute_return': 0.050716, 'max_adverse_excursion': 0.017149, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.095878, 'median_return': 0.121826, 'mean_absolute_return': 0.095878, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.005624, 'median_return': 0.012486, 'mean_absolute_return': 0.01999, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.007083, 'median_return': 0.012604, 'mean_absolute_return': 0.022594, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.012356, 'median_return': 0.01704, 'mean_absolute_return': 0.031081, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.031115, 'median_return': 0.034726, 'mean_absolute_return': 0.043278, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.06467, 'median_return': 0.084216, 'mean_absolute_return': 0.088893, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3625}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.3125}, '20d': {'sample_size': 80, 'hit_rate': 0.225}, '60d': {'sample_size': 80, 'hit_rate': 0.2}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.225, 'secondary_hit_rate': 0.775, 'primary_minus_secondary': -0.55, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.6, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.006489, 'median_return': 0.012217, 'mean_absolute_return': 0.01488, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.008052, 'median_return': 0.012885, 'mean_absolute_return': 0.016687, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.011989, 'median_return': 0.013069, 'mean_absolute_return': 0.01932, 'max_adverse_excursion': -0.038784, 'max_favorable_excursion': 0.050818}, '20d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.033756, 'median_return': 0.03551, 'mean_absolute_return': 0.037194, 'max_adverse_excursion': -0.019951, 'max_favorable_excursion': 0.07754}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.075645, 'median_return': 0.087104, 'mean_absolute_return': 0.083844, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003369, 'median_return': 0.012525, 'mean_absolute_return': 0.024144, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.005614, 'median_return': 0.01152, 'mean_absolute_return': 0.027326, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.012538, 'median_return': 0.021169, 'mean_absolute_return': 0.040756, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.032394, 'median_return': 0.039427, 'mean_absolute_return': 0.050849, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.059936, 'median_return': 0.08619, 'mean_absolute_return': 0.09534, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004929`, median `0.012217`, mae `0.019512`
- 5d: sample `80`, hit `0.5875`, avg `0.006833`, median `0.01152`, mae `0.022007`
- 10d: sample `80`, hit `0.6875`, avg `0.012263`, median `0.01704`, mae `0.030038`
- 20d: sample `80`, hit `0.775`, avg `0.033075`, median `0.03551`, mae `0.044022`
- 60d: sample `80`, hit `0.8`, avg `0.067791`, median `0.08619`, mae `0.089592`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.006489`, median `0.012217`, mae `0.01488`
- 5d: sample `40`, hit `0.625`, avg `0.008052`, median `0.012885`, mae `0.016687`
- 10d: sample `40`, hit `0.75`, avg `0.011989`, median `0.013069`, mae `0.01932`
- 20d: sample `40`, hit `0.825`, avg `0.033756`, median `0.03551`, mae `0.037194`
- 60d: sample `40`, hit `0.85`, avg `0.075645`, median `0.087104`, mae `0.083844`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004929`, median `0.012217`, mae `0.019512`
- 5d: sample `80`, hit `0.5875`, avg `0.006833`, median `0.01152`, mae `0.022007`
- 10d: sample `80`, hit `0.6875`, avg `0.012263`, median `0.01704`, mae `0.030038`
- 20d: sample `80`, hit `0.775`, avg `0.033075`, median `0.03551`, mae `0.044022`
- 60d: sample `80`, hit `0.8`, avg `0.067791`, median `0.08619`, mae `0.089592`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004929`, median `0.012217`, mae `0.019512`
- 5d: sample `80`, hit `0.5875`, avg `0.006833`, median `0.01152`, mae `0.022007`
- 10d: sample `80`, hit `0.6875`, avg `0.012263`, median `0.01704`, mae `0.030038`
- 20d: sample `80`, hit `0.775`, avg `0.033075`, median `0.03551`, mae `0.044022`
- 60d: sample `80`, hit `0.8`, avg `0.067791`, median `0.08619`, mae `0.089592`

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

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
