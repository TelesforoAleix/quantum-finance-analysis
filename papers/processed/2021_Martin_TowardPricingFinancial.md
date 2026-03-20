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
journal_or_venue: PHYSICAL REVIEW RESEARCH
methodology_tags:
- quantum-simulation
- quantum-ML
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2021_Abbas_QuantumMachineLearningFinance
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-19T23:09:02.805005'
step1_model: Mistral-Large-3
step2_date: '2026-03-19T23:09:07.039615'
step2_model: Mistral-Large-3
step3_date: '2026-03-19T12:07:47.188336'
step3_model: Mistral-Large-3
step4_date: '2026-03-19T23:09:27.384177'
step4_model: Mistral-Large-3
step5_date: '2026-03-19T23:10:03.680398'
step5_model: Mistral-Large-3
step6_date: '2026-03-19T23:10:08.147205'
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
- method/variational
- method/classical-simulation
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
This paper explores the application of quantum computing to pricing financial derivatives, specifically focusing on the Heath-Jarrow-Morton (HJM) framework for modeling interest rate dynamics. The authors implement a quantum principal component analysis (qPCA) algorithm on IBM's five-qubit quantum computer to reduce the number of noisy factors in the HJM model, improving computational efficiency. The study demonstrates the feasibility of using quantum computing for financial simulations, even with current noisy intermediate-scale quantum (NISQ) technology.
## Methodology
The paper presents an empirical study applying quantum principal component analysis (qPCA) to reduce the number of noisy factors in the Heath-Jarrow-Morton (HJM) model for pricing interest-rate financial derivatives. The research employs a hybrid classical-quantum approach, where the qPCA algorithm is used to estimate the principal components of cross-correlation matrices derived from historical financial data for time-maturing forward rates. The study implements the algorithm on both a quantum simulator and the IBMQX2 quantum processor, focusing on 2×2 and 3×3 covariance matrices. The methodology involves iterative refinement of eigenvector estimations, followed by quantum phase estimation to improve eigenvalue accuracy. Error mitigation techniques are discussed to address decoherence and gate errors in the quantum hardware.

**Algorithms used:** Quantum Principal Component Analysis (qPCA), Quantum Phase Estimation
**Frameworks:** Qiskit

**Experimental setup:** Experiments were conducted using the IBMQX2 five-qubit superconducting quantum processor and the Qiskit simulator. The quantum circuits were designed to encode covariance matrices into quantum states, with 2×2 and 4×4 matrices tested. The 2×2 case used three qubits (two for eigenvalue approximation, one for eigenvector), while the 4×4 case used three qubits (one for eigenvalue, two for eigenvector). Each iteration of the algorithm was averaged over 8,192 realizations to account for statistical errors. Measurements were performed in multiple bases (z, x, y, and arbitrary directions) to compute relative phases and mitigate systematic errors.

**Dataset:** Historical financial data for 1-, 3-, and 6-month time-maturing forward rates, used to construct 2×2 and 3×3 cross-correlation matrices. Specifically, the covariance matrix from Ref. [36] (Fig. 19.3) was employed, with values such as: σ3 = [[0.000189, 0.000097, 0.000091], [0.000097, 0.000106, 0.000101], [0.000091, 0.000101, 0.000126]].
## Findings
- [supported] The quantum principal component analysis (qPCA) algorithm was implemented on the IBMQX2 quantum computer to reduce the number of noisy factors in the Heath-Jarrow-Morton (HJM) model for pricing interest-rate financial derivatives.
- [supported] For a 2×2 covariance matrix, the qPCA algorithm achieved an eigenvector estimation with a fidelity of 0.965 compared to the exact eigenvector when simulated on QISKIT.
- [supported] The 2×2 matrix experiment on real hardware yielded an eigenvector approximation of |umax⟩ = [(0.87 ± 0.9) - i(0.10 ± 0.9)]|0⟩ + [(0.47 ± 0.9) + i(0.10 ± 0.9)]|1⟩, with an estimated error of δ = 0.9 per two-qubit gate.
- [supported] The 3-bit quantum phase estimation for the 2×2 matrix on the QISKIT simulator produced an eigenvalue approximation of 0.875 (binary 0.111), closely matching the exact eigenvalue of 0.8576.
- [supported] For the 4×4 covariance matrix, the QISKIT simulator provided an eigenvector estimation, but real hardware results were inconclusive due to decoherence and gate errors, with an estimated error exceeding 100%.
- [speculative] The authors suggest that error mitigation techniques, such as Richardson’s extrapolation or readout error mitigation, could improve results for larger matrices on current NISQ devices.
- [speculative] The paper claims that practical applications of quantum computers in finance, including full simulation of the HJM model, will be achievable in the near future as hardware improves.
- [supported] This study represents the first quantum computing experiment in financial option pricing and the largest implementation of qPCA on a quantum platform to date.

