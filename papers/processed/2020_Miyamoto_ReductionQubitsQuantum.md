---
aliases:
- Reduction of Qubits in Quantum Algorithm for Monte Carlo Simulation by Pseudo-random
  Number Generator
- Reduction Qubits Quantum Algorithm
authors:
- Koichi Miyamoto
- Kenji Shiohara
auto_detected: true
classification: ''
contradiction_flags: []
doi: 10.48550/arXiv.1911.12469
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: arXiv
methodology_tags:
- amplitude-estimation
- quantum-simulation
- classical-simulation
paper_type: ''
quantum_advantage_claim: theoretical
related_papers: []
relevance_phase1: high
relevance_phase3: medium
source_type: preprint
source_type_confidence: high
step1_date: '2026-03-19T22:58:16.485270'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T22:59:16.281079'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T23:00:29.757899'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:00:37.683267'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:00:44.980161'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:00:49.383963'
step6_model: Mistral-Large-3
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/risk-modelling
- topic/derivatives-pricing
- method/amplitude-estimation
- method/quantum-simulation
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
title: Reduction of Qubits in Quantum Algorithm for Monte Carlo Simulation by Pseudo-random
  Number Generator
topic_tags:
- risk-modelling
- derivatives-pricing
year: 2020
zotero_key: ''
---

## Abstract summary
This preprint proposes a method to reduce the number of qubits required in quantum algorithms for Monte Carlo simulations, particularly in high-dimensional financial problems like credit risk measurement. The authors introduce a pseudo-random number generator (PRNG) implemented on a quantum circuit to sequentially generate random numbers, thereby avoiding the need for a quantum register per random number. The paper outlines the theoretical framework, provides concrete implementations of PRNGs, and demonstrates applications in credit risk measurement and simple multi-variable integration.
## Methodology
The paper proposes a method to reduce the number of qubits required for quantum Monte Carlo simulations in financial applications, particularly for high-dimensional integrals such as credit risk measurement. The core idea is to implement a pseudo-random number generator (PRNG) on a quantum circuit to sequentially generate random numbers, rather than allocating a quantum register for each random number. This approach mimics classical Monte Carlo methods where PRNGs are used to sample integrand values. The paper details the implementation of a permuted congruential generator (PCG) as the PRNG, which combines linear congruential generation with bit-string permutation. The methodology involves creating a superposition of states representing sampled integrand values using the PRNG, followed by quantum amplitude estimation to compute the average of these values. The trade-off between qubit reduction and increased circuit depth is discussed, highlighting the potential impracticality of full qubit reduction but emphasizing the importance of such trade-offs for future large-scale quantum Monte Carlo simulations.

**Algorithms used:** Quantum Amplitude Estimation, Permuted Congruential Generator (PCG), Linear Congruential Generator (LCG)

**Experimental setup:** The experimental setup involves simulations using the Qiskit quantum circuit simulator by IBM. The study demonstrates the proposed method on a small-scale integration problem (a two-variable trigonometric function) to validate the approach. The PRNG used is a linear congruential generator (LCG) with specific parameters (a=11, c=0, m=31, seed=1), generating 5-bit pseudo-random numbers with a period of 30. The number of samples (Nsamp) is set to 8, utilizing 16 elements of the PRNG sequence.

**Dataset:** The paper does not use a real-world financial dataset but demonstrates the method on a simple multi-variable trigonometric function integral for proof-of-concept purposes.
## Findings
- [supported] The proposed method reduces the required qubit number in quantum Monte Carlo simulations by using a pseudo-random number generator (PRNG) implemented on a quantum circuit, enabling sequential generation of random numbers instead of parallel allocation of quantum registers per random number.
- [supported] The quantum algorithm for Monte Carlo using PRNG achieves quadratic speedup (O(N^{-1}) error scaling) compared to classical Monte Carlo (O(N^{-1/2}) error scaling), similar to previous quantum Monte Carlo methods but with reduced qubit requirements.
- [supported] The error in the proposed method is bounded by the sum of the statistical error (ΔTrSm) and the amplitude estimation error (ΔEst), where ΔTrSm scales as O(2^{-nsamp/2}) and ΔEst scales as O(N_{orac}^{-1}).
- [supported] The permuted congruential generator (PCG) is proposed as a PRNG suitable for quantum circuits, combining linear congruential generator (LCG) with bit-string permutation to balance qubit efficiency and circuit depth.
- [supported] The PCG implementation on a quantum circuit requires O(n) qubits and O(n^2) depth for n-bit operands, with modular multiplication being the dominant contributor to circuit depth.
- [supported] The method is applied to credit risk measurement in the Merton model, demonstrating sequential calculation of portfolio loss using PRNG-generated random numbers, reducing qubit requirements from O(Nobl) to O(1) per random number.
- [supported] A proof-of-concept demonstration on a quantum circuit simulator for a simple multi-variable integral (2D trigonometric function) shows close agreement between the quantum-estimated average and the exact average of integrand values on sample points (0.078391 vs. 0.078394).
- [speculative] Full qubit reduction may be impractical due to increased circuit depth, but the trade-off between qubit number and circuit depth is important for adjusting calculations to machine specifications in future large-scale quantum Monte Carlo simulations.
- [speculative] The proposed method enables partial parallelism in scenarios where full parallel generation of random numbers is impossible due to qubit limitations, allowing for a flexible trade-off between qubit usage and circuit depth.

