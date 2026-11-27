# High Confidence Edge Report

Generated at: `2026-11-27T04:57:43.797483+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `224`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `224`, gate `stronger_evidence`
- 5d: completed `224`, gate `stronger_evidence`
- 10d: completed `224`, gate `stronger_evidence`
- 20d: completed `224`, gate `stronger_evidence`
- 60d: completed `224`, gate `stronger_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.003264`, median `0.007316`, mae `0.021376`
- 5d: sample `80`, hit `0.5875`, avg `0.006045`, median `0.004641`, mae `0.026856`
- 10d: sample `80`, hit `0.625`, avg `0.007305`, median `0.009326`, mae `0.037568`
- 20d: sample `80`, hit `0.575`, avg `-0.001093`, median `0.007017`, mae `0.051178`
- 60d: sample `80`, hit `0.7625`, avg `0.04771`, median `0.067623`, mae `0.086485`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.003275`, median `-0.00201`, mae `0.012932`
- 5d: sample `8`, hit `0.375`, avg `-0.000897`, median `-0.002248`, mae `0.010419`
- 10d: sample `8`, hit `0.5`, avg `-0.005409`, median `0.009326`, mae `0.034956`
- 20d: sample `8`, hit `0.375`, avg `-0.027077`, median `-0.001131`, mae `0.04837`
- 60d: sample `8`, hit `0.75`, avg `0.042088`, median `0.067623`, mae `0.057226`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.003275`, median `-0.00201`, mae `0.012932`
- 5d: sample `8`, hit `0.375`, avg `-0.000897`, median `-0.002248`, mae `0.010419`
- 10d: sample `8`, hit `0.5`, avg `-0.005409`, median `0.009326`, mae `0.034956`
- 20d: sample `8`, hit `0.375`, avg `-0.027077`, median `-0.001131`, mae `0.04837`
- 60d: sample `8`, hit `0.75`, avg `0.042088`, median `0.067623`, mae `0.057226`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.003275, 'median_return': -0.00201, 'mean_absolute_return': 0.012932, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.031732}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.000897, 'median_return': -0.002248, 'mean_absolute_return': 0.010419, 'max_adverse_excursion': -0.021415, 'max_favorable_excursion': 0.020014}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.005409, 'median_return': 0.009326, 'mean_absolute_return': 0.034956, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.027077, 'median_return': -0.001131, 'mean_absolute_return': 0.04837, 'max_adverse_excursion': -0.207737, 'max_favorable_excursion': 0.033017}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.042088, 'median_return': 0.067623, 'mean_absolute_return': 0.057226, 'max_adverse_excursion': -0.053355, 'max_favorable_excursion': 0.075552}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003991, 'median_return': 0.008937, 'mean_absolute_return': 0.022314, 'max_adverse_excursion': -0.070162, 'max_favorable_excursion': 0.054095}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.006816, 'median_return': 0.005082, 'mean_absolute_return': 0.028682, 'max_adverse_excursion': -0.160884, 'max_favorable_excursion': 0.083508}, '10d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.008717, 'median_return': 0.011842, 'mean_absolute_return': 0.037858, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.123482}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.001794, 'median_return': 0.008672, 'mean_absolute_return': 0.05149, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.136797}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.048334, 'median_return': 0.068046, 'mean_absolute_return': 0.089736, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.355869}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.425}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.3625}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.2375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.2625, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2375, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': -0.525, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.003084, 'median_return': 0.004243, 'mean_absolute_return': 0.013972, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.034529}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.000496, 'median_return': -0.002248, 'mean_absolute_return': 0.013909, 'max_adverse_excursion': -0.032974, 'max_favorable_excursion': 0.036358}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.001232, 'median_return': -0.001663, 'mean_absolute_return': 0.023336, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.003948, 'median_return': 0.024382, 'mean_absolute_return': 0.035669, 'max_adverse_excursion': -0.207737, 'max_favorable_excursion': 0.080933}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.064268, 'median_return': 0.072891, 'mean_absolute_return': 0.070323, 'max_adverse_excursion': -0.053355, 'max_favorable_excursion': 0.109145}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.003324, 'median_return': 0.008937, 'mean_absolute_return': 0.023843, 'max_adverse_excursion': -0.070162, 'max_favorable_excursion': 0.054095}, '5d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.007894, 'median_return': 0.005082, 'mean_absolute_return': 0.031172, 'max_adverse_excursion': -0.160884, 'max_favorable_excursion': 0.083508}, '10d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.01015, 'median_return': 0.014392, 'mean_absolute_return': 0.042312, 'max_adverse_excursion': -0.139978, 'max_favorable_excursion': 0.123482}, '20d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.002773, 'median_return': 0.005859, 'mean_absolute_return': 0.056348, 'max_adverse_excursion': -0.302412, 'max_favorable_excursion': 0.136797}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.04219, 'median_return': 0.058024, 'mean_absolute_return': 0.091872, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.355869}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.001175`, median `0.004243`, mae `0.019501`
- 5d: sample `60`, hit `0.5333`, avg `0.003097`, median `0.004338`, mae `0.020956`
- 10d: sample `60`, hit `0.55`, avg `0.000218`, median `0.004301`, mae `0.033869`
- 20d: sample `60`, hit `0.6167`, avg `-0.002794`, median `0.012394`, mae `0.049501`
- 60d: sample `60`, hit `0.8`, avg `0.049059`, median `0.065834`, mae `0.080867`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009532`, median `0.018961`, mae `0.027`
- 5d: sample `20`, hit `0.75`, avg `0.014889`, median `0.033669`, mae `0.044557`
- 10d: sample `20`, hit `0.85`, avg `0.028566`, median `0.048567`, mae `0.048664`
- 20d: sample `20`, hit `0.45`, avg `0.00401`, median `-0.012594`, mae `0.056211`
- 60d: sample `20`, hit `0.65`, avg `0.043661`, median `0.10011`, mae `0.103338`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009532`, median `0.018961`, mae `0.027`
- 5d: sample `20`, hit `0.75`, avg `0.014889`, median `0.033669`, mae `0.044557`
- 10d: sample `20`, hit `0.85`, avg `0.028566`, median `0.048567`, mae `0.048664`
- 20d: sample `20`, hit `0.45`, avg `0.00401`, median `-0.012594`, mae `0.056211`
- 60d: sample `20`, hit `0.65`, avg `0.043661`, median `0.10011`, mae `0.103338`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.001374`, median `0.003885`, mae `0.016422`
- 5d: sample `40`, hit `0.5`, avg `0.001519`, median `0.004263`, mae `0.016513`
- 10d: sample `40`, hit `0.525`, avg `-0.001744`, median `0.002478`, mae `0.026737`
- 20d: sample `40`, hit `0.65`, avg `0.000207`, median `0.024382`, mae `0.04226`
- 60d: sample `40`, hit `0.85`, avg `0.050806`, median `0.068046`, mae `0.066343`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000776`, median `0.007812`, mae `0.025658`
- 5d: sample `20`, hit `0.6`, avg `0.006253`, median `0.004527`, mae `0.029841`
- 10d: sample `20`, hit `0.6`, avg `0.004141`, median `0.011842`, mae `0.048133`
- 20d: sample `20`, hit `0.55`, avg `-0.008797`, median `0.005859`, mae `0.063983`
- 60d: sample `20`, hit `0.7`, avg `0.045566`, median `0.033378`, mae `0.109914`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.575`, avg `0.003264`, median `0.007316`, mae `0.021376`
- 5d: sample `80`, hit `0.5875`, avg `0.006045`, median `0.004641`, mae `0.026856`
- 10d: sample `80`, hit `0.625`, avg `0.007305`, median `0.009326`, mae `0.037568`
- 20d: sample `80`, hit `0.575`, avg `-0.001093`, median `0.007017`, mae `0.051178`
- 60d: sample `80`, hit `0.7625`, avg `0.04771`, median `0.067623`, mae `0.086485`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.003264`, median `0.007316`, mae `0.021376`
- 5d: sample `80`, hit `0.5875`, avg `0.006045`, median `0.004641`, mae `0.026856`
- 10d: sample `80`, hit `0.625`, avg `0.007305`, median `0.009326`, mae `0.037568`
- 20d: sample `80`, hit `0.575`, avg `-0.001093`, median `0.007017`, mae `0.051178`
- 60d: sample `80`, hit `0.7625`, avg `0.04771`, median `0.067623`, mae `0.086485`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.003264`, median `0.007316`, mae `0.021376`
- 5d: sample `80`, hit `0.5875`, avg `0.006045`, median `0.004641`, mae `0.026856`
- 10d: sample `80`, hit `0.625`, avg `0.007305`, median `0.009326`, mae `0.037568`
- 20d: sample `80`, hit `0.575`, avg `-0.001093`, median `0.007017`, mae `0.051178`
- 60d: sample `80`, hit `0.7625`, avg `0.04771`, median `0.067623`, mae `0.086485`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
