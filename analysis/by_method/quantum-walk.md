# Quantum Walk

**Papers:** 5 | **Theoretical:** 2 | **Review:** 1

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |
| [[2024_KI_QuantumFinance]] | 2024 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation | speculative | high |
| [[2021_Bennett_QuantumOptimisationVia]] | 2022 | peer-reviewed-theoretical | portfolio-optimisation | theoretical | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, asset-pricing, quantum-cryptography, regulatory-compliance, market-simulation | speculative | high |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 5 |
| risk-modelling | 2 |
| derivatives-pricing | 2 |
| fraud-detection | 2 |
| credit-scoring | 2 |
| asset-pricing | 2 |
| quantum-cryptography | 2 |
| regulatory-compliance | 2 |
| market-simulation | 2 |
| high-frequency-trading | 1 |

## Key Findings

- [supported] The review analyzes 44 papers from 2003 to 2023 on classical and quantum machine learning (QML) approaches for mutual fund portfolio optimization (PO), identifying a significant gap in literature focusing on mutual funds rather than stocks — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Approximately 67.81% of the reviewed papers were published between 2019 and 2023, indicating QML as a rapidly developing field in financial services — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Quantum algorithms like QAOA and VQE are highlighted as promising tools for solving NP-hard PO problems, though current implementations are limited to NISQ (Noisy Intermediate-Scale Quantum) devices — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Hybrid quantum-classical approaches (e.g., QUBO with simulated annealing, reverse quantum annealing on D-Wave) are the most common implementations due to limited qubit counts and noise in NISQ devices — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Quantum annealers and QUBO models are emerging as de facto standards for solving NP-complete/hard problems in finance, with demonstrated success in small-scale portfolio optimization — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Key research gaps include limited qubit stability, coherence time, error correction, and the need for more effective quantum gate accuracy in NISQ devices — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Most QML implementations for PO rely on hybrid techniques, with classical benchmarks like genetic algorithms, simulated annealing, and Gekko solvers used for evaluation — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The Maximum Amplification Optimisation Algorithm (MAOA) achieves maximum amplification of optimal solutions in combinatorial optimization problems under restricted circuit depth, outperforming Quantum Approximate Optimisation Algorithm (QAOA) and Quantum Walk Optimisation Algorithm (QWOA) in simulation. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] MAOA avoids the computationally expensive variational procedure of QAOA by using a binary marking function on a complete graph with analytically derived optimal parameters (γ = π and t = π/N), repeated for r iterations. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] The MAOA demonstrates substantial speedup over classical random sampling in finding optimal solutions for vehicle routing, portfolio optimization, and normally distributed solution quality problems, with numerical convergence to a theoretically derived upper bound. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] A binary marking function on a complete graph produces the highest amplification of a single marked (optimal) solution, with maximum amplification achieved by repeated application of the same phase-shift and walk-time parameters. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] The MAOA's threshold-finding process reliably navigates to the low-convergence regime of the threshold response curve, ensuring maximum amplification (2r + 1)^2 of marked solutions for a given restricted circuit depth r. — [[2021_Bennett_QuantumOptimisationVia]]
- [speculative] Quantum computing is expected to solve problems intractable for classical computing, such as simulation of complex quantum many-body systems, with linear scaling in system size compared to exponential scaling for classical methods — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
- [speculative] Quantum computing could provide speed-ups for classically tractable problems like searching, with proposed algorithms ranging from quadratic to exponential speed-ups over classical counterparts — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
- [speculative] Finance and economics, due to their reliance on complex calculations, large datasets, and optimization problems, are high-potential sectors for quantum computing applications, particularly in risk assessment, portfolio optimization, fraud detection, and high-frequency trading — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
- [speculative] Quantum computing could enable efficient handling of large-scale, high-dimensional problems in finance and economics without resorting to approximations or truncations required by classical methods, potentially improving accuracy and reducing computational time — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
- [speculative] Quantum computing may face bottlenecks in data loading and readout efficiency, limiting near-term practical gains — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
- [speculative] Three definitions of quantum advantage are proposed: Computational Advantage (quantum supremacy), Quantum Utility, and Practical Quantum Advantage (PQA), with PQA being the most relevant for real-world applications in finance and economics — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
- [speculative] Practical Quantum Advantage (PQA) in finance could contribute up to $622 billion globally by 2035, with the UK potentially seeing an 8.3% economy-wide productivity boost by 2055 due to quantum computing adoption — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
- [speculative] Quantum Phase Estimation (QPE) is a foundational quantum subroutine with applications in Shor’s algorithm, Hamiltonian diagonalization, and solving linear systems, but requires fault-tolerant quantum computing for high accuracy — [[2025_Hlatshwayo_TechnicalReviewQuantum]]
