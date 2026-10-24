# High Confidence Edge Report

Generated at: `2026-10-24T01:22:25.632990+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `132`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `132`, gate `stronger_evidence`
- 5d: completed `132`, gate `stronger_evidence`
- 10d: completed `132`, gate `stronger_evidence`
- 20d: completed `132`, gate `stronger_evidence`
- 60d: completed `132`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.55`, avg `0.001628`, median `0.003066`, mae `0.019357`
- 5d: sample `80`, hit `0.5125`, avg `-0.000572`, median `0.002574`, mae `0.025747`
- 10d: sample `80`, hit `0.4625`, avg `-0.005028`, median `-0.006017`, mae `0.039734`
- 20d: sample `80`, hit `0.45`, avg `-0.009621`, median `-0.011521`, mae `0.041584`
- 60d: sample `80`, hit `0.8375`, avg `0.066698`, median `0.065855`, mae `0.077841`

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
- 3d: sample `8`, hit `0.25`, avg `-0.006152`, median `-0.00518`, mae `0.015169`
- 5d: sample `8`, hit `0.25`, avg `-0.010653`, median `-0.014918`, mae `0.0191`
- 10d: sample `8`, hit `0.125`, avg `-0.033235`, median `-0.038595`, mae `0.042725`
- 20d: sample `8`, hit `0.125`, avg `-0.041288`, median `-0.045639`, mae `0.048503`
- 60d: sample `8`, hit `0.75`, avg `0.025079`, median `0.036183`, mae `0.043275`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.004536`, median `0.017631`, mae `0.01986`
- 5d: sample `8`, hit `0.625`, avg `0.003249`, median `0.002812`, mae `0.027528`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.036012`, mae `0.043349`
- 20d: sample `8`, hit `0.5`, avg `-0.004281`, median `0.02284`, mae `0.038002`
- 60d: sample `8`, hit `0.875`, avg `0.052016`, median `0.069082`, mae `0.054554`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004536, 'median_return': 0.017631, 'mean_absolute_return': 0.01986, 'max_adverse_excursion': -0.026722, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003249, 'median_return': 0.002812, 'mean_absolute_return': 0.027528, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002268, 'median_return': 0.036012, 'mean_absolute_return': 0.043349, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004281, 'median_return': 0.02284, 'mean_absolute_return': 0.038002, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.057759}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.052016, 'median_return': 0.069082, 'mean_absolute_return': 0.054554, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.090399}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001305, 'median_return': 0.003066, 'mean_absolute_return': 0.019301, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.000997, 'median_return': 0.002574, 'mean_absolute_return': 0.025549, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.005839, 'median_return': -0.006017, 'mean_absolute_return': 0.039333, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.010214, 'median_return': -0.011521, 'mean_absolute_return': 0.041982, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.06833, 'median_return': 0.065855, 'mean_absolute_return': 0.080429, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.425}, '60d': {'sample_size': 80, 'hit_rate': 0.2625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2625, 'secondary_hit_rate': 0.7375, 'primary_minus_secondary': -0.475, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001623, 'median_return': 0.002171, 'mean_absolute_return': 0.016689, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.000649, 'median_return': 0.000169, 'mean_absolute_return': 0.022588, 'max_adverse_excursion': -0.041488, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.00776, 'median_return': -0.013567, 'mean_absolute_return': 0.038747, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.014232, 'median_return': -0.02364, 'mean_absolute_return': 0.045811, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.046812, 'median_return': 0.055986, 'mean_absolute_return': 0.05576, 'max_adverse_excursion': -0.039851, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001633, 'median_return': 0.007291, 'mean_absolute_return': 0.022025, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.044418}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.000495, 'median_return': 0.006047, 'mean_absolute_return': 0.028906, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.002297, 'median_return': 0.008188, 'mean_absolute_return': 0.040722, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.075219}, '20d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.00501, 'median_return': 0.003343, 'mean_absolute_return': 0.037357, 'max_adverse_excursion': -0.103697, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.086585, 'median_return': 0.105412, 'mean_absolute_return': 0.099923, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.00175`, median `0.002171`, mae `0.017752`
- 5d: sample `60`, hit `0.4833`, avg `-0.000183`, median `-0.002194`, mae `0.02371`
- 10d: sample `60`, hit `0.3833`, avg `-0.010189`, median `-0.017977`, mae `0.042104`
- 20d: sample `60`, hit `0.4167`, avg `-0.014195`, median `-0.023277`, mae `0.045306`
- 60d: sample `60`, hit `0.7833`, avg `0.05132`, median `0.057953`, mae `0.066178`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001261`, median `0.008574`, mae `0.024171`
- 5d: sample `20`, hit `0.6`, avg `-0.001741`, median `0.009561`, mae `0.031858`
- 10d: sample `20`, hit `0.7`, avg `0.010453`, median `0.010559`, mae `0.032625`
- 20d: sample `20`, hit `0.55`, avg `0.004101`, median `0.003343`, mae `0.030418`
- 60d: sample `20`, hit `1.0`, avg `0.112833`, median `0.127045`, mae `0.112833`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000121`, median `0.000438`, mae `0.013206`
- 5d: sample `20`, hit `0.4`, avg `-0.003755`, median `-0.00891`, mae `0.019161`
- 10d: sample `20`, hit `0.3`, avg `-0.020491`, median `-0.033293`, mae `0.038514`
- 20d: sample `20`, hit `0.25`, avg `-0.024269`, median `-0.025111`, mae `0.040202`
- 60d: sample `20`, hit `0.7`, avg `0.027884`, median `0.036183`, mae `0.044764`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000121`, median `0.000438`, mae `0.013206`
- 5d: sample `20`, hit `0.4`, avg `-0.003755`, median `-0.00891`, mae `0.019161`
- 10d: sample `20`, hit `0.3`, avg `-0.020491`, median `-0.033293`, mae `0.038514`
- 20d: sample `20`, hit `0.25`, avg `-0.024269`, median `-0.025111`, mae `0.040202`
- 60d: sample `20`, hit `0.7`, avg `0.027884`, median `0.036183`, mae `0.044764`

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
- 3d: sample `20`, hit `0.6`, avg `0.001261`, median `0.008574`, mae `0.024171`
- 5d: sample `20`, hit `0.6`, avg `-0.001741`, median `0.009561`, mae `0.031858`
- 10d: sample `20`, hit `0.7`, avg `0.010453`, median `0.010559`, mae `0.032625`
- 20d: sample `20`, hit `0.55`, avg `0.004101`, median `0.003343`, mae `0.030418`
- 60d: sample `20`, hit `1.0`, avg `0.112833`, median `0.127045`, mae `0.112833`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.00175`, median `0.002171`, mae `0.017752`
- 5d: sample `60`, hit `0.4833`, avg `-0.000183`, median `-0.002194`, mae `0.02371`
- 10d: sample `60`, hit `0.3833`, avg `-0.010189`, median `-0.017977`, mae `0.042104`
- 20d: sample `60`, hit `0.4167`, avg `-0.014195`, median `-0.023277`, mae `0.045306`
- 60d: sample `60`, hit `0.7833`, avg `0.05132`, median `0.057953`, mae `0.066178`

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
- 3d: sample `80`, hit `0.55`, avg `0.001628`, median `0.003066`, mae `0.019357`
- 5d: sample `80`, hit `0.5125`, avg `-0.000572`, median `0.002574`, mae `0.025747`
- 10d: sample `80`, hit `0.4625`, avg `-0.005028`, median `-0.006017`, mae `0.039734`
- 20d: sample `80`, hit `0.45`, avg `-0.009621`, median `-0.011521`, mae `0.041584`
- 60d: sample `80`, hit `0.8375`, avg `0.066698`, median `0.065855`, mae `0.077841`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.001628`, median `0.003066`, mae `0.019357`
- 5d: sample `80`, hit `0.5125`, avg `-0.000572`, median `0.002574`, mae `0.025747`
- 10d: sample `80`, hit `0.4625`, avg `-0.005028`, median `-0.006017`, mae `0.039734`
- 20d: sample `80`, hit `0.45`, avg `-0.009621`, median `-0.011521`, mae `0.041584`
- 60d: sample `80`, hit `0.8375`, avg `0.066698`, median `0.065855`, mae `0.077841`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000121`, median `0.000438`, mae `0.013206`
- 5d: sample `20`, hit `0.4`, avg `-0.003755`, median `-0.00891`, mae `0.019161`
- 10d: sample `20`, hit `0.3`, avg `-0.020491`, median `-0.033293`, mae `0.038514`
- 20d: sample `20`, hit `0.25`, avg `-0.024269`, median `-0.025111`, mae `0.040202`
- 60d: sample `20`, hit `0.7`, avg `0.027884`, median `0.036183`, mae `0.044764`

### bounce_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000121`, median `0.000438`, mae `0.013206`
- 5d: sample `20`, hit `0.4`, avg `-0.003755`, median `-0.00891`, mae `0.019161`
- 10d: sample `20`, hit `0.3`, avg `-0.020491`, median `-0.033293`, mae `0.038514`
- 20d: sample `20`, hit `0.25`, avg `-0.024269`, median `-0.025111`, mae `0.040202`
- 60d: sample `20`, hit `0.7`, avg `0.027884`, median `0.036183`, mae `0.044764`

### risk_path_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5667`, avg `0.00213`, median `0.008174`, mae `0.021407`
- 5d: sample `60`, hit `0.55`, avg `0.000489`, median `0.005387`, mae `0.027943`
- 10d: sample `60`, hit `0.5167`, avg `0.000126`, median `0.001411`, mae `0.040141`
- 20d: sample `60`, hit `0.5167`, avg `-0.004738`, median `0.003343`, mae `0.042045`
- 60d: sample `60`, hit `0.8833`, avg `0.079637`, median `0.081441`, mae `0.088867`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
