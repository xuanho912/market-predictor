# High Confidence Edge Report

Generated at: `2026-11-19T02:06:16.429967+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `204`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `204`, gate `stronger_evidence`
- 5d: completed `204`, gate `stronger_evidence`
- 10d: completed `204`, gate `stronger_evidence`
- 20d: completed `204`, gate `stronger_evidence`
- 60d: completed `204`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.525`, avg `0.002547`, median `0.002564`, mae `0.022056`
- 5d: sample `80`, hit `0.4875`, avg `0.00461`, median `-0.000667`, mae `0.025281`
- 10d: sample `80`, hit `0.5875`, avg `0.012618`, median `0.011064`, mae `0.040896`
- 20d: sample `80`, hit `0.75`, avg `0.033954`, median `0.042025`, mae `0.058161`
- 60d: sample `80`, hit `0.8625`, avg `0.100182`, median `0.10984`, mae `0.108557`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.000424`, median `0.007812`, mae `0.020703`
- 5d: sample `8`, hit `0.375`, avg `-0.005439`, median `-0.013064`, mae `0.022111`
- 10d: sample `8`, hit `0.375`, avg `-0.002607`, median `-0.004074`, mae `0.035526`
- 20d: sample `8`, hit `0.75`, avg `0.026848`, median `0.036029`, mae `0.036069`
- 60d: sample `8`, hit `0.875`, avg `0.109967`, median `0.134256`, mae `0.118234`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.000592`, median `0.007101`, mae `0.020022`
- 5d: sample `8`, hit `0.25`, avg `-0.000855`, median `-0.00697`, mae `0.024772`
- 10d: sample `8`, hit `0.5`, avg `0.015397`, median `0.015974`, mae `0.030264`
- 20d: sample `8`, hit `0.875`, avg `0.047328`, median `0.060823`, mae `0.063047`
- 60d: sample `8`, hit `1.0`, avg `0.106961`, median `0.121434`, mae `0.106961`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000592, 'median_return': 0.007101, 'mean_absolute_return': 0.020022, 'max_adverse_excursion': -0.029317, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.000855, 'median_return': -0.00697, 'mean_absolute_return': 0.024772, 'max_adverse_excursion': -0.037174, 'max_favorable_excursion': 0.048375}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.015397, 'median_return': 0.015974, 'mean_absolute_return': 0.030264, 'max_adverse_excursion': -0.031484, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.047328, 'median_return': 0.060823, 'mean_absolute_return': 0.063047, 'max_adverse_excursion': -0.062877, 'max_favorable_excursion': 0.092742}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.106961, 'median_return': 0.121434, 'mean_absolute_return': 0.106961, 'max_adverse_excursion': 0.034922, 'max_favorable_excursion': 0.156899}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.002764, 'median_return': 0.002564, 'mean_absolute_return': 0.022282, 'max_adverse_excursion': -0.078197, 'max_favorable_excursion': 0.069923}, '5d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.005217, 'median_return': 0.00246, 'mean_absolute_return': 0.025338, 'max_adverse_excursion': -0.041867, 'max_favorable_excursion': 0.085723}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.01231, 'median_return': 0.011064, 'mean_absolute_return': 0.042077, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.125958}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.032469, 'median_return': 0.039455, 'mean_absolute_return': 0.057618, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.177814}, '60d': {'sample_size': 72, 'hit_rate': 0.8472, 'avg_return': 0.099429, 'median_return': 0.108121, 'mean_absolute_return': 0.108735, 'max_adverse_excursion': -0.065523, 'max_favorable_excursion': 0.283191}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.4125}, '20d': {'sample_size': 80, 'hit_rate': 0.25}, '60d': {'sample_size': 80, 'hit_rate': 0.1375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.25, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.5, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.1375, 'secondary_hit_rate': 0.8625, 'primary_minus_secondary': -0.725, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.005522, 'median_return': 0.007812, 'mean_absolute_return': 0.027658, 'max_adverse_excursion': -0.078197, 'max_favorable_excursion': 0.069923}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.001847, 'median_return': 0.000889, 'mean_absolute_return': 0.029209, 'max_adverse_excursion': -0.041867, 'max_favorable_excursion': 0.085723}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.01106, 'median_return': 0.016256, 'mean_absolute_return': 0.045709, 'max_adverse_excursion': -0.071498, 'max_favorable_excursion': 0.121489}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.028878, 'median_return': 0.040527, 'mean_absolute_return': 0.051124, 'max_adverse_excursion': -0.066154, 'max_favorable_excursion': 0.143149}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.09058, 'median_return': 0.123132, 'mean_absolute_return': 0.113394, 'max_adverse_excursion': -0.065523, 'max_favorable_excursion': 0.247486}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.001556, 'median_return': 0.000675, 'mean_absolute_return': 0.020189, 'max_adverse_excursion': -0.076776, 'max_favorable_excursion': 0.047825}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.005531, 'median_return': -0.000667, 'mean_absolute_return': 0.023972, 'max_adverse_excursion': -0.040197, 'max_favorable_excursion': 0.06431}, '10d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.013138, 'median_return': 0.011064, 'mean_absolute_return': 0.039291, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.125958}, '20d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.035647, 'median_return': 0.04796, 'mean_absolute_return': 0.060507, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.177814}, '60d': {'sample_size': 60, 'hit_rate': 0.9, 'avg_return': 0.103383, 'median_return': 0.108121, 'mean_absolute_return': 0.106945, 'max_adverse_excursion': -0.037053, 'max_favorable_excursion': 0.283191}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.003598`, median `0.002581`, mae `0.022933`
- 5d: sample `40`, hit `0.475`, avg `0.001849`, median `-0.002406`, mae `0.025819`
- 10d: sample `40`, hit `0.525`, avg `0.009293`, median `0.015799`, mae `0.03957`
- 20d: sample `40`, hit `0.725`, avg `0.027363`, median `0.040527`, mae `0.054131`
- 60d: sample `40`, hit `0.825`, avg `0.085746`, median `0.110811`, mae `0.099419`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `0.001556`, median `0.000675`, mae `0.020189`
- 5d: sample `60`, hit `0.4833`, avg `0.005531`, median `-0.000667`, mae `0.023972`
- 10d: sample `60`, hit `0.6`, avg `0.013138`, median `0.011064`, mae `0.039291`
- 20d: sample `60`, hit `0.7667`, avg `0.035647`, median `0.04796`, mae `0.060507`
- 60d: sample `60`, hit `0.9`, avg `0.103383`, median `0.108121`, mae `0.106945`

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
- 3d: sample `60`, hit `0.5167`, avg `0.001556`, median `0.000675`, mae `0.020189`
- 5d: sample `60`, hit `0.4833`, avg `0.005531`, median `-0.000667`, mae `0.023972`
- 10d: sample `60`, hit `0.6`, avg `0.013138`, median `0.011064`, mae `0.039291`
- 20d: sample `60`, hit `0.7667`, avg `0.035647`, median `0.04796`, mae `0.060507`
- 60d: sample `60`, hit `0.9`, avg `0.103383`, median `0.108121`, mae `0.106945`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.003598`, median `0.002581`, mae `0.022933`
- 5d: sample `40`, hit `0.475`, avg `0.001849`, median `-0.002406`, mae `0.025819`
- 10d: sample `40`, hit `0.525`, avg `0.009293`, median `0.015799`, mae `0.03957`
- 20d: sample `40`, hit `0.725`, avg `0.027363`, median `0.040527`, mae `0.054131`
- 60d: sample `40`, hit `0.825`, avg `0.085746`, median `0.110811`, mae `0.099419`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.002547`, median `0.002564`, mae `0.022056`
- 5d: sample `80`, hit `0.4875`, avg `0.00461`, median `-0.000667`, mae `0.025281`
- 10d: sample `80`, hit `0.5875`, avg `0.012618`, median `0.011064`, mae `0.040896`
- 20d: sample `80`, hit `0.75`, avg `0.033954`, median `0.042025`, mae `0.058161`
- 60d: sample `80`, hit `0.8625`, avg `0.100182`, median `0.10984`, mae `0.108557`

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
- 3d: sample `80`, hit `0.525`, avg `0.002547`, median `0.002564`, mae `0.022056`
- 5d: sample `80`, hit `0.4875`, avg `0.00461`, median `-0.000667`, mae `0.025281`
- 10d: sample `80`, hit `0.5875`, avg `0.012618`, median `0.011064`, mae `0.040896`
- 20d: sample `80`, hit `0.75`, avg `0.033954`, median `0.042025`, mae `0.058161`
- 60d: sample `80`, hit `0.8625`, avg `0.100182`, median `0.10984`, mae `0.108557`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
