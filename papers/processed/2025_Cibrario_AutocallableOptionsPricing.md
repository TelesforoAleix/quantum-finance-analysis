---
aliases:
- Autocallable Options Pricing with Integration-Based Exponential Amplitude Loading
- Autocallable Options Pricing Integration
authors:
- Francesca Cibrario
- Ron Cohen
- Emanuele Dri
- Christian Mattia
- Or Samimi Golan
- Tamuz Danzig
- Giacomo Ranieri
- Hanan Rosemarin
- Davide Corbelletto
- Amir Naveh
- Bartolomeo Montrucchio
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:scalability
doi: 10.1109/QCE65121.2025.00267
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: 2025 IEEE International Conference on Quantum Computing and Engineering
  (QCE)
methodology_tags:
- amplitude-estimation
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers: []
relevance_phase1: high
relevance_phase3: high
source_type: conference-paper
source_type_confidence: high
step1_date: '2026-03-20T00:15:21.728497'
step1_model: Mistral-Large-3
step2_date: '2026-03-20T00:15:25.446409'
step2_model: Mistral-Large-3
step3_date: '2026-03-20T00:15:42.313391'
step3_model: Mistral-Large-3
step4_date: '2026-03-20T00:15:50.619198'
step4_model: Mistral-Large-3
step5_date: '2026-03-20T00:16:21.020894'
step5_model: Mistral-Large-3
step6_date: '2026-03-20T00:17:23.870669'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- method/amplitude-estimation
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
title: Autocallable Options Pricing with Integration-Based Exponential Amplitude Loading
topic_tags:
- derivatives-pricing
year: 2025
zotero_key: ''
---

## Abstract summary
This conference paper introduces a quantum algorithm for pricing autocallable options, a type of path-dependent financial derivative. The authors propose an improved integration-based exponential amplitude loading technique that reduces quantum circuit depth compared to existing methods. The paper includes a complexity analysis demonstrating a significant reduction in T-depth and presents simulation results validating the approach against classical benchmarks.
## Methodology
The paper presents a quantum algorithm for pricing autocallable options, a type of path-dependent financial derivative. The methodology builds on an improved integration-based exponential amplitude loading technique to reduce quantum circuit depth compared to existing approaches. The algorithm involves encoding a probability distribution of asset price paths into a quantum state, followed by payoff evaluation using amplitude loading. The key innovation is the optimization of the normalization factor in the amplitude loading process, which enhances accuracy and reduces resource requirements. The research includes a detailed complexity analysis, comparing T-depth (a measure of quantum gate complexity) with state-of-the-art methods, and validates the approach through simulations on high-performance computing (HPC) hardware, including the LEONARDO pre-exascale supercomputer. The experiments demonstrate convergence to classical Monte Carlo results as the number of qubits for Gaussian encoding and arithmetic precision increases.

**Algorithms used:** Quantum Amplitude Estimation (QAE), Iterative Quantum Amplitude Estimation (IQAE), Integration-based Exponential Amplitude Loading
**Frameworks:** Classiq platform, Qmod language

**Experimental setup:** The experiments were conducted using quantum simulators due to the limited coherence times and fidelity of current quantum hardware. Circuits were synthesized using the Classiq platform to minimize qubit count for simulator compatibility. Simulations were performed on the Classiq default simulator (up to 25 qubits), Nvidia simulator on a single GPU (up to 30 qubits), and the LEONARDO HPC system using the Cirq simulator with multiple GPUs (for circuits exceeding 30 qubits). The experimental setup focused on a single-asset autocallable option with three time steps and two binary options.

**Dataset:** Synthetic financial data for autocallable options pricing, including parameters such as notional value, time steps, volatility, average log-return, barrier and strike returns, and binary option payoffs. The model parameters are detailed in Table II of the paper.
## Findings
- [supported] The proposed integration-based exponential amplitude loading technique reduces circuit depth compared to state-of-the-art approaches, achieving a ~50x reduction in T-depth for the payoff component relative to previous methods.
- [supported] The algorithm was validated through simulations on high-performance computing (HPC) hardware, including the LEONARDO pre-exascale supercomputer, with experiments conducted using up to 33 qubits.
- [supported] The complexity analysis demonstrates that the proposed method requires fewer resources than Quantum Signal Processing (QSP)-based approaches, particularly in T-depth for amplitude loading modules.
- [speculative] The authors suggest that the methodology represents a step toward achieving quantum utility, defined as a practical advantage of quantum computing over classical methods in financial derivative pricing.
- [supported] The quantum algorithm's convergence to classical Monte Carlo results was demonstrated by increasing the number of qubits allocated for Gaussian encoding and quantum arithmetic precision.
- [speculative] The paper claims that further optimizations could enable tests on real quantum hardware using error mitigation techniques.
- [supported] The rescaling factor for the integration method is optimized to avoid degrading the normalization factor, improving the accuracy of subsequent estimates compared to prior work.

