# High Confidence Edge Report

Generated at: `2026-11-06T19:27:59.553312+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `172`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `172`, gate `stronger_evidence`
- 5d: completed `172`, gate `stronger_evidence`
- 10d: completed `172`, gate `stronger_evidence`
- 20d: completed `172`, gate `stronger_evidence`
- 60d: completed `172`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.65`, avg `0.004984`, median `0.010078`, mae `0.020445`
- 5d: sample `80`, hit `0.625`, avg `0.009424`, median `0.01371`, mae `0.026649`
- 10d: sample `80`, hit `0.65`, avg `0.01336`, median `0.023889`, mae `0.042962`
- 20d: sample `80`, hit `0.7125`, avg `0.027491`, median `0.042025`, mae `0.05727`
- 60d: sample `80`, hit `0.8125`, avg `0.04898`, median `0.072365`, mae `0.082398`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.005652`, median `0.013309`, mae `0.016317`
- 5d: sample `8`, hit `0.625`, avg `0.007707`, median `0.012625`, mae `0.019323`
- 10d: sample `8`, hit `0.5`, avg `0.009064`, median `0.006878`, mae `0.027861`
- 20d: sample `8`, hit `0.75`, avg `0.027152`, median `0.029234`, mae `0.035404`
- 60d: sample `8`, hit `0.875`, avg `0.04327`, median `0.043989`, mae `0.052534`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.017723`, median `0.028886`, mae `0.026407`
- 5d: sample `8`, hit `0.875`, avg `0.01833`, median `0.014974`, mae `0.020467`
- 10d: sample `8`, hit `0.625`, avg `0.012889`, median `0.038296`, mae `0.051153`
- 20d: sample `8`, hit `0.75`, avg `0.011016`, median `0.028264`, mae `0.065331`
- 60d: sample `8`, hit `0.875`, avg `0.056559`, median `0.068318`, mae `0.069897`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.017723, 'median_return': 0.028886, 'mean_absolute_return': 0.026407, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.01833, 'median_return': 0.014974, 'mean_absolute_return': 0.020467, 'max_adverse_excursion': -0.00855, 'max_favorable_excursion': 0.044138}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.012889, 'median_return': 0.038296, 'mean_absolute_return': 0.051153, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.076904}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011016, 'median_return': 0.028264, 'mean_absolute_return': 0.065331, 'max_adverse_excursion': -0.207737, 'max_favorable_excursion': 0.085922}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.056559, 'median_return': 0.068318, 'mean_absolute_return': 0.069897, 'max_adverse_excursion': -0.053355, 'max_favorable_excursion': 0.105209}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.003568, 'median_return': 0.007915, 'mean_absolute_return': 0.019782, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.045561}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.008434, 'median_return': 0.012762, 'mean_absolute_return': 0.027335, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.013412, 'median_return': 0.023525, 'mean_absolute_return': 0.042052, 'max_adverse_excursion': -0.124781, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.029321, 'median_return': 0.050841, 'mean_absolute_return': 0.056375, 'max_adverse_excursion': -0.174323, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.048138, 'median_return': 0.072891, 'mean_absolute_return': 0.083786, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.179244}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.35}, '5d': {'sample_size': 80, 'hit_rate': 0.375}, '10d': {'sample_size': 80, 'hit_rate': 0.3375}, '20d': {'sample_size': 80, 'hit_rate': 0.2875}, '60d': {'sample_size': 80, 'hit_rate': 0.1875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.35, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.3125, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.2875, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.425, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_minus_secondary': -0.625, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.008055, 'median_return': 0.011103, 'mean_absolute_return': 0.018396, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.049499}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.011187, 'median_return': 0.012762, 'mean_absolute_return': 0.019179, 'max_adverse_excursion': -0.025448, 'max_favorable_excursion': 0.044138}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.015658, 'median_return': 0.017689, 'mean_absolute_return': 0.032168, 'max_adverse_excursion': -0.11923, 'max_favorable_excursion': 0.076904}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.029489, 'median_return': 0.035918, 'mean_absolute_return': 0.047678, 'max_adverse_excursion': -0.207737, 'max_favorable_excursion': 0.096037}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.059473, 'median_return': 0.072365, 'mean_absolute_return': 0.068801, 'max_adverse_excursion': -0.076188, 'max_favorable_excursion': 0.136738}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.001912, 'median_return': 0.007911, 'mean_absolute_return': 0.022494, 'max_adverse_excursion': -0.083565, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.007661, 'median_return': 0.017466, 'mean_absolute_return': 0.034118, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.011061, 'median_return': 0.034539, 'mean_absolute_return': 0.053755, 'max_adverse_excursion': -0.124781, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.025493, 'median_return': 0.052608, 'mean_absolute_return': 0.066863, 'max_adverse_excursion': -0.174323, 'max_favorable_excursion': 0.124329}, '60d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.038487, 'median_return': 0.082244, 'mean_absolute_return': 0.095994, 'max_adverse_excursion': -0.324011, 'max_favorable_excursion': 0.179244}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.00362`, median `0.007915`, mae `0.02055`
- 5d: sample `60`, hit `0.5833`, avg `0.003719`, median `0.011065`, mae `0.025204`
- 10d: sample `60`, hit `0.6`, avg `0.007698`, median `0.011842`, mae `0.038729`
- 20d: sample `60`, hit `0.6833`, avg `0.021181`, median `0.029234`, mae `0.053203`
- 60d: sample `60`, hit `0.8167`, avg `0.044208`, median `0.067623`, mae `0.073254`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009075`, median `0.011957`, mae `0.02013`
- 5d: sample `20`, hit `0.75`, avg `0.026537`, median `0.030262`, mae `0.030981`
- 10d: sample `20`, hit `0.8`, avg `0.030343`, median `0.049918`, mae `0.055659`
- 20d: sample `20`, hit `0.8`, avg `0.04642`, median `0.069372`, mae `0.069474`
- 60d: sample `20`, hit `0.8`, avg `0.063296`, median `0.087843`, mae `0.109827`

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
- 3d: sample `20`, hit `0.75`, avg `0.009075`, median `0.011957`, mae `0.02013`
- 5d: sample `20`, hit `0.75`, avg `0.026537`, median `0.030262`, mae `0.030981`
- 10d: sample `20`, hit `0.8`, avg `0.030343`, median `0.049918`, mae `0.055659`
- 20d: sample `20`, hit `0.8`, avg `0.04642`, median `0.069372`, mae `0.069474`
- 60d: sample `20`, hit `0.8`, avg `0.063296`, median `0.087843`, mae `0.109827`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.008055`, median `0.011103`, mae `0.018396`
- 5d: sample `40`, hit `0.625`, avg `0.011187`, median `0.012762`, mae `0.019179`
- 10d: sample `40`, hit `0.6`, avg `0.015658`, median `0.017689`, mae `0.032168`
- 20d: sample `40`, hit `0.8`, avg `0.029489`, median `0.035918`, mae `0.047678`
- 60d: sample `40`, hit `0.875`, avg `0.059473`, median `0.072365`, mae `0.068801`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.005252`, median `0.005555`, mae `0.024858`
- 5d: sample `20`, hit `0.5`, avg `-0.011216`, median `0.004484`, mae `0.037256`
- 10d: sample `20`, hit `0.6`, avg `-0.008221`, median `0.011842`, mae `0.051852`
- 20d: sample `20`, hit `0.45`, avg `0.004565`, median `-0.004875`, mae `0.064251`
- 60d: sample `20`, hit `0.7`, avg `0.013678`, median `0.030649`, mae `0.082162`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6833`, avg `0.008395`, median `0.011636`, mae `0.018974`
- 5d: sample `60`, hit `0.6667`, avg `0.016303`, median `0.014974`, mae `0.023113`
- 10d: sample `60`, hit `0.6667`, avg `0.020553`, median `0.029984`, mae `0.039998`
- 20d: sample `60`, hit `0.8`, avg `0.035133`, median `0.052608`, mae `0.054944`
- 60d: sample `60`, hit `0.85`, avg `0.060748`, median `0.074922`, mae `0.082476`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.65`, avg `0.004984`, median `0.010078`, mae `0.020445`
- 5d: sample `80`, hit `0.625`, avg `0.009424`, median `0.01371`, mae `0.026649`
- 10d: sample `80`, hit `0.65`, avg `0.01336`, median `0.023889`, mae `0.042962`
- 20d: sample `80`, hit `0.7125`, avg `0.027491`, median `0.042025`, mae `0.05727`
- 60d: sample `80`, hit `0.8125`, avg `0.04898`, median `0.072365`, mae `0.082398`

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
- 3d: sample `80`, hit `0.65`, avg `0.004984`, median `0.010078`, mae `0.020445`
- 5d: sample `80`, hit `0.625`, avg `0.009424`, median `0.01371`, mae `0.026649`
- 10d: sample `80`, hit `0.65`, avg `0.01336`, median `0.023889`, mae `0.042962`
- 20d: sample `80`, hit `0.7125`, avg `0.027491`, median `0.042025`, mae `0.05727`
- 60d: sample `80`, hit `0.8125`, avg `0.04898`, median `0.072365`, mae `0.082398`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
