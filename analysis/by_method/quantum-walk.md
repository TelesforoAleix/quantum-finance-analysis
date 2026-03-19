# Quantum Walk

**Papers:** 6 | **Empirical:** 2 | **Review:** 2

## Papers

| Paper | Year | Source Type | Topics | QA Claim | Relevance |
|-------|------|-------------|--------|----------|-----------|
| [[2025_Hlatshwayo_TechnicalReviewQuantum]] | 2025 | preprint | portfolio-optimisation, risk-modelling, derivatives-pricing, fraud-detection, credit-scoring, high-frequency-trading, asset-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2024_KI_QuantumFinance]] | 2024 | peer-reviewed-empirical | portfolio-optimisation, asset-pricing | theoretical | high |
| [[2023_Fernandes_SystematicLiteratureReview]] | 2023 | review-article | portfolio-optimisation, risk-modelling | speculative | high |
| [[2023_Markna_UnveilingAdvancedComputational]] | 2023 | review-article | portfolio-optimisation, risk-modelling, derivatives-pricing, quantum-cryptography, market-simulation | speculative | high |
| [[2021_Bennett_QuantumOptimisationVia]] | 2022 | peer-reviewed-empirical | portfolio-optimisation | theoretical | high |
| [[2020_Kommadi_QuantumComputingSolutions]] | 2020 | technical-report | portfolio-optimisation, risk-modelling, fraud-detection, credit-scoring, quantum-cryptography, high-frequency-trading, regulatory-compliance | speculative | medium |

## Topics Using This Method

| Topic | Papers |
|-------|--------|
| portfolio-optimisation | 6 |
| risk-modelling | 4 |
| quantum-cryptography | 3 |
| derivatives-pricing | 2 |
| fraud-detection | 2 |
| credit-scoring | 2 |
| high-frequency-trading | 2 |
| asset-pricing | 2 |
| market-simulation | 2 |
| regulatory-compliance | 1 |

## Key Findings

- [supported] The quantum algorithm for portfolio optimization can determine the optimal risk-return tradeoff curve and sample from the optimal portfolio using quantum operations on historical asset returns. — [[2024_KI_QuantumFinance]]
- [supported] The algorithm achieves a runtime of O(poly(log(TN))) for analyzing data loaded into quantum random access memory (qRAM), where T is the number of time steps and N is the number of assets, compared to classical O(poly(TN)) runtime. — [[2024_KI_QuantumFinance]]
- [supported] The algorithm prepares the optimal portfolio as a quantum state, allowing sampling of asset weights with probability proportional to their squared portfolio weights, and measurements to determine sector allocations or sub-optimality. — [[2024_KI_QuantumFinance]]
- [supported] The quantum state encoding the covariance matrix can be prepared and measured to identify assets with the largest variances and pairs with the largest covariances. — [[2024_KI_QuantumFinance]]
- [supported] The review analyzes 44 papers from 2003 to 2023 on classical and quantum machine learning (QML) approaches for mutual fund portfolio optimization (PO), identifying key trends and gaps in the literature. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Approximately 67.81% of the reviewed papers were published between 2019 and 2023, indicating QML as a rapidly developing field in financial services. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Quantum algorithms like QAOA and VQE are highlighted as promising tools for solving NP-hard PO problems, though current implementations are limited to NISQ (Noisy Intermediate-Scale Quantum) devices. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Hybrid quantum-classical approaches (e.g., QUBO with simulated annealing, reverse quantum annealing) are the most common methods for PO in the reviewed literature, as pure quantum solutions lack sufficient qubits for large-scale problems. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Quantum annealers (e.g., D-Wave) and QUBO models are becoming standard for tackling NP-complete/hard problems in PO, with experimental success reported in small-scale implementations. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Classical ML techniques (e.g., multilayer perceptrons, random forests, LSTM) dominate PO construction in the reviewed literature, but face limitations like high computational costs and the curse of dimensionality. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] Research gaps identified include the lack of studies on mutual funds (vs. stocks), limited validation of quantum outputs due to NISQ limitations, and the need for improved quantum gate accuracy. — [[2023_Fernandes_SystematicLiteratureReview]]
- [supported] The Maximum Amplification Optimisation Algorithm (MAOA) demonstrates substantial speedup over classical random sampling in finding optimal solutions for vehicle routing, portfolio optimization, and normally distributed solution quality problems, as shown through numerical simulations. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] MAOA outperforms the Quantum Approximate Optimisation Algorithm (QAOA) and the Restricted Grover Adaptive Search (RGAS) by amplifying optimal solutions more effectively without requiring computationally expensive variational procedures. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] MAOA achieves maximum amplification of optimal solutions by using a binary marking function on a complete graph and applying derived optimal parameters (γ = π and t = π/N) repeatedly, avoiding the variational procedure of QAOA/QWOA. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] The amplification of optimal solutions in MAOA is quantified by a theoretically derived upper bound, with numerical convergence demonstrated in simulations. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] For a given circuit depth (r iterations), MAOA produces a maximally amplified state where optimal solutions are amplified by a factor of (2r + 1)^2, as validated by simulations on a complete graph with 10^8 vertices. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] The threshold response curve analysis shows that MAOA reliably navigates to a quality threshold within the low-convergence regime, ensuring maximum amplification of optimal solutions for restricted circuit depths. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] MAOA's performance is independent of the exact shape of the solution quality distribution, making it robust for large-scale combinatorial optimization problems where distribution tails are uncertain. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] The Grover Adaptive Search (GAS) is used as a benchmark, but its requirement for large rotation counts (O(√N)) makes it impractical for near-term quantum devices, whereas MAOA is designed for restricted circuit depths. — [[2021_Bennett_QuantumOptimisationVia]]
- [supported] The book provides code samples and simulations for quantum algorithms (e.g., QAOA, Grover’s, Shor’s) but does not demonstrate results on real quantum hardware — [[2020_Kommadi_QuantumComputingSolutions]]