**Results summary:** The paper demonstrates the application of quantum principal component analysis (qPCA) to reduce the dimensionality of the Heath-Jarrow-Morton (HJM) model for pricing interest-rate financial derivatives. The algorithm was implemented on the IBMQX2 quantum computer for 2×2 and 3×3 covariance matrices derived from historical data. For the 2×2 matrix, the qPCA algorithm successfully estimated the principal eigenvector and eigenvalue with high fidelity in simulation (0.965) and reasonable accuracy on real hardware, despite an estimated error of δ = 0.9 per two-qubit gate. The 3-bit quantum phase estimation further refined the eigenvalue approximation. However, for the 4×4 matrix, the depth of the quantum circuit led to decoherence and errors on real hardware, rendering results inconclusive, though simulations remained promising. The authors highlight the potential of error mitigation techniques to address these challenges and suggest that this work paves the way for broader quantum applications in finance.

**Performance claims:**
- Fidelity of 0.965 between the simulated eigenvector and the exact eigenvector for the 2×2 matrix
- Eigenvector approximation error of δ = 0.9 per two-qubit gate for the 2×2 matrix on real hardware
- 3-bit eigenvalue approximation of 0.875 (binary 0.111) for the 2×2 matrix, closely matching the exact eigenvalue of 0.8576
- Estimated error exceeding 100% for the 4×4 matrix on real hardware due to circuit depth and decoherence
## Quantum advantage claim
**Classification:** speculative

The paper claims that quantum computers could provide a significant computational advantage for simulating the HJM model by reducing the number of noisy factors and enabling more accurate pricing of financial derivatives. However, this advantage is not demonstrated on real hardware for larger matrices (e.g., 4×4), and results are primarily derived from simulations. The authors suggest that near-term improvements in quantum hardware and error mitigation techniques could realize this advantage.
## Limitations
- Experiments limited to small qubit count (5 qubits on IBMQX2), restricting the problem size to 2×2 and 3×3 covariance matrices
- Algorithm depth and gate count lead to decoherence and high error rates on real quantum hardware, particularly for the 4×4 matrix case
- Only tested on historical financial data for 1-, 3-, and 6-month forward rates; generalizability to other financial instruments not demonstrated
- Assumed non-negative covariance matrices with trace equal to 1, limiting applicability to other types of financial data
- Error estimation assumes worst-case scenario (8% error per two-qubit gate), which may overstate limitations but reflects NISQ-era constraints
- No noise mitigation techniques applied beyond basic error averaging, which may limit accuracy on real hardware
- [inferred] Lack of comparison with classical PCA performance for the same dataset size and problem complexity
- [inferred] No assessment of algorithm robustness to different market conditions or volatility regimes
- [inferred] Limited exploration of how qubit connectivity constraints on IBMQX2 affect circuit compilation and performance
## Open questions
- How does the quantum PCA algorithm scale to larger covariance matrices (e.g., 10×10 or higher) relevant for production financial applications?
- What is the minimum qubit count and gate fidelity required to achieve quantum advantage for financial derivative pricing?
- How does the algorithm perform under different market conditions (e.g., high volatility periods) compared to classical methods?
- Can error mitigation techniques (e.g., Richardson extrapolation, readout error mitigation) sufficiently improve results for the 4×4 case and beyond?
- What is the impact of different quantum hardware architectures (e.g., trapped ions, photonics) on the algorithm's performance?
- How does the quantum PCA approach compare to other quantum algorithms (e.g., HHL for linear systems) for financial modeling tasks?

**Future work:**
- Extend the algorithm to larger covariance matrices using more advanced quantum hardware (e.g., IBM Eagle processor)
- Implement and test error mitigation techniques to improve accuracy on NISQ devices
- Develop a full quantum simulation of the Heath-Jarrow-Morton model for pricing interest-rate derivatives
- Compare quantum PCA performance with classical PCA and other quantum algorithms for financial applications
- Explore hybrid quantum-classical approaches to leverage the strengths of both paradigms for financial modeling
- Investigate the algorithm's performance on different types of financial data (e.g., equities, commodities) and market conditions
- Develop methods to reduce circuit depth and gate count to improve performance on near-term quantum devices
- Assess the economic viability of quantum computing for financial applications by estimating the required hardware improvements
## Key ideas
- #idea:quantum-advantage — qPCA demonstrates potential for reducing noisy factors in the HJM model for interest-rate derivatives pricing, with high fidelity (0.965) for small matrices on real quantum hardware
- #idea:near-term-feasibility — Paper suggests NISQ-era applicability for financial simulations despite current hardware limitations, proposing error mitigation as a path forward
- #idea:hybrid-approach — Hybrid classical-quantum workflow (qPCA on IBMQX2 with classical preprocessing) enables practical implementation for small-scale problems
- #limitation:noise — High error rates (8% per two-qubit gate) and decoherence limit scalability to larger matrices (4×4 case failed without error mitigation)
- #limitation:qubit-count — IBMQX2's 5-qubit limit restricts analysis to 2×2/3×3 covariance matrices, insufficient for real-world financial datasets
- #limitation:no-empirical-validation — No direct comparison with classical PCA or benchmarking of quantum advantage, leaving claims speculative
## Contradictions
- #contradiction:scalability — Paper claims near-term feasibility for financial applications but fails to produce meaningful results for 4×4 matrices due to hardware limitations, contradicting its own speculative advantage claims
- #contradiction:classical-vs-quantum — Lack of comparison with classical PCA leaves quantum advantage claims unsubstantiated, aligning with broader critiques in [2021_Abbas_QuantumMachineLearningFinance] about premature advantage claims in NISQ-era finance papers
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
