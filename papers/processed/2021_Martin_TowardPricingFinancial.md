---
aliases:
- Toward pricing financial derivatives with an IBM quantum computer
- Toward pricing financial derivatives
authors:
- Ana Martin
- Bruno Candelas
- Ángel Rodríguez-Rozas
- José D. Martín-Guerrero
- Xi Chen
- Lucas Lamata
- Román Orús
- Enrique Solano
- Mikel Sanz
auto_detected: true
classification: ''
contradiction_flags:
- contradiction:classical-vs-quantum
- contradiction:scalability
doi: 10.1103/PhysRevResearch.3.013167
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review Research
methodology_tags:
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2021_Abbas_QuantumMachineLearningFinance
relevance_phase1: high
relevance_phase3: medium
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-25T15:54:39.540250'
step1_model: gpt-5.1
step2_date: '2026-03-25T15:54:43.492170'
step2_model: gpt-5.1
step3_date: '2026-03-25T15:55:13.778821'
step3_model: gpt-5.4
step4_date: '2026-03-25T15:55:47.231609'
step4_model: gpt-5.4
step5_date: '2026-03-25T15:56:16.720341'
step5_model: gpt-5.4
step6_date: '2026-03-25T15:56:32.954614'
step6_model: gpt-5.4
steps_completed:
- 1
- 2
- 3
- 4
- 5
- 6
tags:
- topic/derivatives-pricing
- topic/asset-pricing
- method/classical-simulation
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/classical-vs-quantum
- contradiction/scalability
title: Toward pricing financial derivatives with an IBM quantum computer
topic_tags:
- derivatives-pricing
- asset-pricing
year: 2021
zotero_key: ''
---

## Abstract summary
The paper implements a quantum principal component analysis algorithm on IBM's five-qubit superconducting quantum processor to reduce the number of stochastic factors in the multifactor Heath-Jarrow-Morton interest-rate model. Using historical data for several time-maturing forward rates, the authors experimentally estimate principal components of 2×2 and 3×3 covariance matrices, demonstrating a proof-of-concept for quantum-assisted dimensionality reduction in interest-rate derivative pricing. This work is positioned as an initial step toward full quantum simulation of the HJM framework for pricing interest-rate derivatives on near-term quantum hardware.
## Methodology
The paper presents a peer-reviewed empirical study implementing a modified quantum principal component analysis (qPCA) approach to reduce the dimensionality of the multifactor Heath-Jarrow-Morton (HJM) interest-rate model. The authors encode normalized covariance/cross-correlation matrices of forward-rate dynamics as quantum states and use a phase-estimation-based qPCA circuit to estimate the dominant eigenvalue and eigenvector, which correspond to the principal volatility factors used in HJM. Because of NISQ hardware limitations, they adapt the original qPCA method into a hybrid classical-quantum iterative procedure: starting from a random initial state, they repeatedly run the circuit, project onto the bitstring associated with the largest eigenvalue, and feed the resulting state back as the next initialization until the eigenvector estimate stabilizes. They test the method on small 2x2 and 3x3 financial correlation structures, implemented as 2x2 and 4x4 quantum-state encodings, and evaluate performance on both the IBMQX2 five-qubit superconducting quantum processor and the Qiskit simulator. The study compares experimental outputs against exact classical eigendecompositions of the same matrices, reports convergence behavior and fidelity-like agreement, and discusses the impact of circuit depth, gate noise, decoherence, and possible error-mitigation strategies.

**Algorithms used:** qPCA, Quantum Phase Estimation, PCA
**Frameworks:** Qiskit, IBM Quantum

**Experimental setup:** Experiments were run both on the IBMQX2 five-qubit superconducting quantum processor and on the Qiskit built-in simulator. The implementation used a modified qPCA/phase-estimation circuit tailored to NISQ constraints. For the 2x2 case, 3 qubits were used for eigenvector estimation (2 qubits for a 2-bit eigenvalue estimate and 1 qubit for the eigenvector), followed by a 4-qubit quantum phase estimation step for a 3-bit eigenvalue estimate. For the expanded 4x4 case, 3 qubits were used (1 qubit for a 1-bit eigenvalue estimate and 2 qubits for the eigenvector). Each experiment was repeated 8192 shots. Measurements were taken in the computational basis and additional rotated bases (x, y, and an arbitrary basis) to estimate relative phases and reduce systematic errors.

