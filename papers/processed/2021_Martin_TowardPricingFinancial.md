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
- contradiction:scalability
- contradiction:classical-vs-quantum
doi: 10.1103/PhysRevResearch.3.013167
evidence_type: ''
idea_tags:
- idea:quantum-advantage
- idea:near-term-feasibility
- idea:hybrid-approach
journal_or_venue: Physical Review Research
methodology_tags:
- quantum-simulation
- quantum-ML
- HHL
- variational
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2021_Abbas_QuantumMachineLearningFinance
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T12:05:56.266127'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T12:07:29.128897'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:07:47.188336'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T12:08:57.804875'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T12:09:20.506196'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T12:09:31.240097'
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
- topic/asset-pricing
- method/quantum-simulation
- method/quantum-ML
- method/HHL
- method/variational
- idea/quantum-advantage
- idea/near-term-feasibility
- idea/hybrid-approach
- contradiction/scalability
- contradiction/classical-vs-quantum
title: Toward pricing financial derivatives with an IBM quantum computer
topic_tags:
- derivatives-pricing
- asset-pricing
year: 2021
zotero_key: ''
---

## Abstract summary
This paper explores the application of quantum computing to financial derivative pricing, specifically using the Heath-Jarrow-Morton (HJM) framework for interest rate modeling. The authors implement a quantum principal component analysis (qPCA) algorithm on IBM’s five-qubit quantum computer to reduce the number of noisy factors in the HJM model, improving computational efficiency. The study demonstrates experimental results for small-scale covariance matrices derived from historical financial data, marking a step toward practical quantum advantage in financial simulations.
## Methodology
The paper presents an empirical study applying quantum principal component analysis (qPCA) to reduce the number of noisy factors in the Heath-Jarrow-Morton (HJM) model for pricing interest-rate financial derivatives. The research employs a hybrid classical-quantum approach, where the qPCA algorithm is used to estimate the principal components of cross-correlation matrices derived from historical financial data for time-maturing forward rates. The study implements the algorithm on both a quantum simulator and the IBMQX2 quantum processor, focusing on 2×2 and 3×3 covariance matrices. The methodology involves iterative refinement of eigenvector estimations, followed by quantum phase estimation to improve eigenvalue accuracy. Error mitigation techniques are discussed to address decoherence and gate errors in the quantum hardware.

**Algorithms used:** Quantum Principal Component Analysis (qPCA), Quantum Phase Estimation
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using the IBMQX2 five-qubit superconducting quantum processor and the Qiskit simulator. The quantum circuits were designed to encode covariance matrices into quantum states, with 2×2 and 4×4 matrices tested. The 2×2 case used three qubits (two for eigenvalue approximation, one for eigenvector), while the 4×4 case used three qubits (one for eigenvalue, two for eigenvector). Each iteration of the algorithm was averaged over 8,192 realizations to account for statistical errors. Measurements were performed in multiple bases (z, x, y, and arbitrary directions) to compute relative phases and mitigate systematic errors.

**Dataset:** Historical financial data for 1-, 3-, and 6-month time-maturing forward rates, used to construct 2×2 and 3×3 cross-correlation matrices. Specifically, the covariance matrix from Ref. [36] (Fig. 19.3) was employed, with values such as: σ3 = [[0.000189, 0.000097, 0.000091], [0.000097, 0.000106, 0.000101], [0.000091, 0.000101, 0.000126]].
## Findings
- [supported] Quantum Principal Component Analysis (qPCA) was experimentally implemented on the IBMQX2 5-qubit quantum computer to reduce the number of noisy factors in the Heath-Jarrow-Morton (HJM) model for pricing interest-rate derivatives, using 2×2 and 3×3 cross-correlation matrices based on historical data.
- [supported] For the 2×2 covariance matrix, the qPCA algorithm achieved an estimated eigenvector |umax⟩ = [(0.87 ± 0.9) - i(0.10 ± 0.9)]|0⟩ + [(0.47 ± 0.9) + i(0.10 ± 0.9)]|1⟩, with a fidelity of 0.965 compared to the ideal result from the QISKIT simulator.
- [supported] The 3-bit quantum phase estimation for the 2×2 matrix yielded an eigenvalue approximation of 0.875 (binary 0.111), closely matching the exact eigenvalue of 0.8576.
- [supported] Results for the 2×2 matrix were obtained on both the QISKIT simulator and real IBMQX2 hardware, with simulator results showing near-ideal performance and hardware results limited by decoherence and gate errors.
- [supported] For the 4×4 matrix, the qPCA algorithm's depth exceeded the capabilities of the IBMQX2 processor, leading to decoherence and errors exceeding 100%, rendering results meaningless without error mitigation techniques.
- [speculative] The authors suggest that practical applications of quantum computing in finance, including full simulation of the HJM model, will be achievable in the near future with improvements in quantum hardware.
- [speculative] Quantum advantage in financial modeling may emerge from the ability to handle larger covariance matrices and more noisy factors than classical methods, though this remains unproven on current NISQ devices.

