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
- variational
- classical-simulation
paper_type: ''
quantum_advantage_claim: speculative
related_papers:
- 2020_Rebentrost_QuantumPrincipalComponentAnalysis
- 2019_Lloyd_QuantumAlgorithmsFinance
relevance_phase1: high
relevance_phase3: high
source_type: peer-reviewed-empirical
source_type_confidence: high
step1_date: '2026-03-18T22:46:19.290149'
step1_model: Mistral-Large-3
step2_date: '2026-03-18T22:46:23.026550'
step2_model: Mistral-Large-3
step3_date: '2026-03-18T22:46:28.941830'
step3_model: Mistral-Large-3
step4_date: '2026-03-18T22:47:12.253612'
step4_model: Mistral-Large-3
step5_date: '2026-03-18T22:47:21.261793'
step5_model: Mistral-Large-3
step6_date: '2026-03-18T22:47:28.680696'
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
title: Toward pricing financial derivatives with an IBM quantum computer
topic_tags:
- derivatives-pricing
- asset-pricing
year: 2021
zotero_key: ''
---

## Abstract summary
This paper explores the application of quantum computing to price financial derivatives, specifically focusing on the Heath-Jarrow-Morton (HJM) framework for modeling interest rate dynamics. The authors use quantum principal component analysis (qPCA) to reduce the number of noisy factors in the HJM model, improving computational efficiency. The study demonstrates the approach experimentally on an IBM quantum computer, marking an early step toward scalable quantum algorithms for financial simulations.
## Methodology
The paper presents an empirical study employing quantum principal component analysis (qPCA) to reduce the number of noisy factors in the Heath-Jarrow-Morton (HJM) model for pricing interest-rate financial derivatives. The research involves a hybrid classical-quantum approach where the qPCA algorithm is implemented on the IBMQX2 superconducting quantum processor. The methodology includes estimating the principal components of cross-correlation matrices derived from historical financial data for time-maturing forward rates. The study first addresses a 2×2 covariance matrix and then extends to a 4×4 matrix, using iterative quantum circuits to approximate the largest eigenvalues and corresponding eigenvectors. The algorithm is tested both on a quantum simulator (QISKIT) and the real IBM quantum processor, with results compared to classical spectral decomposition.

**Algorithms used:** Quantum Principal Component Analysis (qPCA), Quantum Phase Estimation
**Frameworks:** QISKIT

**Experimental setup:** The experiments were conducted using the IBMQX2 five-qubit superconducting quantum processor and the QISKIT simulator. The quantum circuits were designed to encode the covariance matrices of financial data into quantum states, with controlled unitary operations applied to perform the qPCA. The setup involved 3 to 5 qubits for eigenvalue and eigenvector estimation, with iterative refinements to improve accuracy. Measurements were performed in multiple bases (z, x, y, and arbitrary directions) to mitigate systematic errors and enhance fidelity.

**Dataset:** Historical data for 1-, 3-, and 6-month forward rates, specifically using the covariance matrix from Ref. [36] (Fig. 19.3). The 2×2 and 3×3 submatrices of this covariance matrix were used for the experiments.
## Findings
- [supported] The quantum principal component analysis (qPCA) algorithm was implemented on the IBMQX2 quantum computer to reduce the number of noisy factors in the Heath-Jarrow-Morton (HJM) model for pricing interest-rate financial derivatives.
- [supported] For a 2 × 2 cross-correlation matrix, the qPCA algorithm achieved an estimated eigenvector |umax⟩ = [(0.87 ± 0.09) - i(0.10 ± 0.09)]|0⟩ + [(0.47 ± 0.09) + i(0.10 ± 0.09)]|1⟩, with an eigenvalue estimation of 0.875 (3-bit precision) and a fidelity of 0.965 compared to the exact eigenvector.
- [supported] The 2 × 2 matrix results were obtained from both the QISKIT simulator and the real IBMQX2 quantum processor, with the simulator yielding near-ideal results.
- [supported] For the 4 × 4 matrix, the algorithm's depth exceeded the capabilities of the IBMQX2 processor, leading to decoherence and errors that prevented meaningful results without error mitigation techniques.
- [supported] The study demonstrates the first experimental implementation of qPCA on a quantum computer for financial applications, specifically for interest-rate derivative pricing.
- [speculative] The authors suggest that practical applications of quantum computers in finance will be achievable in the near future, even with current noisy intermediate-scale quantum (NISQ) technology.
- [speculative] The paper posits that reducing the number of noisy factors in the HJM model via qPCA could enable the construction of a general quantum Monte Carlo algorithm for financial simulations.
- [disputed] The claim of achieving useful results for the 4 × 4 matrix is disputed due to the high error rates (over 100%) observed, which render the results meaningless without error mitigation.

**Results summary:** The paper presents an empirical implementation of quantum principal component analysis (qPCA) on the IBMQX2 quantum computer to reduce the dimensionality of the Heath-Jarrow-Morton (HJM) model for pricing interest-rate financial derivatives. The study successfully demonstrates the algorithm on a 2 × 2 cross-correlation matrix, achieving high fidelity (0.965) for the estimated eigenvector and eigenvalue. However, the 4 × 4 matrix implementation faced significant challenges due to the depth of the quantum circuit, leading to decoherence and high error rates on the real hardware. While the QISKIT simulator showed promise for larger matrices, the current NISQ hardware limitations prevent meaningful results without error mitigation techniques. The work marks a step toward practical quantum computing applications in finance but highlights the need for improved hardware or error correction methods.