**Dataset:** Historical data for time-maturing forward rates used to build 2x2 and 3x3 cross-correlation/covariance matrices. The illustrative 3x3 covariance matrix is based on historical 1-month, 3-month, and 6-month forward rates, taken from a published finance reference (Fig. 19.3 in Wilmott, 2007).
## Findings
- [supported] The paper experimentally implemented a quantum principal component analysis (qPCA) workflow on IBM's 5-qubit IBMQX2 to estimate principal components of small covariance/correlation matrices derived from historical forward-rate data relevant to the Heath-Jarrow-Morton interest-rate model.
- [supported] For the 2x2 normalized covariance matrix, the exact spectral decomposition reported was λ1 = 0.8576 with eigenvector 0.8347|0⟩ + 0.5508|1⟩, and λ2 = 0.1424 with eigenvector 0.5508|0⟩ - 0.8347|1⟩.
- [supported] On real hardware, the 2x2 experiment produced an estimated dominant eigenvector |u_max⟩ ≈ [(0.87 ± δ) - i(0.10 ± δ)]|0⟩ + [(0.47 ± δ) + i(0.10 ± δ)]|1⟩, qualitatively close to the exact dominant eigenvector; results were obtained on real IBM hardware with additional simulator runs.
- [supported] In the 2x2 case, the iterative eigenvector estimation stabilized by the first iteration and was stopped after four iterations, with z-basis coefficient estimates across iterations remaining near 0.68-0.72 for |0⟩ and 0.69-0.73 for |1⟩.
- [supported] For the 2x2 case, simulator-based quantum phase estimation with 3-bit precision produced the state |111⟩ ⊗ [0.8150|0⟩ + 0.5794|1⟩], corresponding to an estimated eigenvalue of 0.875 and reported fidelity F = 0.965 relative to the target eigenvector.
- [supported] The real-hardware 3-bit quantum phase estimation for the 2x2 case failed due to decoherence, yielding an almost homogeneous output distribution rather than a clear eigenvalue peak.
- [supported] For the 4x4 embedding of the 3x3 covariance matrix, the exact dominant eigenvalue reported was λ4 = 0.800 with eigenvector (0.669, 0.516, 0.536, 0.000) in the {|00⟩,|01⟩,|10⟩,|11⟩} basis.
- [supported] On the 4x4 problem, the authors report that real-hardware results were not useful because circuit depth and noise were too high; they estimate at least 18 entangling gates and state that experimental errors prevented extraction of meaningful information.
- [supported] The authors explicitly conclude that they obtained a reasonable approximation for the maximum eigenvalue and eigenvector only in the 2x2 case, while the 4x4 case exhausted the capabilities of the available processor in terms of gate fidelities, connectivity, and qubit count.
- [speculative] The authors argue that qPCA could reduce the number of noisy factors in multifactor HJM simulations and thereby help construct future quantum Monte Carlo algorithms for pricing interest-rate derivatives, but this full pricing workflow was not implemented here.
- [speculative] The paper suggests that practical quantum-computing applications in finance may be achievable in the near future or in the NISQ era, but this is not empirically demonstrated by the reported experiments.
- [speculative] The manuscript references exponential speedup properties of qPCA from prior literature, but no speedup or quantum advantage over classical methods is empirically demonstrated in this paper.

**Results summary:** This peer-reviewed empirical paper presents a small-scale experimental qPCA implementation for financial covariance matrices relevant to the Heath-Jarrow-Morton framework, using IBM's 5-qubit IBMQX2 and Qiskit simulation. The main empirical success is on a 2x2 normalized covariance matrix derived from historical forward-rate data, where the dominant eigenvector was estimated on real hardware with qualitative agreement to the exact solution, and simulator-based quantum phase estimation gave a 3-bit dominant eigenvalue estimate of 0.875 versus the exact 0.8576, with reported fidelity 0.965 for the eigenvector. However, when scaling to a 4x4 embedding of a 3x3 covariance matrix, circuit depth and noise on real hardware prevented useful extraction of the dominant principal component; the authors report that current hardware limitations, especially decoherence and two-qubit gate errors, made the larger instance unsuccessful. Overall, the paper demonstrates proof-of-concept feasibility for very small instances on NISQ hardware, but not end-to-end derivative pricing or any empirical quantum advantage.