**Results summary:** The paper demonstrates the first experimental implementation of quantum computing for financial derivative pricing, specifically using qPCA to reduce the dimensionality of the HJM model on the IBMQX2 quantum processor. For a 2×2 covariance matrix, the algorithm successfully estimated the principal components with high fidelity (0.965) on the simulator and reasonable accuracy on real hardware, despite noise and decoherence. However, the 4×4 matrix case proved too complex for the current hardware, highlighting the limitations of NISQ devices. The results suggest that quantum computing could enhance financial modeling by enabling more accurate simulations with reduced computational trade-offs, though practical quantum advantage remains speculative at this stage.

**Performance claims:**
- Fidelity of 0.965 between the estimated and ideal eigenvector for the 2×2 matrix (simulator results)
- Eigenvalue estimation of 0.875 (3-bit precision) for the 2×2 matrix, compared to the exact value of 0.8576
- Error rate of ±0.9 for the 2×2 matrix eigenvector coefficients, based on two-qubit gate and measurement fidelity
- Over 100% estimated error for the 4×4 matrix due to circuit depth and hardware limitations
## Quantum advantage claim
**Classification:** speculative

The paper claims that quantum computing could provide a computational advantage for financial modeling by enabling more accurate simulations of the HJM model with reduced trade-offs between noisy factors and computational time. However, this advantage is not demonstrated on real hardware for practical problem sizes, and the results are limited to small-scale simulations (2×2 and 4×4 matrices) with significant errors for the larger case.
## Limitations
- Experiments limited to 5 qubits (IBMQX2 quantum computer), restricting the problem size to 2×2 and 3×3 cross-correlation matrices
- Hardware noise and decoherence significantly affect results, especially for deeper circuits (e.g., 4×4 matrix case)
- Error rates of ~8% per two-qubit gate accumulate, leading to high total error (e.g., >100% for 4×4 matrix)
- Only tested on historical data for 1-, 3-, and 6-month forward rates; generalizability to other financial instruments unclear
- No noise mitigation techniques applied, limiting accuracy on real quantum hardware
- Algorithm depth exceeds current NISQ device capabilities for larger matrices (e.g., 4×4 case)
- Reproducibility constrained by limited access to IBMQX2 and lack of detailed error characterization
- [inferred] No comparison with classical PCA performance or state-of-the-art classical solvers for financial derivative pricing
- [inferred] Limited exploration of alternative quantum algorithms for principal component analysis in finance
## Open questions
- How does the quantum PCA algorithm scale to larger matrices (e.g., 10×10 or higher) required for practical financial applications?
- What is the impact of different noise profiles (e.g., amplitude damping, phase flip) on solution quality?
- Can error mitigation techniques (e.g., Richardson extrapolation, readout error mitigation) sufficiently improve results for larger matrices?
- How does the quantum algorithm perform under real-time market data conditions compared to synthetic/historical data?
- What is the minimum qubit count and gate fidelity required to achieve quantum advantage for financial derivative pricing?
- How does the quantum PCA approach compare to hybrid quantum-classical methods for dimensionality reduction in finance?

**Future work:**
- Test on larger quantum processors (e.g., IBM Eagle or Osprey) to evaluate scalability
- Implement error mitigation techniques to improve accuracy for larger matrices
- Extend the algorithm to full Heath-Jarrow-Morton model simulation for multi-factor interest rate derivatives
- Compare quantum PCA performance with classical methods for real-world financial datasets
- Explore alternative quantum algorithms (e.g., variational quantum eigensolvers) for principal component analysis in finance
- Develop hybrid quantum-classical approaches to leverage near-term quantum devices for financial modeling
- Investigate the impact of different volatility factorizations on pricing accuracy
- Apply the method to other financial instruments (e.g., swaptions, caps/floors) beyond forward rates
## Key ideas
- #idea:quantum-advantage — qPCA demonstrates potential for reducing noisy factors in the HJM model for interest-rate derivatives pricing, with high fidelity (0.965) for small matrices on real quantum hardware
- #idea:near-term-feasibility — Paper suggests NISQ-era applicability for financial simulations despite current hardware limitations
- #idea:hybrid-approach — Hybrid classical-quantum workflow (qPCA on IBMQX2 with classical preprocessing) enables practical implementation
- #limitation:noise — High error rates (8% per two-qubit gate) and decoherence limit scalability to larger matrices (4×4 case failed without error mitigation)
- #limitation:qubit-count — IBMQX2's 5-qubit limit restricts analysis to 2×2/3×3 covariance matrices, insufficient for real-world financial datasets
- #limitation:no-empirical-validation — No direct comparison with classical PCA or benchmarking of quantum advantage
## Contradictions
- #contradiction:scalability — Paper claims near-term feasibility for financial applications but fails to produce meaningful results for 4×4 matrices due to hardware limitations, contradicting its own speculative advantage claims
- #contradiction:classical-vs-quantum — Lack of comparison with classical PCA leaves quantum advantage claims unsubstantiated, aligning with broader critiques in [2021_Abbas_QuantumMachineLearningFinance] about premature advantage claims in NISQ-era finance papers
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