**Results summary:** The paper presents a quantum algorithm for pricing autocallable options, a path-dependent financial derivative, using an improved integration-based exponential amplitude loading technique. The algorithm was validated through extensive simulations on HPC hardware, demonstrating a ~50x reduction in T-depth for the payoff component compared to state-of-the-art methods. The complexity analysis highlights significant resource savings, particularly in T-gate depth, relative to QSP-based approaches. Experimental results show convergence to classical Monte Carlo benchmarks as qubit precision and Gaussian discretization increase, though real hardware execution remains challenging due to circuit size constraints. The work positions itself as a step toward quantum utility in financial services.

**Performance claims:**
- ~50x reduction in T-depth for the payoff component relative to previous methods
- Simulations conducted with up to 33 qubits on the LEONARDO supercomputer
- Convergence to classical Monte Carlo results demonstrated with increasing qubit precision (up to 5 fractional qubits) and Gaussian discretization (up to 3 qubits per Gaussian)
## Quantum advantage claim
**Classification:** speculative

The paper claims the methodology is a step toward quantum utility (practical quantum advantage) but does not demonstrate it empirically. Results are based on simulations, and the authors acknowledge that real hardware execution remains impractical due to circuit size constraints. The claimed advantage is theoretical, contingent on further optimizations and error mitigation techniques.
## Limitations
- Experiments limited to simulations on HPC hardware (LEONARDO supercomputer) due to current quantum hardware constraints [inferred]
- Algorithm validated only on a small instance of the autocallable pricing problem (single asset, three time steps, two binary options)
- Circuit size exceeds current quantum hardware capabilities, making real hardware execution infeasible without error mitigation [inferred]
- Simulations constrained by qubit count (up to 33 qubits), limiting scalability to larger problem instances
- Use of synthetic data parameters rather than real market data for validation [inferred]
- Page-limit constraints of conference paper may have restricted detailed discussion of certain implementation aspects [inferred]
- Normalization factor issues in the original integration-based exponential amplitude loading method could degrade accuracy
- Complexity analysis assumes fault-tolerant quantum computing, which is not yet available [inferred]
- Error mitigation techniques not applied or discussed for potential real hardware execution [inferred]
- Comparison with classical methods limited by simulator capabilities, preventing fair benchmarking at scale
## Open questions
- How does the algorithm perform with more complex autocallable options involving multiple assets (best-of/worst-of baskets)?
- What is the impact of quantum noise and decoherence on solution quality when executed on real hardware?
- How does the algorithm scale with an increasing number of time steps and observation dates?
- What are the exact resource requirements (qubit count, circuit depth) for achieving quantum advantage in practical settings?
- How does the integration-based amplitude loading technique compare with QSP-based methods in terms of robustness to noise?
- What is the minimum qubit count and coherence time required for practical deployment on near-term quantum devices?
- How sensitive is the algorithm to parameter variations (e.g., volatility models, strike prices, barriers)?
- What are the implications of using different volatility models (e.g., stochastic or local volatility) on the algorithm's performance?