**Performance claims:**
- 2x2 normalized covariance matrix exact dominant eigenvalue: 0.8576
- 2x2 exact dominant eigenvector: 0.8347|0⟩ + 0.5508|1⟩
- 2x2 hardware-estimated dominant eigenvector: [(0.87 ± δ) - i(0.10 ± δ)]|0⟩ + [(0.47 ± δ) + i(0.10 ± δ)]|1⟩
- 2x2 iterative z-basis coefficients across four iterations: c0 ≈ 0.719, 0.707, 0.720, 0.680 and c1 ≈ 0.695, 0.707, 0.694, 0.734
- 2x2 simulator quantum phase estimation produced 3-bit eigenvalue estimate 0.111₂ = 0.875
- Reported fidelity between simulator QPE eigenvector and target eigenvector: F = 0.965
- Each iteration/evaluation used 8192 shots
- Estimated experimental error per two-qubit gate assumed by authors: 8%
- Estimated total error for 2x2 eigenvector experiment: 24% gate-related plus about 11% statistical, for about 35% total
- 4x4 exact eigenvalues reported: 0.000, 0.031, 0.169, 0.800
- 4x4 exact dominant eigenvector reported: (0.669, 0.516, 0.536, 0.000)
- 4x4 circuit required at least 18 entangling gates
- Authors state estimated total coefficient error for 4x4 exceeded 100%
## Quantum advantage claim
**Classification:** speculative

The paper does not demonstrate quantum advantage. Empirical results are limited to very small matrices, with only the 2x2 case working reasonably on real hardware and the 4x4 case failing on hardware due to noise and circuit depth. Any claims about future usefulness, scalability, or speedup are forward-looking rather than demonstrated.
## Limitations
- Experiments were limited to a five-qubit IBMQX2 device, restricting the study to only 2×2 and 3×3 cross-correlation matrices (implemented as 2×2 and 4×4 quantum states).
- Current NISQ hardware is described as small and noisy, which limits applicability to toy models rather than realistic production-scale derivative pricing.
- For the 4×4 matrix, circuit depth was too large and experimental errors prevented extraction of useful information from the real quantum processor.
- Quantum phase estimation with higher precision decohered on the real device; the authors report an almost homogeneous output distribution due to loss of coherence.
- The study exhausted the computational power of the processor in terms of gate fidelities, connectivity, and number of qubits.
- The implementation only estimated principal components as a first step; it did not fully simulate the Heath-Jarrow-Morton model or perform end-to-end derivative pricing.
- The empirical demonstration used historical data for only two and three time-maturing forward rates, limiting external validity for richer term-structure settings.
- The qPCA approach assumes the covariance/correlation matrix can be well approximated by a low-rank matrix, which may not hold universally.
- The algorithm assumes efficient generation of the unitary exp(itσ); this relies on access assumptions that may be difficult to realize efficiently at larger scales.
- The precision of eigenvalue estimation was limited by processor size, constraining the accuracy of the reported results.
- Error estimates are very coarse: the paper uses a worst-case upper-bound error model because the authors lacked direct access to the processor and could not disentangle gate, decoherence, measurement, crosstalk, and other noise sources.
- For the 4×4 case, the estimated total error exceeded 100%, making the raw result effectively unreliable without mitigation.
- Reproducibility is partially constrained because the code depends on Qiskit version 0.7.1 and hardware calibrations/noise characteristics of IBMQX2 at the time of execution may no longer be available.
- [inferred] No benchmark against state-of-the-art classical PCA or classical HJM calibration/simulation runtimes is provided, so practical quantum advantage is not demonstrated.
- [inferred] The paper does not quantify end-to-end financial impact, such as pricing accuracy improvements, calibration quality, or risk metric improvements from using qPCA.
- [inferred] Scalability to realistic financial datasets with many maturities, larger covariance matrices, and production latency requirements is not empirically validated.
- [inferred] The use of a very small sample of maturities and a single illustrative covariance matrix limits confidence that results generalize across market regimes or instruments.
- [inferred] The claimed exponential speedup of qPCA is not empirically substantiated on hardware; the study demonstrates feasibility only at very small scale.
## Open questions
- Can the proposed qPCA-based approach scale to larger covariance matrices relevant for realistic HJM term-structure models?
- How well will the method perform on improved hardware with higher gate fidelity, better connectivity, and more qubits?
- To what extent can error mitigation recover useful results for larger instances such as the 4×4 case and beyond?
- How many principal components are sufficient in practice for accurate quantum simulation of HJM across different markets and datasets?
- Can a full quantum algorithm for simulating the HJM model and pricing interest-rate derivatives be implemented efficiently end to end?
- Will the low-rank structure exploited here remain strong for broader sets of maturities and more complex market conditions?
- What is the true resource scaling, including state preparation and controlled-unitary synthesis, for financially relevant problem sizes?
- How robust is the approach to realistic hardware noise, decoherence, readout errors, and non-Markovian effects?
- Can the method deliver practical quantum advantage over optimized classical PCA and Monte Carlo workflows used in finance?
- [inferred] How sensitive are the results to the choice of historical dataset, market regime, and covariance estimation methodology?
- [inferred] What are the implications of approximate eigenvector/eigenvalue recovery on downstream derivative prices and hedging decisions?

