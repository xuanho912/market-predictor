# High Confidence Edge Report

Generated at: `2026-10-15T17:04:55.248121+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `108`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `108`, gate `stronger_evidence`
- 5d: completed `108`, gate `stronger_evidence`
- 10d: completed `108`, gate `stronger_evidence`
- 20d: completed `108`, gate `stronger_evidence`
- 60d: completed `108`, gate `stronger_evidence`

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
- 3d: sample `40`, hit `0.5`, avg `-0.006154`, median `0.000603`, mae `0.014978`
- 5d: sample `40`, hit `0.45`, avg `-0.007931`, median `-0.006464`, mae `0.016925`
- 10d: sample `40`, hit `0.425`, avg `-0.00322`, median `-0.005891`, mae `0.019075`
- 20d: sample `40`, hit `0.625`, avg `0.018069`, median `0.021759`, mae `0.029475`
- 60d: sample `40`, hit `0.7`, avg `0.038638`, median `0.059104`, mae `0.066107`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.008494`, median `-0.009843`, mae `0.017046`
- 5d: sample `40`, hit `0.35`, avg `-0.009782`, median `-0.013229`, mae `0.021067`
- 10d: sample `40`, hit `0.35`, avg `-0.012118`, median `-0.015101`, mae `0.029558`
- 20d: sample `40`, hit `0.6`, avg `0.01562`, median `0.015713`, mae `0.036246`
- 60d: sample `40`, hit `0.85`, avg `0.072205`, median `0.079528`, mae `0.088375`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.002903`, median `0.001405`, mae `0.009668`
- 5d: sample `8`, hit `0.5`, avg `-0.006121`, median `0.000688`, mae `0.014627`
- 10d: sample `8`, hit `0.5`, avg `-0.006253`, median `0.000197`, mae `0.012124`
- 20d: sample `8`, hit `0.5`, avg `0.014079`, median `0.01927`, mae `0.023566`
- 60d: sample `8`, hit `0.625`, avg `0.021077`, median `0.053855`, mae `0.043847`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.002903`, median `0.001405`, mae `0.009668`
- 5d: sample `8`, hit `0.5`, avg `-0.006121`, median `0.000688`, mae `0.014627`
- 10d: sample `8`, hit `0.5`, avg `-0.006253`, median `0.000197`, mae `0.012124`
- 20d: sample `8`, hit `0.5`, avg `0.014079`, median `0.01927`, mae `0.023566`
- 60d: sample `8`, hit `0.625`, avg `0.021077`, median `0.053855`, mae `0.043847`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.002903, 'median_return': 0.001405, 'mean_absolute_return': 0.009668, 'max_adverse_excursion': -0.029438, 'max_favorable_excursion': 0.010897}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006121, 'median_return': 0.000688, 'mean_absolute_return': 0.014627, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.018625}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006253, 'median_return': 0.000197, 'mean_absolute_return': 0.012124, 'max_adverse_excursion': -0.025298, 'max_favorable_excursion': 0.017201}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.014079, 'median_return': 0.01927, 'mean_absolute_return': 0.023566, 'max_adverse_excursion': -0.016058, 'max_favorable_excursion': 0.046563}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.021077, 'median_return': 0.053855, 'mean_absolute_return': 0.043847, 'max_adverse_excursion': -0.046594, 'max_favorable_excursion': 0.059948}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.007815, 'median_return': -0.007083, 'mean_absolute_return': 0.016717, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': -0.009161, 'median_return': -0.011925, 'mean_absolute_return': 0.019481, 'max_adverse_excursion': -0.04605, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.007826, 'median_return': -0.010145, 'mean_absolute_return': 0.025671, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.017151, 'median_return': 0.020226, 'mean_absolute_return': 0.033893, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.059238, 'median_return': 0.074296, 'mean_absolute_return': 0.080951, 'max_adverse_excursion': -0.12745, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.275, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.003122, 'median_return': 0.001405, 'mean_absolute_return': 0.012269, 'max_adverse_excursion': -0.03413, 'max_favorable_excursion': 0.023395}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.004238, 'median_return': 0.000688, 'mean_absolute_return': 0.014617, 'max_adverse_excursion': -0.033868, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.001521, 'median_return': 0.000197, 'mean_absolute_return': 0.019594, 'max_adverse_excursion': -0.038784, 'max_favorable_excursion': 0.035901}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.01514, 'median_return': 0.01927, 'mean_absolute_return': 0.023087, 'max_adverse_excursion': -0.02849, 'max_favorable_excursion': 0.053054}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.029024, 'median_return': 0.053855, 'mean_absolute_return': 0.050254, 'max_adverse_excursion': -0.049378, 'max_favorable_excursion': 0.098228}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.35, 'avg_return': -0.008725, 'median_return': -0.009843, 'mean_absolute_return': 0.01726, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.010397, 'median_return': -0.013987, 'mean_absolute_return': 0.020456, 'max_adverse_excursion': -0.04605, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 60, 'hit_rate': 0.35, 'avg_return': -0.009718, 'median_return': -0.011432, 'mean_absolute_return': 0.02589, 'max_adverse_excursion': -0.060434, 'max_favorable_excursion': 0.093249}, '20d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.017412, 'median_return': 0.02093, 'mean_absolute_return': 0.036118, 'max_adverse_excursion': -0.077689, 'max_favorable_excursion': 0.110633}, '60d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.064221, 'median_return': 0.077304, 'mean_absolute_return': 0.086237, 'max_adverse_excursion': -0.12745, 'max_favorable_excursion': 0.19082}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.006154`, median `0.000603`, mae `0.014978`
- 5d: sample `40`, hit `0.45`, avg `-0.007931`, median `-0.006464`, mae `0.016925`
- 10d: sample `40`, hit `0.425`, avg `-0.00322`, median `-0.005891`, mae `0.019075`
- 20d: sample `40`, hit `0.625`, avg `0.018069`, median `0.021759`, mae `0.029475`
- 60d: sample `40`, hit `0.7`, avg `0.038638`, median `0.059104`, mae `0.066107`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.008494`, median `-0.009843`, mae `0.017046`
- 5d: sample `40`, hit `0.35`, avg `-0.009782`, median `-0.013229`, mae `0.021067`
- 10d: sample `40`, hit `0.35`, avg `-0.012118`, median `-0.015101`, mae `0.029558`
- 20d: sample `40`, hit `0.6`, avg `0.01562`, median `0.015713`, mae `0.036246`
- 60d: sample `40`, hit `0.85`, avg `0.072205`, median `0.079528`, mae `0.088375`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003122`, median `0.001405`, mae `0.012269`
- 5d: sample `20`, hit `0.5`, avg `-0.004238`, median `0.000688`, mae `0.014617`
- 10d: sample `20`, hit `0.5`, avg `-0.001521`, median `0.000197`, mae `0.019594`
- 20d: sample `20`, hit `0.6`, avg `0.01514`, median `0.01927`, mae `0.023087`
- 60d: sample `20`, hit `0.7`, avg `0.029024`, median `0.053855`, mae `0.050254`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003122`, median `0.001405`, mae `0.012269`
- 5d: sample `20`, hit `0.5`, avg `-0.004238`, median `0.000688`, mae `0.014617`
- 10d: sample `20`, hit `0.5`, avg `-0.001521`, median `0.000197`, mae `0.019594`
- 20d: sample `20`, hit `0.6`, avg `0.01514`, median `0.01927`, mae `0.023087`
- 60d: sample `20`, hit `0.7`, avg `0.029024`, median `0.053855`, mae `0.050254`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003122`, median `0.001405`, mae `0.012269`
- 5d: sample `20`, hit `0.5`, avg `-0.004238`, median `0.000688`, mae `0.014617`
- 10d: sample `20`, hit `0.5`, avg `-0.001521`, median `0.000197`, mae `0.019594`
- 20d: sample `20`, hit `0.6`, avg `0.01514`, median `0.01927`, mae `0.023087`
- 60d: sample `20`, hit `0.7`, avg `0.029024`, median `0.053855`, mae `0.050254`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003122`, median `0.001405`, mae `0.012269`
- 5d: sample `20`, hit `0.5`, avg `-0.004238`, median `0.000688`, mae `0.014617`
- 10d: sample `20`, hit `0.5`, avg `-0.001521`, median `0.000197`, mae `0.019594`
- 20d: sample `20`, hit `0.6`, avg `0.01514`, median `0.01927`, mae `0.023087`
- 60d: sample `20`, hit `0.7`, avg `0.029024`, median `0.053855`, mae `0.050254`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.325`, avg `-0.008494`, median `-0.009843`, mae `0.017046`
- 5d: sample `40`, hit `0.35`, avg `-0.009782`, median `-0.013229`, mae `0.021067`
- 10d: sample `40`, hit `0.35`, avg `-0.012118`, median `-0.015101`, mae `0.029558`
- 20d: sample `40`, hit `0.6`, avg `0.01562`, median `0.015713`, mae `0.036246`
- 60d: sample `40`, hit `0.85`, avg `0.072205`, median `0.079528`, mae `0.088375`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003122`, median `0.001405`, mae `0.012269`
- 5d: sample `20`, hit `0.5`, avg `-0.004238`, median `0.000688`, mae `0.014617`
- 10d: sample `20`, hit `0.5`, avg `-0.001521`, median `0.000197`, mae `0.019594`
- 20d: sample `20`, hit `0.6`, avg `0.01514`, median `0.01927`, mae `0.023087`
- 60d: sample `20`, hit `0.7`, avg `0.029024`, median `0.053855`, mae `0.050254`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.4125`, avg `-0.007324`, median `-0.006508`, mae `0.016012`
- 5d: sample `80`, hit `0.4`, avg `-0.008857`, median `-0.011804`, mae `0.018996`
- 10d: sample `80`, hit `0.3875`, avg `-0.007669`, median `-0.009882`, mae `0.024316`
- 20d: sample `80`, hit `0.6125`, avg `0.016844`, median `0.01927`, mae `0.03286`
- 60d: sample `80`, hit `0.775`, avg `0.055422`, median `0.063683`, mae `0.077241`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.003122`, median `0.001405`, mae `0.012269`
- 5d: sample `20`, hit `0.5`, avg `-0.004238`, median `0.000688`, mae `0.014617`
- 10d: sample `20`, hit `0.5`, avg `-0.001521`, median `0.000197`, mae `0.019594`
- 20d: sample `20`, hit `0.6`, avg `0.01514`, median `0.01927`, mae `0.023087`
- 60d: sample `20`, hit `0.7`, avg `0.029024`, median `0.053855`, mae `0.050254`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

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