**Results summary:** The paper introduces a quantum algorithm for Monte Carlo simulation that reduces qubit requirements by implementing a pseudo-random number generator (PRNG) on a quantum circuit. This approach enables sequential generation of random numbers, addressing the high qubit demand in high-dimensional financial problems like credit risk measurement. The method maintains the quadratic speedup of quantum Monte Carlo (O(N^{-1}) error scaling) while significantly lowering qubit usage. The authors propose the permuted congruential generator (PCG) as a PRNG suitable for quantum circuits, demonstrating its implementation and application to credit risk measurement and a simple multi-variable integral. Simulation results validate the method's accuracy, though the trade-off between qubit reduction and increased circuit depth is noted as a potential limitation for practical deployment.

**Performance claims:**
- Quadratic speedup in error scaling (O(N^{-1})) compared to classical Monte Carlo (O(N^{-1/2})).
- Qubit reduction from O(Nran) to O(nPRN), where nPRN is the bit-length of the PRNG output (e.g., 32-64 bits).
- Error bound: Δour ~ cσ_fNran * 2^{-nsamp/2} + 2πd * sqrt(Esamp(1-Esamp)) * N_{orac}^{-1}.
- PCG circuit depth dominated by modular multiplication: O(n^2) for n-bit operands.
- Proof-of-concept integral estimation accuracy: 0.078391 (quantum) vs. 0.078394 (exact average).
## Quantum advantage claim
**Classification:** theoretical

The paper claims a theoretical quantum advantage in Monte Carlo simulation due to quadratic speedup in error scaling (O(N^{-1}) vs. O(N^{-1/2}) classically). However, this advantage is demonstrated only in simulation and not on real quantum hardware. The advantage is contingent on the trade-off between qubit reduction and increased circuit depth, which may limit practical deployment on near-term devices.
## Limitations
- Proposed method reduces qubit count but increases circuit depth, making full reduction potentially impractical due to error accumulation on near-term quantum hardware [inferred]
- Trade-off between qubit number and circuit depth may limit practical applicability on current and near-term quantum devices
- Method assumes integrand can be computed sequentially, which is not universally applicable [inferred]
- PRNG implementation (PCG) requires O(n) qubits and O(n²) depth for modular multiplication, which may dominate computational resources for large n
- Lack of peer review as this is a preprint [inferred]
- Experiments limited to small-scale problems (e.g., 2-variable integration) due to simulator constraints
- Statistical concerns with small-scale PRNG (5-bit, period 30) used in demonstration, which may not generalize to real-world applications
- No empirical validation on real quantum hardware, only simulator-based proof-of-concept
- Assumes existence of quantum gates for functions like trigonometric operations and logarithms (e.g., Box-Muller method) without detailed implementation
- Error analysis shows convergence to classical Monte Carlo error (ΔTrSm) for large sample sizes, limiting quantum advantage in some regimes [inferred]
- No comparison with state-of-the-art classical Monte Carlo methods for financial applications [inferred]
- Credit risk measurement example assumes Merton model, which may not capture all real-world credit risk dynamics [inferred]
## Open questions
- How does the proposed method perform on real quantum hardware with noise and decoherence?
- What is the optimal balance between qubit reduction and circuit depth for practical financial applications?
- Can the sequential integrand computation assumption be relaxed for broader applicability?
- How do statistical properties of PRNGs (e.g., PCG) affect solution quality in high-dimensional financial problems?
- What is the impact of PRNG period limitations on large-scale Monte Carlo simulations?
- How does the method compare to hybrid quantum-classical approaches for Monte Carlo simulation?
- What are the implications of the memory-speed trade-off for fault-tolerant quantum computing?
- Can the method be extended to other financial applications beyond credit risk measurement and simple integrations?

