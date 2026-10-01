# High Confidence Edge Report

Generated at: `2026-10-01T18:27:23.428816+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `68`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `68`, gate `moderate_evidence`
- 5d: completed `68`, gate `moderate_evidence`
- 10d: completed `68`, gate `moderate_evidence`
- 20d: completed `68`, gate `moderate_evidence`
- 60d: completed `68`, gate `moderate_evidence`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.003355`, median `-0.001658`, mae `0.015599`
- 5d: sample `40`, hit `0.45`, avg `-0.009102`, median `-0.003262`, mae `0.018575`
- 10d: sample `40`, hit `0.475`, avg `-0.006908`, median `-0.0004`, mae `0.022261`
- 20d: sample `40`, hit `0.6`, avg `0.002733`, median `0.015725`, mae `0.040098`
- 60d: sample `40`, hit `0.8`, avg `0.035371`, median `0.044683`, mae `0.072668`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.006456`, median `-0.003995`, mae `0.017074`
- 5d: sample `40`, hit `0.425`, avg `-0.006823`, median `-0.005632`, mae `0.020993`
- 10d: sample `40`, hit `0.525`, avg `-0.00628`, median `0.003815`, mae `0.031914`
- 20d: sample `40`, hit `0.525`, avg `0.003909`, median `0.001515`, mae `0.047051`
- 60d: sample `40`, hit `0.825`, avg `0.066977`, median `0.084216`, mae `0.085036`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.001368`, median `0.004068`, mae `0.013065`
- 5d: sample `8`, hit `0.625`, avg `-0.001273`, median `0.001479`, mae `0.010447`
- 10d: sample `8`, hit `0.5`, avg `0.006154`, median `0.012066`, mae `0.014225`
- 20d: sample `8`, hit `0.875`, avg `0.028741`, median `0.033164`, mae `0.029518`
- 60d: sample `8`, hit `0.875`, avg `0.037695`, median `0.05019`, mae `0.048747`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.001368`, median `0.004068`, mae `0.013065`
- 5d: sample `8`, hit `0.625`, avg `-0.001273`, median `0.001479`, mae `0.010447`
- 10d: sample `8`, hit `0.5`, avg `0.006154`, median `0.012066`, mae `0.014225`
- 20d: sample `8`, hit `0.875`, avg `0.028741`, median `0.033164`, mae `0.029518`
- 60d: sample `8`, hit `0.875`, avg `0.037695`, median `0.05019`, mae `0.048747`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001368, 'median_return': 0.004068, 'mean_absolute_return': 0.013065, 'max_adverse_excursion': -0.031857, 'max_favorable_excursion': 0.022103}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001273, 'median_return': 0.001479, 'mean_absolute_return': 0.010447, 'max_adverse_excursion': -0.026896, 'max_favorable_excursion': 0.013193}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.006154, 'median_return': 0.012066, 'mean_absolute_return': 0.014225, 'max_adverse_excursion': -0.01411, 'max_favorable_excursion': 0.035913}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.028741, 'median_return': 0.033164, 'mean_absolute_return': 0.029518, 'max_adverse_excursion': -0.003108, 'max_favorable_excursion': 0.059335}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.037695, 'median_return': 0.05019, 'mean_absolute_return': 0.048747, 'max_adverse_excursion': -0.044207, 'max_favorable_excursion': 0.075909}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.005603, 'median_return': -0.003676, 'mean_absolute_return': 0.0167, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': -0.008706, 'median_return': -0.007994, 'mean_absolute_return': 0.020821, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.034453}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.00801, 'median_return': 0.000397, 'mean_absolute_return': 0.028517, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.000497, 'median_return': 0.005106, 'mean_absolute_return': 0.045137, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.052672, 'median_return': 0.065995, 'mean_absolute_return': 0.082197, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.167846}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.1875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1875, 'secondary_hit_rate': 0.8125, 'primary_minus_secondary': -0.625, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.004906, 'median_return': -0.003649, 'mean_absolute_return': 0.016337, 'max_adverse_excursion': -0.071222, 'max_favorable_excursion': 0.033159}, '5d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.007962, 'median_return': -0.005632, 'mean_absolute_return': 0.019784, 'max_adverse_excursion': -0.069614, 'max_favorable_excursion': 0.034453}, '10d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.006594, 'median_return': 0.000397, 'mean_absolute_return': 0.027088, 'max_adverse_excursion': -0.085905, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.003321, 'median_return': 0.013156, 'mean_absolute_return': 0.043575, 'max_adverse_excursion': -0.162095, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 80, 'hit_rate': 0.8125, 'avg_return': 0.051174, 'median_return': 0.059131, 'mean_absolute_return': 0.078852, 'max_adverse_excursion': -0.146095, 'max_favorable_excursion': 0.167846}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.425`, avg `-0.004906`, median `-0.003649`, mae `0.016337`
- 5d: sample `80`, hit `0.4375`, avg `-0.007962`, median `-0.005632`, mae `0.019784`
- 10d: sample `80`, hit `0.5`, avg `-0.006594`, median `0.000397`, mae `0.027088`
- 20d: sample `80`, hit `0.5625`, avg `0.003321`, median `0.013156`, mae `0.043575`
- 60d: sample `80`, hit `0.8125`, avg `0.051174`, median `0.059131`, mae `0.078852`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.425`, avg `-0.004906`, median `-0.003649`, mae `0.016337`
- 5d: sample `80`, hit `0.4375`, avg `-0.007962`, median `-0.005632`, mae `0.019784`
- 10d: sample `80`, hit `0.5`, avg `-0.006594`, median `0.000397`, mae `0.027088`
- 20d: sample `80`, hit `0.5625`, avg `0.003321`, median `0.013156`, mae `0.043575`
- 60d: sample `80`, hit `0.8125`, avg `0.051174`, median `0.059131`, mae `0.078852`

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
- 3d: sample `80`, hit `0.425`, avg `-0.004906`, median `-0.003649`, mae `0.016337`
- 5d: sample `80`, hit `0.4375`, avg `-0.007962`, median `-0.005632`, mae `0.019784`
- 10d: sample `80`, hit `0.5`, avg `-0.006594`, median `0.000397`, mae `0.027088`
- 20d: sample `80`, hit `0.5625`, avg `0.003321`, median `0.013156`, mae `0.043575`
- 60d: sample `80`, hit `0.8125`, avg `0.051174`, median `0.059131`, mae `0.078852`

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
- 3d: sample `80`, hit `0.425`, avg `-0.004906`, median `-0.003649`, mae `0.016337`
- 5d: sample `80`, hit `0.4375`, avg `-0.007962`, median `-0.005632`, mae `0.019784`
- 10d: sample `80`, hit `0.5`, avg `-0.006594`, median `0.000397`, mae `0.027088`
- 20d: sample `80`, hit `0.5625`, avg `0.003321`, median `0.013156`, mae `0.043575`
- 60d: sample `80`, hit `0.8125`, avg `0.051174`, median `0.059131`, mae `0.078852`

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