**Future work:**
- Apply error mitigation techniques, including Richardson extrapolation and readout error mitigation, to improve results on noisy hardware.
- Use better experimental hardware with improved gate fidelities, connectivity, and qubit counts to run deeper circuits successfully.
- Design a general quantum algorithm to fully simulate the HJM model on quantum computers for pricing interest-rate financial derivatives.
- Develop quantum Monte Carlo algorithms for the HJM framework after dimensionality reduction via qPCA.
- Increase eigenvalue precision and improve eigenvector estimation as hardware capabilities advance.
- Extend the approach from small proof-of-concept matrices to larger cross-correlation matrices built from more maturities.
- Further optimize the algorithm for NISQ devices to reduce gate count and alleviate decoherence constraints.
- [inferred] Benchmark the quantum approach against strong classical baselines on runtime, accuracy, and financial relevance.
- [inferred] Validate the method on larger and more diverse real market datasets and on actual derivative pricing tasks rather than only PCA subroutines.
- [inferred] Study production-oriented issues such as calibration stability, reproducibility across hardware backends, and integration into financial risk systems.
## Key ideas
- #idea:hybrid-approach — The paper uses a hybrid classical-quantum iterative qPCA workflow, with classical preprocessing and repeated circuit runs to estimate dominant principal components of HJM covariance matrices.
- #idea:near-term-feasibility — It presents a NISQ proof-of-concept on IBM's 5-qubit hardware for very small covariance matrices relevant to interest-rate derivative pricing.
- #idea:quantum-advantage — The paper positions qPCA as a possible building block for future quantum HJM simulation and quantum Monte Carlo workflows, but this advantage claim is only speculative.
- #idea:near-term-feasibility — Real hardware produced a qualitatively reasonable dominant eigenvector estimate for the 2x2 case, while simulator runs achieved a reported eigenvector fidelity of 0.965.
- #idea:hybrid-approach — The work frames dimensionality reduction of stochastic factors as a practical first step before full end-to-end quantum derivative pricing.
## Contradictions
- The paper suggests near-term applicability in finance, but its hardware results fail already at the 4x4 embedded covariance-matrix case, indicating a contradiction between NISQ-feasibility rhetoric and observed scalability limits.
- The manuscript references potential qPCA speedups, yet provides no benchmark against classical PCA or classical HJM workflows; this contradicts any implied claim of quantum superiority.
- Although framed as relevant to derivative pricing, the study only demonstrates a PCA subroutine and does not implement end-to-end HJM simulation or pricing, weakening broader performance claims.
- This aligns with critiques such as 2021_Abbas_QuantumMachineLearningFinance, which caution that many NISQ-era finance papers overstate quantum advantage without strong empirical comparison.
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->

## Experiment details
### Input
Input consists of normalized covariance/cross-correlation matrices derived from historical forward-rate data. The main example uses a 3x3 covariance matrix for 1-, 3-, and 6-month rates: [[0.000189, 0.000097, 0.000091], [0.000097, 0.000106, 0.000101], [0.000091, 0.000101, 0.000126]]. A 2x2 submatrix was normalized by its trace to form a density-matrix-like input rho2 = [[0.6407, 0.3288], [0.3288, 0.3593]]. The 3x3 case was embedded into a 4x4 density matrix rho4 for two-qubit encoding. The paper does not report the raw sample size, exact time span, or preprocessing pipeline beyond covariance/correlation construction and trace normalization.