**Future work:**
- Test the proposed method on real quantum hardware to validate performance under noise
- Explore hybrid quantum-classical approaches to mitigate circuit depth limitations
- Develop more efficient quantum implementations of PRNGs with better statistical properties
- Extend the method to multi-period financial problems (e.g., dynamic portfolio optimization)
- Investigate alternative integrand computation strategies to relax sequential computation assumptions
- Compare performance with state-of-the-art classical Monte Carlo methods for financial applications
- Optimize circuit implementations for specific financial use cases (e.g., derivative pricing)
- Study the impact of quantum error correction on the memory-speed trade-off
- Apply the method to larger-scale financial problems with more realistic data
- Develop benchmarking frameworks for quantum Monte Carlo methods in finance
## Key ideas
- #idea:quantum-advantage — Proposes a quantum Monte Carlo method with quadratic speedup (O(N⁻¹) error scaling) compared to classical Monte Carlo (O(N⁻¹/²)), demonstrated via simulation for credit risk measurement and multi-variable integration.
- #idea:near-term-feasibility — Introduces a pseudo-random number generator (PRNG) on quantum circuits to reduce qubit requirements (O(n_PRN) vs. O(N_ran)), making large-scale simulations (e.g., O(10⁶) obligors) theoretically feasible on near-term devices.
- #idea:hybrid-approach — Suggests trade-offs between qubit reduction and circuit depth could be optimized via hybrid quantum-classical approaches, though not explicitly implemented.
- #limitation:qubit-count — Despite qubit reduction, the method's practicality is constrained by increased circuit depth and noise susceptibility on NISQ devices.
- #limitation:no-empirical-validation — All results are simulation-based; no real quantum hardware validation is provided, limiting claims of quantum advantage.
- #limitation:noise — Increased circuit depth due to qubit reduction may exacerbate noise-related errors on near-term quantum hardware.
- #limitation:data-encoding — Assumes seamless conversion of uniform PRNs to desired distributions (e.g., normal), but this may introduce additional errors or overhead.
## Contradictions
<!-- Step 6 output — where this paper contradicts others -->

## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
For the demonstration, the input is a simple trigonometric function integral with θ = π/6 and Nvar = 2. The PRNG generates pseudo-random numbers to sample grid points for the integral approximation. The sample size is Nsamp = 8, with each sample using 2 random numbers (total 16 PRNG elements).

### Process
1. Initialize quantum registers Rsamp, RPRN, and Rrot. 2. Create a superposition of sample indices using Hadamard gates on Rsamp. 3. Use JPRN to set the starting points of PRN subsequences on RPRN. 4. Sequentially apply the PRNG progression gate (PPRN) and integrand calculation gates (f) to compute sampled integrand values. 5. Encode the integrand values into the phase of the ancilla qubit Rrot using controlled rotations. 6. Estimate the probability of observing |1⟩ in Rrot using quantum amplitude estimation techniques (e.g., as proposed in Suzuki et al., 2019). 7. Repeat observations for different powers of the Q operation to estimate the integral value.

### Output
The output is the estimated value of the integral, reported as 0.078391 for the demonstration case. This is compared against the exact value of the original integral (0.074578) and the exact average of integrand values on sample points (0.078394). The results show close agreement with the expected sampled average, validating the method.

### Parameters
- PRNG_parameters: {'a': 11, 'c': 0, 'm': 31, 'seed': 1, 'bit_length': 5, 'period': 30}
- sample_size: {'Nsamp': 8, 'nsamp': 3}
- integral_parameters: {'θ': 'π/6', 'Nvar': 2}
- amplitude_estimation_parameters: {'M': 8, 'Nk': 100, 'mk': [1, 2, 4, 8, 16, 32, 64, 128]}

### Hardware
The experiments were conducted using the IBM Qiskit Aer quantum circuit simulator. No real quantum processing unit (QPU) was used.

### Reproducibility
The paper provides sufficient detail for replicating the demonstration, including PRNG parameters, circuit diagrams, and amplitude estimation settings. The code for the simulation is not explicitly stated as available, but the methodology is described in enough detail to allow reproduction using Qiskit or similar quantum simulators. The data used (simple trigonometric function) is trivial and does not require external sources.