**Performance claims:**
- 0.965 fidelity for the estimated eigenvector of the 2 × 2 matrix compared to the exact eigenvector
- 0.875 eigenvalue estimation (3-bit precision) for the 2 × 2 matrix
- 8% error per two-qubit gate assumed for error estimation
- Over 100% estimated error for the 4 × 4 matrix coefficients due to the high number of entangling gates
## Quantum advantage claim
**Classification:** speculative

The paper claims that quantum computers could provide a significant computational advantage for financial simulations by reducing the number of noisy factors in the HJM model. However, this advantage is speculative as it is based on simulations and small-scale experiments on real hardware (IBMQX2), which are limited by noise and decoherence. No empirical demonstration of quantum advantage over classical methods is provided.
## Limitations
- Experiments conducted on a small-scale quantum processor (IBMQX2 with 5 qubits), limiting the size of the covariance matrices (2×2 and 3×3) that could be analyzed
- High error rates in quantum gates (estimated 8% per two-qubit gate) and decoherence effects, particularly evident in the 4×4 matrix case, leading to unreliable results
- Algorithm depth and gate count constraints due to NISQ-era hardware limitations, preventing meaningful results for larger matrices
- Use of synthetic or simplified covariance matrices based on historical data, which may not fully represent real-world financial market complexities
- Lack of noise mitigation techniques applied, which could improve the fidelity of results on real hardware [inferred]
- No comparison with classical PCA or other state-of-the-art classical methods to benchmark quantum advantage [inferred]
- Limited reproducibility due to hardware noise and variability in quantum processor performance over time [inferred]
- Assumption that the covariance matrix can be well-approximated by a low-rank matrix, which may not hold for all financial datasets [inferred]
- Statistical errors in measurements due to finite sampling (8192 realizations per iteration), which may affect the accuracy of eigenvector and eigenvalue estimations
- Dependence on hybrid classical-quantum approaches without full end-to-end quantum simulation of the HJM model
## Open questions
- How does the quantum PCA algorithm perform with larger covariance matrices (e.g., 10×10 or higher) that are more representative of real-world financial datasets?
- What is the impact of different noise profiles (e.g., depolarizing, amplitude damping) on the accuracy of the qPCA algorithm?
- Can error mitigation techniques (e.g., Richardson extrapolation, readout error mitigation) sufficiently improve results for larger matrices on NISQ devices?
- How does the quantum algorithm compare to classical PCA in terms of computational time and accuracy for financial applications?
- What are the minimum hardware requirements (qubit count, gate fidelity, coherence times) to achieve a practical quantum advantage for financial derivative pricing?
- How sensitive is the algorithm to the choice of initial random states or measurement bases?
- Can the algorithm be adapted to handle non-stationary financial data where covariance matrices evolve over time?

**Future work:**
- Extend the algorithm to larger covariance matrices using more advanced quantum processors (e.g., IBM Eagle or Osprey)
- Incorporate error mitigation techniques to improve the fidelity of results on NISQ devices
- Benchmark the quantum PCA algorithm against classical PCA and other dimensionality reduction methods for financial datasets
- Develop a full quantum simulation of the Heath-Jarrow-Morton (HJM) model for pricing interest-rate derivatives
- Explore hybrid quantum-classical approaches to integrate the qPCA algorithm into existing financial modeling frameworks
- Investigate the use of quantum algorithms for other financial applications, such as risk analysis or portfolio optimization
- Test the algorithm on real-world financial datasets to validate its practical applicability
- Optimize the quantum circuit to reduce gate count and depth, improving performance on NISQ devices
## Key ideas
- #idea:quantum-advantage — qPCA demonstrates potential for reducing noisy factors in the HJM model for interest-rate derivatives pricing, with high fidelity (0.965) for small matrices on real quantum hardware
- #idea:near-term-feasibility — Paper suggests NISQ-era applicability for financial simulations despite current hardware limitations
- #idea:hybrid-approach — Hybrid classical-quantum workflow (qPCA on IBMQX2 with classical preprocessing) enables practical implementation
- #limitation:noise — High error rates (8% per two-qubit gate) and decoherence limit scalability to larger matrices (4×4 case failed without error mitigation)
- #limitation:qubit-count — IBMQX2's 5-qubit limit restricts analysis to 2×2/3×3 covariance matrices, insufficient for real-world financial datasets
- #limitation:no-empirical-validation — No direct comparison with classical PCA or benchmarking of quantum advantage
## Contradictions
- #contradiction:scalability — Paper claims near-term feasibility for financial applications but fails to produce meaningful results for 4×4 matrices due to hardware limitations, contradicting its own speculative advantage claims
- #contradiction:classical-vs-quantum — [Inferred] Lack of comparison with classical PCA leaves quantum advantage claims unsubstantiated, aligning with broader critiques in [2021_Abbas_QuantumMachineLearningFinance] about premature advantage claims in NISQ-era finance papers
## Notable quotes
<!-- Researcher-added — verbatim quotes with page references -->

## Researcher notes
<!-- Researcher-added — not LLM generated -->