### Process
1. Construct covariance/cross-correlation matrices from historical forward-rate data and normalize by trace so they can be treated as density matrices. 2. Build the unitary exp(i t rho) corresponding to the encoded matrix. 3. Run a modified qPCA circuit based on quantum phase estimation, with ancilla qubits encoding a low-bit approximation of the dominant eigenvalue and data qubits encoding the eigenvector. 4. Initialize the eigenvector register in a random state: for the 2x2 case the first iteration used |+>, and for the 4x4 case the initial state was (|00>+|01>+|10>+|11>)/2. 5. Measure and project onto the bitstring corresponding to the largest eigenvalue estimate (e.g., |11> in the 2-bit case), obtaining an approximate dominant eigenvector. 6. Feed this estimated eigenvector back as the initial state and iterate until stabilization; the authors used four iterations. 7. Measure in z basis and also in x, y, and one arbitrary rotated basis to estimate relative phases and average out some systematic errors. 8. After obtaining an eigenvector estimate, run a separate quantum phase estimation step with more ancilla bits to refine the dominant eigenvalue estimate. 9. Compare simulator and hardware outputs with exact classical eigendecomposition results. 10. Assess errors using shot noise and an assumed per-two-qubit-gate error model; discuss possible error mitigation such as Richardson extrapolation and readout mitigation, though these were not fully applied in the reported experiments.

### Output
Outputs are estimated dominant eigenvectors and eigenvalues of the covariance matrices, reported as state amplitudes, bitstring populations, and approximate eigenvalue bitstrings. For the 2x2 case, the hardware experiment produced an eigenvector estimate close to the classical dominant eigenvector and a 2-bit eigenvalue estimate of 0.11, while the simulator gave a 3-bit phase-estimation result of 0.111 (0.875 decimal) with reported fidelity 0.965 relative to the exact eigenvector. Results are compared against exact classical spectral decomposition of the same matrices. Additional outputs include per-iteration population tables, convergence behavior across four iterations, and qualitative comparison between simulator and real hardware, showing that the 4x4 case failed on hardware due to decoherence and gate errors.

### Parameters
- hardware_qubits_total: 5
- matrix_cases: ['2x2', '3x3 embedded as 4x4']
- shots: 8192
- iterations_eigenvector_estimation: 4
- eigenvalue_precision_bits_2x2_initial: 2
- eigenvalue_precision_bits_2x2_qpe: 3
- eigenvalue_precision_bits_4x4: 1
- initial_state_2x2: |+>
- initial_state_4x4: (|00>+|01>+|10>+|11>)/2
- projection_target_2x2: |11>
- arbitrary_basis_angles: {'alpha': 1.0, 'beta': 0.8, 'gamma': 0.16}
- reported_two_qubit_gate_error_assumption: 8% per two-qubit gate
- estimated_total_error_2x2_eigenvector: delta = 0.9 upper bound
- minimum_entangling_gates_4x4: 18

### Hardware
Real-device experiments used the IBMQX2 five-qubit superconducting quantum processor from IBM Quantum. Simulations used the Qiskit built-in simulator (paper notes Qiskit version 0.7.1 for code). The authors state they did not have direct access to the exact low-level processor circuit/transpilation details, limiting precise attribution of errors. No explicit noise model or transpilation settings are reported. The 2x2 eigenvector circuit involved at least three two-qubit gates; the 3-bit phase-estimation circuit involved at least six entangling gates; the 4x4 implementation required controlled-U decomposition with at least 18 entangling gates, causing severe decoherence on hardware.

### Reproducibility
Code is publicly available on GitHub (https://github.com/amartinfer/QPCA.git), and the paper specifies use of Qiskit version 0.7.1. Matrix inputs are reported explicitly for the main examples, enabling partial replication. However, the underlying historical forward-rate dataset is not fully described in terms of source file, sample size, or time period, and hardware-level execution details/transpilation are not fully available. Overall reproducibility is moderate: simulator experiments are reasonably reproducible, but exact hardware replication is limited.
