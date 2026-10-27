# High Confidence Edge Report

Generated at: `2026-10-27T00:58:20.151421+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `136`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `136`, gate `stronger_evidence`
- 5d: completed `136`, gate `stronger_evidence`
- 10d: completed `136`, gate `stronger_evidence`
- 20d: completed `136`, gate `stronger_evidence`
- 60d: completed `136`, gate `stronger_evidence`

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
- 3d: sample `80`, hit `0.6`, avg `0.004064`, median `0.008574`, mae `0.019791`
- 5d: sample `80`, hit `0.55`, avg `0.000958`, median `0.006018`, mae `0.025796`
- 10d: sample `80`, hit `0.5125`, avg `-0.002705`, median `0.001411`, mae `0.039462`
- 20d: sample `80`, hit `0.4625`, avg `-0.00827`, median `-0.007733`, mae `0.042327`
- 60d: sample `80`, hit `0.825`, avg `0.064235`, median `0.065855`, mae `0.075283`

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
- 3d: sample `8`, hit `0.25`, avg `-0.007794`, median `-0.00518`, mae `0.013528`
- 5d: sample `8`, hit `0.25`, avg `-0.010277`, median `-0.014918`, mae `0.019476`
- 10d: sample `8`, hit `0.125`, avg `-0.030498`, median `-0.038595`, mae `0.039988`
- 20d: sample `8`, hit `0.125`, avg `-0.036915`, median `-0.033468`, mae `0.04413`
- 60d: sample `8`, hit `0.625`, avg `0.021487`, median `0.036183`, mae `0.043201`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.004536`, median `0.017631`, mae `0.01986`
- 5d: sample `8`, hit `0.625`, avg `0.003249`, median `0.002812`, mae `0.027528`
- 10d: sample `8`, hit `0.5`, avg `0.002268`, median `0.036012`, mae `0.043349`
- 20d: sample `8`, hit `0.5`, avg `-0.004281`, median `0.02284`, mae `0.038002`
- 60d: sample `8`, hit `0.875`, avg `0.052016`, median `0.069082`, mae `0.054554`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004536, 'median_return': 0.017631, 'mean_absolute_return': 0.01986, 'max_adverse_excursion': -0.026722, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003249, 'median_return': 0.002812, 'mean_absolute_return': 0.027528, 'max_adverse_excursion': -0.039725, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002268, 'median_return': 0.036012, 'mean_absolute_return': 0.043349, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004281, 'median_return': 0.02284, 'mean_absolute_return': 0.038002, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.057759}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.052016, 'median_return': 0.069082, 'mean_absolute_return': 0.054554, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.090399}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.004012, 'median_return': 0.008574, 'mean_absolute_return': 0.019783, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000703, 'median_return': 0.006712, 'mean_absolute_return': 0.025604, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.003257, 'median_return': 0.001411, 'mean_absolute_return': 0.03903, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.008713, 'median_return': -0.007733, 'mean_absolute_return': 0.042807, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.065593, 'median_return': 0.065855, 'mean_absolute_return': 0.077586, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.188608}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.5375}, '60d': {'sample_size': 80, 'hit_rate': 0.175}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.175, 'secondary_hit_rate': 0.825, 'primary_minus_secondary': -0.65, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006135, 'median_return': 0.018606, 'mean_absolute_return': 0.022013, 'max_adverse_excursion': -0.038555, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004539, 'median_return': 0.005387, 'mean_absolute_return': 0.025868, 'max_adverse_excursion': -0.041488, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007323, 'median_return': 0.017429, 'mean_absolute_return': 0.04069, 'max_adverse_excursion': -0.104082, 'max_favorable_excursion': 0.080901}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.006046, 'median_return': 0.02284, 'mean_absolute_return': 0.049569, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 20, 'hit_rate': 0.9, 'avg_return': 0.055044, 'median_return': 0.059606, 'mean_absolute_return': 0.059576, 'max_adverse_excursion': -0.035165, 'max_favorable_excursion': 0.117089}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.003374, 'median_return': 0.006321, 'mean_absolute_return': 0.01905, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.000236, 'median_return': 0.006712, 'mean_absolute_return': 0.025772, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.059395}, '10d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': -0.006047, 'median_return': 0.000466, 'mean_absolute_return': 0.039053, 'max_adverse_excursion': -0.110898, 'max_favorable_excursion': 0.075219}, '20d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.009011, 'median_return': -0.011521, 'mean_absolute_return': 0.039913, 'max_adverse_excursion': -0.103697, 'max_favorable_excursion': 0.094221}, '60d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.067299, 'median_return': 0.06911, 'mean_absolute_return': 0.080518, 'max_adverse_excursion': -0.057863, 'max_favorable_excursion': 0.188608}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.005326`, median `0.010986`, mae `0.018385`
- 5d: sample `60`, hit `0.5333`, avg `0.001908`, median `0.002812`, mae `0.023826`
- 10d: sample `60`, hit `0.45`, avg `-0.006378`, median `-0.012607`, mae `0.042454`
- 20d: sample `60`, hit `0.4333`, avg `-0.013177`, median `-0.020804`, mae `0.045512`
- 60d: sample `60`, hit `0.7667`, avg `0.047991`, median `0.055986`, mae `0.062721`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000277`, median `0.007291`, mae `0.024008`
- 5d: sample `20`, hit `0.6`, avg `-0.001893`, median `0.010926`, mae `0.031706`
- 10d: sample `20`, hit `0.7`, avg `0.008314`, median `0.010559`, mae `0.030485`
- 20d: sample `20`, hit `0.55`, avg `0.006453`, median `0.003343`, mae `0.03277`
- 60d: sample `20`, hit `1.0`, avg `0.112967`, median `0.113503`, mae `0.112967`

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
- 3d: sample `20`, hit `0.55`, avg `0.000277`, median `0.007291`, mae `0.024008`
- 5d: sample `20`, hit `0.6`, avg `-0.001893`, median `0.010926`, mae `0.031706`
- 10d: sample `20`, hit `0.7`, avg `0.008314`, median `0.010559`, mae `0.030485`
- 20d: sample `20`, hit `0.55`, avg `0.006453`, median `0.003343`, mae `0.03277`
- 60d: sample `20`, hit `1.0`, avg `0.112967`, median `0.113503`, mae `0.112967`

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
- 3d: sample `80`, hit `0.6`, avg `0.004064`, median `0.008574`, mae `0.019791`
- 5d: sample `80`, hit `0.55`, avg `0.000958`, median `0.006018`, mae `0.025796`
- 10d: sample `80`, hit `0.5125`, avg `-0.002705`, median `0.001411`, mae `0.039462`
- 20d: sample `80`, hit `0.4625`, avg `-0.00827`, median `-0.007733`, mae `0.042327`
- 60d: sample `80`, hit `0.825`, avg `0.064235`, median `0.065855`, mae `0.075283`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.00202`, median `0.005136`, mae `0.012928`
- 5d: sample `20`, hit `0.4`, avg `-0.00453`, median `-0.00891`, mae `0.019344`
- 10d: sample `20`, hit `0.3`, avg `-0.019777`, median `-0.030112`, mae `0.038023`
- 20d: sample `20`, hit `0.25`, avg `-0.024884`, median `-0.02364`, mae `0.040817`
- 60d: sample `20`, hit `0.65`, avg `0.023385`, median `0.031838`, mae `0.040996`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.004064`, median `0.008574`, mae `0.019791`
- 5d: sample `80`, hit `0.55`, avg `0.000958`, median `0.006018`, mae `0.025796`
- 10d: sample `80`, hit `0.5125`, avg `-0.002705`, median `0.001411`, mae `0.039462`
- 20d: sample `80`, hit `0.4625`, avg `-0.00827`, median `-0.007733`, mae `0.042327`
- 60d: sample `80`, hit `0.825`, avg `0.064235`, median `0.065855`, mae `0.075283`

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
- 3d: sample `80`, hit `0.6`, avg `0.004064`, median `0.008574`, mae `0.019791`
- 5d: sample `80`, hit `0.55`, avg `0.000958`, median `0.006018`, mae `0.025796`
- 10d: sample `80`, hit `0.5125`, avg `-0.002705`, median `0.001411`, mae `0.039462`
- 20d: sample `80`, hit `0.4625`, avg `-0.00827`, median `-0.007733`, mae `0.042327`
- 60d: sample `80`, hit `0.825`, avg `0.064235`, median `0.065855`, mae `0.075283`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
