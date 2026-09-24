# High Confidence Edge Report

Generated at: `2026-09-24T01:06:34.387714+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `43`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `43`, gate `early_evidence`
- 5d: completed `43`, gate `early_evidence`
- 10d: completed `43`, gate `early_evidence`
- 20d: completed `43`, gate `early_evidence`
- 60d: completed `43`, gate `early_evidence`

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
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

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
- 3d: sample `8`, hit `0.5`, avg `-0.000656`, median `0.003757`, mae `0.015483`
- 5d: sample `8`, hit `0.625`, avg `0.000493`, median `0.007948`, mae `0.015148`
- 10d: sample `8`, hit `0.625`, avg `0.009459`, median `0.020334`, mae `0.018685`
- 20d: sample `8`, hit `0.875`, avg `0.047912`, median `0.058396`, mae `0.049233`
- 60d: sample `8`, hit `1.0`, avg `0.104005`, median `0.121826`, mae `0.104005`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.000656`, median `0.003757`, mae `0.015483`
- 5d: sample `8`, hit `0.625`, avg `0.000493`, median `0.007948`, mae `0.015148`
- 10d: sample `8`, hit `0.625`, avg `0.009459`, median `0.020334`, mae `0.018685`
- 20d: sample `8`, hit `0.875`, avg `0.047912`, median `0.058396`, mae `0.049233`
- 60d: sample `8`, hit `1.0`, avg `0.104005`, median `0.121826`, mae `0.104005`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.002573, 'median_return': 0.004542, 'mean_absolute_return': 0.01638, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.00505, 'median_return': 0.007948, 'mean_absolute_return': 0.01971, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.007943, 'median_return': 0.007751, 'mean_absolute_return': 0.027479, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.032868, 'median_return': 0.033704, 'mean_absolute_return': 0.044827, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.8625, 'avg_return': 0.081503, 'median_return': 0.098256, 'mean_absolute_return': 0.09181, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000656, 'median_return': 0.003757, 'mean_absolute_return': 0.015483, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.000493, 'median_return': 0.007948, 'mean_absolute_return': 0.015148, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009459, 'median_return': 0.020334, 'mean_absolute_return': 0.018685, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.032575}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.047912, 'median_return': 0.058396, 'mean_absolute_return': 0.049233, 'max_adverse_excursion': -0.005283, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.104005, 'median_return': 0.121826, 'mean_absolute_return': 0.104005, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002931, 'median_return': 0.004815, 'mean_absolute_return': 0.016479, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.005556, 'median_return': 0.008152, 'mean_absolute_return': 0.020217, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.007775, 'median_return': 0.006423, 'mean_absolute_return': 0.028457, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.031197, 'median_return': 0.033164, 'mean_absolute_return': 0.044337, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.8472, 'avg_return': 0.079003, 'median_return': 0.097048, 'mean_absolute_return': 0.090455, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5625}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.7875}, '60d': {'sample_size': 80, 'hit_rate': 0.8625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.05, 'both_hit': 27, 'both_miss': 13}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.025, 'both_hit': 27, 'both_miss': 13}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.1, 'both_hit': 25, 'both_miss': 15}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.7875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.225, 'both_hit': 34, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.8625, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.4, 'both_hit': 33, 'both_miss': 7}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.002573, 'median_return': 0.004542, 'mean_absolute_return': 0.01638, 'max_adverse_excursion': -0.038158, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.00505, 'median_return': 0.007948, 'mean_absolute_return': 0.01971, 'max_adverse_excursion': -0.046715, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.007943, 'median_return': 0.007751, 'mean_absolute_return': 0.027479, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.032868, 'median_return': 0.033704, 'mean_absolute_return': 0.044827, 'max_adverse_excursion': -0.075684, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.8625, 'avg_return': 0.081503, 'median_return': 0.098256, 'mean_absolute_return': 0.09181, 'max_adverse_excursion': -0.085385, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002742`, median `0.004542`, mae `0.015777`
- 5d: sample `40`, hit `0.575`, avg `0.005334`, median `0.008152`, mae `0.019944`
- 10d: sample `40`, hit `0.6`, avg `0.010075`, median `0.005356`, mae `0.025041`
- 20d: sample `40`, hit `0.9`, avg `0.042441`, median `0.033597`, mae `0.044784`
- 60d: sample `40`, hit `0.85`, avg `0.074569`, median `0.081673`, mae `0.085903`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.004657`, median `-0.002952`, mae `0.016668`
- 5d: sample `20`, hit `0.45`, avg `-0.00177`, median `-0.002452`, mae `0.018926`
- 10d: sample `20`, hit `0.5`, avg `-0.003199`, median `0.004306`, mae `0.035357`
- 20d: sample `20`, hit `0.55`, avg `0.005644`, median `0.026005`, mae `0.044994`
- 60d: sample `20`, hit `0.85`, avg `0.086992`, median `0.104804`, mae `0.097441`

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
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5625`, avg `0.002573`, median `0.004542`, mae `0.01638`
- 5d: sample `80`, hit `0.575`, avg `0.00505`, median `0.007948`, mae `0.01971`
- 10d: sample `80`, hit `0.6125`, avg `0.007943`, median `0.007751`, mae `0.027479`
- 20d: sample `80`, hit `0.7875`, avg `0.032868`, median `0.033704`, mae `0.044827`
- 60d: sample `80`, hit `0.8625`, avg `0.081503`, median `0.098256`, mae `0.09181`

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