**Future work:**
- Further optimization of circuit size and depth to enable execution on near-term quantum hardware
- Extension of the methodology to multi-asset autocallable options (best-of/worst-of baskets)
- Testing on real quantum hardware with error mitigation techniques to assess practical performance
- Exploration of more complex volatility models (e.g., stochastic or local volatility) for derivative pricing
- Development of hybrid quantum-classical approaches to bridge the gap between simulation and real hardware execution
- Investigation of alternative amplitude loading techniques to further reduce circuit depth and resource requirements
- Benchmarking against state-of-the-art classical methods for larger problem instances as quantum hardware improves
- Application of the methodology to other path-dependent financial derivatives beyond autocallable options
## Key ideas
- #idea:quantum-advantage — Proposed integration-based exponential amplitude loading technique achieves ~50x reduction in T-depth for autocallable options pricing, demonstrating potential quantum advantage via QAE's quadratic speedup over classical Monte Carlo
- #idea:near-term-feasibility — Algorithm validated through HPC simulations (up to 33 qubits) with convergence to classical benchmarks, suggesting near-term applicability despite current hardware limitations
- #idea:hybrid-approach — Classical HPC simulations and quantum circuit synthesis tools (Classiq, Cirq) used to bridge the gap between theoretical quantum algorithms and practical implementation
- #limitation:noise — Noise and decoherence on real quantum hardware remain unaddressed, with simulations assuming fault-tolerant conditions
- #limitation:qubit-count — Current qubit requirements (up to 33) exceed NISQ device capabilities, limiting real-world validation
- #limitation:data-encoding — Synthetic data used for validation, raising questions about performance with real market data violating Black-Scholes assumptions
## Contradictions
- #contradiction:scalability — Claims of ~50x T-depth reduction are context-specific (single asset, 3 time steps) and may not generalize to larger problem instances (e.g., multi-asset autocallables with >20 timesteps), contradicting broader quantum advantage claims for derivatives pricing
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
{'source': 'Synthetic data generated based on model parameters', 'size': 'Single-asset, 3 time steps, 2 binary options', 'parameters': {'notional_value': 18, 'time_step': '1 year', 'number_of_time_steps': 3, 'annual_volatility': 0.2382, 'annual_average_log_return': 0.1274, 'put_barrier': 0.7, 'put_strike_return': 1, 'risk_free_rate': 0.04, 'binary_option_strikes': [1.1, 1.1], 'binary_option_payoffs': [2, 5], 'standard_gaussian_truncation': 3}, 'preprocessing_steps': 'Discretization of Gaussian distributions, log-return calculations, and normalization of payoff values to the range [0, 1].'}

### Process
1. Load Gaussian distributions for each time step into quantum registers. 2. Compute log-returns using affine transformations and in-place addition. 3. Apply comparators to check binary option conditions and barrier crossings in log-return space. 4. Use integration-based exponential amplitude loading to encode payoff values into quantum amplitudes. 5. Apply controlled Ry rotations to map constant payoffs and normalization factors. 6. Use Iterative Quantum Amplitude Estimation (IQAE) to estimate the probability of the target qubit being in the |1⟩ state, corresponding to the expected payoff. 7. Repeat simulations with increasing qubits for Gaussian encoding and arithmetic precision to demonstrate convergence.

### Output
{'metrics_reported': ['Expected payoff', 'Convergence to classical Monte Carlo results'], 'comparison_baselines': ['Traditional Monte Carlo simulation', 'Monte Carlo with Gaussian discretization', 'Closed-form calculation with Gaussian discretization', 'Closed-form calculation with Gaussian discretization and fixed-point precision'], 'output_format': 'Expected payoff values plotted against the number of qubits per Gaussian, with confidence intervals for quantum simulations.'}

### Parameters
- qubits_per_gaussian: [1, 2, 3, 4]
- arithmetic_precision_qubits: [1, 2, 3, 4, 5, 16]
- shots: Determined by IQAE with target confidence level (ϵ = 0.001, α = 0.002)
- circuit_depth_optimization: Minimized for simulator compatibility
- error_thresholds: {'truncation_error': '≤ ϵ', 'discretization_error': '≤ ϵ', 'approximation_error': '≤ ϵ', 'arithmetic_error': '≤ ϵ', 'amplitude_loading_error': '≤ ϵ'}

### Hardware
{'simulator': ['Classiq default simulator', 'Nvidia simulator', 'Cirq simulator on LEONARDO HPC'], 'qpu_model': 'Not applicable (simulator-based experiments)', 'cloud_provider': 'LEONARDO HPC system for large-scale simulations', 'transpilation_settings': 'Optimized for circuit width (qubit count) to enable simulation'}

### Reproducibility
Code and implementation details are available at http://short.classiq.io/quantum_autocallable. The synthetic dataset parameters are fully specified in Table II of the paper. The methodology provides sufficient detail for replication, including circuit synthesis, simulation parameters, and error thresholds.
